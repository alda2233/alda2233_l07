"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from functions import meal_costs
# Constants


b_total, l_total, s_total, a_total = meal_costs()
print(
    f"{b_total:.2f},{l_total:.2f},{s_total:.2f},{a_total:.2f}")
