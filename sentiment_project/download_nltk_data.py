import nltk
import os

# Find path of nltk.txt relative to this script
base_dir = os.path.dirname(__file__)
nltk_path = os.path.join(base_dir, "nltk.txt")

with open("nltk.txt") as f:
    packages = f.read().splitlines()

for package in packages:
    nltk.download(package)
