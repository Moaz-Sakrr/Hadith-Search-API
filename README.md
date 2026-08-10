# 📖 Hadith Search API

A RESTful API for searching Arabic Hadith using **Arabic text preprocessing, exact matching, and fuzzy matching**.

The project is built with **Python and Flask** and provides a simple API that allows users and applications to search Hadith efficiently, even when the search query contains variations in Arabic text.

---

## ✨ Features

* 🔍 **Fuzzy Hadith Search** using RapidFuzz
* 🎯 **Exact Hadith Search**
* 🧹 **Arabic Text Preprocessing**
* 🔤 Arabic text normalization
* 🚫 Arabic stopword removal
* ✂️ Tokenization
* 🧼 Tashkeel/diacritics removal
* 🌐 RESTful API built with Flask
* 📚 Interactive API documentation using Swagger
* 📦 JSON responses
* ⚡ Lightweight and easy to run locally

---

## 🧠 How It Works

The API processes the user's Arabic search query before performing the search.

```text
                 User Query
                     │
                     ▼
            Arabic Preprocessing
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Remove     Normalize   Remove
      Tashkeel     Arabic     Stopwords
                     │
                     ▼
              Processed Query
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Exact Search         Fuzzy Search
          │                     │
          └──────────┬──────────┘
                     ▼
              Search Results
                     │
                     ▼
                JSON Response
```

This preprocessing helps improve search quality when Arabic text contains different forms, diacritics, or common words that are not useful for matching.

---

## 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| 🐍 Python    | Main programming language |
| 🌐 Flask     | REST API framework        |
| 📊 Pandas    | Dataset handling          |
| 🔤 NLTK      | Arabic text preprocessing |
| 🔎 RapidFuzz | Fuzzy string matching     |
| 📚 Flasgger  | Swagger API documentation |
| 🗃️ CSV      | Hadith dataset storage    |

---

## 📂 Project Structure

```text
Hadith-Search-API/
│
├── app.py                 # Flask application and API endpoints
├── preprocess.py          # Arabic text preprocessing
├── Search.py              # Search and matching logic
├── utilz.py               # Utility functions and dataset handling
│
├── Hadeths.csv            # Hadith dataset
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignored files
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Moaz-Sakrr/Hadith-Search-API.git
```

Move into the project directory:

```bash
cd Hadith-Search-API
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the API

```bash
python app.py
```

The API should now be available at:

```text
http://127.0.0.1:5000
```

---

# 📚 API Documentation

The project includes interactive Swagger documentation through **Flasgger**.

After starting the application, open:

```text
http://127.0.0.1:5000/apidocs
```

From Swagger UI, you can explore and test the available endpoints directly from your browser.

---

# 🔌 API Endpoints

## 🏠 Home

### `GET /`

Returns basic information about the API.

Example:

```http
GET /
```

---

## 🔍 Fuzzy Search

### `GET /search`

Searches for Hadith using fuzzy matching.

This endpoint is designed to find relevant results even when the user's query is not an exact match.

Example:

```http
GET /search?search=الصلاة
```

Example using Python:

```python
import requests

url = "http://127.0.0.1:5000/search"

params = {
    "search": "الصلاة"
}

response = requests.get(url, params=params)

print(response.json())
```

---

## 🎯 Exact Search

### `GET /search/exact`

Searches the dataset using exact matching.

Example:

```http
GET /search/exact?search=الصلاة
```

Example using Python:

```python
import requests

url = "http://127.0.0.1:5000/search/exact"

params = {
    "search": "الصلاة"
}

response = requests.get(url, params=params)

print(response.json())
```

---

## 🧹 Text Cleaning

### `GET /clean`

Processes Arabic text using the project's preprocessing pipeline.

The preprocessing includes operations such as:

* Removing HTML
* Removing Arabic diacritics
* Arabic character normalization
* Stopword removal
* Text tokenization

Example:

```http
GET /clean?search=الصَّلَاةُ
```

---

# 🔤 Arabic Text Preprocessing

One of the main components of the project is the Arabic preprocessing pipeline.

The preprocessing module is designed to make Arabic search more consistent by handling common variations in Arabic text.

### Processing Steps

```text
Raw Arabic Text
      │
      ▼
Remove HTML
      │
      ▼
Remove Tashkeel
      │
      ▼
Arabic Normalization
      │
      ▼
Stopword Removal
      │
      ▼
Tokenization
      │
      ▼
Processed Text
```

This processed text is then used by the search functionality.

---

# 🔎 Fuzzy Matching

The project uses **RapidFuzz** to perform approximate string matching.

Instead of requiring an exact character-by-character match, fuzzy search can identify text that is sufficiently similar to the user's query.

This is particularly useful for Arabic search, where differences in:

* Diacritics
* Character forms
* Spelling
* Extra words
* Query formatting

can affect traditional exact matching.

---

# 📊 Dataset

The API uses a CSV dataset containing Arabic Hadith.

The dataset is stored locally as:

```text
Hadeths.csv
```

The dataset is used for educational and development purposes within this project.

---

# 📸 API Demo

## Swagger UI

Add a screenshot of the Swagger interface here:

```markdown
![Swagger UI](images/swagger.png)
```

## Example API Response

You can also add a screenshot or example response here:

```markdown
![API Response](images/api-response.png)
```

---

# ⚙️ Requirements

The main dependencies include:

```text
Flask
Flasgger
NumPy
Pandas
RapidFuzz
NLTK
```

All required packages are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 🧪 Example Workflow

A typical search request works as follows:

```text
Client
  │
  │  Search Query
  ▼
Flask API
  │
  ▼
Arabic Preprocessing
  │
  ▼
Search Engine
  │
  ├── Exact Matching
  │
  └── Fuzzy Matching
  │
  ▼
Matching Hadith
  │
  ▼
JSON Response
```

---

# 🎯 Project Goals

The main goals of this project are:

* Build a practical REST API using Python and Flask.
* Apply Arabic NLP preprocessing techniques.
* Improve text search using fuzzy matching.
* Provide an easy-to-use API for Hadith retrieval.
* Practice designing and documenting backend APIs.
* Explore practical applications of Arabic text processing.

---

# 🔮 Future Improvements

Possible future improvements include:

* 🔹 Add more advanced Arabic NLP techniques.
* 🔹 Improve ranking of search results.
* 🔹 Add pagination.
* 🔹 Add filtering by Hadith book/source.
* 🔹 Add authentication and API keys.
* 🔹 Add automated unit tests.
* 🔹 Add Docker support.
* 🔹 Deploy the API to a cloud platform.
* 🔹 Add a web interface for users.
* 🔹 Add semantic search using Arabic embeddings.
* 🔹 Replace CSV storage with a database for larger datasets.

---

# 📄 License

This project is intended for educational and learning purposes.

---

# 👨‍💻 Author

**Moaz Mohamed**

AI Student | Machine Learning | Deep Learning | Computer Vision | Data Science

GitHub:

https://github.com/Moaz-Sakrr

LinkedIn :

www.linkedin.com/in/moaz-mohamed-71b9a7312

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 🔗 Repository

https://github.com/Moaz-Sakrr/Hadith-Search-API
