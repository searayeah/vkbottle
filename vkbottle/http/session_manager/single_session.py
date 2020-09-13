from .abc import ABCSessionManager
from vkbottle.http.client import ABCHTTPClient, AiohttpClient
import typing


class SingleSessionManager(ABCSessionManager):
    def __init__(self, http_client: typing.Optional[typing.Type[ABCHTTPClient]] = None):
        self.http_client: typing.Type[ABCHTTPClient] = http_client or AiohttpClient
        self._session: typing.Optional[ABCHTTPClient] = None

    @property
    def session(self) -> ABCHTTPClient:
        if not self._session:
            self._session = self.http_client()
        return self._session

    async def __aenter__(self) -> ABCHTTPClient:
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
