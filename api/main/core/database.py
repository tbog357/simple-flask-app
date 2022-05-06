import psycopg2


class PostgresClient:
    def __init__(self, dbname: str) -> None:
        self.connection = psycopg2.connect(
            host="localhost",
            dbname=dbname,
            user="postgres",
            password="root",
            options="-c search_path=public",
        )

    def get_query_result(self, query: str):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query=query)
            result = cursor.fetchall()
            self.connection.commit()
            return result
        except Exception as error:
            print(f"Error: '{error}'")
            return None