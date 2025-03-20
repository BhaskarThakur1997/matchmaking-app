from flask import Flask, jsonify
import random

app = Flask(__name__)

events = ["Music Festival", "Tech Meetup", "Book Club", "Gaming Night", "Art Expo"]
names = ["Alex", "Sam", "Jordan", "Taylor", "Chris", "Morgan"]

def generate_matches():
    return [
        {
            "id": i,
            "name": random.choice(names),
            "compatibility": f"{random.randint(70, 99)}%",
            "event": random.choice(events),
            "image": f"https://randomuser.me/api/portraits/{'men' if i % 2 == 0 else 'women'}/{i}.jpg"
        }
        for i in range(1, 6)
    ]

@app.route("/get_matches", methods=["GET"])
def get_matches():
    return jsonify(generate_matches())

if __name__ == "__main__":
    app.run(port=5000)
