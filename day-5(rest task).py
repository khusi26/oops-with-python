#OOPR-ASSGN-30

types=['small','medium','small','medium']
class customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name.title()
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity

class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in types:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and customer.validate_quantity(self.__customer):
            print("its entering")
            if self.__pizza_type.title()=="small":
                print(self.__pizza_type)
                self.pizza_cost=150 * customer.get_quantity(self.__customer)
                print(self.pizza_cost)
                if self.__additional_topping:
                    self.pizza_cost+=35 * customer.get_quantity(self.__customer)
            if self.__pizza_type=="medium":
                self.pizza_cost=200 * customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=50 * customer.get_quantity(self.__customer)
            if not self.__service_id:
                self.__service_id=self.__pizza_type[0] + str(Pizzaservice.counter+1)
                Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping
    
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms = distance_in_kms
        Pizzaservice.__init__(self,customer,pizza_type,additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                distance=1
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost +=5
                    if distance in range(6,11):
                        self.pizza_cost += 7
                    distance += 1
        else:
            self.pizza_cost = -1
    def get_delivery_charge(self):
        return self._delivery_charge
    def get_distance_in_kms(self):
        return self._distance_in_kms
c=customer("Asha",5)
p1 = Pizzaservice(c,"medium",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1 = Doordelivery(c,"medium",True,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())

#d6-task1
'''
class PrivilegedCustomer(Customer):
    def _init_(self, customer_id, customer_name, age, account, bonus_points):
        super()._init_(customer_id, customer_name, age, account)
        self.bonus_points = bonus_points
    
    def increase_bonus(self):
        if self.account.balance > 1000:
            self.bonus_points += 10
        else:
            self.bonus_points += 2
    
    def withdraw(self, amount):
        try:
            super().withdraw(amount)
        except OverdrawException as e:
            print(e)
        except LimitReachedException as e:
            print(e)
        else:
            self.increase_bonus()
            print(f"Bonus points: {self.bonus_points}")
        finally:
            self.take_card()
account = Account("Savings", 1000, 500)
p_customer = PrivilegedCustomer(100, "Gopal", 43, account, 100)
p_customer.withdraw(100)                 

'''















                 
                 









                
            
