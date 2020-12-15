from flask import Flask
import redis
app = Flask(__name__)
pool = redis.ConnectionPool(host='localhost',port=6379,db=0)
r = redis.Redis(connection_pool=pool)
p = r.pubsub()
@app.route('/')
def index():
	return 'hworld'

def handler(msg):
	print(msg)

p.subscribe(**{'myChannel':handler})
p.run_in_thread(sleep_time=.01)
