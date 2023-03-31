'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            net += check_payment_input(item.amount)
        elif item.type == 'product':
            input_validated = check_product_input(item_quantity=item.quantity, item_amount=item.amount)
                        
            net -= input_validated
        else:
            return("Invalid item type: %s" % item.type)
    
    print(f"net:{net}")
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)

def check_payment_input(value: int):
    max_reinbusement_value = -10000
    
    if value > max_reinbusement_value and value < 10000:
        return value
    else:
        return 0
    
def check_product_input(item_quantity: int, item_amount: int):
    maximum_quantity = 5
    max_item_amount = 10000
    
    if item_quantity > 0 and item_quantity <= maximum_quantity and item_amount > 0 and item_amount <= max_item_amount:
            return item_amount * item_quantity
        