import requests
import json


class fetch:
    def __init__(self, **params):
        self.ROOT_URL = "http://localhost:8000"
        self.PARAMS = params

    def get(self):
        fetch_data = requests.get(self.ROOT_URL, self.PARAMS).json()
        return fetch_data

    def post(self, query, **variables):
        variables = variables
        r = requests.post(self.ROOT_URL, json={"query": query, 'variables': variables})
        print(r.json())
        return r.json()

    def mutation(self, mutation, **variables):
        variables = variables
        r = requests.post(self.ROOT_URL, json={"query": mutation, 'variables': variables})
        print(r.json())
        return r.json()
