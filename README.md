# Binomial Option Pricing Model

This project implements a Binomial Options Pricing Model in Python. The model uses a custom binary tree data structure to calculate the fair value of European-style call or put options through reverse induction.

## How It Works

A binomial model represents potential future price movements of the underlying stock as a tree structure, where each node corresponds to a possible stock price at a given time step. The model calculates option prices through reverse induction and applying risk-neutral probabilities to discount future payoffs to their present value.

### Key Features

- **Binary Tree Implementation:** A `TreeNode` class is used to construct and navigate the binary tree.
- **Reverse Induction:** The model performs backward induction to calculate option prices at each step, considering risk-neutral probabilities.
- **Flexible Input Options:** Users can specify key parameters such as the stock price, strike price, option type, number of steps, risk-free rate, and up/down movements.
- **Dynamic Payoff Calculation:** Supports call and put options with automatic payoff evaluation.

## Inputs

The user is prompted for several inputs. These include:
- Initial stock price
- Option strike price
- Option type (call or put)
- Number of steps (periods) in the binomial tree
- Risk-free interest rate
- Up-move (the amount that the stock price will increase on an up-step of the tree)
- Down-move (the amount that the stock price will decrease on a down-step of the tree) 

### Example

```bash
$ python binomial_option_pricing.py
Stock Price: 100
Strike Price: 105
Option Type, please input 'call' or 'put': call
Binomial Tree Steps: 3
Risk Free Rate, please input as a whole number: 5
Stock Up Move, please input up % as a whole number: 20
Stock Down Move, please input down % as a whole number: 10
Fair Value of call option: $4.58
