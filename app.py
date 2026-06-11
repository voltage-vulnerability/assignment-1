import sqlite3
def search_user(username):
  conn = sqlite3.connect("users.db")
  cursor = conn.cursor()
  query = "SELECT * FROM users WHERE username = '" + username + "'"
  print("Executing:", query)
  cursor.execute(query)
  results = cursor.fetchall()
  conn.close()
  return results
user_input = input("Enter username: ")
print(search_user(user_input))
