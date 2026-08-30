Compound Interest / Savings Calculator

A Python command-line tool that calculates and visualizes how a savings account grows over time with monthly contributions and compound interest.

Why I built this

I'm a Grade 11 student planning to study Computer Science and Finance/Math at university, and I wanted a project that sits on both sides. Compound interest is one of the first "big ideas" you learn in finance, it's the reason a small, consistent monthly saving habit can turn into a large sum over time with the interest provided by the organization. I wanted to actually build the math myself instead of just using an online calculator, and turn it into something visual and interactive using Python.

What it does

The program asks you for your starting amount, how much you add every month, the annual interest rate, and how many years you want to project. It also shows a graph chart to show the amount of money you have in each year, to give a more visible way to understand your money growth.

It calculates the balance at the end of every month using compound interest (interest is calculated and added monthly, not just once a year), prints a summary of total money contributed, total interest earned, and the final balance, and saves a line chart (savings_growth.png) showing the balance growing over time.

Example
=== Compound Interest / Savings Calculator ===

Starting amount ($): 1000
Monthly contribution ($): 200
Annual interest rate (%, e.g. 5 for 5%): 7
Number of years: 10

--- Results after 10 year(s) ---
Total contributed:  $25,000.00
Interest earned:    $11,626.62
Final balance:      $36,626.62

Chart saved to 'savings_growth.png'
How the math works

Every month, two things happen to your balance: it earns interest based on the current balance, then you add your monthly contribution.

python
monthly_rate = annual_rate / 100 / 12
balance = balance * (1 + monthly_rate) + monthly_contribution

The annual rate gets divided by 12 to turn it into a monthly rate, and divided by 100 to turn a percentage (like 7) into a decimal (0.07). This is repeated once for every month in the time period, which is what creates compound growth, you eventually earn interest on interest you earned in previous months, not just on your original contributions.

Getting started

Requirements: Python 3.8+ and matplotlib (pip install matplotlib)

bash
git clone https://github.com/zinnats7-cpu/savings-calculator.git
cd savings-calculator
pip install -r requirements.txt
python savings_calculator.py
Project structure
savings-calculator/
├── savings_calculator.py   # main program
├── requirements.txt        # dependencies
└── README.md
Possible next features

Inflation adjustment: show the balance in today's dollars by also applying an inflation rate, so the chart reflects real purchasing power rather than just nominal dollars.

Scenario comparison: let the user run two or three scenarios (different interest rates or contribution amounts) and plot them on the same chart to compare outcomes side by side.

About me

I'm an international student from Bangladesh studying in British Columbia, Canada, applying to university for Fall 2027 with interests in Computer Science, Finance, and Math. This project is part of my portfolio.
