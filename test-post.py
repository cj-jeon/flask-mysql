from flask import Flask, request, Response
import json, requests  

app = Flask(__name__)

@app.route('/xxx',  methods = ['POST']) 
def xxx():
    print('got data: {}'.format(request.json))
    return Response()

@app.route("/yyy", methods=["POST"])
def yyy():
    dicts = {"key1": "value1"}
    rrr = requests.post(url="http://localhost:5000/xxx", json=dicts)
    print( rrr )
    return "aaa"

if __name__ == "__main__":
    app.run(debug=True)


## curl -X POST http://localhost:5000/yyy
## aaa
