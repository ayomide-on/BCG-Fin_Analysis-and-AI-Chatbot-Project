import pandas as pd
data = pd.read_csv('Fin_Analysis.csv')

def chatbot():
    print("Welcome to the Financial Analysis Chatbot!")
    print("Ask me any of the following questions:")
    print("1. What is the total revenue for [Company] in [Year]?")
    print("2. What is the net income for [Company]?")
    print("3. What is net income changed over the last year for [Company]?")
    print("4. What is the cash flow ratio for [Company] in [Year]?")
    print("5. What is the Profitability index for [Company]?")
    print("Type 'Exit' to quit.")

    while True:
        query = input("Enter your question: ").strip().lower()

        if "total revenue" in query:
            Company_and_Year = query.split("for")[1].split("in")
            Company, Year = Company_and_Year[0].strip(), int(Company_and_Year[1].strip().replace("?", ""))
            result = data[(data['Company'] == Company) & (data['Year'] == Year)]['Total Revenue']
            if not result.empty:
                print(f"Total Revenue for {Company} in {Year}: {result.iloc[0]}")
            else:
                print("Data not found")

        elif "net income" in query:
            company = query.split("for")[1].strip()
            result = data[data['Company'] == company]['Net Income']
            if not result.empty:
                print(f"Net Income for {company}: {result.iloc[0]}")
            else:
                print("Data not found")

        elif "net income change" in query:
            company = query.split("for")[1].strip()
            result = data[data['Company'] == company]['Net Income Change']
            if not result.empty:
                print(f"Net Income Change for {company}: {result.iloc[0]}")
            else:
                print("Data not found")

        elif "cash flow ratio" in query:
            company, year = query.split("for")[1].split("in")
            company, year = company.strip(), int(year.strip().replace("?", ""))
            result = data[(data['Company'] == company) & (data['Year'] == year)]['Cash Flow Ratio']
            if not result.empty:
                print(f"Cash Flow Ratio for {company} in {year}: {result.iloc[0]}")
            else:
                print("Data not found")

        elif "profitability index" in query:
            company = query.split("for")[1].strip()
            result = data[data['Company'] == company]['Profitability Index']
            if not result.empty:
                print(f"Profitability Index for {company}: {result.iloc[0]}")
            else:
                print("Data not found")

        elif 'exit' in query:
            print("Goodbye!")
            break

        else:
            print("Sorry, I didn't understand that. Please Try Again")

chatbot()
