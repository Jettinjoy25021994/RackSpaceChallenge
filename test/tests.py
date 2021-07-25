import unittest
from utils import get_total_price


class TestTotalPrice(unittest.TestCase):

    def test_price_basket_1(self):
        basket = ['Chai - $ 3.11', 'Apples - $ 6.0', 'Coffee - $ 11.23']
        expected_prod_list = ['Chai', 'Apples', 'Coffee', 'Milk', 'Coffee']
        tot, final_basket = get_total_price(basket)
        assert tot == 20.34
        assert final_basket == expected_prod_list

    def test_price_basket_2(self):
        basket = ['Milk - $ 4.75', 'Apples - $ 6.0']
        expected_prod_list = ['Milk', 'Apples']
        tot, final_basket = get_total_price(basket)
        assert tot == 10.75
        assert final_basket == expected_prod_list

    def test_price_basket_3(self):
        basket = ['Coffee - $ 11.23']
        expected_prod_list = ['Coffee', 'Coffee']
        tot, final_prod_list = get_total_price(basket)
        assert tot == 11.23
        assert final_prod_list == expected_prod_list

    def test_price_basket_4(self):
        basket = ['Apples - $ 6.0', 'Apples - $ 6.0', 'Chai - $ 3.11', 'Apples - $ 6.0']
        expected_prod_list = ['Apples', 'Apples', 'Chai', 'Apples', 'Milk']
        tot, final_basket = get_total_price(basket)
        assert tot == 16.61
        assert final_basket == expected_prod_list


if __name__ == '__main__':
    unittest.main()