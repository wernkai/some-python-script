"""
Purpose: a class for pytest testing
"""
class Cart:

    def __init__(self, customer:str):
      self.customer = customer
      self.cart = []

    def add_item(self, item:str):
        notification = ''
        try:
          self.cart.append(item)
          notification = 'Item added successful' 
        except:
          notification = 'Fail to add item'
        finally:
           return notification
