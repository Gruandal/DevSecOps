# insecure.py
# This file contains intentional security vulnerabilities.

import os
import yaml

# ❌ Command Injection (Semgrep picks this up)
user_input = input("Enter a command: ")
os.system(user_input)  # vulnerable

# ❌ YAML unsafe load (Semgrep / Bandit picks up)
data = yaml.load("foo: bar")  # should be yaml.safe_load

# ❌ Hardcoded secret
API_KEY = "123456-SECRET-KEY-LEAKED"

# ❌ Insecure eval
def run_code(x):
    return eval(x)

run_code("print('This is unsafe')")
