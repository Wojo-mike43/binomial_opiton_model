import numpy as np

class TreeNode:
    def __init__(self, stock_price, strike_price, option_type, step=0, option_price=0, upchild=None, downchild=None):
        self.stock_price = stock_price
        self.k = strike_price
        self.o_type = option_type
        self.step = step
        self.option_price = option_price
        self.up_child = upchild
        self.down_child = downchild

    def tree_builder(self, up_move, down_move, steps_remaining):
        if steps_remaining == 0:
            self.option_price = option_payoff(self.stock_price, self.k, self.o_type)

        else:
            up_price = self.stock_price * up_move
            down_price = self.stock_price * down_move

            up_tree = TreeNode(stock_price=up_price, strike_price=self.k, option_type=self.o_type, step=self.step+1)
            down_tree = TreeNode(stock_price=down_price, strike_price=self.k, option_type=self.o_type, step=self.step+1)

            self.up_child = up_tree
            self.down_child = down_tree

            up_tree.tree_builder(up_move, down_move, steps_remaining - 1)
            down_tree.tree_builder(up_move, down_move, steps_remaining - 1)

    def reverse_induction(self, risk_free, delta_t, up_prob):
        if self.up_child == None and self.down_child == None:
            return

        else:
            if self.up_child:
                self.up_child.reverse_induction(risk_free, delta_t, up_prob)

            if self.down_child:
                self.down_child.reverse_induction(risk_free, delta_t, up_prob)

            self.option_price = np.exp(-risk_free * delta_t) * (up_prob * self.up_child.option_price) + ((1-up_prob) * self.down_child.option_price)


#Option Payoff
def option_payoff(stock_price, strike_price, option_type):
    try:
        if option_type.strip().lower() == 'call':
            option_price = max(stock_price - strike_price, 0)

        elif option_type.strip().lower() == 'put':
            option_price = max(strike_price - stock_price, 0)

        else:
            raise ValueError("Invalid option type. Please input 'call' or 'put'")

    except AttributeError:
        raise TypeError('Option type must be a call or a put.')

    return option_price


if __name__ == '__main__':
    #Inputs
    s0 = float(input('Stock Price: '))
    k = int(input('Strike Price: '))
    o_type = str(input("Option Type, please input 'call' or 'put': "))
    steps = int(input("Binomial Tree Steps: "))
    risk_free = float(input("Risk Free Rate, please input as a whole number: ")) / 100
    up_move = 1 + ((float(input("Stock Up Move, please input up % as a whole number: "))) / 100)
    down_move = 1 - ((float(input("Stock Down Move, please input up % as a whole number: "))) / 100)


    delta_t = 1/steps
    up_prop = (np.exp(risk_free * delta_t) - down_move) / (up_move - down_move)

    binomial_tree = TreeNode(stock_price=s0, strike_price=k, option_type=o_type)
    binomial_tree.tree_builder(up_move=up_move, down_move=down_move, steps_remaining=steps)
    binomial_tree.reverse_induction(risk_free=risk_free, delta_t=delta_t, up_prob=up_prop)

    print(f"Fair Value of {o_type} option: ${round(binomial_tree.option_price, 2)}")
