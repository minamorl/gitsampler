import redis

REDIS_PREFIX = "gitsampler:commits:"

def get_redis():
    return redis.StrictRedis()

def save_all(redis, iterable):
    redis.flushall()
    for dict in iterable:
        redis.hmset(REDIS_PREFIX + ' '.join(dict.values()) ,dict)
