from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"  # For session

# Initialize database (only run once or add separate init script)
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            department TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/department", methods=["GET", "POST"])
def department():
    return render_template("department.html")

@app.route("/job_list", methods=["GET", "POST"])
def job_list():
    return render_template("job_list.html")

@app.route("/employee", methods=["GET", "POST"])
def employee():
    return render_template("employee.html")

@app.route("/visitor_list", methods=["GET", "POST"])
def visitor_list():
    return render_template("visitor_list.html")

@app.route("/attendance_report", methods=["GET", "POST"])
def attendance_report():
    return render_template("attendance_report.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    return "Logout"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)