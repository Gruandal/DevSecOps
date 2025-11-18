# DevSecOps Assignment 10

This repository is created for practicing basic DevSecOps concepts:

## ✔ A — Static Code Analysis (Linting)
- Using **Flake8** to detect code style and quality issues.
- Files tested: `app.py`

## ✔ E — Software Composition Analysis (SCA)
- Using **Dependabot** or **Mend Bolt**.
- Vulnerable packages included in `requirements.txt`:
  - PyYAML 5.3 – contains CVE-2020-14343
  - requests 2.19.0 – contains CVE-2018-18074
  - Flask 0.12 – multiple vulnerabilities

## ✔ O — SAST (Semgrep)
The file `insecure.py` contains intentionally vulnerable patterns:
- Command injection
- YAML unsafe loading
- Hardcoded secret
- eval() injection

These will be caught by Semgrep rules.

---

## How to run the project

### Install dependencies:
