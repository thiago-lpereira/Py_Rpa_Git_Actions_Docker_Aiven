from flask import Flask
app = Flask(__name__)
@app.route('/')
def devops():
 return '<center><h1><font color=red>Germinare Tech, EU AMO DEVOPS</center>'
def salah():
 return '<center><h1><font color=red>Germinare Tech, EU AMO DEVOPS</center>'
if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
