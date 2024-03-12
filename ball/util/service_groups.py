from __future__ import annotations

from typing import Generator, Iterable, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "ball_harvester",
        "ball_timelord_launcher",
        "ball_timelord",
        "ball_farmer",
        "ball_full_node",
        "ball_wallet",
        "ball_data_layer",
        "ball_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["ball_wallet", "ball_data_layer"],
    "data_layer_http": ["ball_data_layer_http"],
    "node": ["ball_full_node"],
    "harvester": ["ball_harvester"],
    "farmer": ["ball_harvester", "ball_farmer", "ball_full_node", "ball_wallet"],
    "farmer-no-wallet": ["ball_harvester", "ball_farmer", "ball_full_node"],
    "farmer-only": ["ball_farmer"],
    "timelord": ["ball_timelord_launcher", "ball_timelord", "ball_full_node"],
    "timelord-only": ["ball_timelord"],
    "timelord-launcher-only": ["ball_timelord_launcher"],
    "wallet": ["ball_wallet"],
    "introducer": ["ball_introducer"],
    "simulator": ["ball_full_node_simulator"],
    "crawler": ["ball_crawler"],
    "seeder": ["ball_crawler", "ball_seeder"],
    "seeder-only": ["ball_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups: Iterable[str]) -> Generator[str, None, None]:
    for group in groups:
        yield from SERVICES_FOR_GROUP[group]


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
