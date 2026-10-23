import mysql.connector

class db_connect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "AlthafSQL@123",
                database ="shop-DB"
            )
            return self.connection
        except Exception as e:
            print("Connection Error")
            return None

class ProductManager(db_connect):
    def get(self):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()
        query = "select * from product"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for r in result:
            print(r)

    def post(self,**kwargs):
        query = "insert into product(name,category,price,quandity,manufacturer) values(%s,%s,%s,%s,%s,%S)"
        values = [v for v in kwargs.values()]
        self.cursor.execute(query,values)
        self.connect.commit()
        print("Added successfully")

    def get_object(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connection.cursor()
            query = "select * from product where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self .cursor.fetchone()
            return record
        except Exception as e:
            return None
    def delete(self,id = None):
        try:
            records = self.get_object(id = id)
            values=(id,)
            if records!=None:
                query = "delete from products where id = %s"
                self.cursor.execute(query,values)
                self.connection.commit()
print("Deleted successfully..")



connection_instance = db_connect()
product_instance = ProductManager()
product_instance.get()