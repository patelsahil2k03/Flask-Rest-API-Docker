import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler('api_logs.log', maxBytes=100000, backupCount=1)
log_handler.setFormatter(log_formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.DEBUG)
customers = [
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "meal_size": "Below 500kcal",
    "meal_time": ["Lunch", "Dinner"],
    "days": "1 week (5 days)",
    "status": "Active"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "meal_size": "500-650kcal",
    "meal_time": ["Breakfast", "Morning Snack", "Dinner"],
    "days": "4 weeks (20 days)",
    "status": "Inactive"
  },
  {
    "id": 3,
    "name": "Bob Johnson",
    "email": "bob@example.com",
    "meal_size": "650+kcal",
    "meal_time": ["Breakfast", "Lunch", "Evening Snack"],
    "days": "1 week (5 days)",
    "status": "Active"
  },
  {
    "id": 4,
    "name": "Alice Brown",
    "email": "alice@example.com",
    "meal_size": "Below 500kcal",
    "meal_time": ["Lunch", "Dinner"],
    "days": "4 weeks (20 days)",
    "status": "Active"
  },
  {
    "id": 5,
    "name": "Charlie Wilson",
    "email": "charlie@example.com",
    "meal_size": "650+kcal",
    "meal_time": ["Breakfast", "Dinner"],
    "days": "1 week (5 days)",
    "status": "Active"
  }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Restaurant Subscription Service</h1>
                <p>A Flask API for managing customer subscriptions and meal plans.</p>'''

@app.route('/api/v1/customers/all', methods=['GET'])
def api_all_customers():
    app.logger.info('GET request received for all customers.')
    return jsonify(customers)

@app.route('/api/v1/customers', methods=['GET'])
def api_get_customer_by_id():
    if 'id' in request.args:
        customer_id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    app.logger.info(f'GET request received for customer with id {customer_id}.')
    results = [customer for customer in customers if customer['id'] == customer_id]
    
    # if 'ids' in request.args:
    #     customer_ids = [int(id) for id in request.args.get('ids').split(',')]
    # else:
    #     return "Error: No ids field provided. Please specify ids."

    # results = [customer for customer in customers if customer['id'] in customer_ids]

    return jsonify(results)

@app.route("/api/v1/customers", methods=['POST'])
def api_create_customer():
    new_customer = request.get_json()
    customers.append(new_customer)
    app.logger.info('POST request received. New customer added.')
    return "Success: Customer has been added."

@app.route("/api/v1/customers/<id>", methods=["PUT"])
def api_update_customer(id):
    for customer in customers:
        if customer['id'] == int(id):
            updated_customer = request.get_json()
            customer.update(updated_customer)
            app.logger.info(f'PUT request received for customer with id {id}. Customer information updated.')
            return "Success: Customer information has been updated."

    return "Error: Customer not found."

@app.route("/api/v1/customers/<id>", methods=["DELETE"])
def api_delete_customer(id):
    for customer in customers:
        if customer['id'] == int(id):
            customers.remove(customer)
            app.logger.info(f'DELETE request received for customer with id {id}. Customer information deleted.')
            return "Success: Customer information has been deleted."

    return "Error: Customer not found."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)

def api_all_customers():
    logging.info('GET request received for all customers.')
    return jsonify(customers)