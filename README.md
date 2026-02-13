# expense-tracker
A lightweight Python CLI-based application to track daily expenses. This tool allows you to log expenses, categorise them, and view a summary of your spending habits, all stored locally in a CSV file.

## Problem Statement
Create a command‑line application that lets users add, view, and categorize daily expenses.

The program should store transactions (date, amount, category, notes) in a local file (CSV or JSON) and allow users to view a summary of total spending by category.

## Features
**Add Expenses**: Add an expense using the fields: amount, category, and notes.

**Persistent Storage**: Save expenses to a file: expenses.csv (in this case).

**Data Validation**: Provides dynamic feedback to ensure user input matches menu options and formats invalid/empty entries.

**Spending Summary**: View a breakdown of total spending grouped by a user specified category.

**Auto-Formatting**: Automatically handles date and timestamp generation and currency formatting.

## Design Choices
**Why CSV over JSON?**\
My reasoning for using a .csv format for data storage and manipulation was primarily as the requirements in the problem statement explicitly stated only 4 categories (date, amount, category, notes) were required.

JSON is useful when working with nested data and for displaying data on the web, both of which are out of the scope of this CLI-based project.

**Why Pandas over CSV or SQLite?**\
I chose to use Pandas as I'm working with a relatively small and portable dataset and the ability to natively query data e.g. sum of expenses by each category/for a specified category with a one-liner.

The CSV module is great for appending, storing and retrieving data, but lags behind in analysing data and retrieving queried data e.g. sum of expenses by each category. I also wanted to try a new tool as I have experimented with the CSV module in previous tasks.

SQLite would be a great option as a built-in relational database engine that both excels when ensuring data persistence across multiple concurrent users and allows for concurrency. Also, the scope of the project did not justify the creation and altering of tables and bringing with it the complexities of SQL.

If I wanted to further develop and add new features, Pandas provides me with a wide range of options from creating graphs to analysing trends and merging with other files storing expenses.


## Getting Started
**Prerequisites**:\
[Python 3.x](https://www.python.org/)\
[Pandas](https://pandas.pydata.org/)

**Installation**:

Clone the git repository

```bash
git clone https://github.com/yashjagani17/expense-tracker.git
cd expense-tracker
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

**Usage**:

Run the application
```bash
python3 main.py
```

## Demo
**Menu**

![menu](/assets/menu.png)

**Add Expense**

![add expense](/assets/add-expense.png)

**View Expenses**

![view expenses](/assets/view-expenses.png)

**Expense Summary**

![expenses by category](/assets/expenses-by-category.png)

## How It Works

**Add Expense**: Enter the cost, category, and a note to create an expense and save to expenses.csv.

**View Expenses**: Display a table of all transactions from expenses.csv.

**Expenses Summary**: Shows the total amount spent per category.

**Exit**: Closes the program.
