from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "bitchiavdf==1.0.2",  # timelord and vdf verification
    "bitchiabip158==1.0",  # bip158-style wallet filters
    "bitchiapos==1.0.3",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the bitchia processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
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
]

kwargs = dict(
    name="bitchia-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@bitchia.net",
    description="BitChia blockchain full node, farmer, timelord, and wallet.",
    url="https://bitchia.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="bitchia blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "bitchia",
        "bitchia.cmds",
        "bitchia.consensus",
        "bitchia.daemon",
        "bitchia.full_node",
        "bitchia.timelord",
        "bitchia.farmer",
        "bitchia.harvester",
        "bitchia.introducer",
        "bitchia.plotting",
        "bitchia.protocols",
        "bitchia.rpc",
        "bitchia.server",
        "bitchia.simulator",
        "bitchia.types.blockchain_format",
        "bitchia.types",
        "bitchia.util",
        "bitchia.wallet",
        "bitchia.wallet.puzzles",
        "bitchia.wallet.rl_wallet",
        "bitchia.wallet.cc_wallet",
        "bitchia.wallet.did_wallet",
        "bitchia.wallet.settings",
        "bitchia.wallet.trading",
        "bitchia.wallet.util",
        "bitchia.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "bitchia = bitchia.cmds.bitchia:main",
            "bitchia_wallet = bitchia.server.start_wallet:main",
            "bitchia_full_node = bitchia.server.start_full_node:main",
            "bitchia_harvester = bitchia.server.start_harvester:main",
            "bitchia_farmer = bitchia.server.start_farmer:main",
            "bitchia_introducer = bitchia.server.start_introducer:main",
            "bitchia_timelord = bitchia.server.start_timelord:main",
            "bitchia_timelord_launcher = bitchia.timelord.timelord_launcher:main",
            "bitchia_full_node_simulator = bitchia.simulator.start_simulator:main",
        ]
    },
    package_data={
        "bitchia": ["pyinstaller.spec"],
        "bitchia.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "bitchia.util": ["initial-*.yaml", "english.txt"],
        "bitchia.ssl": ["bitchia_ca.crt", "bitchia_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
