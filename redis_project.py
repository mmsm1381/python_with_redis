import redis

r = redis.Redis("localhost","6379",charset="utf-8", decode_responses=True,db=1)
