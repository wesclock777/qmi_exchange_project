import datetime
import copy


# this is the main file you will be editing -> feel free to change the structure or methods

# Exchange Object (used to run the exchange)
class Exchange:
    # think about what types of datastructures you need to store the state of the
    # system
    def __init__(self):
        pass

    # finds orders related to traderid
    def ret_orders(self, traderid):
        pass

    # adding an order from json dict
    def add_order(self, traderid, initialdata):
        pass

    # adding an order from order object
    def add_order_obj(self, order):
        pass

    # fill the orders and mark them as filled
    def fill_orders(self, order):
        pass

# order object to respresent a listing
class Order:
    def __init__(self, initialdata, traderid):
        # sets symbol, quantity, and orderType
        pass
    # formats the order for output as a json
    def ret(self):
        pass

    # marks an order as filled
    def fill(self):
        pass
