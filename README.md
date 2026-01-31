# Python Bank Account Management System

This project demonstrates Object-Oriented Programming (OOP) in Python by simulating a **bank account management system**. It includes classes, inheritance, encapsulation, method overriding, and realistic banking operations.

## File Included

- `bank_account.py` – Python script demonstrating bank account classes and operations

## Features Demonstrated

1. **Class and Constructor** – Defines `BankAccount` with attributes and methods
2. **Attributes & Methods** – Deposit, withdraw, check balance, and display account info
3. **Encapsulation** – Private `__balance` attribute with getter method
4. **Inheritance** – `SavingsAccount` and `CheckingAccount` inherit from `BankAccount`
5. **Method Overriding** – Overridden `account_info()` and `withdraw()` methods
6. **Multiple Objects** – Create multiple account instances
7. **Realistic Bank Operations** – Deposit, withdraw, transfer, and add interest
8. **Comments & Structured Code** – Clear and beginner-friendly code organization

## Classes Overview

### BankAccount
- Base class
- Attributes: `account_number`, `account_holder`, `__balance`
- Methods: `deposit()`, `withdraw()`, `get_balance()`, `account_info()`

### SavingsAccount (Inherits BankAccount)
- Adds `interest_rate` attribute
- Methods: `add_interest()`, overridden `account_info()`

### CheckingAccount (Inherits BankAccount)
- Adds `overdraft_limit` attribute
- Overridden `withdraw()` method to allow overdraft

## Bank Operations

- **Deposit**: Add money to account
- **Withdraw**: Remove money with balance or overdraft check
- **Transfer**: Move money from one account to another
- **Add Interest**: Apply interest for savings accounts

## How to Run

Ensure Python 3 is installed. Then run:

```bash
python bank_account.py
