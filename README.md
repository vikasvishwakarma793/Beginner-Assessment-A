# Coding Challenges

This repository contains **5 SQL programming problems** and **1 Python programming problem** based on real-world scenarios designed to test your data manipulation, cleaning, and reporting skills.

## 📁 Problems

Navigate to the `SQL-Challenge` folder to find individual sql challenges. Each folder contains its own `README.md` with specific details.

* `SQL-Challenge/Problem1/` - **Last Non-Null Value Logic** 
    * *Goal:* Return the last available non-null value for each column to build a "footer" row.
* `SQL-Challenge/Problem2/` - **Complex Join & Pivot** 
    * *Goal:* Calculate taxes/allowances based on percentage tables and generate a consolidated salary report.
* `SQL-Challenge/Problem3/` - **Trend Analysis** 
    * *Goal:* Identify tests where a student's performance improved compared to the previous test.
* `SQL-Challenge/Problem4/` - **Bitwise/String Logic & Dates** 
    * *Goal:* Filter dates based on a binary string indicator representing days of the week.
* `SQL-Challenge/Problem5/` - **Data Cleaning/Forward Fill** 
    * *Goal:* Fill missing `JOB_ROLE` values by carrying forward the last valid entry (Forward Fill).

Navigate to the `Python-Challenge` folder to find python coding problem. The folder contains its own `README.md` with specific details.

* `Python-Challenge/Problem1` - **Pandas Data Analysis**
    * *Goal:* Clean a raw sales dataset, handle missing values, and perform time-series aggregation to find monthly revenue trends using the Pandas library.

## 🚀 Setup & Getting Started

### Prerequisites

* A SQL Database (PostgreSQL is recommended for advanced window functions, but MySQL 8+ works too).
* Python >= 3.11
* Git
* GitHub account

### Initial Setup

1.  **Fork this repository** to your GitHub account.
2.  **Clone your forked repository**:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/assessment-30jan.git](https://github.com/YOUR_USERNAME/assessment-30jan.git)
    cd SQL-Challenge
    ```
3.  **Load the Data**:
    * Execute the provided `schema.sql` file for each problem in your local database (DBeaver) using ORM(SQLAlchemy,psycopg2,etc). This will create all 5 tables and insert the sample data shown in the problem statements.

4. **For python problem**
   ```bash
    cd Python-Challenge
    ```
    * Write your solution in solution.py. Run it to return expected output.

## 📋 Working Instructions

1.  **Read the Requirements**: Each problem corresponds to a specific logic challenge.
2.  **Write your Solution**: Create a file named `solution.sql` inside the respective problem folder.
3.  **Verify Output**: Compare your query results with the "Expected Output" images provided in the problem descriptions.
4.  **Commit and push** your changes.
5.  **Create ONE Pull Request** for all problems.

## ⚠️ Important Rules

**NO USE OF AI TOOLS ALLOWED**
* Avoid ChatGPT, Copilot, or AI SQL Generators.
* Rely on official documentation and your own logic.

## 📝 Submission Process

### Single Pull Request for All Problems

Once you've completed **ALL 6** problems:

1.  **Commit your changes**:
    ```bash
    git add .
    git commit -m "Complete Assessment solutions - Solved 5 SQL challenges and 1 python challenge"
    ```

2.  **Push to your fork**:
    ```bash
    git push origin master
    ```

3.  **Create Pull Request**:
    * Title: **Solution: [Your Name] - Assessment-30jan**
    * Use this description template:

```markdown
🎯 Problems Completed

✅ 01 Fetch Footer Values - Correctly identified last non-nulls
✅ 02 Generate Salary Report - Calculations match expected net pay
✅ 03 Student Performance - Provided both solutions (inc/exc first test)
✅ 04 Find Relevant Dates - Day-of-week logic implemented correctly
✅ 05 Fill Missing Values - Forward fill logic applied successfully
✅ 06 Pandas Data Analysis - Analysed data using pandas/standard python

💡 Approach

01 Fetch Footer Values
[Explain how you handled the NULL values to get the last one]

04 Find Relevant Dates
[Explain how you matched the date to the binary string]

05 Fill Missing Values
[Did you use a Recursive CTE, Window Function, or User Variables?]

🧪 Verification

* All `solution.sql` files created ✅
* Queries execute against `schema.sql` data without error ✅
* Outputs match the expected results exactly ✅
* Python solution running without error ✅
