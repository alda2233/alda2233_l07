"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-08"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0

    while count != number:
        guess = int(input("guess"))
        count += 1

        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again.")
        else:
            break

    print(f"Congratulations you made {count} guesses {number}")
    return int(count)


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """

    power = 1

    while power < target:
        power *= 2

    return int(power)


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """

    current_sum = 0
    current_number = 1

    while current_sum < target:
        current_sum += current_number ** 2
        current_number += 1

    return int(current_sum)


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """

    day = 1
    away = 'Y'
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0

    while away == 'Y':
        print(f"for day {day}")
        breakfast = float(input("How much was breakfast?"))
        lunch = float(input("How much was lunch?"))
        supper = float(input("How much was supper?"))
        total = breakfast + lunch + supper
        day += 1
        print(f"Your total for the day was ${total}")

        b_total += breakfast
        l_total += lunch
        s_total += supper
        a_total += total
        away = input("Were you away another day (Y/N)?")

    return float(b_total), float(l_total), float(s_total), float(a_total)


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    OVERTIME = 0.0
    AVERAGE = 0.0
    OVERTIME_RATE = 1.5
    TAX_RATE = 0.03625

    total_net_payment = OVERTIME
    employee_count = 0
    employee_id = None

    while True:
        employee_id = int(input("Employee ID: "))

        if employee_id == 0:
            break

        hourly_wage_rate = float(input("Hourly wage rate: $"))
        hours_worked = float(input("Hours worked: "))

        if hours_worked > 40:
            regular_payment = 40 * hourly_wage_rate
            overtime_payment = (hours_worked - 40) * \
                (hourly_wage_rate * OVERTIME_RATE)
            gross_payment = regular_payment + overtime_payment
        else:
            gross_payment = hours_worked * hourly_wage_rate

        tax = gross_payment * TAX_RATE
        net_payment = gross_payment - tax

        total_net_payment += net_payment
        employee_count += 1

        print(f"Net payment for employee {employee_id}: ${net_payment:.2f}\n")

    if employee_count == 0:
        total_net_payment = OVERTIME
        average_net_payment = AVERAGE
    else:
        average_net_payment = total_net_payment / employee_count

    return total_net_payment, average_net_payment
