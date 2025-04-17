"""
数据源对象类型的枚举类
"""

import enum

__all__ = [
    "DataType"
]


class DataType(enum.IntEnum):
    """数据源对象类型的枚举类"""

    UNKNOWN = 0  # 未知数据类型
    HIVE = 1  # Hive
    MYSQL = 2  # MySQL
    KAFKA = 3  # Kafka
    HBASE = 4  # HBase
    OTS = 5  # OTS (tablestore)
    DORIS = 6  # Doris
    REDIS = 7  # Redis
    ES = 8  # ElasticSearch
    HDFS = 9  # HDFS
