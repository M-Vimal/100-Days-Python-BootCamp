MENU = {
    'espresso':{
        "ingrediants":{
            'water':50,
            'coffee':18
        },
        "cost":100
    },
    'latte':{
        "ingrediants":{
            'water':200,
            'coffee':24,
            'milk':150
        },
        "cost":180
    },
    'capacino':{
        "ingrediants":{
            'water':250,
            'coffee':24,
            'milk':100
        },
        "cost":250
    }
}

RESOURCES = {
    'water':300,
    'milk':200,
    'coffee':100
}

profit = 0

#check resources
def checkResource(order):
    ingredients = MENU[order]['ingrediants'] 
    for item in ingredients:
        if RESOURCES[item] < ingredients[item]:
            return False
    # Reduce resources if all ingredients are sufficient
    for item in ingredients:
        RESOURCES[item] -= ingredients[item]
    return True

def pay():
    one_rupee = int(input("How many 1 rupee's"))
    ten_rupee = int(input("How many 10 rupee's"))
    fifty_rupee = int(input("How many 50 rupee's"))
    hundred_rupee = int(input("How many 100 rupee's"))
    total = (one_rupee*1)+(ten_rupee*10)+(fifty_rupee*50)+(hundred_rupee*100)
    return total




def order_amount(order):
    return MENU[order]['cost']


def start_game():
    global profit
    start = False
    while not start:
        order = input("What would you like? (espresso/latte/cappuccino):")
        if order == 'off':
            start = True
            break
        if order == 'report':
            print(RESOURCES)
        else:
            ready  = checkResource(order)
            if ready:
                print("please insert coins")            
                total = pay()
                order_price = order_amount(order)
                profit += order_price
                if total > order_price:
                    print(f"here is your change {total-order_price}.enjoy your {order}")
                elif total==order_price:
                    print(f"enjoy your {order}")
                else:
                    print(f"{order} is {order_price} .you give only {total}")
            else:
                print("sorry,Not enogh resources")
                start = True
start_game()

