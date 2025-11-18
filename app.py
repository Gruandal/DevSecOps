# app.py

import os
import flask
import requests # 故意引入，E級時會用來檢查版本漏洞

# 程式碼品質問題 1: 變數名稱使用大寫，但不是常數 (Flake8 預設不報錯，但會檢查)
# 程式碼品質問題 2: 行尾有不必要的空格 (Flake8 會報錯 W291)
def Check_Auth(user_input):  
    # 程式碼品質問題 3: 未使用的變數 (Flake8 會報錯 F841)
    TEMP_VAR = "some value" 

    # 程式碼品質問題 4: 縮排不符合 PEP 8 規範 (使用 Tab 或不是四個空格，Flake8 會報錯 E101, E111)
    if user_input:
      # 程式碼品質問題 5: 缺少一個空格 (E231)
      print('User authenticated')

    return True

# 程式碼品質問題 6: 函數之間缺少兩行空行 (Flake8 會報錯 E302)
def main():
    secret_key = "MyHardcodedSecret" # O級任務可能用到
    result = Check_Auth("admin")

    if result == True: # 這裡應該是 `is True` 或直接 `if result:`
        # 故意引入一個長行 (Flake8 預設會檢查 E501)
        long_string = "This is a very long string that will definitely exceed the 79 character limit set by PEP 8, which is a common check for static analysis tools like Flake8. Flake8 will raise an E501 error here." 
        print(long_string)

if __name__ == '__main__':
    main()
