#!/usr/bin/python3
"""
A simple Flask API that handles users.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yadda saxlamaq üçün lüğət (Dictionary)
# Tələbə əsasən test məlumatları daxil edilmir.
users = {}


@app.route('/')
def home():
    """
    Root endpoint that returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    Returns a list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Returns the status of the API.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full object corresponding to the provided username.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary.
    """
    # Gələn məlumatın JSON olub-olmadığını yoxlayırıq
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # İstifadəçini əlavə edirik
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
