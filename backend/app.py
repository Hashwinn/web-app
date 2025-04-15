from flask import Flask, request, jsonify
import mysql.connector

print("Starting Flask App...")

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql',
        user='root',
        password='rootpass',
        database='userdb'
    )

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (data['username'], data['password']))
    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify({"message": f"Hello {data['username']}"}), 200
    return jsonify({"message": "Invalid credentials"}), 401
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

