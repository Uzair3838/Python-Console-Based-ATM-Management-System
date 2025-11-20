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

📊 Flowchart (Program Logic)
flowchart TD

A[Start Program] --> B[Main Menu]
B -->|Admin Login| C[Authenticate Admin]
B -->|Create Account| D[Create New Account]
B -->|User Login| E[Authenticate User]
B -->|Exit| Z[Exit Program]

C -->|Success| CA[Admin Options]
C -->|Fail| B

CA -->|View Accounts| C1[Display all accounts] --> CA
CA -->|Add Account| C2[Admin Creates Account] --> CA
CA -->|Remove Account| C3[Delete Account] --> CA
CA -->|Logout| B

E -->|Success| U[User Options]
E -->|Fail| B

U -->|Deposit| U1[Deposit Money] --> U
U -->|Withdraw| U2[Withdraw Money] --> U
U -->|Balance Inquiry| U3[Show Balance] --> U
U -->|Change PIN| U4[Change User PIN] --> U
U -->|Logout| B

Z --> End[Program Ends]

🧩 UML Class Diagram (ATM System)

classDiagram
    class ATM {
        -adminUsername : str
        -adminPin : str
        -isloginAdmin : bool
        -accountsInfo : dict
        -balance : int
        -islogin : bool
        -accNumber : int
        -pin : str

        +menu()
        +admin()
        +adminOpt()
        +createAccount()
        +login()
        +authentication()
        +deposit()
        +withdraw()
        +balanceInquiry()
        +changePin()
        +logout()
        +optSelection()
        +exit()
    }


