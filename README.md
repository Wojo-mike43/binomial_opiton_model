# Binomial Option Pricing Model

This project implements a **Binomial Options Pricing Model** in Python. The model uses a custom binary tree data structure to calculate the fair value of European-style call or put options through reverse induction.

## How It Works

The binomial model represents potential future price movements of the underlying stock as a tree structure, where each node corresponds to a possible stock price at a given time step. The model calculates option prices by traversing the tree backward, applying risk-neutral probabilities to discount future payoffs to their present value.

### Key Features

- **Binary Tree Implementation:** A `TreeNode` class is used to construct and navigate the binary tree.
- **Reverse Induction:** The model performs backward induction to calculate option prices at each step, considering risk-neutral probabilities.
- **Flexible Input Options:** Users can specify key parameters such as the stock price, strike price, option type, number of steps, risk-free rate, and up/down movements.
- **Dynamic Payoff Calculation:** Supports call and put options with automatic payoff evaluation.

## Usage

To use this script, run it in a Python environment. The program will prompt for the following inputs:

1. **Stock Price (`s0`)**: The current price of the stock.
2. **Strike Price (`k`)**: The strike price of the option.
3. **Option Type (`o_type`)**: Input either "call" or "put."
4. **Number of Steps (`steps`)**: The number of steps in the binomial tree.
5. **Risk-Free Rate (`risk_free`)**: The annualized risk-free rate as a percentage (e.g., enter 5 for 5%).
6. **Stock Up Move (`up_move`)**: The percentage increase in stock price for an upward move.
7. **Stock Down Move (`down_move`)**: The percentage decrease in stock price for a downward move.

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
