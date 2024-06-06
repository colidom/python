from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Getting the input dates from the form
    start_date_input = request.form['start_date']
    end_date_input = request.form['end_date']
    
    # Converting input strings to datetime objects
    start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_input, "%Y-%m-%d")
    
    # Calculating the difference between the dates
    difference = end_date - start_date
    
    # Number of days
    number_of_days = difference.days
    
    return render_template('result.html', start_date=start_date_input, end_date=end_date_input, days=number_of_days)

if __name__ == '__main__':
    app.run(debug=True)
