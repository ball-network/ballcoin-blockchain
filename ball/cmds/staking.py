from typing import Optional

import click

from ball.cmds.cmds_util import execute_with_wallet


@click.group("staking", short_help="Manage your staking")
@click.pass_context
def staking_cmd(ctx: click.Context) -> None:
    pass


@staking_cmd.command("info", short_help="Query staking info")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
def staking_info(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
) -> None:
    import asyncio
    from .staking_funcs import info

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, {}, info))


@staking_cmd.command("send", short_help="Send ball to staking address")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option("-a", "--amount", help="How much ball to send, in GBTC", type=str, required=True)
def staking_send_cmd(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
    amount: str,
) -> None:
    extra_params = {
        "amount": amount,
    }
    import asyncio
    from .staking_funcs import send

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, send))


@staking_cmd.command("withdraw", short_help="Withdraw staking ball")
@click.option(
    "-wp",
    "--wallet-rpc-port",
    help="Set the port where the Wallet is hosting the RPC interface. See the rpc_port under wallet in config.yaml",
    type=int,
    default=None,
)
@click.option("-f", "--fingerprint", help="Set the fingerprint to specify which wallet to use", type=int)
@click.option(
    "-a",
    "--amount",
    help="withdraw staking GBTC, 0 will withdraw all staking",
    type=str,
    default="0",
    show_default=True
)
@click.option("-t", "--address", help="staking withdraw address", type=str, default="", show_default=True)
def staking_withdraw_cmd(
    wallet_rpc_port: Optional[int],
    fingerprint: int,
    amount: str,
    address: str,
) -> None:
    extra_params = {
        "amount": amount,
        "address": address,
    }
    import asyncio
    from .staking_funcs import withdraw

    asyncio.run(execute_with_wallet(wallet_rpc_port, fingerprint, extra_params, withdraw))
