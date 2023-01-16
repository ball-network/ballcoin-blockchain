from setuptools import setup

dependencies = [
    "multidict==5.1.0",  # Avoid 5.2.0 due to Avast
    "blspy==1.0.6",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.6",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.15",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the ball processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspythonchia==2.2.0",  # Query DNS seeds
    "watchdog==2.1.6",  # Filesystem event watching - watches keyring.yaml
    "nest-asyncio==1.5.1",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="ballcoin-blockchain",
    author="ball",
    author_email="admin@ballcoin.top",
    description="Ball blockchain full node, farmer, timelord, and wallet.",
    url="https://ballcoin.top/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="ball blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "ball",
        "ball.cmds",
        "ball.clvm",
        "ball.consensus",
        "ball.daemon",
        "ball.full_node",
        "ball.timelord",
        "ball.farmer",
        "ball.harvester",
        "ball.introducer",
        "ball.plotters",
        "ball.plotting",
        "ball.pools",
        "ball.protocols",
        "ball.rpc",
        "ball.server",
        "ball.simulator",
        "ball.types.blockchain_format",
        "ball.types",
        "ball.util",
        "ball.wallet",
        "ball.wallet.puzzles",
        "ball.wallet.rl_wallet",
        "ball.wallet.cc_wallet",
        "ball.wallet.did_wallet",
        "ball.wallet.settings",
        "ball.wallet.trading",
        "ball.wallet.util",
        "ball.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "ball = ball.cmds.ball:main",
            "ball_wallet = ball.server.start_wallet:main",
            "ball_full_node = ball.server.start_full_node:main",
            "ball_harvester = ball.server.start_harvester:main",
            "ball_farmer = ball.server.start_farmer:main",
            "ball_introducer = ball.server.start_introducer:main",
            "ball_timelord = ball.server.start_timelord:main",
            "ball_timelord_launcher = ball.timelord.timelord_launcher:main",
            "ball_full_node_simulator = ball.simulator.start_simulator:main",
        ]
    },
    package_data={
        "ball": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "ball.util": ["initial-*.yaml", "english.txt"],
        "ball.ssl": ["ball_ca.crt", "ball_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
