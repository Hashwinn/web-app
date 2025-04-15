from flask import Flask, render_template, request
import requests

print("Starting Flask App...")


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        response = requests.post('http://backend:5000/login', json={
            "username": request.form['username'],
            "password": request.form['password']
        })
        if response.status_code == 200:
            return render_template('success.html', username=request.form['username'])
        return "Login Failed", 401
    return render_template('login.html')
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

