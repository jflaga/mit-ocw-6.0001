# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 00:41:29 2017
Finished: 02:19 AM

@author: Dev Jboy Flaga
"""

# Part A: House Hunting


annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
monthly_savings = (annual_salary / 12) * portion_saved

total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25 #25%
down_payment = total_cost * portion_down_payment

annual_return = 0.04
current_savings = 0.0

number_of_months = 0

while current_savings < down_payment:
    current_savings += monthly_savings + ((current_savings * annual_return) / 12)
    number_of_months += 1

print('Number of months: {}'.format(number_of_months))