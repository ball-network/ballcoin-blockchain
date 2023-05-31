from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": (
        "ball_harvester ball_timelord_launcher ball_timelord ball_farmer "
        "ball_full_node ball_wallet ball_data_layer ball_data_layer_http"
    ).split(),
    # TODO: should this be `data_layer`?
    "data": "ball_wallet ball_data_layer".split(),
    "data_layer_http": "ball_data_layer_http".split(),
    "node": "ball_full_node".split(),
    "harvester": "ball_harvester".split(),
    "farmer": "ball_harvester ball_farmer ball_full_node ball_wallet".split(),
    "farmer-no-wallet": "ball_harvester ball_farmer ball_full_node".split(),
    "farmer-only": "ball_farmer".split(),
    "timelord": "ball_timelord_launcher ball_timelord ball_full_node".split(),
    "timelord-only": "ball_timelord".split(),
    "timelord-launcher-only": "ball_timelord_launcher".split(),
    "wallet": "ball_wallet".split(),
    "introducer": "ball_introducer".split(),
    "simulator": "ball_full_node_simulator".split(),
    "crawler": "ball_crawler".split(),
    "seeder": "ball_crawler ball_seeder".split(),
    "seeder-only": "ball_seeder".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
