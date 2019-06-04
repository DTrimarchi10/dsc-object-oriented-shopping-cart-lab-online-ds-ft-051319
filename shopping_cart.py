class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
      self.total = 0
      self.employee_discount = emp_discount
      self.items = []

    def add_item(self, name, price, quantity=1):
      for i in range(quantity):
        self.items.append({'name': name, 'price': price})
        self.total+=price
      return self.total

    def mean_item_price(self):
      return self.total/len(self.items)

    def median_item_price(self):
      sorted_list = sorted(self.items, key=lambda item: item['price'])
      list_length = len(self.items)
      if list_length%2 == 0:
        val1 = sorted_list[list_length/2]['price']
        val2 = sorted_list[(list_length/2)-1]['price']
        return (val1+val2)*0.5
      else:
        return sorted_list[list_length//2]['price']

    def apply_discount(self):
      if self.employee_discount:
        return self.total*(1-(self.employee_discount/100))
      else:
        return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
      if len(self.items)==0:
        return "There are no items in your cart!"
      else:
        self.total-=self.items[-1]['price']
        self.items.pop()