#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    # Basic Authentication istifadə edərək sorğu göndəririk
    # auth parametri (username, password) tuplu qəbul edir
    r = requests.get(url, auth=(username, password))

    # Cavabı JSON-a çeviririk və 'id' dəyərini götürürük.
    # Əgər giriş uğursuz olarsa, 'id' açarı tapılmayacaq və
    # .get() metodu avtomatik olaraq None qaytaracaq.
    print(r.json().get('id'))
