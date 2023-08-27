import requests

AIRTABLE_BASE_ID = 'appusI3ZyTQerSfSa'
AIRTABLE_API_KEY = 'patFfF4vN9DZI2qMc'
AIRTABLE_TABLE_NAME = 'Words'

ENDPOINT = 'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# Python Requests Headers
headers = {
    "Authorization": "Bearer {AIRTABLE_API_KEY}",
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
        "Conjugation": [
          "rec7nIHffS0Hoialz",
          "recN9gRxxPEd4qf65",
          "reclFodJHhW5SxPsy",
          "recQphl3CE3gYY8lp",
          "recG0sRlSPoIJJwfj",
          "recOJkOOPWW1BVSct",
          "recP2i5qbNs2oTb0e",
          "reck7HXuRdoZq9Dw0",
          "recJhSVQlGABnNAH7",
          "recTGXygnupuRTT8u",
          "recetNlYvvT8H1zSt",
          "recW4MBs06aUvq6Dy",
          "recPr4CR66ZrEDvFZ",
          "recZRfxQeHMWVHZ3H",
          "reclyilnHKeCcTk38",
          "recw6BkM17xK0vcFt",
          "recnXHPV9fIjXVsvs",
          "recSULhH8fL1ngb7j",
          "reca5hs7359ArXvwQ",
          "recq3iuH9nSortw19",
          "recYhMqoBdnTo2duq",
          "recb8pUTrEvNF5nAo",
          "rec8JMUcvVBTGG1TF",
          "recisUM7NV0CWH0y0",
          "recGKY8SSZiMK4vY0",
          "recfohE4W5WuJynb9",
          "rec7Q5yd0F6qkpHgt",
          "recIRiKCjJhLcHPuV",
          "recxL2IPpT9PNakuh",
          "recFwOvrojrKRmFUI",
          "recqNqbtaCGYY57yI",
          "recrFDTJJcMXz0TK4",
          "reck69s7bP1sHKNDy",
          "recXukWPchAw89GEi",
          "reclrcy79KoNA8YxP",
          "rec1J5AMSH503tpQz",
          "recmAOEpHvzBsmvKs",
          "recQ3ij6TJYFcXkDa",
          "recCyHsb9fszqQe37",
          "rec3Jz6lPkOFyoK8z",
          "recI2xAjI0u8pXjFo",
          "recuHBU0DIA0LSsV4",
          "recsgHIxdI0yoT8xT",
          "recvsBZFr7yWYYPDV",
          "recjZc55uNYxtJI8U",
          "reczOlAUTYhkeVdZP",
          "recsjqBxciwLdMzZR",
          "rectMyvwDUoPCTsgT",
          "recM4ObGty8wvFoOE",
          "recV5nwusqV44wMlV",
          "recHA7MQd0RNCBTf4",
          "recNKMlGKD7cqn8oD",
          "recO9mNey1UaO21ng",
          "recqEqJxNzMI79qfg",
          "recBaAGyeHTEOKLU2",
          "recJ8lI3uwfLSI8FE",
          "recnGoGLlFW5aW3t9"
        ]
      }
    },
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
        "Conjugation": [
          "rec7nIHffS0Hoialz",
          "recN9gRxxPEd4qf65",
          "reclFodJHhW5SxPsy",
          "recQphl3CE3gYY8lp",
          "recG0sRlSPoIJJwfj",
          "recOJkOOPWW1BVSct",
          "recP2i5qbNs2oTb0e",
          "reck7HXuRdoZq9Dw0",
          "recJhSVQlGABnNAH7",
          "recTGXygnupuRTT8u",
          "recetNlYvvT8H1zSt",
          "recW4MBs06aUvq6Dy",
          "recPr4CR66ZrEDvFZ",
          "recZRfxQeHMWVHZ3H",
          "reclyilnHKeCcTk38",
          "recw6BkM17xK0vcFt",
          "recnXHPV9fIjXVsvs",
          "recSULhH8fL1ngb7j",
          "reca5hs7359ArXvwQ",
          "recq3iuH9nSortw19",
          "recYhMqoBdnTo2duq",
          "recb8pUTrEvNF5nAo",
          "rec8JMUcvVBTGG1TF",
          "recisUM7NV0CWH0y0",
          "recGKY8SSZiMK4vY0",
          "recfohE4W5WuJynb9",
          "rec7Q5yd0F6qkpHgt",
          "recIRiKCjJhLcHPuV",
          "recxL2IPpT9PNakuh",
          "recFwOvrojrKRmFUI",
          "recqNqbtaCGYY57yI",
          "recrFDTJJcMXz0TK4",
          "reck69s7bP1sHKNDy",
          "recXukWPchAw89GEi",
          "reclrcy79KoNA8YxP",
          "rec1J5AMSH503tpQz",
          "recmAOEpHvzBsmvKs",
          "recQ3ij6TJYFcXkDa",
          "recCyHsb9fszqQe37",
          "rec3Jz6lPkOFyoK8z",
          "recI2xAjI0u8pXjFo",
          "recuHBU0DIA0LSsV4",
          "recsgHIxdI0yoT8xT",
          "recvsBZFr7yWYYPDV",
          "recjZc55uNYxtJI8U",
          "reczOlAUTYhkeVdZP",
          "recsjqBxciwLdMzZR",
          "rectMyvwDUoPCTsgT",
          "recM4ObGty8wvFoOE",
          "recV5nwusqV44wMlV",
          "recHA7MQd0RNCBTf4",
          "recNKMlGKD7cqn8oD",
          "recO9mNey1UaO21ng",
          "recqEqJxNzMI79qfg",
          "recBaAGyeHTEOKLU2",
          "recJ8lI3uwfLSI8FE",
          "recnGoGLlFW5aW3t9"
        ]
      }
    }
  ]
}

# HTTP Methods
# What is the method for "create" -> POST


r = requests.post(ENDPOINT, json=data, headers=headers, timeout=10)
print(r.json())