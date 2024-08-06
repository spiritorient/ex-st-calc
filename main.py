# main.py

from flask import Flask, render_template, request

from exit_strategy_1 import exit_strategy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Extract form data
        portfolio = {
            'ASSET 1': float(request.form['asset1']),
            'ASSET 2': float(request.form['asset2']),
            'ASSET 3': float(request.form['asset3'])
        }
        risk_multiplier = float(request.form['risk_multiplier'])
        reward_multiplier = float(request.form['reward_multiplier'])
        win_probability = float(request.form['win_probability'])
        win_loss_ratio = float(request.form['win_loss_ratio'])

        # Debug print statements
        print(f"Portfolio: {portfolio}")
        print(f"Risk Multiplier: {risk_multiplier}")
        print(f"Reward Multiplier: {reward_multiplier}")
        print(f"Win Probability: {win_probability}")
        print(f"Win/Loss Ratio: {win_loss_ratio}")

        # Calculate exit strategy
        strategy = exit_strategy(portfolio, risk_multiplier, reward_multiplier, win_probability, win_loss_ratio)

        return render_template('result.html', strategy=strategy)

    except Exception as e:
        # Print error message and return a generic error page
        print(f"Error: {e}")
        return "An error occurred during calculation."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
    app.run(debug=True)