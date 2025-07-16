# Complaint Classification by LLM and External APIs

## Project Description


This project implements a system for **automated customer complaint processing** using FastAPI integrated with public APIs.

The application accepts POST requests with the complaint text, sends it to a Sentiment Analysis API to detect sentiment, and uses OpenAI GPT to automatically categorize the complaint as **“technical,” “payment,” or “other.”**

All data is stored in a SQLite database with information about the text, status, timestamp, sentiment, and category, and the user receives a JSON response with the result.

If external APIs are unavailable, the system saves “unknown” for sentiment and “other” for the category, ensuring **stable complaint processing without data loss.**

## Project Installation

### Clone the repository

```bash
    mkdir project \
    cd project \
    git clone git@github.com:Trydimas/message_classification.git
```

### Create a virtual environment and install requirements (Linux)

```bash
   cd message_classification
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```

### Configure environment variables


## Running the Project

```bash
    python main.py
```


## User Guide

### Health check

```bash
    'http://localhost:8080/api/' \
  -H 'accept: application/json'; echo    
```

Example response:

```commandline
    OK!
```

### Submit a complaint for classification and save it to the database

```bash
    curl -X POST \
      "http://localhost:8080/api/message/" \
      -H "accept: application/json" \
      -H "Content-Type: application/json" \
      -d '{"message": "good service"}'
```

Example response:

```commandline
Response body
{
  "status": "Open",
  "sentiment": "positive",
  "category": "Другое",
}
```

### Retrieve all saved complaints

```bash
    curl -X 'GET' \
  'http://localhost:8080/api/message/' \
  -H 'accept: application/json'; echo
```


Example response:

```commandline
Response body
[
  {
    "text": "good service",
    "status": "Open",
    "id": 1,
    "category": "Другое",
    "created_on": "2025-07-16T18:30:58",
    "sentiment": "positive"
  }
]
```


