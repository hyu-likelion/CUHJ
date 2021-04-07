
# def cost_calculator(toppings = [], drinks = [], wings = [], coupon = 0, *pizzas ):
def cost_calculator( *args,**kwargs ):
    # print(args,kwargs)

    total_price = 0.0
    discount = 0.0
    TAX = 0.0625

    pizza_price = 13.0
    toppings_price = { "pepperoni" : 1.00, "mushroom" : 0.50, "olive" : 0.50, "anchovy" : 2.00, "ham" : 1.50 }
    drinks_price = { "small" : 2.00, "medium" : 3.00, "large" : 3.50, "tub" : 3.75 }
    wings_price = { 10 : 5.00, 20 : 9.00, 40 : 17.50, 100 : 48.00 }

    for pizza in args :
        if not pizza :
            total_price += pizza_price
        else :
            total_price += pizza_price
            for topping in pizza: 
                total_price += toppings_price[topping]

    # print('after pizza',total_price)

    try :
        for drink in kwargs['drinks']:
            total_price += drinks_price[drink]
    except KeyError:
        pass

    # print('after drink',total_price)

    try :
        for wing in kwargs['wings']:
            total_price += wings_price[wing]
    except KeyError:
        pass

    # print('after wing',total_price)

    try :
        # discount -= round(total_price * kwargs['coupon'], 2)
        discount -= total_price * kwargs['coupon']
    except KeyError:
        pass

    # TAX = round(total_price * TAX,2)
    TAX = total_price * TAX

    total_price += (discount+TAX)

    # print('after tax and coup',total_price)

    # return total_price
    return round(total_price,2)


# print(cost_calculator([], ["ham", "anchovy"], drinks=["tub", "tub"], coupon=0.1))
# print(cost_calculator(drinks=["small"]))
# print(cost_calculator([], [], ["pepperoni", "pepperoni"], wings=[10, 20], drinks=["small"]))

from bwsi_grader.python.pizza_shop import grader
grader(cost_calculator)