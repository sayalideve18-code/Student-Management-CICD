from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Aarav"},
    {"id": 2, "name": "Priya"}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Student Management System is running",
        "students": students
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
