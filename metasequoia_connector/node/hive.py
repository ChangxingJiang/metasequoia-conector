"""
Hive 连接器节点
"""

import dataclasses
from typing import List, Optional

from metasequoia_connector.node.data_type import DataType
from metasequoia_connector.node.node_base import DataInstanceBase
from metasequoia_connector.node.ssh_tunnel import SshTunnel

__all__ = ["HiveInstance", "HiveTable"]


class HiveInstance(DataInstanceBase):
    """Hive 实例"""

    def __init__(self,
                 hosts: List[str], port: int, username: Optional[str],
                 ssh_tunnel: Optional[SshTunnel] = None,
                 name: Optional[str] = None):
        super().__init__(DataType.HIVE, name)
        self._hosts = hosts
        self._port = port
        self._username = username
        self._ssh_tunnel = ssh_tunnel

    @property
    def hosts(self) -> List[str]:
        return self._hosts

    @property
    def port(self) -> int:
        return self._port

    @property
    def username(self) -> Optional[str]:
        return self._username

    @property
    def ssh_tunnel(self) -> Optional[SshTunnel]:
        return self._ssh_tunnel

    def set_username(self, username: str) -> None:
        self._username = username

    def __hash__(self):
        """根据 data_type、hosts、port、username 和 ssh_tunnel 计算哈希值"""
        return hash((self._data_type, tuple(self._hosts), self._port, self._username, self._ssh_tunnel))

    def __eq__(self, other):
        """定义两个 HiveInstance 对象相等的条件"""
        if not isinstance(other, HiveInstance):
            return None
        return (self._data_type == other._data_type
                and self._hosts == other._hosts
                and self._port == other._port
                and self._username == other._username
                and self._ssh_tunnel == other._ssh_tunnel
                )

    def __repr__(self):
        return (f"HiveInstance("
                f"hosts={self._hosts}, "
                f"port={self._port}, "
                f"username={self._username}, "
                f"ssh_tunnel={self._ssh_tunnel})")


@dataclasses.dataclass(slots=True, frozen=True, eq=True)
class HiveTable:
    """Hive 表"""

    instance: HiveInstance = dataclasses.field(kw_only=True)
    schema: str = dataclasses.field(kw_only=True)
    table: str = dataclasses.field(kw_only=True)
