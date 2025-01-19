# Cafe Management System

## Author
Samridhi Gupta

## Date
20/01/2025

## Overview
The Cafe Management System is a command-line application designed to streamline the ordering process in a cafe. It allows users to place orders, view their ordered items, calculate the total cost, and delete items from their order.

## Features
- View a menu of available items with prices.
- Place orders for multiple items with specified quantities.
- View the current order summary with total cost.
- Delete specific items from the order.
- Handle case-insensitive item deletion.

## Installation
To run this application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Steps to Run
1. Clone the repository or download the script file.
2. Open a terminal (or command prompt).
3. Navigate to the directory where the script is located.
4. Run the following command:

   ```bash
   python cafe_management_system.py
   ```

## Usage
1. Upon starting the application, the menu will be displayed.
2. Enter the item number to order.
3. Specify the number of plates for the selected item.
4. After placing orders, you can choose to delete items from your order.
5. The application will show the updated order summary and total cost after any deletions.

## Example
```
Welcome to the Love Cafe
---Menu---
1. Pizza: 200
2. Pasta: 350
3. Burger: 200
4. Sandwich: 150
5. Cold Coffee: 100
6. Hot Coffee: 50
7. Cold Drink: 50
8. Salad: 300

What would you like to order? (Enter the item number): 3
Enter the number of plates: 7
You have ordered Burger X 7 plates.
Your Ordered items are:
Burger X 7 = 1400
Your total order is: 2000
Would you like to delete an item from your order? (y/n): y
Please enter the name of the item you want to delete: burger
How many plates of burger would you like to delete? 3
3 plates of Burger have been removed from your order.
```
