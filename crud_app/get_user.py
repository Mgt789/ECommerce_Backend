from app import db_config
import mysql.connector

@app.route("/users", methods=["GET"])
def get_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    users = [{"id": row[0], "name": row[1], "email": row[2]} for row in rows]
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
