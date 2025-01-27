from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the financial dataset
data = pd.read_csv('Fin_Analysis.csv')

# Define a route for chatbot queries
@app.route('/chatbot', methods=['POST'])
def chatbot():
    query = request.json.get('query', '').lower()

    if "total revenue" in query:
        company, year = query.split("for")[1].split("in")
        company, year = company.strip(), int(year.strip())
        result = data[(data['Company'] == company) & (data['Year'] == year)]['Total Revenue']
        if not result.empty:
            return jsonify({"response": f"Total Revenue for {company} in {year}: {result.iloc[0]}"})
        else:
            return jsonify({"response": "Sorry, no data found."})

    elif "net income" in query:
        company = query.split("for")[1].strip()
        result = data[data['Company'] == company]['Net Income']
        if not result.empty:
            return jsonify({"response": f"Net Income for {company}: {result.iloc[0]}"})
        else:
            return jsonify({"response": "Sorry, no data found."})

    else:
        return jsonify({"response": "Sorry, I didn't understand that."})

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port = 8081)
