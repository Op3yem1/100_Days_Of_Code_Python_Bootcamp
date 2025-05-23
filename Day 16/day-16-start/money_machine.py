class MoneyMachine:

    CURRENCY = "£"

    COIN_VALUES = {
        "£2": 2.00,
        "£1": 1.00,
        "50p": 0.50,
        "20p": 0.20,
        "10p": 0.10
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        return f"Money: {self.CURRENCY}{self.profit:.2f}"

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0.0:
                print(f"Please collect your {self.CURRENCY}{change:.2f} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
