from __future__ import annotations

import os
import sys

from setuptools import setup

dependencies = [
    "aiofiles==23.1.0",  # Async IO for files
    "anyio==3.6.2",
    "boto3==1.26.111",  # AWS S3 for DL s3 plugin
    "blspy==1.0.16",  # Signature library
    "chiavdf==1.0.8",  # timelord and vdf verification
    "chiabip158==1.2",  # bip158-style wallet filters
    "chiapos==1.0.11",  # proof of space
    "clvm==0.9.7",
    "clvm_tools==0.4.6",  # Currying, Program.to, other conveniences
    "chia_rs==0.2.7",
    "clvm-tools-rs==0.1.30",  # Rust implementation of clvm_tools' compiler
    "aiohttp==3.8.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==4.0.1",  # Binary data management library
    "colorama==0.4.6",  # Colorizes terminal output
    "colorlog==6.7.0",  # Adds color to logs
    "concurrent-log-handler==0.9.20",  # Concurrently log and rotate logs
    "cryptography==39.0.1",  # Python cryptography library for TLS - keyring conflict
    "filelock==3.9.0",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "keyring==23.13.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "PyYAML==6.0",  # Used for config file format
    "setproctitle==1.3.2",  # Gives the ball processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "click==8.1.3",  # For the CLI
    "dnspython==2.3.0",  # Query DNS seeds
    "watchdog==2.2.0",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.23",  # dns lib
    "typing-extensions==4.5.0",  # typing backports like Protocol and TypedDict
    "zstd==1.5.4.0",
    "packaging==23.0",
    "psutil==5.9.4",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build",
    "coverage",
    "diff-cover",
    "pre-commit",
    "py3createtorrent",
    "pylint",
    "pytest",
    "pytest-asyncio>=0.18.1",  # require attribute 'fixture'
    "pytest-cov",
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "twine",
    "isort",
    "flake8",
    "mypy",
    "black==23.3.0",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "pyinstaller==5.8.0",
    "types-aiofiles",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
]

legacy_keyring_dependencies = [
    "keyrings.cryptfile==1.3.9",
]

kwargs = dict(
    name="ballcoin-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@ballcoin.top",
    description="BallCoin Blockchain full node, farmer, timelord, and wallet.",
    url="https://ballcoin.top/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="BallCoin Blockchain node",
    install_requires=dependencies,
    extras_require=dict(
        dev=dev_dependencies,
        upnp=upnp_dependencies,
        legacy_keyring=legacy_keyring_dependencies,
    ),
    packages=[
        "build_scripts",
        "ball",
        "ball.cmds",
        "ball.clvm",
        "ball.consensus",
        "ball.daemon",
        "ball.data_layer",
        "ball.full_node",
        "ball.timelord",
        "ball.farmer",
        "ball.harvester",
        "ball.introducer",
        "ball.plot_sync",
        "ball.plotters",
        "ball.plotting",
        "ball.pools",
        "ball.protocols",
        "ball.rpc",
        "ball.seeder",
        "ball.server",
        "ball.simulator",
        "ball.types.blockchain_format",
        "ball.types",
        "ball.util",
        "ball.wallet",
        "ball.wallet.db_wallet",
        "ball.wallet.puzzles",
        "ball.wallet.cat_wallet",
        "ball.wallet.did_wallet",
        "ball.wallet.nft_wallet",
        "ball.wallet.trading",
        "ball.wallet.util",
        "ball.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "ball = ball.cmds.ball:main",
            "ball_daemon = ball.daemon.server:main",
            "ball_wallet = ball.server.start_wallet:main",
            "ball_full_node = ball.server.start_full_node:main",
            "ball_harvester = ball.server.start_harvester:main",
            "ball_farmer = ball.server.start_farmer:main",
            "ball_introducer = ball.server.start_introducer:main",
            "ball_crawler = ball.seeder.start_crawler:main",
            "ball_seeder = ball.seeder.dns_server:main",
            "ball_timelord = ball.server.start_timelord:main",
            "ball_timelord_launcher = ball.timelord.timelord_launcher:main",
            "ball_full_node_simulator = ball.simulator.start_simulator:main",
            "ball_data_layer = ball.server.start_data_layer:main",
            "ball_data_layer_http = ball.data_layer.data_layer_server:main",
            "ball_data_layer_s3_plugin = ball.data_layer.s3_plugin_service:run_server",
        ]
    },
    package_data={
        "ball": ["pyinstaller.spec"],
        "": ["*.clsp", "*.clsp.hex", "*.clvm", "*.clib", "py.typed"],
        "ball.util": ["initial-*.yaml", "english.txt"],
        "ball.ssl": ["ball_ca.crt", "ball_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/Ball-Network/ballcoin-blockchain/",
        "Changelog": "https://github.com/Ball-Network/ballcoin-blockchain/blob/main/CHANGELOG.md",
    },
)

if "setup_file" in sys.modules:
    # include dev deps in regular deps when run in snyk
    dependencies.extend(dev_dependencies)

if len(os.environ.get("BALL_SKIP_SETUP", "")) < 1:
    setup(**kwargs)  # type: ignore
