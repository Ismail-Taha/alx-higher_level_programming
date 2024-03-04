#!/usr/bin/python3
"""
script that:
    - takes in a letter
    - sends POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    query_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": query_letter}

    resp = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        rest_json = resp.json()
        if rest_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(rest_json.get("id"), rest_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
