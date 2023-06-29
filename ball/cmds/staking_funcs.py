from __future__ import annotations

import asyncio
import time
from decimal import Decimal

from ball.cmds.cmds_util import transaction_status_msg, transaction_submitted_msg
from ball.cmds.units import units
from ball.rpc.wallet_rpc_client import WalletRpcClient
from ball.util.ints import uint64


async def info(args: dict, wallet_client: WalletRpcClient, fingerprint: int) -> None:
    balance, address = await wallet_client.staking_info(fingerprint)
    ball = balance / units["ball"]
    print(f"Staking balance: {ball}")
    print(f"Staking address: {address}")


async def send(args: dict, wallet_client: WalletRpcClient, fingerprint: int) -> None:
    amount = Decimal(args["amount"])

    if amount == 0:
        print("You can not staking an empty transaction")
        return

    print("Submitting staking transaction...")
    res = await wallet_client.staking_send(
        uint64(int(amount * units["ball"])), fingerprint
    )

    tx_id = res.name
    start = time.time()
    while time.time() - start < 10:
        await asyncio.sleep(0.1)
        tx = await wallet_client.get_transaction(1, tx_id)
        if len(tx.sent_to) > 0:
            print(transaction_submitted_msg(tx))
            print(transaction_status_msg(fingerprint, tx_id))
            return None

    print("Staking transaction not yet submitted to nodes")
    print(f"To get status, use command: ball wallet get_transaction -f {fingerprint} -tx 0x{tx_id}")


async def withdraw(args: dict, wallet_client: WalletRpcClient, fingerprint: int) -> None:
    amount = Decimal(args["amount"])
    address = args["address"]

    print("Submitting withdraw staking transaction...")
    res = await wallet_client.staking_withdraw(
        address, uint64(int(amount * units["ball"])), fingerprint
    )

    tx_id = res.name
    start = time.time()
    while time.time() - start < 10:
        await asyncio.sleep(0.1)
        tx = await wallet_client.get_transaction(1, tx_id)
        if len(tx.sent_to) > 0:
            print(transaction_submitted_msg(tx))
            print(transaction_status_msg(fingerprint, tx_id))
            return None

    print("Withdraw staking transaction not yet submitted to nodes")
    print(f"To get status, use command: ball wallet get_transaction -f {fingerprint} -tx 0x{tx_id}")


async def find_pool_nft(args: dict, wallet_client: WalletRpcClient, fingerprint: int) -> None:
    launcher_id: str = args["launcher_id"]
    contract_address: str = args["contract_address"]
    response = await wallet_client.find_pool_nft(launcher_id, contract_address)
    address = response["contract_address"]
    total_amount = response["total_amount"] / units["ball"]
    record_amount = response["record_amount"] / units["ball"]
    balance_amount = response["balance_amount"] / units["ball"]
    print(f"Contract Address: {address}")
    print(f"Total Amount: {total_amount} BALL")
    print(f"Balance Amount: {balance_amount} BALL")
    print(f"Record Amount: {record_amount} BALL")


async def recover_pool_nft(args: dict, wallet_client: WalletRpcClient, fingerprint: int) -> None:
    launcher_id: str = args["launcher_id"]
    contract_address: str = args["contract_address"]
    response = await wallet_client.recover_pool_nft(launcher_id, contract_address)
    address = response["contract_address"]
    status = response["status"]
    amount = response["amount"] / units["ball"]
    print(f"Contract Address: {address}")
    print(f"Record Amount: {amount} BALL")
    print(f"Status: {status}")
