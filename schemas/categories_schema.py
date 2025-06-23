def serialize_category(row):
    return {
        "id": row[0],
        "name": row[1],
        "description": row[2]
    }
