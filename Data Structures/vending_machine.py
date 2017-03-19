"""
Vending Machine

Introduction

A vending machine is a machine that dispenses items such as snacks and
beverages to customers automatically, after the customer inserts currency
or credit into the machine. The first modern vending machines were developed
in England in the early 19th century and dispensed postcards. (Source Wikipedia)


Task

In this simple Kata aimed at beginners your task is to recreate a vending machine.
You will have to make a class called VendingMachine with at least one method
called vend. On creation of a new instance of VendingMachine the items Array
and Initial vending machine money is passed. The vend method should take two
arguments 1. Selection code of the item (not case sensitive) and 2. Amount of
money the user inserts into the machine.

An example call of the vend method

machine.vend("A01", 0.90)
where the selected item is A01 and the money given to the machine is 90p

An example of the items Array is below

items = [{'name':"Smarties", 'code':"A01", 'quantity':10, 'price':0.60},
         {'name':"Caramac Bar", 'code':"A02", 'quantity':5, 'price':0.60},
         {'name':"Dairy Milk", 'code':"A03", 'quantity':1, 'price':0.65},
         {'name':"Freddo", 'code':"A04", 'quantity':1, 'price':0.25}];

Rules

1. If the money given to the machine is less than the item cost return "Not enough money!"

2. If the quantity is 0 for an item return "Item Name: Out of stock!".
   Where "Item Name" is the name of the item selected.

3. If an item is correctly selected return "Vending Item Name with 9.40 change.".
   Where "Item Name" is the name of the item and change if any given.

4. If an item is correctly selected and there is no change needed then return
   "Vending Item Name". Where "Item Name" is the name of the item.

5. If an invalid item is selected return "Invalid selection! : Money in
   vending machine = 11.20". Where 11.20 is the machines money float.

6. If a selection is successful then the quantity should be updated.

7. The vending machine never runs out of money for simplicity however you will
   need to keep track of the amount of money in the machine at anytime

8. Change is always given to 2 decimal places ie 7.00
"""
import sys
sys.path.append('..')

from helpers.test_wrapper import Test


class VendingMachine(object):
    """Vending machine implementation"""

    def __init__(self, items, money):
        self.items = items
        self.money = money

    def vend(self, selection, item_money):
        selection = selection.upper()
        for product in self.items:
            if product['code'] == selection:
                if product['price'] > item_money:
                    return 'Not enough money!'
                elif product['quantity'] == 0:
                    return '{}: Out of stock!'.format(product['name'])
                elif product['price'] == item_money:
                    self.money += item_money
                    product['quantity'] -= 1
                    return 'Vending {}'.format(product['name'])
                else:
                    self.money += product['price']
                    product['quantity'] -= 1
                    return 'Vending {} with {:.2f} change.'.format(
                        product['name'],
                        item_money - product['price'])
        return 'Invalid selection! : Money in vending machine = {:.2f}'.format(self.money)


def run_tests():

    items = [{'name': "Smarties", 'code': "A01", 'quantity': 10, 'price': 0.60},
             {'name': "Caramac Bar", 'code': "A02", 'quantity': 5, 'price': 0.60},
             {'name': "Dairy Milk", 'code': "A03", 'quantity': 1, 'price': 0.65},
             {'name': "Freddo", 'code': "A04", 'quantity': 1, 'price': 0.25},
             {'name': 'Cheese and Onion Crisps', 'code': 'B06', 'quantity': 0, 'price': 5}]

    with Test() as test:
        test.describe("Example tests")

        machine = VendingMachine(items, 10.0)
        test.it("Should return 'Vending Smarties'")
        test.assert_equals(machine.vend("A01", 0.60), "Vending Smarties")
        test.it("Should return 'Vending Smarties with 9.40 change.'")
        test.assert_equals(machine.vend("A01", 10.0),
                           "Vending Smarties with 9.40 change.")
        test.it("Should return 'Invalid selection! : Money in vending machine = 11.20'")
        test.assert_equals(machine.vend(
            "Z01", 0.41), "Invalid selection! : Money in vending machine = 11.20")
        test.it("Should return 'Not enough money!'")
        test.assert_equals(machine.vend("a02", 0.40), "Not enough money!")
        test.it("Should return 'Cheese and Onion Crisps: Out of stock!'")
        test.assert_equals(machine.vend("B06", 4.60),
                           "Cheese and Onion Crisps: Out of stock!")


if __name__ == '__main__':
    run_tests()
