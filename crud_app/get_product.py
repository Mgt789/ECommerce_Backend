from app import db_config
import mysql.connector

@app.route("/products", methods=["GET"])
def get_products():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM E_commerce.products")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()

    products=[{"id":row[0], "name":row[1],"description":row[2], "price":row[3], "stock":row[4]} for row in rows]
    return jsonify(products)

if __name__=="__main__":
    app.run(debug=True)