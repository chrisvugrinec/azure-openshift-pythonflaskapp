from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, db=0, password='123QWEasd', socket_timeout=None, connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None)
#redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
