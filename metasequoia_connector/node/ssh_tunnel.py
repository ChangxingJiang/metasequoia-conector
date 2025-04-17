"""
SSH 隧道
"""

from typing import Optional

__all__ = ["SshTunnel"]


class SshTunnel:
    """SSH 隧道"""

    def __init__(self, host: str, port: int, username: str,
                 password: Optional[str] = None,
                 pkey: Optional[str] = None,
                 name: Optional[str] = None):
        self._host = host  # 对应 ssh_address_or_host 参数
        self._port = port  # 对应 ssh_address_or_host 参数
        self._username = username
        self._password = password
        self._pkey = pkey
        self._name = name

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> Optional[str]:
        return self._password

    @property
    def pkey(self) -> Optional[str]:
        return self._pkey

    @property
    def name(self) -> Optional[str]:
        return self._name

    def __hash__(self):
        """根据 host、port、username、password 和 pkey 计算哈希值"""
        return hash((self._host, self._port, self._username, self._password, self._pkey))

    def __eq__(self, other):
        """定义两个 SshTunnel 对象相等的条件"""
        if not isinstance(other, SshTunnel):
            return None
        return (self._host == other._host
                and self._port == other._port
                and self._username == other._username
                and self._password == other._password
                and self._pkey == other._pkey)

    def __repr__(self):
        return (f"SshTunnel("
                f"host={self._host}, "
                f"port={self._port}, "
                f"user={self._username}, "
                f"passwd={self._password}, "
                f"pkey={self._pkey})")
