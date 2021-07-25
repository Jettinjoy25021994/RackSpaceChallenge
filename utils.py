from collections import Counter


def get_total_price(basket):
    """
    Compute the total basket price after offer
    Parameters:
        basket (list of product with price): a list of items in basket
        offers (list): a list of applicable ofers
    """
    products, prices = zip(*[[item.split(" ")[0],  float(item.split(" ")[3])] for item in basket])
    totat_price = sum(prices)
    product_counts = dict(Counter(products))
    apple_count = product_counts.get('Apples', 0)
    final_products = list(products)
    chai_offer_applied = False
    apple_offer_applied = False
    for product in products:
        if product_counts.get('Apples', 0) >= 3 and not apple_offer_applied:
            totat_price -= 4.50
            apple_offer_applied = True
        if product == 'Chai' and not chai_offer_applied:
            final_products.append('Milk')
            chai_offer_applied = True
        if product == 'Oatmeal' and apple_count > 0:
            totat_price -= 0.75
            apple_count -= 1
        if product == 'Coffee':
            final_products.append('Coffee')
    return totat_price, final_products


def get_offers_data(offers):
    """
    Get the offer data applicable
    Parameters:
        basket (list): a list of products
    Returns:
        offers (list): a list of applicable products
    """
    offer, desc = zip(*[(item[0], item[1]) for item in offers])
    return offer, desc
