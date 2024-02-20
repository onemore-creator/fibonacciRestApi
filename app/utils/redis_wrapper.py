import aioredis
from app.config import config

class RedisWrapper:

    def __init__(self) -> None:
        self.pool = aioredis.ConnectionPool.from_url("redis://redis", max_connections=10)

    def getRedisInstance(self) -> aioredis.Redis:
        redis = aioredis.Redis(connection_pool=self.pool, decode_responses=True)
        return redis

redisWrapper = RedisWrapper()