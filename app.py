from flask import Flask, render_template, request

app = Flask(__name__)

bookings = []

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        booking = {
            "name": request.form["name"],
            "roll": request.form["roll"],
            "computer": request.form["computer"]
        }

        bookings.append(booking)
        message = "Booking Successful!"

    return render_template("index.html", bookings=bookings, message=message)

if __name__ == "__main__":
    app.run(debug=True)
