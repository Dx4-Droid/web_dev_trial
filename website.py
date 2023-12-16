from flask import Flask, render_template

test = Flask(__name__)

@test.route('/')
def hello(): 
  return "Hello World"

if __name__ == "__main__":
  test.run(host='0.0.0.0', debug=True)