# Financial Analysis and Ai Chatbot
This project integrates financial data analysis with an interactive AI-powered chatbot to provide actionable insights into company performance. It highlights year-over-year growth, profitability, and operational efficiency while allowing users to query financial metrics.

## Project Overview
The repository combines:

## Financial Analysis:
Automated analysis of revenue, profitability, and asset turnover for major companies.
## AI Chatbot:
An interactive system answering financial queries using both command-line and web API interfaces.

# Files in the Repository
## app.py:
Implements a Flask-based API for the chatbot.
Processes JSON queries and returns structured responses for financial metrics.

## chatbot.py:
Command-line interactive chatbot.
Handles user queries like total revenue, profitability index, and net income change.

## financial_analysis.py:
Conducts data analysis on financial metrics.
Includes calculations for revenue growth, profitability index, and asset turnover.

# Analysis Workflow
## Data Preparation:
Load and clean the dataset from Fin_Analysis.csv.
Handle missing values and group data by company and year.

## Exploratory Data Analysis:
Analyze revenue, net income, and asset utilization trends.
Visualize data insights using Seaborn and Matplotlib.

## Result Interpretation:
Identify growth trends for companies like Tesla, Apple, and Microsoft.
Highlight key financial strengths and weaknesses.

## Conclusion:
Summarize the analysis findings for actionable recommendations.
Highlight standout company performances and improvement areas.

# Usage Instructions
Setup Environment:
Install dependencies:

pip install -r requirements.txt

## Run Analysis:
Execute the financial analysis:

python financial_analysis.py

## Interact with the chatbot via CLI:

python chatbot.py 

# View Results:

Start the Flask app for the chatbot API:

</> python app.py </>

Access insights and data analysis outputs in the terminal or through the API.

# Notes
Ensure the dataset Fin_Analysis.csv is in the root directory.
Flask application runs on default localhost:8081; modify configurations as needed.
Use proper query formatting when interacting with the chatbot to avoid errors.
