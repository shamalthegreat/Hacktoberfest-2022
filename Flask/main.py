from flask import Flask, redirect,render_template,request,url_for,jsonify,flash,session
import json

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
        return render_template('/signup.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        return "Hey Welcome to Hacktober Fest"
    else:
        return render_template('/signup.html')

if __name__ == "__main__":
    app.run(debug=True)