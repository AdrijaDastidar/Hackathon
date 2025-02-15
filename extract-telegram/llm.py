import os
import groq
from groq import GroqClient
from string import Template
import json
import glob
from timeit import default_timer as timer
from dotenv import load_dotenv
from time import sleep
from tqdm import tqdm
from typing import List
from node import Node
import csv

# Initialize Groq client
load_dotenv()
groq_client = GroqClient(api_key=os.getenv("GROQ_API_KEY"))

# Parse the given CSV for telegram
def parse_csv(file_path: str) -> List[Node]:
    nodes = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            node = extract_information(row)
            nodes.append(node)
    return nodes

# Extract information from the given row
def extract_information(row: dict) -> Node:
    node = Node(
        id=row.get("id"),
        sender=row.get("sender"),
        message=row.get("message"),
        date=row.get("date"),
        translation=row.get("translation")
    )
    return node

if __name__ == "__main__":
    nodes = parse_csv("telegram-eda/top_20_rows.csv")
    for node in nodes:
        print(node)
