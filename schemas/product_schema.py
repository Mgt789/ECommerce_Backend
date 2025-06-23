def serialize_product(row):
    return {
        "id": row[0],
        "name": row[1],
        "description": row[2],
        "price": row[3],
        "stock": row[4],
    }
