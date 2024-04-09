def cho_calculator(total_money, price_perbar):
    number_affordable = total_money // price_perbar
    change = total_money % price_perbar
    return number_affordable, change

#An example
total_money = 100
price_perbar = 7
number_affordable, change = cho_calculator(total_money, price_perbar)
print(f"With {total_money} money and a price of {price_perbar} per bar, you can buy {number_affordable} bars and have {change} left over.")