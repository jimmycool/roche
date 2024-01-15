from flask import Flask,request, json  # From 'flask' module import 'Flask' class
import requests
app = Flask(__name__)    # Construct an instance of Flask class for our webapp
import numpy as np
import os
import subprocess
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
r={"POST":0,"GET":0,"PUT":0}
app.config['CORS_HEADERS'] = 'Content-Type'
'''def fio_test():
    g=""
    file1="out.txt"
    file2="err.txt"
    with open(file1,"w+") as e, open(file2,"w+") as d:
        try:
            v=subprocess.Popen(["fio","random-read.fio"],stdout=e,stderr=d)
        except Exception as ex:
            return (ex)
   
    return "completed"
'''    
@app.route('/test', methods = ['POST'])  
@cross_origin()
def main():
    """Say hello"""
    r["POST"]=r["POST"]+1
    i1=int(request.form.to_dict()["int1"])
    i2=int(request.form.to_dict()["int2"])
    i3=int(request.form.to_dict()["limit"])
    s1=request.form.to_dict()["str1"]
    s1=request.form.to_dict()["str2"]
    s=[]
    for i in  range(1,int(i3)+2,1):
        if(i%(i1*i2)==0):
            s.append("fizzbuzz")
        elif(i%i1==0):
            s.append("fizz")
        elif(i%i2==0):
            s.append("buzz")
        else:
            s.append(str(i))    
    return str(s)              
@app.route('/',methods=['Get'])
def home():
   r["GET"]+=1 
   return json.dumps(r)



if __name__ == '__main__':
   port = os.environ.get('FLASK_PORT')
   #port = int(port)
   #app.run(port=port,host='0.0.0.0')   
   app.run(debug=True)