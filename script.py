import requests
from models import Band, Bank, Robbery
from faker import Faker
from datetime import date
import random

BASE_URL = "http://127.0.0.1:8000"

fake = Faker()

# create a bandit
def create_bandit():
    url = f"{BASE_URL}/bandits/"
    data = {
        "specialization": fake.job(),
        "level": random.randint(1, 5),
        "status": random.choice(["good", "bad"]),
        "nickname": fake.user_name(),
        "contact": fake.email(),
        "date": str(fake.date_this_decade()),
    }
    response = requests.post(url, json=data)
    print(response.content)
    return response.json()

# create a bank
def create_bank():
    url = f"{BASE_URL}/banks/"
    data = {
        "rate": random.randint(1, 5),
        "total_sum": random.randint(100000, 1000000),
        "address": fake.address(),
        "security_rate": random.randint(1, 5),
        "name": fake.company(),
    }
    response = requests.post(url, json=data)
    return response.json()

# Create a robbery
def create_robbery():
    url = f"{BASE_URL}/robberies/"
    data = {
        "total_sum_for_each": random.randint(1000, 10000),
        "part": random.randint(1, 5),
        "date": str(fake.date_this_decade()),
        "mark": random.randint(1, 100),
        "band_id": random.randint(1, 500),  
        "bank_id": random.randint(1, 500),
    }
    response = requests.post(url, json=data)
    return response.json()

# Create a large number of bandits, banks, and robberies
for _ in range(500):
    create_bandit()

for _ in range(500):
    create_bank()

for _ in range(500):
    create_robbery()

