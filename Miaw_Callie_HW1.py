# Author: Callie Miaw
# Homework Number & Name: 1 & Face Mask Store Sales
# Due Date: September 10, 2020
# Program Description: A local store wants to identify which face mask have the highest
# profit margin and are the most popular.
# They have hired you to update some of their systems.
# Your first task is to create an application to record the sales and calculate profit for individual masks sold.
# Write a program that accepts information from the user (a store clerk), calculates the total selling price, cost,
# and profit, and displays a summary of the item sold.

def main():
    #gathering inputs
    item_name = input("What is the name of the item being sold? ")
    item_price = float(input("What is the price of the item being sold? "))
    item_cost = float(input("What is the cost of the item being sold? "))
    item_amount = int(input("How many of the items were sold? "))

    #simple math to determine outputs using variables
    total_revenue = item_price * item_amount
    total_cost = item_cost * item_amount
    total_profit = total_revenue - total_cost
    #multiply by 100 to get the decimals and make it an int to remove 0's
    profit_percentage = total_profit/total_revenue * 100

    #outputs
    #blank line before output is shown
    print("\nItem Name:", item_name)

    #format to have two decimal places to represent cents
    print("Total Revenue: $" + "{:.2f}".format(total_revenue))
    print("Total Cost: $" + "{:.2f}".format(total_cost))
    print("Quantity Sold: " + str(item_amount))
    print("Total Profit: $" + "{:.2f}".format(total_profit))
    print("Percentage profit generated by the product: " + str("{:.0f}".format(profit_percentage)) + "%")

main()