import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. HARDCODED SECRET VULNERABILITY1
# CodeQL / Secret Scanning will flag this as an exposed credential risk.
API_SECRET_KEY = "xoxb-123456789012-345678901234-vulnerablesecretkeyabc123"

@app.route("/profile")
def user_profile():
    # Fetching input parameters directly from the URL query string
    user_id = request.args.get("id")
    custom_theme = request.args.get("theme", "default")

    # 2. SQL INJECTION (SQLi) VULNERABILITY
    # Vulnerable because it builds the query string dynamically using raw input.
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM accounts WHERE id = '{user_id}'"
    cursor.execute(query)
    user_data = cursor.fetchone()
    conn.close()

    # 3. REFLECTED CROSS-SITE SCRIPTING (XSS) VULNERABILITY
    # Vulnerable because it renders raw user input directly into HTML without escaping it.
    html_template = f"""
    <html>
        <body>
            <h1>Welcome back, user!</h1>
            <p>Your current active UI theme is: {custom_theme}</p>
        </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
