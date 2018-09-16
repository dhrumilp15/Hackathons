import requests
import json
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/banana")
def banana():
    return "Hello World!"

response = requests.get('https://api.td-davinci.com/api/customers/0096e7fb-b384-4dc2-a6b0-3faf6de5686b_c18dca28-f10f-4a0a-b905-db636046bd4c',
    headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiZThmZGM2ZWQtOWVmMi0zZTViLWFjNzItYzAzZGUyNWY2ZDYzIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIwMDk2ZTdmYi1iMzg0LTRkYzItYTZiMC0zZmFmNmRlNTY4NmIifQ.lN1DmnXacItZYY63EGTZPiXXeh7UIKx-55X6NOwlX0g'})
response_data = response.json()

with open('data.json', 'w') as outfile:
    json.dump(response_data, outfile)
