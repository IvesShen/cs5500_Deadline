from flask import Flask, request, jsonify
from restfultools import *

app = Flask(__name__)

#data source
datas = [{''}]

#DELETE
@app.route('your_url', methods=['DELETE'])
def deleteMethod(name):
    result = [data for data in datas if data['name'] == name]
    if len(result) == 0:
        return statusResponse(R404_NOTFOUND)
    datas.remove(result[0])
    return statusResponse(R204_NOCONTENT)
