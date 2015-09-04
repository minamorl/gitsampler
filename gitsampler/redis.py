import redis

def get_redis():
    return redis.Redis(host='localhost', port=6379, db=0)

def save_all(redis, iterable):
    redis.flushall()
    for dict in iterable:
        redis.hmset(' '.join(dict.values()) ,dict)
