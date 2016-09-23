from flask import Flask
import os
application = Flask(__name__)

@application.route('/info')
def info():
   return str(os.uname())

@application.route('/')
@application.route('/index.html')
def works():
   return str("It works!")

def main():
   application.run(host='0.0.0.0')

if __name__ == '__main__':
   main()
