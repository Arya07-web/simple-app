from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    students = [
        {"name": "Arya", "course": "Computer Engineering", "marks": 92},
        {"name": "Rahul", "course": "AI & DS", "marks": 88},
        {"name": "Sneha", "course": "IT", "marks": 95}
    ]

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
