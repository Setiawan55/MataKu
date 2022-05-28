#import modul yang dibutuhkan, sementara ini dulu
from flask import Flask, request, jsonify

app = Flask(__name__)

#LOAD MODEL
"""
model=load_model('namamodel')
"""

"""
BUAT ROUTING DAN HANDLER
formatnya :
@app.route('/namaroutenya', methods=['namamethodnya'])
def handler():
    disini ditulis cara kita ngehandle / fungsinya        
"""

#contoh
@app.route("/")
def handler1():
    return "You call this API from root"


@app.route("/photopost", methods=['POST'])
def handler2():
    var1=request.form.get('var1')
    return jsonify({'result of the pict' :str(var1)})

    """
    cara deploy model :
    result = model.predict()
    return result"""

@app.route("/photoget", methods=['GET'])
def handler3():
    return "here's the prediction you want"

#untuk ngerun
if __name__ == '__main__':
    app.run()