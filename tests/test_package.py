import re

import olstorage


def test_olstorage_has_version() -> None:
    assert re.match(r"\d+\.\d+\.\d+", olstorage.__version__)
