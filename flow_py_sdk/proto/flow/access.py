# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: flow/access/access.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import betterproto
import grpclib

from .flow import entities


@dataclass
class PingRequest(betterproto.Message):
    pass


@dataclass
class PingResponse(betterproto.Message):
    pass


@dataclass
class GetLatestBlockHeaderRequest(betterproto.Message):
    is_sealed: bool = betterproto.bool_field(1)


@dataclass
class GetBlockHeaderByIDRequest(betterproto.Message):
    id: bytes = betterproto.bytes_field(1)


@dataclass
class GetBlockHeaderByHeightRequest(betterproto.Message):
    height: int = betterproto.uint64_field(1)


@dataclass
class BlockHeaderResponse(betterproto.Message):
    block: entities.BlockHeader = betterproto.message_field(1)


@dataclass
class GetLatestBlockRequest(betterproto.Message):
    is_sealed: bool = betterproto.bool_field(1)
    full_block_response: bool = betterproto.bool_field(2)


@dataclass
class GetBlockByIDRequest(betterproto.Message):
    id: bytes = betterproto.bytes_field(1)
    full_block_response: bool = betterproto.bool_field(2)


@dataclass
class GetBlockByHeightRequest(betterproto.Message):
    height: int = betterproto.uint64_field(1)
    full_block_response: bool = betterproto.bool_field(2)


@dataclass
class BlockResponse(betterproto.Message):
    block: entities.Block = betterproto.message_field(1)


@dataclass
class GetCollectionByIDRequest(betterproto.Message):
    id: bytes = betterproto.bytes_field(1)


@dataclass
class CollectionResponse(betterproto.Message):
    collection: entities.Collection = betterproto.message_field(1)


@dataclass
class SendTransactionRequest(betterproto.Message):
    transaction: entities.Transaction = betterproto.message_field(1)


@dataclass
class SendTransactionResponse(betterproto.Message):
    id: bytes = betterproto.bytes_field(1)


@dataclass
class GetTransactionRequest(betterproto.Message):
    id: bytes = betterproto.bytes_field(1)


@dataclass
class GetTransactionByIndexRequest(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)
    index: int = betterproto.uint32_field(2)


@dataclass
class GetTransactionsByBlockIDRequest(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)


@dataclass
class TransactionResultsResponse(betterproto.Message):
    transaction_results: List["TransactionResultResponse"] = betterproto.message_field(
        1
    )


@dataclass
class TransactionsResponse(betterproto.Message):
    transactions: List[entities.Transaction] = betterproto.message_field(1)


@dataclass
class TransactionResponse(betterproto.Message):
    transaction: entities.Transaction = betterproto.message_field(1)


@dataclass
class TransactionResultResponse(betterproto.Message):
    status: entities.TransactionStatus = betterproto.enum_field(1)
    status_code: int = betterproto.uint32_field(2)
    error_message: str = betterproto.string_field(3)
    events: List[entities.Event] = betterproto.message_field(4)
    block_id: bytes = betterproto.bytes_field(5)
    transaction_id: bytes = betterproto.bytes_field(6)
    collection_id: bytes = betterproto.bytes_field(7)
    block_height: int = betterproto.uint64_field(8)


@dataclass
class GetAccountRequest(betterproto.Message):
    address: bytes = betterproto.bytes_field(1)


@dataclass
class GetAccountResponse(betterproto.Message):
    account: entities.Account = betterproto.message_field(1)


@dataclass
class GetAccountAtLatestBlockRequest(betterproto.Message):
    address: bytes = betterproto.bytes_field(1)


@dataclass
class AccountResponse(betterproto.Message):
    account: entities.Account = betterproto.message_field(1)


@dataclass
class GetAccountAtBlockHeightRequest(betterproto.Message):
    address: bytes = betterproto.bytes_field(1)
    block_height: int = betterproto.uint64_field(2)


@dataclass
class ExecuteScriptAtLatestBlockRequest(betterproto.Message):
    script: bytes = betterproto.bytes_field(1)
    arguments: List[bytes] = betterproto.bytes_field(2)


@dataclass
class ExecuteScriptAtBlockIDRequest(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)
    script: bytes = betterproto.bytes_field(2)
    arguments: List[bytes] = betterproto.bytes_field(3)


@dataclass
class ExecuteScriptAtBlockHeightRequest(betterproto.Message):
    block_height: int = betterproto.uint64_field(1)
    script: bytes = betterproto.bytes_field(2)
    arguments: List[bytes] = betterproto.bytes_field(3)


@dataclass
class ExecuteScriptResponse(betterproto.Message):
    value: bytes = betterproto.bytes_field(1)


@dataclass
class GetEventsForHeightRangeRequest(betterproto.Message):
    type: str = betterproto.string_field(1)
    start_height: int = betterproto.uint64_field(2)
    end_height: int = betterproto.uint64_field(3)


@dataclass
class GetEventsForBlockIDsRequest(betterproto.Message):
    type: str = betterproto.string_field(1)
    block_ids: List[bytes] = betterproto.bytes_field(2)


@dataclass
class EventsResponse(betterproto.Message):
    results: List["EventsResponseResult"] = betterproto.message_field(1)


@dataclass
class EventsResponseResult(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)
    block_height: int = betterproto.uint64_field(2)
    events: List[entities.Event] = betterproto.message_field(3)
    block_timestamp: datetime = betterproto.message_field(4)


@dataclass
class GetNetworkParametersRequest(betterproto.Message):
    pass


@dataclass
class GetNetworkParametersResponse(betterproto.Message):
    chain_id: str = betterproto.string_field(1)


@dataclass
class GetLatestProtocolStateSnapshotRequest(betterproto.Message):
    pass


@dataclass
class ProtocolStateSnapshotResponse(betterproto.Message):
    serialized_snapshot: bytes = betterproto.bytes_field(1)


@dataclass
class GetExecutionResultForBlockIDRequest(betterproto.Message):
    block_id: bytes = betterproto.bytes_field(1)


@dataclass
class ExecutionResultForBlockIDResponse(betterproto.Message):
    execution_result: entities.ExecutionResult = betterproto.message_field(1)


class AccessAPIStub(betterproto.ServiceStub):
    """AccessAPI is the public-facing API provided by access nodes."""

    async def ping(self) -> PingResponse:
        """Ping is used to check if the access node is alive and healthy."""

        request = PingRequest()

        return await self._unary_unary(
            "/flow.access.AccessAPI/Ping",
            request,
            PingResponse,
        )

    async def get_latest_block_header(
        self, *, is_sealed: bool = False
    ) -> BlockHeaderResponse:
        """
        GetLatestBlockHeader gets the latest sealed or unsealed block header.
        """

        request = GetLatestBlockHeaderRequest()
        request.is_sealed = is_sealed

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetLatestBlockHeader",
            request,
            BlockHeaderResponse,
        )

    async def get_block_header_by_i_d(self, *, id: bytes = b"") -> BlockHeaderResponse:
        """GetBlockHeaderByID gets a block header by ID."""

        request = GetBlockHeaderByIDRequest()
        request.id = id

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetBlockHeaderByID",
            request,
            BlockHeaderResponse,
        )

    async def get_block_header_by_height(
        self, *, height: int = 0
    ) -> BlockHeaderResponse:
        """GetBlockHeaderByHeight gets a block header by height."""

        request = GetBlockHeaderByHeightRequest()
        request.height = height

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetBlockHeaderByHeight",
            request,
            BlockHeaderResponse,
        )

    async def get_latest_block(
        self, *, is_sealed: bool = False, full_block_response: bool = False
    ) -> BlockResponse:
        """
        GetLatestBlock gets the full payload of the latest sealed or unsealed
        block.
        """

        request = GetLatestBlockRequest()
        request.is_sealed = is_sealed
        request.full_block_response = full_block_response

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetLatestBlock",
            request,
            BlockResponse,
        )

    async def get_block_by_i_d(
        self, *, id: bytes = b"", full_block_response: bool = False
    ) -> BlockResponse:
        """GetBlockByID gets a full block by ID."""

        request = GetBlockByIDRequest()
        request.id = id
        request.full_block_response = full_block_response

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetBlockByID",
            request,
            BlockResponse,
        )

    async def get_block_by_height(
        self, *, height: int = 0, full_block_response: bool = False
    ) -> BlockResponse:
        """GetBlockByHeight gets a full block by height."""

        request = GetBlockByHeightRequest()
        request.height = height
        request.full_block_response = full_block_response

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetBlockByHeight",
            request,
            BlockResponse,
        )

    async def get_collection_by_i_d(self, *, id: bytes = b"") -> CollectionResponse:
        """GetCollectionByID gets a collection by ID."""

        request = GetCollectionByIDRequest()
        request.id = id

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetCollectionByID",
            request,
            CollectionResponse,
        )

    async def send_transaction(
        self, *, transaction: Optional[entities.Transaction] = None
    ) -> SendTransactionResponse:
        """SendTransaction submits a transaction to the network."""

        request = SendTransactionRequest()
        if transaction is not None:
            request.transaction = transaction

        return await self._unary_unary(
            "/flow.access.AccessAPI/SendTransaction",
            request,
            SendTransactionResponse,
        )

    async def get_transaction(self, *, id: bytes = b"") -> TransactionResponse:
        """GetTransaction gets a transaction by ID."""

        request = GetTransactionRequest()
        request.id = id

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetTransaction",
            request,
            TransactionResponse,
        )

    async def get_transaction_result(
        self, *, id: bytes = b""
    ) -> TransactionResultResponse:
        """GetTransactionResult gets the result of a transaction."""

        request = GetTransactionRequest()
        request.id = id

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetTransactionResult",
            request,
            TransactionResultResponse,
        )

    async def get_transaction_result_by_index(
        self, *, block_id: bytes = b"", index: int = 0
    ) -> TransactionResultResponse:
        """
        GetTransactionResultByIndex gets the result of a transaction at a
        specified block and index
        """

        request = GetTransactionByIndexRequest()
        request.block_id = block_id
        request.index = index

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetTransactionResultByIndex",
            request,
            TransactionResultResponse,
        )

    async def get_transaction_results_by_block_i_d(
        self, *, block_id: bytes = b""
    ) -> TransactionResultsResponse:
        """
        GetTransactionResultsByBlockID gets all the transaction results for a
        specified block
        """

        request = GetTransactionsByBlockIDRequest()
        request.block_id = block_id

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetTransactionResultsByBlockID",
            request,
            TransactionResultsResponse,
        )

    async def get_transactions_by_block_i_d(
        self, *, block_id: bytes = b""
    ) -> TransactionsResponse:
        """
        GetTransactionsByBlockID gets all the transactions for a specified
        block
        """

        request = GetTransactionsByBlockIDRequest()
        request.block_id = block_id

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetTransactionsByBlockID",
            request,
            TransactionsResponse,
        )

    async def get_account(self, *, address: bytes = b"") -> GetAccountResponse:
        """
        GetAccount is an alias for GetAccountAtLatestBlock. Warning: this
        function is deprecated. It behaves identically to
        GetAccountAtLatestBlock and will be removed in a future version.
        """

        request = GetAccountRequest()
        request.address = address

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetAccount",
            request,
            GetAccountResponse,
        )

    async def get_account_at_latest_block(
        self, *, address: bytes = b""
    ) -> AccountResponse:
        """
        GetAccountAtLatestBlock gets an account by address from the latest
        sealed execution state.
        """

        request = GetAccountAtLatestBlockRequest()
        request.address = address

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetAccountAtLatestBlock",
            request,
            AccountResponse,
        )

    async def get_account_at_block_height(
        self, *, address: bytes = b"", block_height: int = 0
    ) -> AccountResponse:
        """
        GetAccountAtBlockHeight gets an account by address at the given block
        height
        """

        request = GetAccountAtBlockHeightRequest()
        request.address = address
        request.block_height = block_height

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetAccountAtBlockHeight",
            request,
            AccountResponse,
        )

    async def execute_script_at_latest_block(
        self, *, script: bytes = b"", arguments: List[bytes] = []
    ) -> ExecuteScriptResponse:
        """
        ExecuteScriptAtLatestBlock executes a read-only Cadence script against
        the latest sealed execution state.
        """

        request = ExecuteScriptAtLatestBlockRequest()
        request.script = script
        request.arguments = arguments

        return await self._unary_unary(
            "/flow.access.AccessAPI/ExecuteScriptAtLatestBlock",
            request,
            ExecuteScriptResponse,
        )

    async def execute_script_at_block_i_d(
        self, *, block_id: bytes = b"", script: bytes = b"", arguments: List[bytes] = []
    ) -> ExecuteScriptResponse:
        """
        ExecuteScriptAtBlockID executes a ready-only Cadence script against the
        execution state at the block with the given ID.
        """

        request = ExecuteScriptAtBlockIDRequest()
        request.block_id = block_id
        request.script = script
        request.arguments = arguments

        return await self._unary_unary(
            "/flow.access.AccessAPI/ExecuteScriptAtBlockID",
            request,
            ExecuteScriptResponse,
        )

    async def execute_script_at_block_height(
        self, *, block_height: int = 0, script: bytes = b"", arguments: List[bytes] = []
    ) -> ExecuteScriptResponse:
        """
        ExecuteScriptAtBlockHeight executes a ready-only Cadence script against
        the execution state at the given block height.
        """

        request = ExecuteScriptAtBlockHeightRequest()
        request.block_height = block_height
        request.script = script
        request.arguments = arguments

        return await self._unary_unary(
            "/flow.access.AccessAPI/ExecuteScriptAtBlockHeight",
            request,
            ExecuteScriptResponse,
        )

    async def get_events_for_height_range(
        self, *, type: str = "", start_height: int = 0, end_height: int = 0
    ) -> EventsResponse:
        """
        GetEventsForHeightRange retrieves events emitted within the specified
        block range.
        """

        request = GetEventsForHeightRangeRequest()
        request.type = type
        request.start_height = start_height
        request.end_height = end_height

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetEventsForHeightRange",
            request,
            EventsResponse,
        )

    async def get_events_for_block_i_ds(
        self, *, type: str = "", block_ids: List[bytes] = []
    ) -> EventsResponse:
        """
        GetEventsForBlockIDs retrieves events for the specified block IDs and
        event type.
        """

        request = GetEventsForBlockIDsRequest()
        request.type = type
        request.block_ids = block_ids

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetEventsForBlockIDs",
            request,
            EventsResponse,
        )

    async def get_network_parameters(self) -> GetNetworkParametersResponse:
        """GetNetworkParameters retrieves the Flow network details"""

        request = GetNetworkParametersRequest()

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetNetworkParameters",
            request,
            GetNetworkParametersResponse,
        )

    async def get_latest_protocol_state_snapshot(self) -> ProtocolStateSnapshotResponse:
        """
        GetLatestProtocolStateSnapshot retrieves the latest sealed protocol
        state snapshot. Used by Flow nodes joining the network to bootstrap a
        space-efficient local state.
        """

        request = GetLatestProtocolStateSnapshotRequest()

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetLatestProtocolStateSnapshot",
            request,
            ProtocolStateSnapshotResponse,
        )

    async def get_execution_result_for_block_i_d(
        self, *, block_id: bytes = b""
    ) -> ExecutionResultForBlockIDResponse:
        """
        GetExecutionResultForBlockID returns Execution Result for a given
        block. At present, Access Node might not have execution results for
        every block and as usual, until sealed, this data can change
        """

        request = GetExecutionResultForBlockIDRequest()
        request.block_id = block_id

        return await self._unary_unary(
            "/flow.access.AccessAPI/GetExecutionResultForBlockID",
            request,
            ExecutionResultForBlockIDResponse,
        )
