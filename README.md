# 🚕 Demand Prediction API

> A Machine Learning-powered API to predict demand based on location, time, and historical patterns.

---

## 🌐 Live Demo

🚀 **API Endpoint:**
https://uber-demand-prediction-2.onrender.com

---

## 📖 Overview

This project builds an end-to-end Machine Learning pipeline to predict demand (e.g., ride requests).
The trained model is deployed as a REST API, enabling real-time predictions.

---

## 🧠 Key Features

* ⚡ Real-time demand prediction via API
* 📊 Feature engineering with temporal & lag features
* 🔄 Log transformation for improved accuracy
* 🌐 Deployed on cloud (Render)
* 🧩 Modular and production-ready structure

---

## 🏗️ Tech Stack

| Category      | Tools         |
| ------------- | ------------- |
| Language      | Python        |
| ML Model      | XGBoost       |
| Data Handling | Pandas, NumPy |
| API Framework | Flask         |
| Deployment    | Render        |

---

## 📊 Model Inputs

| Feature      | Description                   |
| ------------ | ----------------------------- |
| `location`   | Pickup location ID            |
| `hour`       | Hour of the day (0–23)        |
| `dow`        | Day of week (0=Mon, 6=Sun)    |
| `pre_demand` | Previous demand (lag feature) |

---

## 🔮 API Usage

### Endpoint

```http
POST /predict
```

### Request

```json
{
  "location": 261,
  "hour": 9,
  "dow": 1,
  "pre_demand": 120
}
```

### Response

```json
{
  "predicted_demand": 180
}
```

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd project
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Server

```bash
python app.py
```

---

## 🧪 Testing

```python
import requests

url = "https://your-app-name.onrender.com/predict"

data = {
    "location": 261,
    "hour": 9,
    "dow": 1,
    "pre_demand": 120
}

response = requests.post(url, json=data)
print(response.json())
```

---

## 📁 Project Structure

```
.
├── app.py                # Flask API
├── demand_model.pkl      # Trained model
├── k.py                  # Test script
├── requirements.txt
└── README.md
```

---

## 🚀 Future Enhancements

* 📍 Geospatial demand visualization
* 📱 Interactive UI (Streamlit)
* 🔔 Real-time alert system
* 📈 Model optimization & tuning


