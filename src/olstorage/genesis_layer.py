from .settings import GenesisLayerSettings


class GenesisLayer: ...


def create_genesis_layer(settings: GenesisLayerSettings) -> GenesisLayer:
    raise NotImplementedError
