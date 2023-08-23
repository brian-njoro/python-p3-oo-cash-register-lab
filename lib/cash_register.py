#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount,total = 0):
    self.discount = discount
    self.total = total
    self.items = []

  def add_items(self, item, price ,quantity=1):
    for quantity in range(quantity):
      self.items.append(item)
    self.total +=(price * quantity)
    return self.total

  def apply_discount(self):
    if self.discount > 0:
      self.total -= (self.discount/100 * self.total)
      return self.total
    else:
      print("No discount available")

  
  #uncertain
  # def void_last_transaction(self):
  #       if self.items:
  #           last_item_price = self.total(self.items.pop())
  #           self.total -= last_item_price

  def get_item_price(self,item):
    if len(self.items)  ==  0:
      self.total = 0
      return self.total 

