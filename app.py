import sqlite3
from flask import Flask, request # Simulating a Web Server

app = Flask(__name__)

def search_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # CRITICAL SQL INJECTION: Concatenating string directly into the query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/search")
def web_search():
    # CodeQL knows that URL parameters from the internet are dangerous!
    user_input = request.args.get("username") 
    return str(search_user(user_input))

if __name__ == "__main__":
    app.run()
