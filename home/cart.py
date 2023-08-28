from decimal import Decimal
from .models import *

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})
        
    def add_item(self, item, quantity=1):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'quantity': 0,
                'price': str(item.price),
                'title' : str(item.title),
            
                
            }
        self.cart[item_id]['quantity'] += quantity
        
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
        
    def remove_item(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def get_items(self):
        return self.cart.items()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def get_total(self):
        total = 0
        for item_id, item_data in self.cart.items():
            total += Decimal(item_data['price']) * item_data['quantity']
        return total
    
    def get_subtotal(self, item_id):
        item_data = self.cart.get(str(item_id), {})
        quantity = item_data.get('quantity', 0)
        price = Decimal(item_data.get('price', '0'))
        return quantity * price
    

    def create_order(self, user):
        order = Order.objects.create(user=user, total_amount=self.get_total())
        for item_id, item_data in self.cart.items():
            item = Item.objects.get(id=int(item_id))
            OrderItem.objects.create(order=order, item=item, quantity=item_data['quantity'], price=item.price)
        self.clear()
        return order
    
