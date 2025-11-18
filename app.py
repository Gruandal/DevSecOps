# app.py
import os 
import sys # F401: 'sys' imported but unused

def calculate_sum(a,b ): # E202: whitespace before ')' 
    
    # W293: blank line contains whitespace
    
    if True: print("This is a bad style.") # E701: multiple statements on one line 
    
    return a + b

result = calculate_sum(10, 5)
