from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis.chris1.svc', port=6379)

# bugfix
try:
    username = getpass.getuser()
except KeyError:
    username = str(os.getuid())
tempdir = os.path.join(tempdir, 'matplotlib-%s' % username)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
