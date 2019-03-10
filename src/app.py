from flask import Flask
import common
import models
# this is a built in varible for a private varible if we are running a project directly
app = Flask(__name__)  #'__main__'

@app.route('/') #www.mysite.com/api
def hello_method():
    return "hello, world"  # this method access the end when we execute it

if __name__== '__main__':
    app.run()

