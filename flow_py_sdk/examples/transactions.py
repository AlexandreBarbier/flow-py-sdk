import logging
from typing import Optional

import rlp
from ecdsa import SigningKey

from flow_py_sdk.cadence.types import Dictionary, Array, String
from flow_py_sdk.client import flow_client
from flow_py_sdk.examples.common import ExampleContext, Example
from flow_py_sdk.signer import get_signing_curve, InMemorySigner
from flow_py_sdk.tx import Tx

log = logging.getLogger(__name__)


class AccountKey(object):
    weight_threshold: int = 1000

    def __init__(self, *, public_key: bytes, sign_algo: int, hash_algo: int, weight: Optional[int] = None) -> None:
        super().__init__()
        self.index: Optional[int] = None
        self.public_key: bytes = public_key
        self.sign_algo: int = sign_algo
        self.hash_algo: int = hash_algo
        self.weight: int = weight if weight is not None else self.weight_threshold
        self.sequence_number: Optional[int] = None
        self.revoked: Optional[bool] = None

    def rlp(self) -> bytes:
        return rlp.encode([
            self.public_key,
            self.sign_algo.to_bytes(8, 'big', signed=False).lstrip(b'\0'),
            self.hash_algo.to_bytes(8, 'big', signed=False).lstrip(b'\0'),
            self.weight.to_bytes(8, 'big', signed=False).lstrip(b'\0')
        ])


class TransactionExample1(Example):
    def __init__(self) -> None:
        super().__init__('Create account transaction')

    async def run(self, ctx: ExampleContext):
        async with flow_client(host=ctx.access_node_host, port=ctx.access_node_port) as client:
            result = await client.get_latest_block()
            block_id = result.block.id
            result = await client.get_account_at_latest_block(address=ctx.service_account_address.bytes)
            proposer = result.account

            signer = InMemorySigner(3, 2, 'd7b1e643cdf601c5b3ca2cdabd731a563f100a42a2c658ece09572ae99295abf')

            tx = Tx("""transaction(){prepare(){log("OK")}}""") \
                .with_payer(ctx.service_account_address) \
                .with_reference_block_id(block_id) \
                .with_proposal_key(ctx.service_account_address, 0, proposer.keys[0].sequence_number) \
                .with_envelope_signature(ctx.service_account_address, 0, signer)

            await client.execute_transaction(tx)


class TransactionExample2(Example):

    def __init__(self) -> None:
        super().__init__('Create account transaction')

    async def run(self, ctx: ExampleContext):
        async with flow_client(host=ctx.access_node_host, port=ctx.access_node_port) as client:
            sk = SigningKey.generate(curve=get_signing_curve(3))
            account_key = AccountKey(public_key=sk.verifying_key.to_string().hex(), sign_algo=2, hash_algo=3)
            public_key = String(account_key.rlp().hex())
            cadence_public_keys = Array([public_key])
            cadence_contracts = Dictionary()

            result = await client.get_latest_block()
            block_id = result.block.id

            result = await client.get_account_at_latest_block(address=ctx.service_account_address.bytes)
            proposer = result.account

            signer = InMemorySigner(3, 2, '9655ccc27e1d08f87ac2a89d70ad140d5bad16b6b5cfda90614a9b7816a8450f')

            tx = Tx(
                f"""
                    transaction(publicKeys: [String], contracts:{{String: String}}) {{
                        prepare(signer: AuthAccount) {{
                            let acct = AuthAccount(payer: signer)
                    
                            for key in publicKeys {{
                                acct.addPublicKey(key.decodeHex())
                            }}
                    
                            for contract in contracts.keys {{
                                acct.contracts.add(name: contract, code: contracts[contract]!.decodeHex())
                            }}
                        }}
                    }}
                """) \
                .add_authorizers(ctx.service_account_address) \
                .add_arguments(cadence_public_keys) \
                .add_arguments(cadence_contracts) \
                .with_payer(ctx.service_account_address) \
                .with_reference_block_id(block_id) \
                .with_proposal_key(ctx.service_account_address, 0, proposer.keys[0].sequence_number) \
                .with_payload_signature(ctx.service_account_address, 0, signer) \
                .with_envelope_signature(ctx.service_account_address, 0, signer)

            await client.execute_transaction(tx)