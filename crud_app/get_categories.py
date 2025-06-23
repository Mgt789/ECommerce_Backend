from app import db_config
import mysql.connector

@app.route("/category", methods=["GET"])
def get_category():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM E_commerce.categories")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()

    category=[{"id":row[0], "name":row[1],"description":row[2]} for row in rows]
    return jsonify(category)

if __name__=="__main__":
    app.run(debug=True)