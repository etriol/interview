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

    def get_top_products_ids (self, quantity:int) -> list:
        sql =   f"select id from stock.products " \
                f"order by rating desc " \
                f"limit {quantity}"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def get_top_products (self, quantity:int) -> list:
        top_products = []
        top_products_ids = self.get_top_products_ids(quantity)
        for id in top_products_ids:
            top_products.append (self.get_product_details(id[0]))
        return top_products
