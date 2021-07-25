from collections import Counter
from flask import Flask, render_template, jsonify, request
from db_util import DBUtils
from utils import get_total_price, get_offers_data

app = Flask(__name__)
db_utils_obj = DBUtils()
@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        basket = request.form.getlist('product[]')
        total_price, final_basket = get_total_price(basket)
        final_products, counts = zip(*dict(Counter(final_basket)).items())
        return render_template("basketsummary.html",
                                    total_price=total_price,
                                    final_products=zip(final_products, counts)
                                    )
    product_data = [product[0] + " - $ " + str(product[1]) 
                        for product in db_utils_obj.select_product_data()]
    offers = db_utils_obj.select_offer_data()
    applicable_offers, offer_desc = get_offers_data(offers)
    return render_template('index.html', product_data=product_data,
                            applicable_offers=zip(applicable_offers, offer_desc))
       