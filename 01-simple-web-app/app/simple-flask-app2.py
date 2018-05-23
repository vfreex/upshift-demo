from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World, ' + os.environ['MY_ENV_VAR'] 

if __name__ == '__main__':
   app.run()

