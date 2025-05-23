"""
通用工具类
"""

from typing import Optional

__all__ = ["HostPort"]


class HostPort:
    """服务器地址和端口"""

    def __init__(self, host: str, port: Optional[int]):
        self._host = host
        self._port = port

    @staticmethod
    def create_by_url(url: str) -> "HostPort":
        if ":" not in url:
            return HostPort(url.strip(), None)
        else:
            host, port = url.split(":")
            return HostPort(host.strip(), int(port))

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> Optional[int]:
        return self._port

    def __hash__(self):
        return hash((self._host, self._port))

    def __eq__(self, other):
        return (isinstance(other, HostPort) and
                self._host == other._host and
                self._port == other._port)
