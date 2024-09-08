from typing import Any

from .base import BaseNexusLayer


class KvsNexusLayer(BaseNexusLayer):
    def set(self, key: Any, value: Any) -> None:
        raise NotImplementedError

    def get(self, key: Any) -> Any:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError
