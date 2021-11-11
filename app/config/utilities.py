def add_column_fields(query, data):
    query += " ("
    for (key, _) in data:
        query += f" {key}, "
    query = query[:-2] + ") "
    return query

def add_value_fields(query, data):
    query += " ("
    for (_, value) in data:
        query += " ?, "
    query = query[:-2] + ") "
    return query