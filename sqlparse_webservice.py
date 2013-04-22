from flask import Flask, make_response

from legacy import legacy

app = Flask(__name__)
app.register_blueprint(legacy)

@app.route('/ping')
def ping():
    return make_response('pong')

@app.route('/_ah/warmup')
def warmup():
    return make_response('polishing chrome')

if __name__ == '__main__':    
    app.run(host='0.0.0.0')

