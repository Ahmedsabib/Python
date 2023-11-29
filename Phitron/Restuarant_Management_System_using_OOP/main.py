from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from User import Chef, Customer, Server, Manager
from Order import Order

def main():
    menu = Menu()

    pizza_1 = Pizza('Shutki Pizza', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)


    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)


    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha', 300, False)
    menu.add_menu_item('drinks', coffee)

    menu.show_menu()

    restaurant = Restaurant('Sai Baba Restaurant', 2000, menu)

    manager = Manager('kala Chan Manager', 5, 'kalachan@chan.com', 'kaliapur', 1500, '1st November 2021', 'core')
    restaurant.add_employee('manager', manager)

    chef = Chef('Rustom Baburchi', 6, 'chupa@rustom.com', 'rustomNaar', 3500, '1st November 2021', 'Chef', 'everything')
    restaurant.add_employee('chef', chef)

    server = Server('Chotu server', 6, 'nai@jai.com', 'restaurant', 200, '1st November 2021', 'server')
    restaurant.add_employee('server', server)

    restaurant.show_employees()

    customer_1 = Customer('Sakib Khan', 6, 'king@khan.com', 'banani', 10000)
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    restaurant.receive_payment(order_1, 2000, customer_1)

    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rent', restaurant.revenue, restaurant.balance, restaurant.expense)

if __name__ == '__main__':
    main()