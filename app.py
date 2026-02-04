from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@gmail.com" and password == "1234":
            return redirect(url_for("dashboard"))
        else:
            return "Invalid login. Try again."

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_table()


@app.route("/alert", methods=["POST"])
def alert():
    amb_id = request.form.get("amb_id")
    from_loc = request.form.get("from_loc")
    to_loc = request.form.get("to_loc")

    message = f"🚨 Green Corridor Activated for Ambulance {amb_id} from {from_loc} to {to_loc}"
    return render_table(message)


def render_table(message=None):
    data = {
        "From": [
            "Andheri East", "Andheri West", "Bandra East", "Bandra West",
            "Dadar East", "Dadar West", "Borivali East", "Borivali West",
            "Kurla", "Ghatkopar", "Mulund", "Thane",
            "Vashi", "Nerul", "Panvel", "Colaba", "Churchgate"
        ],
        "To": [
            "Bandra East", "Jogeshwari", "Dadar East", "Mahim",
            "Sion", "Lower Parel", "Kandarpada", "Malad West",
            "Chembur", "Powai", "Bhandup", "Mulund",
            "Belapur", "CBD Belapur", "Kharghar", "Marine Lines", "Nariman Point"
        ],
        "Signals": [
            ["S1", "S2"], ["S3"], ["S1"], ["S1", "S4"],
            ["S2"], ["S1", "S2", "S3"], ["S5"], ["S2"],
            ["S1"], ["S3"], ["S2"], ["S4"],
            ["S1"], ["S2"], ["S3"], ["S1"], ["S2"]
        ]
    }

    df = pd.DataFrame(data)
    table = df.to_html(index=False)
    return render_template("dashboard.html", table=table, message=message)


if __name__ == "__main__":
    app.run(debug=True)
