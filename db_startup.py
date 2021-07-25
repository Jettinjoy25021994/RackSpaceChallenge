from db_util import DBUtils


db_util_obj = DBUtils()
db_util_obj.create_product_table()
db_util_obj.insert_product_data()
db_util_obj.create_offer_table()
db_util_obj.insert_offer_data()