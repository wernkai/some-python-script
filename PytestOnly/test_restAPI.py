"""
Purpose: Use pytest to verify REST API respond
"""

import requests
import pytest

url = "https://api.funtranslations.com/translate/yoda.json?text=Let go for a drink"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
responsej = response.json()

class TestClass:
    def test_response_type(self):
        assert str(type(response)) == "<class 'requests.models.Response'>"

    def test_response_json(self):
        assert str(type(response.json())) == "<class 'dict'>"

    def test_response_status(self):
        assert response.status_code == 429
    
    def test_response_json_status(self):
        assert responsej["error"]["code"] == 429
