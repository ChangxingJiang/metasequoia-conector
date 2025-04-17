import dataclasses
from typing import Optional

from metasequoia_connector.node.data_type import DataType
from metasequoia_connector.node.node_base import DataInstanceBase
from metasequoia_connector.node.ssh_tunnel import SshTunnel

__all__ = ["MysqlInstance", "MysqlTable"]


class MysqlInstance(DataInstanceBase):
    """MySQL 实例"""

    def __init__(self, host: str, port: int, user: str, passwd: str,
                 ssh_tunnel: Optional[SshTunnel] = None, name: Optional[str] = None):
        super().__init__(DataType.MYSQL, name)
        self._host = host
        self._port = port
        self._user = user
        self._passwd = passwd
        self._ssh_tunnel = ssh_tunnel

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def user(self) -> str:
        return self._user

    @property
    def passwd(self) -> str:
        return self._passwd

    @property
    def ssh_tunnel(self) -> Optional[SshTunnel]:
        return self._ssh_tunnel

    def __hash__(self):
        """根据 data_type、host、port、user、passwd 和 ssh_tunnel 计算哈希值"""
        return hash((self._data_type, self._host, self._port, self._user, self._passwd, self._ssh_tunnel))

    def __eq__(self, other):
        """定义两个 MySQLInstance 对象相等的条件"""
        if not isinstance(other, MysqlInstance):
            return None
        return (self._data_type == other._data_type
                and self._host == other._host
                and self._port == other._port
                and self._user == other._user
                and self._passwd == other._passwd
                and self._ssh_tunnel == other._ssh_tunnel
                )

    def __repr__(self):
        return (f"MysqlInstance("
                f"host={self._host}, "
                f"port={self._port}, "
                f"user={self._user}, "
                f"passwd={self._passwd}, "
                f"ssh_tunnel={self._ssh_tunnel})")


@dataclasses.dataclass(slots=True, frozen=True, eq=True)
class MysqlTable:
    """MySQL 表"""

    instance: MysqlInstance = dataclasses.field(kw_only=True)
    schema: str = dataclasses.field(kw_only=True)
    table: str = dataclasses.field(kw_only=True)
