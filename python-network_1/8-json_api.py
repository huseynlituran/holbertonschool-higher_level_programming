#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
ht.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # arqument verilibsə onu götürürük, yoxdursa boş string ""
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    # POST sorğusu üçün parametrlər
    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"

    r = requests.post(url, data=payload)

    try:
        # JSON formatına çevirməyə çalışırıq
        json_response = r.json()

        # Əgər JSON boşdursa (dictionary boşdursa)
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")

    except ValueError:
        # Əgər JSON valid deyilsə
        print("Not a valid JSON")
