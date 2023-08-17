"""
Purpose: Use Pytest to perform basic functional test
"""
import pytest
from Cart import Cart

# order.add_item('bread')
# order.add_item('jam')
# order.add_item(123)
# order.add_item(['coffee','tea'])
# order.add_item('noodle')

class TestClass:
    
    def test_integer(self):
        self.order = Cart(customer='Kai')
        assert self.order.add_item(123) == 'Fail to add item'
    
    def test_string(self):
        self.order = Cart(customer='Kai')
        assert self.order.add_item('bread') == 'Item added successful'
