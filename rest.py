from flask import Flask, request, jsonify, render_template, Blueprint
from restfultools import *

rest = Blueprint('rest',__name__)

#data source
datas = [{''}]

#MAIN ROUTE
@rest.route('/')
def hello_world():
   return 'Hello, World!'

#DELETE
@rest.route('/your_url', methods=['DELETE'])
def deleteMethod(name):
    result = [data for data in datas if data['name'] == name]
    if len(result) == 0:
        return statusResponse(R404_NOTFOUND)
    datas.remove(result[0])
    return statusResponse(R204_NOCONTENT)

#UPDATE
@rest.route('/cs5500/update', methods=['GET', 'POST'])
def update_draft():
    if request.method == 'POST':
        return render_template('update.html', status = 'It is updated!')
    else:
        return render_template('update.html', status = 'It is not updated...')


