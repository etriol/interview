import psycopg2

class database:
    def __init__(self, host, port='5432', database='postgres', user='postgres', password='postgres'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def open_connection (self):
        self.connection = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)

    def close_connection (self):
        self.connection.close()

    def get_product_details (self, product_id:int) -> list:
        sql =   f"select name, price, image_url, description from stock.products " \
                f"where id = {product_id}"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result[0]
