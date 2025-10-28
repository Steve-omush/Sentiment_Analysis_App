import nltk

with open("nltk.txt") as f:
    packages = f.read().splitlines()

for package in packages:
    nltk.download(package)