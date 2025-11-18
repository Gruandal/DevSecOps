# app.py
import os 
import sys # 故意留一個未使用的 import，會被 Flake8 警告

def calculate_sum( a,b): # 故意在參數周圍加入多餘空格，會被 Flake8 警告
    print("Hello DevSecOps World!")
    return a + b

result = calculate_sum(10, 5)
