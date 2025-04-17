"""
数据实例的抽象基类
"""

import abc
from typing import Optional

from metasequoia_connector.node.data_type import DataType

__all__ = [
    "DataInstanceBase",
    "DataEntityBase"
]


class DataInstanceBase(abc.ABC):
    """数据实例的抽象基类"""

    def __init__(self, data_type: DataType, name: Optional[str] = None):
        self._data_type = data_type
        self._name = name

    @property
    def data_type(self) -> DataType:
        """返回数据实例的数据源类型"""
        return self._data_type

    @property
    def name(self) -> Optional[str]:
        """返回数据实例的实例名称"""
        return self._name


class DataEntityBase(abc.ABC):
    """数据实体的抽象基类"""

    @abc.abstractmethod
    def standard_name(self) -> str:
        """返回数据实体的标准名称"""
