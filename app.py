from flask import Flask, render_template,request,jsonify, url_for
import os
import random
import subprocess


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/output',methods=['GET', 'POST'])
def output():
    if request.method == "POST":
        url = request.get_json()
        results = url
        print(results['code'])
        random_name = random.randint(0, 50)
        path_file = "./files/{0}.f90".format(random_name)
        file1 = open("{0}".format(path_file), "w") 
        file1.write(results['code'])
        file1.close()
        
        command = ['gfortran',path_file, '-o', './files/output/{0}'.format(random_name)]
        subprocess.check_call(command)
        final = subprocess.check_output([ './files/output/{0}'.format(random_name)]).decode()
        print(str(jsonify(final)))



    return jsonify(output=final)

if __name__ == '__main__':
    app.run()