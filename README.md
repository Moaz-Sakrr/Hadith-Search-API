# 📖 Hadith Search API

A RESTful API built with **Flask** for searching Hadiths using Arabic text preprocessing and multiple search techniques. The API supports text cleaning, exact matching, and approximate (fuzzy) matching, and includes interactive API documentation powered by **Swagger (Flasgger)**.

---

## 🚀 Features

- 🧹 Clean Arabic text by removing:
  - HTML tags
  - Arabic diacritics (Tashkeel)
  - Arabic stopwords
- 🔍 Exact Match Search
- 🤖 Approximate (Fuzzy) Search using **RapidFuzz**
- 📚 Interactive Swagger Documentation
- ⚡ Fast and lightweight Flask REST API

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Flasgger (Swagger UI)
- Pandas
- NLTK
- RapidFuzz

---

## 📂 Project Structure

```
.
├── app.py                # Main Flask application
├── Search.py             # Search algorithms
├── preprocess.py         # Arabic text preprocessing
├── utilz.py              # Dataset loading
├── requirements.txt
├── README.md
└── ...
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Hadith-Search-API.git
cd Hadith-Search-API
```

### 2. Create a virtual environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

```bash
python app.py
```

The server will start on:

```
http://127.0.0.1:5000
```

---

## 📖 Swagger Documentation

After running the server, open:

```
http://127.0.0.1:5000/apidocs
```

to explore and test all API endpoints.

---

# API Endpoints

## 🏠 Home

**GET /**

Returns general information about the API.

---

## 🧹 Clean Input

**GET /clean**

Cleans Arabic text before searching.

### Example

```
GET /clean?search=وَاللَّهُ يَعْصِمُكَ مِنَ النَّاسِ
```

### Response

```json
{
    "cleaned_input": "الله يعصمك الناس"
}
```

---

## 🔍 Exact Match Search

**GET /search/exact**

Searches for Hadiths that exactly match the processed query.

### Example

```
GET /search/exact?search=الصلاة
```

---

## 🤖 Approximate (Fuzzy) Search

**GET /search/fuzzy**

Performs approximate string matching using **RapidFuzz**.

### Example

```
GET /search/fuzzy?search=الصلاه
```

---

## 🧠 Text Preprocessing

The API preprocesses Arabic text by:

- Removing HTML tags
- Removing Arabic diacritics (Tashkeel)
- Normalizing Arabic letters
- Removing Arabic stopwords
- Tokenizing the text

This improves the quality and consistency of search results.

---

## 📌 Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Moaz Mohamed**

AI Student | Machine Learning & Computer Vision Enthusiast

---

## 📄 License

This project is intended for educational and learning purposes.