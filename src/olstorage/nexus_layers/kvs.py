from typing import Any

from ..backends.base import BaseBackend
from .base import BaseNexusLayer


class KvsNexusLayer(BaseNexusLayer):
    def __init__(self, backend: BaseBackend) -> None:
        self._backend = backend

    @property
    def backend(self) -> BaseBackend:
        return self._backend

    def set(self, key: Any, value: Any) -> None:
        raise NotImplementedError

    def get(self, key: Any) -> Any:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError
        raise NotImplementedError
