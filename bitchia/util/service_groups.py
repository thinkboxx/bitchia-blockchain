from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "bitchia_harvester bitchia_timelord_launcher bitchia_timelord bitchia_farmer bitchia_full_node bitchia_wallet".split(),
    "node": "bitchia_full_node".split(),
    "harvester": "bitchia_harvester".split(),
    "farmer": "bitchia_harvester bitchia_farmer bitchia_full_node bitchia_wallet".split(),
    "farmer-no-wallet": "bitchia_harvester bitchia_farmer bitchia_full_node".split(),
    "farmer-only": "bitchia_farmer".split(),
    "timelord": "bitchia_timelord_launcher bitchia_timelord bitchia_full_node".split(),
    "timelord-only": "bitchia_timelord".split(),
    "timelord-launcher-only": "bitchia_timelord_launcher".split(),
    "wallet": "bitchia_wallet bitchia_full_node".split(),
    "wallet-only": "bitchia_wallet".split(),
    "introducer": "bitchia_introducer".split(),
    "simulator": "bitchia_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
