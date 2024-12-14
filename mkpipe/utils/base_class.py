from pydantic import BaseModel
from typing import Optional


class PipeSettings(BaseModel):
    timezone: str = 'UTC'
    compression_codec: str = 'zstd'  # Options: snappy, gzip, zstd, lz4, none
    spark_driver_memory: str = '4g'
    spark_executor_memory: str = '3g'
    partitions_count: int = 2
    default_iterate_max_loop: int = 1000
    default_iterate_batch_size: int = 500000
    ROOT_DIR: str
    driver_name: Optional[str] = None


class InputTask(BaseModel):
    extractor_variant: str
    current_table_conf: dict
    loader_variant: str
    loader_conf: dict
    priority: Optional[int] = None
    data: Optional[dict] = None
    settings: PipeSettings
