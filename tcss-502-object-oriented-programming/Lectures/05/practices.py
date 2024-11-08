# Create an order system where an order can be in one of three states: Pending, Shipped, or Delivered. Each state should have its own behavior for next_state. Use the State pattern to allow state transitions for an order.
# usage
# order = Order()
# order.proceed()  # Pending -> Shipped
# order.proceed()  # Shipped -> Delivered
# order.proceed()  # Delivered -> No further transition
# The output should be:
# Order is now shipped.
# Order is now delivered.
# Order has already been delivered. No further state transitions.

from abc import abstractmethod

class OrderState:
    @abstractmethod
    def proceed(self):
        pass

class Pending(OrderState):
    def proceed(self):
        print("Order is now shipped.")
        return Shipped()

class Shipped(OrderState):
    def proceed(self):
        print("Order is now delivered.")
        return Delivered()

class Delivered(OrderState):
    def proceed(self):
        print("Order has already been delivered. No further state transitions.")
        return Delivered()


class State:
   @abstractmethod
   def process(self, context):
       pass


class StateA(State):
   def process(self, context):
       print("transition to state B")
       context.current_state = StateB()


class StateB(State):
   def process(self, context):
       print("transition to state C")
       context.current_state = StateC()


class StateC(State):
   def process(self, context):
       print("transition to state A")
       context.current_state = StateA()


class Context:
   def __init__(self):
       self.current_state = StateA()
   def process(self):
       self.current_state.process(self)
   @property
   def state(self):
       return self.current_state


# ctx = Context()
# ctx.process()
# ctx.process()
# ctx.process()
# print(ctx.state)

# Create a payment system where users can choose between CreditCard, PayPal, and Bitcoin as payment methods. Implement the Strategy pattern so that each payment method has a unique pay behavior.
class Payment:
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paying ${amount} with Credit Card")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal")

class BitcoinPayment(Payment):
    def pay(self, amount):
        print(f"Paying ${amount} with Bitcoin")
        
class ShoppingCart:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        
    def checkout(self, amount):
        self.payment_method.pay(amount)
        
# usage
cart = ShoppingCart(CreditCardPayment())
cart.checkout(50)

cart = ShoppingCart(PayPalPayment())
cart.checkout(75)
# The output should be:
# Paying $50 with Credit Card
# Paying $75 with PayPal

# We take 15-min break and get back at 3:15 PM
# Example on the next page:
class Sorter:
   def __init__(self, array):
       self.__array = array
   def sort(self):
       pass


class MergeSorter(Sorter):
   def __init__(self, array):
       super().__init__(array)
       self.__name = "Merge"
   def sort(self):
       print("using the mergesort algorithm")


class QuickSorter(Sorter):
   def __init__(self, array):
       super().__init__(array)
       self.__name = "Quick"
   def sort(self):
       print("using the quicksort algorithm")


# client side
import timeit
array = [3, 3, 2, 123, 23, 32, 13, 23, 123, 231]
for algorithm in [MergeSorter(array), QuickSorter(array)]:
   clock = timeit.default_timer()
   algorithm.sort()
   print("Time taken:", timeit.default_timer() - clock)