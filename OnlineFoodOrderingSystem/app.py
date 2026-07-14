from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Store orders in memory (in production, use a database)
orders_list = []

# Menu items database
menu_items = [
    {"id": 1, "name": "Margherita Pizza", "price": 299, "category": "Pizza", "icon": "🍕"},
    {"id": 2, "name": "Pepperoni Pizza", "price": 349, "category": "Pizza", "icon": "🍕"},
    {"id": 3, "name": "Chicken Burger", "price": 199, "category": "Burger", "icon": "🍔"},
    {"id": 4, "name": "Veggie Burger", "price": 179, "category": "Burger", "icon": "🍔"},
    {"id": 5, "name": "Biryani", "price": 249, "category": "Indian", "icon": "🍚"},
    {"id": 6, "name": "Paneer Tikka", "price": 229, "category": "Indian", "icon": "🍗"},
    {"id": 7, "name": "Chocolate Cake", "price": 149, "category": "Dessert", "icon": "🍰"},
    {"id": 8, "name": "Ice Cream", "price": 99, "category": "Dessert", "icon": "🍦"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/menu')
def get_menu():
    """API endpoint to get all menu items"""
    return jsonify(menu_items)

@app.route('/api/place-order', methods=['POST'])
def place_order():
    """API endpoint to place an order"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('customer_name'):
            return jsonify({"success": False, "message": "Customer name is required"}), 400
        if not data.get('mobile_number'):
            return jsonify({"success": False, "message": "Mobile number is required"}), 400
        if not data.get('address'):
            return jsonify({"success": False, "message": "Address is required"}), 400
        if not data.get('items') or len(data.get('items', [])) == 0:
            return jsonify({"success": False, "message": "Please add items to cart"}), 400
        
        # Create order object
        order = {
            "order_id": len(orders_list) + 1001,
            "customer_name": data['customer_name'],
            "mobile_number": data['mobile_number'],
            "address": data['address'],
            "items": data['items'],
            "total_amount": data['total_amount'],
            "order_date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "status": "Confirmed"
        }
        
        # Add to orders list
        orders_list.append(order)
        
        return jsonify({
            "success": True,
            "message": "Order placed successfully!",
            "order_id": order['order_id'],
            "order": order
        }), 201
        
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/orders')
def get_orders():
    """API endpoint to get all orders"""
    return jsonify(orders_list)

@app.route('/api/test-data')
def test_data():
    """Generate test data for demonstration"""
    global orders_list
    orders_list = [
        {
            "order_id": 1001,
            "customer_name": "Raj Kumar",
            "mobile_number": "9876543210",
            "address": "123 Main Street, Mumbai",
            "items": [
                {"name": "Margherita Pizza", "quantity": 2, "price": 299},
                {"name": "Chicken Burger", "quantity": 1, "price": 199}
            ],
            "total_amount": 797,
            "order_date": "15-12-2024 10:30:00",
            "status": "Delivered"
        },
        {
            "order_id": 1002,
            "customer_name": "Priya Sharma",
            "mobile_number": "9123456789",
            "address": "456 Park Avenue, Delhi",
            "items": [
                {"name": "Biryani", "quantity": 3, "price": 249}
            ],
            "total_amount": 747,
            "order_date": "16-12-2024 14:45:00",
            "status": "Delivered"
        }
    ]
    return jsonify({"success": True, "message": "Test data loaded"})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
