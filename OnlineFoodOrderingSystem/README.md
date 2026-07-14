# Online Food Ordering System - Flask Mini Project

A complete, single-file Flask mini project for an online food ordering system with a beautiful, responsive UI.

## Project Structure

```
OnlineFoodOrderingSystem/
├── app.py
└── templates/
    └── index.html
```

## Features

✅ **Beautiful Modern UI**
- Responsive design (works on desktop, tablet, mobile)
- Gradient backgrounds and smooth animations
- Card-based layout for menu items
- Interactive hover effects

✅ **Food Menu**
- 8 different food items
- Categorized items (Pizza, Burger, Indian, Dessert)
- Price display for each item
- Food emojis for visual appeal

✅ **Shopping Cart**
- Add items with quantity selection
- Increase/decrease quantity using +/- buttons
- Remove items from cart
- Real-time cart updates
- Display cart summary with subtotal, tax, and total

✅ **Order Placement**
- Customer name input (validation: min 3 characters)
- Mobile number input (validation: 10-digit format)
- Delivery address input (validation: min 5 characters)
- Form validation with error messages
- Place order button

✅ **Order Confirmation**
- Success message with check mark icon
- Display order ID
- Show total amount
- Estimated delivery time
- Animated confirmation box

✅ **Order History**
- Display all placed orders in a table
- Show order ID, customer name, date/time, items, total, status
- Click on "View Items" to see order details in a modal
- Order status badges (Confirmed, Pending, Delivered)

✅ **Additional Features**
- Form validation using JavaScript
- Alert notifications (success/error)
- Persistent cart during session
- Modal popup for order details
- Tab navigation between Order and History
- Professional navigation bar

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Create project folder:**
   ```bash
   mkdir OnlineFoodOrderingSystem
   cd OnlineFoodOrderingSystem
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install Flask:**
   ```bash
   pip install flask
   ```

5. **Create app.py file** with the provided code

6. **Create templates folder and index.html:**
   ```bash
   mkdir templates
   ```
   Place index.html in the templates folder

7. **Run the application:**
   ```bash
   python app.py
   ```

8. **Open browser and go to:**
   ```
   http://localhost:5000
   ```

## How to Use

### Ordering Food
1. Click on "📋 Order Food" tab
2. Browse the menu items
3. Use +/- buttons to select quantity
4. Click "Add to Cart" button
5. Fill in your details (Name, Mobile, Address)
6. Review your cart summary
7. Click "Place Order" button
8. Receive order confirmation with Order ID

### Viewing Order History
1. Click on "📦 Order History" tab
2. View all your orders in a table
3. Click on "View Items" to see detailed order information
4. Close the modal by clicking the X or outside the modal

### Form Validation
- Customer Name: Minimum 3 characters required
- Mobile Number: Must be exactly 10 digits
- Delivery Address: Minimum 5 characters required
- Error messages appear below each field
- Cart must have at least one item

## File Structure

### app.py
- Flask application setup
- Route for home page
- API endpoints:
  - `GET /` - Serve main page
  - `GET /api/menu` - Get menu items
  - `POST /api/place-order` - Place new order
  - `GET /api/orders` - Get all orders
  - `GET /api/test-data` - Load test data

### templates/index.html
- Complete HTML structure
- All CSS styling (embedded in `<style>` tag)
- All JavaScript functionality (embedded in `<script>` tag)
- Responsive navigation bar
- Menu display with cards
- Shopping cart section
- Checkout form
- Order history table
- Modal for order details

## API Endpoints

### GET /api/menu
Returns array of menu items:
```json
[
  {
    "id": 1,
    "name": "Margherita Pizza",
    "price": 299,
    "category": "Pizza",
    "icon": "🍕"
  },
  ...
]
```

### POST /api/place-order
Request body:
```json
{
  "customer_name": "John Doe",
  "mobile_number": "9876543210",
  "address": "123 Main St",
  "items": [
    {
      "id": 1,
      "name": "Pizza",
      "price": 299,
      "quantity": 2
    }
  ],
  "total_amount": 628
}
```

Response:
```json
{
  "success": true,
  "message": "Order placed successfully!",
  "order_id": 1001,
  "order": { ... }
}
```

### GET /api/orders
Returns array of all orders

## Customization

### Add More Menu Items
Edit the `menu_items` list in `app.py`:
```python
menu_items = [
    {"id": 1, "name": "Item Name", "price": 299, "category": "Category", "icon": "🍕"},
    # Add more items
]
```

### Change Colors
Edit CSS variables in `index.html`:
```css
:root {
    --primary-color: #ff6b35;      /* Orange */
    --secondary-color: #f7931e;    /* Yellow-Orange */
    --dark-color: #1a1a1a;         /* Dark */
    --light-color: #f5f5f5;        /* Light */
}
```

### Modify Styling
Find and edit the CSS in the `<style>` tag of index.html

## Troubleshooting

### Issue: "Port 5000 is already in use"
**Solution:** Change port in app.py:
```python
app.run(debug=True, host='localhost', port=5001)
```

### Issue: "No module named 'flask'"
**Solution:** Install Flask:
```bash
pip install flask
```

### Issue: "Template not found"
**Solution:** Make sure index.html is in `templates/` folder

### Issue: Styles not loading
**Solution:** CSS is embedded in HTML, no external files needed

## Browser Compatibility
- Chrome (Recommended) ✅
- Firefox ✅
- Safari ✅
- Edge ✅

## Performance Notes
- Single HTML file for easy deployment
- No external dependencies (pure HTML/CSS/JS)
- Orders stored in memory (will reset on server restart)
- For production, use a database

## Future Enhancements
- Database integration (SQLite, PostgreSQL)
- User authentication
- Payment gateway integration
- Email notifications
- Admin dashboard
- Search and filter functionality
- Rating and reviews system

## License
This project is open source and free to use.

## Support
For issues or questions, please refer to the code comments or Flask documentation.

---

**Created:** December 2024
**Last Updated:** December 2024
**Version:** 1.0
