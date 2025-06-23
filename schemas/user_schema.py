def serialize_user(row):
    return {
        'id': row[0],
        'name': row[1],
        'email': row[2]
    }
