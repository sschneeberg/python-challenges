users = {
    "Bob": 4000,
    "Jane": 500000,
    "Sally": 8
}

def showBalance(user): 
    amount = users[user]
    print(f"Your balance is {amount}")
    return 


def deposit(user):
    print("how much would you like to deposit?")
    amount = input()
    users[user] = users[user] + int(amount)
    showBalance(user)
    return

def withdraw(user):
    print("how much would you like to withdraw?")
    amount = input()
    users[user] = users[user] - int(amount)
    showBalance(user)
    if (users[user] < 0): print(f'You now owe us {users[user]}')
    return



actions = {
    "deposit" : deposit,
    "withdraw" : withdraw,
    "check balance" : showBalance
}


def bank():
    print("Welcome to Chase bank.")
    print("Please enter your name: ")
    user = input()
    if (user in users): 
        showBalance(user)
        print("What would you like to do? (deposit, withdraw, check balance)")
        action = input()
        if (action in actions): actions[action](user)
        else: 
            print('Invalid option')
            print("Have a nice day!")
            return
    else: 
        print('We do not have a record for that account')
        print("Have a nice day!")
        return
    print("Have a nice day!")
    return

bank()