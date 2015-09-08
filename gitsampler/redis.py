import redis

REDIS_PREFIX = "gitsampler:commits:"

def get_redis():
    return redis.StrictRedis()

def delete_all(redis, prefix):
    for key in redis.keys(REDIS_PREFIX + "*"):
        redis.delete(key)

def save_all(redis, iterable):
    try:
        delete_all(redis, REDIS_PREFIX)
        for dict in iterable:
            redis.hmset(REDIS_PREFIX + '@'.join(dict.values()) ,dict)
    except redis.exceptions.ResponseError:
        print('Redis server is not ready. [Skip]')
