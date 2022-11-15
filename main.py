import os
import sys
import json
import requests

def dox(name, email):
    print("Collecting data on {}".format(name))
    print("Collecting data on {}".format(email))

    # Search Google for the person's name
    google_results = requests.get("https://www.google.com/search?q={}".format(name))

    # Search Google for the person's email
    google_email_results = requests.get("https://www.google.com/search?q={}".format(email))

    # Search Github for the person's name
    github_results = requests.get("https://api.github.com/search/users?q={}".format(name))

    # Search Facebook for the person's name
    facebook_results = requests.get("https://www.facebook.com/search/people/?q={}".format(name))

    print("Google results:")
    print(google_results.text)
    print("Google email results:")
    print(google_email_results.text)
    print("Github results:")
    print(github_results.text)
    print("Facebook results:")
    print(facebook_results.text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dox.py [name] [email]")
        sys.exit(1)

    dox(sys.argv[1], sys.argv[2])
