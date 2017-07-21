# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:34:10 2017
Finished: Jul 18, 2017 1:14 AM

@author: Dev Jboy Flaga
"""

total_cost = 1000000
portion_down_payment = 0.25 #25%
down_payment = total_cost * portion_down_payment
semi_annual_raise = .07
annual_return = 0.04

starting_annual_salary = float(input('Enter your starting annual salary: '))

one_hundred_dollars_as_epsilon = 100
steps_in_bisection_search = 0
possible_to_pay_in_three_years = True
max_portion_saved_as_integer = 10000
min_portion_saved_as_integer = 0
best_portion_saved_as_integer = max_portion_saved_as_integer
while True:
    steps_in_bisection_search += 1
    annual_salary = starting_annual_salary
    best_portion_saved = best_portion_saved_as_integer / 10000
    monthly_savings = (annual_salary / 12) * best_portion_saved
    
    current_savings = 0.0
    number_of_months = 0
    while number_of_months <= 36:        
        #print('current_savings: {}'.format(current_savings))
        #print('number_of_months: {}'.format(number_of_months))
        current_savings += monthly_savings + ((current_savings * annual_return) / 12)
        number_of_months += 1
            
        if number_of_months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = (annual_salary / 12) * best_portion_saved            
    
    #print('current_savings: {}'.format(current_savings))
    if abs(current_savings - down_payment) <= one_hundred_dollars_as_epsilon:
        break
    
    if current_savings > down_payment:
        max_portion_saved_as_integer = best_portion_saved_as_integer
    else:
        min_portion_saved_as_integer = best_portion_saved_as_integer
        
    if min_portion_saved_as_integer >= max_portion_saved_as_integer:
        possible_to_pay_in_three_years = False
        break
        
    best_portion_saved_as_integer = (max_portion_saved_as_integer + min_portion_saved_as_integer) // 2 # we will guess the value of this
    

if possible_to_pay_in_three_years:
    #print('current_savings: {}'.format(current_savings))
    print('Best savings rate: {}'.format(best_portion_saved))
    print('Steps in bisection search: {}'.format(steps_in_bisection_search))
else:
    print('It is not possible to pay the down payment in three years.')
