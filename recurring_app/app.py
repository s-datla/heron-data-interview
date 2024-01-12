import os
from flask import Flask, request
from recurring_app.logic import *
from recurring_app.data.transaction import Transaction

def create_app():
    app = Flask(__name__)
    
    @app.route('/recurring', methods=['POST'])
    def findRecurringTransactions():
        json = request.json
        transaction_list = []
        for i in json['transactions']:
            transaction_list.append(Transaction(i['amount'], i['description'], i['date']))
        return identify_recurring_transactions(transaction_list)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)