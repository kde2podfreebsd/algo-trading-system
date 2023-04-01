from redis import Redis
import pickle
import configparser
import os

basedir = os.path.abspath(os.path.dirname(__file__))

config = configparser.ConfigParser()
config.read(f"{basedir}/../config.ini")

class redisInstance(object):

    redis = Redis(host=config['Redis']['host'], port=int(config['Redis']['port']))

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(redisInstance, cls).__new__(cls)
        return cls.instance

    def push_context(self, chat_id: int, context):
        context = pickle.dumps(context)
        self.redis.rpush(chat_id, context)
        c = self.redis.lrange(chat_id, 0, -1)

        try:
            for i in c:
                print(pickle.loads(i))
        except Exception:
            pass



r = redisInstance()
r.push_context(chat_id=12345, context={"ticker": 123, "context": {"1":{}, 2: {}}})
