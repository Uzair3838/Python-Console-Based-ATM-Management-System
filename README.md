# ATM Banking System in Python

This project is a **console-based ATM simulation** implemented using **Object-Oriented Programming (OOP)** in Python.  
It allows users to create bank accounts, perform banking operations, and provides an admin interface to manage all registered accounts.

---

## 🚀 Features

### 👤 **User Features**
- Create new account  
- Log in with account number & PIN  
- Deposit money  
- Withdraw money  
- Balance inquiry  
- Change PIN  
- Logout  

### 🔐 **Admin Features**
- Admin login  
- View all registered accounts  
- Add new accounts  
- Remove accounts  
- Logout  

---

## 🧠 How the System Works

- All account information is stored in a dictionary:
  ```python
  {accNumber: {"Name": name, "PIN": pin, "Balance": balance}}

  Users authenticate using account number + 4-digit PIN

Both user and admin have separate login processes

Authentication allows 3 attempts

Menu-driven program flow

System exits safely on request
🛠 Technologies Used

Python

Object-Oriented Programming (OOP)

📂 Project Structure
ATM/
│── atm.py
│── README.md

▶️ Running the Program

Run the following command:
python atm.py

