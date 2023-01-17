from base64 import b64encode
from hashlib import sha1
from json import dumps
from logging import getLogger
from typing import Any

logger = getLogger(__name__)


class BaseLiqPayAdapter:
    def __init__(self, public_key: str, private_key: str):
        self._public_key = public_key
        self._private_key = private_key

    async def create_payment_link(
        self,
        url: str,
        raw_data: dict[str, Any],
    ) -> str:
        raw_data.update(public_key=self._public_key)

        data = b64encode(dumps(raw_data).encode()).decode()
        signature = create_signature(data, self._private_key)

        return url + f"?data={data}&signature={signature}"


def create_signature(
    data: str,
    private_key: str,
) -> str:
    joined_fields = (private_key + data + private_key).encode()
    return b64encode(sha1(joined_fields).digest()).decode()
