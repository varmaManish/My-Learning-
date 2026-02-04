'''Encapsulation = Wrapping data and the methods that use that data into a single unit (a class), and controlling how the outside world can access it.

You don’t let random code reach inside and break your object’s state.
You expose safe, intentional entry points.

# suppose in bank acc you cannot modify direct to the bacnk balance
 you have to method to update balance
 1) deposit()
 2)withdraw()
  after this actions we can modify the balance

'''
class Bank:
    def __init__(self):
        self.__balance=890
    def show(self):
        print(f"balance:{self.__balance}")
    def withdraw(self,ammont):
        self.ammount=ammont
        if ammont>self.__balance:
            return "ammout must be less than balance"
        if ammont>0:
             self.__balance-=ammont
    
        
    
B1=Bank()
B1.show()
B1.withdraw(800)   
B1.show()
