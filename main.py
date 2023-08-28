import requests

AIRTABLE_BASE_ID = 'appusI3ZyTQerSfSa'
AIRTABLE_API_KEY = 'patFfF4vN9DZI2qMc.ef219b1cb4cc4b365f432c23f0738551ceae78cdfced6cace4517167b5668876'
AIRTABLE_TABLE_NAME = 'Words'

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# Python Requests Headers
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application.json"
}

# Data / Content
data = {
  "records": [
    {
      "fields": {
        "Word": "Choose",
        "Root": "Choose",
        "Past Tense": "Chose",
        "Palabra": "Escoger",
        "Raiz": "Escog",
        "Shimi": "Akllay",
        "Sapi": "Aklla",
        "Word Type": [
          "Verb"
        ],
        "Category": [
          "Action"
        ],
      }
    }
    }

# HTTP Methods
# What is the method for "create" -> POST


r = requests.post(endpoint, json=data, headers=headers, timeout=10)
print(r.json())
