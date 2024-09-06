class BaseError(Exception):
    pass


class DataNotFoundError(BaseError):
    pass


class NoSuchNexusLayer(BaseError):
    def __init__(self, layer_type: str):
        self._layer_type = layer_type

    def __str__(self) -> str:
        return f"Non-such nexus layer: {self._layer_type}"


class BaseConfigurationError(BaseError):
    pass


class InvalidNexusLayerType(BaseConfigurationError):
    def __init__(self, expected_layer_type: str, actual_layer_type: str):
        self._expected_layer_type = expected_layer_type
        self._actual_layer_type = actual_layer_type

    def __str__(self) -> str:
        return f"Invalid nexus layer type: expected {self._expected_layer_type}, actual {self._actual_layer_type}"
