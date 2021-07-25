"""
Module that contains DB Related utilities
Created By: Jettin Joy
Created On: 07/24/2021
"""


import os
import psycopg2


class DBUtils:
    """Class with db utility methods"""
    def __init__(self):
        self.db = os.environ.get("POSTGRES_DB")
        self.user = os.environ.get('POSTGRES_USER')
        self.password = os.environ.get("POSTGRES_PASSWORD")
        self.host = os.environ.get("DB_SERVICE")
        self.port = os.environ.get("DB_PORT")

    def db_connect(self):
        """Connect to the db
        Parameters: None
        Returns:
            connction (psycopg2.connect): A connection object to the database
            
        """
        conn = None
        try:
            conn = psycopg2.connect(user=self.user,
                                  password=self.password,
                                  host=self.host,
                                  port=self.port,
                                  database=self.db)
        except psycopg2.Error as e:
            print(f"Cannot connect to database error occured {str(e)}")
        else:
            print(f"Connected to {self.db}")
        return conn
    
    def create_product_table(self):
        """Create the DB table"""
        conn = self.db_connect()
        if conn:
            sql = """
                  CREATE TABLE IF NOT EXISTS product(
                      product_code text PRIMARY KEY,
                      product_name text NOT NULL,
                      price REAL NOT NULL
                  );
                  """
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            print(f"created table product")
        else:
            raise psycopg2.Error("No DB Created Program terminated")
    
    def insert_product_data(self):
        """Insert data into the table"""
        conn = self.db_connect()
        if conn:
            cur = conn.cursor()
            with open('product_data.csv', 'r') as pd:
                next(pd)
                cur.copy_from(pd, 'product', sep=',')
            conn.commit()
        else:
            raise psycopg2.Error("Error in inserting data")
    
    def select_product_data(self):
        conn = self.db_connect()
        product_data = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT product_name, price FROM product")
            product_data = cur.fetchall()
        else:
            print("an error occured")
        return product_data

    def create_offer_table(self):
        """Create the offers table"""
        conn = self.db_connect()
        if conn:
            sql = """
                  CREATE TABLE IF NOT EXISTS offer(
                      offer text PRIMARY KEY,
                      description text NOT NULL
                  );
                  """
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            print(f"created table product")
        else:
            raise psycopg2.Error("No DB Created Program terminated")

    def insert_offer_data(self):
        """Insert data into the table"""
        conn = self.db_connect()
        if conn:
            cur = conn.cursor()
            with open('offer.csv', 'r') as pd:
                next(pd)
                cur.copy_from(pd, 'offer', sep=',')
            conn.commit()
        else:
            raise psycopg2.Error("Error in inserting data")

    def select_offer_data(self):
        conn = self.db_connect()
        offer_data = []
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT offer, description FROM offer")
            offer_data = cur.fetchall()
        else:
            print("an error occured")
        return offer_data
