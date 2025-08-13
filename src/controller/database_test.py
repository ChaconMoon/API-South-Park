from sqlalchemy import text
from src.controller.database_connection import get_query_result


# Connection with the database
def test_database():
    rows = dict()
    try:
        query_result = get_query_result(text("SELECT version()"))
        for row in query_result:
            rows["version"] = str(row[0])
            rows["status"] = "connected"
    except Exception as e:
        rows["error"] = str(e)
        rows["status"] = "failed"
    return rows
