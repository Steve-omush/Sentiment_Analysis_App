import nltk
import os

# Ensure NLTK data goes into a predictable location Render will use
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download only the required datasets
nltk.download("stopwords", download_dir=nltk_data_dir)
nltk.download("twitter_samples", download_dir=nltk_data_dir)

print("✅ NLTK data downloaded successfully to", nltk_data_dir)
