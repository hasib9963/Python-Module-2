balance = 3000 # Global variables

def buy_things(item, price):
    # local scope variables
    global balance
    print(f'previous balance value', balance)
    balance = balance - price
    print( f'Balance inside the Buying {item}', balance)

buy_things('sunglass', 1000)
