from flask import Flask,render_template,request,jsonify
from celery import Celery
import time

app = Flask(__name__)
app.config['SECRET_KEY']='1245'
app.config['CELERY_BROKER_URL']='redis://localhost:6379/0'
app.config['result_backend']='redis://localhost:6379/0'
celery = Celery(app.name,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

if __name__=="__main__":
    app.run(debug=True)

@app.route('/a')
def index():
    task = check.apply_async(args=["somevalue"])
    return jsonify({'state':'http://127.0.0.1:5000/status/'+task.id})

@app.route('/status/<taskid>')
def status(taskid):
    task = check.AsyncResult(taskid)
    return task.info['STATE']

@celery.task(bind=True)
def check(self,x):
    i=100
    while i:
        time.sleep(1)
        self.update_state(state="PROGRSS",meta={"item":i})
        i=i-1
    
    return {"STATE":"SUCCESS","meta":{"item":12}}