# Sentiment Show 💬✨

A lightweight sentiment analysis web app that helps users understand the tone of their text in real-time. Type a sentence, and Sentiment Show will classify it as Positive Sentiment or Negative Sentiment.

---

## How It Works 🧭

- Enter a sentence into the input box (e.g., "I love this product!") ✍️
- Click the Analyze button 🔍
- Immediately see the predicted sentiment:
  - Positive Sentiment
  - Negative Sentiment
- Behind the scenes, your text is preprocessed (tokenized, cleaned, normalized), vectorized using word frequencies, and fed into a Logistic Regression model to produce a probability-based prediction using the sigmoid function.

---

## Why It Matters: UN SDG Alignment 🌍

Sentiment Show contributes to multiple United Nations Sustainable Development Goals by enabling safe, inclusive, and informed digital interactions.

- SDG 16 — Peace, Justice, and Strong Institutions 🕊️⚖️

  - Detects toxic or hostile language to promote safer digital spaces.
  - Can be adapted for moderation workflows to reduce harassment and abuse.
  - Supports transparent and auditable decision-making via a simple, interpretable model.

- SDG 3 — Good Health and Well‑being 🧠💚

  - Can act as a signal detector for negative affect or distress in text (e.g., social posts, feedback), supporting early well-being interventions.
  - Enables lightweight monitoring tools for mental health support systems.

- SDG 10 — Reduced Inequalities 🤝🌐
  - Helps identify biased, hateful, or exclusionary language to mitigate inequality and discrimination.
  - Can be embedded into reporting tools to surface patterns of bias for corrective action.

Additional SDG impact:

- SDG 4 — Quality Education 🎓

  - Teaches core NLP and ML concepts with an interpretable from-scratch implementation.
  - Can be used in classrooms and workshops to demonstrate ethical AI.

- SDG 9 — Industry, Innovation and Infrastructure 🏗️

  - Implements a robust, efficient, low-dependency model suitable for scalable deployments.
  - Encourages reproducible ML pipelines with transparent metrics and artifacts.

- SDG 11 — Sustainable Cities and Communities 🏙️

  - Supports community moderation and civic platforms to maintain healthy discourse.

- SDG 17 — Partnerships for the Goals 🤝
  - Provides a simple baseline system that organizations can extend, benchmark, or integrate into larger responsible AI initiatives.

---

## Technical Implementation 🛠️

Model: Logistic Regression (binary classification) trained on Twitter data.

1. Data Pipeline 🧹📊

- Dataset: Labeled Twitter data (positive/negative).
- Preprocessing: Lowercasing, URL/handle removal, tokenization, stopword filtering, stemming/lemmatization.
- Feature Engineering: Word frequency dictionary built over the corpus; each tweet mapped to a feature vector of token counts/frequencies.
- Split: Train/validation/test split to ensure unbiased evaluation.

2. Learning Algorithm (built from first principles) 🧮

- Sigmoid function σ(z) = 1 / (1 + e^(−z)) to convert linear scores to probabilities.
- Hypothesis: h_θ(x) = σ(θ·x).
- Loss: Binary cross-entropy to penalize misclassifications.
- Gradient Descent: Iteratively updated parameters to minimize the loss.
- Parameter Updates: θ := θ − α ∇J(θ), where α is the learning rate; implemented with vectorized operations for efficiency.
- Regularization (optional): Can incorporate L2 penalty to reduce overfitting.

3. Training Loop 🔁

- Initialize θ to zeros/small random values.
- For each epoch: compute predictions, loss, gradients; update θ.
- Track metrics on a validation set to detect over/underfitting.
- Persist Artifacts: Learned parameters (theta.pickle) and frequency dictionary (freqs.pickle) saved for inference.

4. Inference Pathway 🚀

- Preprocess input sentence using the same pipeline as training.
- Vectorize with the stored frequency dictionary.
- Compute probability p = σ(θ·x).
- Classify as Positive if p ≥ 0.5, else Negative.

5. Evaluation 📈

- Tested on held-out Twitter data with an accuracy of 0.9970 ✅.
- Metrics like precision, recall, and F1 can also be computed depending on the use case.

6. System/Integration 🧩

- Backend serves a form where users submit text.
- The app loads theta.pickle and freqs.pickle at startup for low-latency predictions.
- Lightweight design enables fast responses without heavy external dependencies.

7. Interpretability and Ethics 🧭

- Logistic Regression provides interpretable coefficients that indicate which tokens drive predictions.
- Recommended safeguards: bias evaluation, threshold tuning, and human-in-the-loop review for sensitive domains.

---

## Screenshots 🖼️

Below are screenshots of the app with short explanations.

|                                                                                                                        Screenshot | Description                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                          <img src="images/src/app.png" alt="App main screen" style="width:400px; height:250px; object-fit:contain;"/> | **App main screen** — the home interface where users enter text to analyze sentiment. The input box and the "Analyze Sentiment" button are visible.                                                   |
| <img src="images/src/negative-sentiment.png" alt="Negative sentiment result" style="width:400px; height:250px; object-fit:contain;"/> | **Negative sentiment result** — an example output when the model classifies the input as negative. Shows the predicted label and any additional info (score, highlighted words, etc.) as implemented. |
| <img src="images/src/positive-sentiment.png" alt="Positive sentiment result" style="width:400px; height:250px; object-fit:contain;"/> | **Positive sentiment result** — an example output when the model classifies the input as positive. Displays the predicted label and related details.                                                  |

---

## 🚀 Deployment

The **Sentiment Analysis Model** was deployed as a **Django web application** 🌐.  
Deployment was done on [**Render**](https://render.com/), a reliable cloud hosting platform that supports **automatic builds** and **continuous deployment** directly from GitHub.

### ⚙️ Configuration Details

- 🧠 **Framework:** Django
- 🐍 **Backend Language:** Python
- 🔥 **Server:** Gunicorn (used as the WSGI HTTP server)
- 📦 **Dependencies:** Listed in `requirements.txt`
- 🗂️ **NLTK Data:** The required datasets (`stopwords` and `twitter_samples`) are automatically downloaded during the build process using the custom `download_nltk_data.py` script.
- 🔐 **Environment Variables:**  
  The app dynamically sets the `ALLOWED_HOSTS` using the `RENDER_EXTERNAL_HOSTNAME` environment variable for secure deployment.

### 🌍 Live Application

You can access the live app here:  
👉 **[https://sentiment-analysis-app-8b4o.onrender.com](https://sentiment-analysis-app-8b4o.onrender.com)**

Once deployed, the app allows users to:

- ✍️ Enter any statement or sentence
- 🤖 Analyze its sentiment
- 🎯 Receive a classification as either **Positive Sentiment** or **Negative Sentiment**

### 🧩 Example Use

Type something like:

> “I love how easy this app is to use!” 💬  
> and the model will return **Positive Sentiment\*\***

---

## 🤖 Ethical Reflection

### ⚖️ How might bias in your data affect outcomes?

Like most AI models trained on text data, the sentiment analysis model can inherit **biases present in the training dataset**.  
If the tweets used to train the model are **not diverse or balanced**, the model might:

- Misinterpret neutral or culturally specific expressions 😕
- Associate certain words or phrases with a particular sentiment unfairly 😔
- Perform better on some linguistic styles or demographics than others 🗣️

To minimize this, diverse and representative datasets should be used, and the model should be **periodically retrained** to adapt to new language patterns and avoid reinforcing stereotypes.

---

### 🌱 How does your solution promote fairness and sustainability?

This solution promotes **fairness** by:

- Treating all input text equally regardless of the author’s identity or origin 👥
- Providing **transparent results** that users can interpret and question 🔍
- Encouraging responsible use of AI by highlighting both its power and limitations ⚙️

It supports **sustainability** by:

- Helping organizations and researchers understand public opinion more efficiently 💡
- Enabling **data-driven decision-making** that can improve communication, service delivery, and policy design 📊
- Aligning with **UN SDG 9 (Industry, Innovation & Infrastructure)** and **UN SDG 16 (Peace, Justice & Strong Institutions)** through the use of ethical and transparent technology 💚

---

## 👨‍💻 Author

**Name:** Stephen Omusula  
**📧 Email:** [stephenomusula3@gmail.com](mailto:stephenomusula3@gmail.com)

💡 _Created and deployed a sentiment analysis web app using Django and Render._  
🌍 _Passionate about Artificial Intelligence, ethics in technology, and sustainable development._
