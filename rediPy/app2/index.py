from flask import Flask
import redis
app = Flask(__name__)
pool = redis.ConnectionPool(host='localhost',port=6379,db=0)
r = redis.Redis(connection_pool=pool)

@app.route('/')
def index():
    r.publish('myChannel','Beta Rays Split Through')
    return "Hworld"
