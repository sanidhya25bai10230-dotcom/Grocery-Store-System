# Grocery-Store-System
# 5.1 README.md

---

## 🛒 Project Title
**Simple Command-Line Grocery Store Simulator**

---

## 📝 Overview of the Project
This project is a basic console-based application written in Python that simulates a virtual grocery shopping experience. It allows a user to select various items from pre-defined categories (Dairy, Fruits, Cookies, Chocolates), calculates the cost of each item, and provides a running total amount at the end of the shopping session. It serves as an excellent introductory example of using fundamental Python concepts such as **variables**, **input/output**, **conditional logic (`if/elif/else`)**, and **loops (`while`)**.

---

## ✨ Features
* **Interactive Menu:** Guides the user through starting, shopping, and exiting the program.
* **Multiple Categories:** Offers distinct categories: Dairy Products, Fruits, Cookies, and Chocolates.
* **Item Selection:** Within Dairy and Fruits, users can select specific items using corresponding letter codes (A, B, C, D, etc.).
* **Price Calculation:** Automatically adds the price of selected items to a running `total_amount`.
* **Checkout:** Allows the user to exit the shopping loop to view their final bill.
* **Error Handling:** Provides messages for invalid choices in both the main menu and within product selection.

---

## 🛠️ Technologies/Tools Used
* **Language:** Python 3 (Any recent version)
* **Environment:** Any standard command-line interface (CLI) or Integrated Development Environment (IDE) that supports Python (e.g., VS Code, PyCharm, IDLE).

---

## 🚀 Steps to Install & Run the Project

1.  **Save the Code:** Save the provided Python script (the Grocery Store code) to a file named `grocery_store.py`.
2.  **Open Terminal/CMD:** Navigate to the directory where you saved the file using your system's terminal or command prompt.
3.  **Run the Script:** Execute the program using the Python interpreter:

    ```bash
    python grocery_store.py
    ```

---

## 🧪 Instructions for Testing
Follow these steps to ensure all features of the application are working correctly:

| Test Case | Steps to Execute | Expected Outcome |
| :--- | :--- | :--- |
| **Start & Checkout** | 1. Run the script. 2. Enter **1** to start. 3. Enter **0** to exit immediately. | The program prints: `Your total amount is 0` |
| **Full Transaction** | 1. Start (1). 2. Buy **Milk (3 -> A)** (Price: 24). 3. Buy **Apple (4 -> F)** (Price: 56). 4. Buy **Cookies (5)** (Price: 75). 5. Exit (0). | The program prints: `Your total amount is 155` (24 + 56 + 75) |
| **Invalid Input** | 1. Start (1). 2. Enter a random number like **9**. | The program prints: `Wrong option is choosen` and returns to the shopping menu. |
| **Exit at Start** | 1. Run the script. 2. Enter **0** at the initial prompt. | The program prints: `Thank you for your visit` |

---
