# 🚀 SVACS End-to-End Pipeline Integration (NICAI + Sanskar)

## 📌 Overview

This project demonstrates a **fully integrated, real-time SVACS pipeline** connecting:

Perception Layer → NICAI → Validation → Sanskar (Intelligence) → State Engine

The system is **deterministic, traceable, and validated using real integration**, not mocks.

---

## 🎯 Objective

Convert the system from:

> “Working modules in isolation”

to:

> “Proven end-to-end pipeline with real execution proof”

---

## 🔗 System Architecture

```
Perception Event (Nupur)
        ↓
NICAI Signal Builder
        ↓
Validation Layer
        ↓
Sanskar Intelligence Engine
        ↓
State Engine (Raj)
        ↓
State Event Output
```

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Requests
* Ngrok

---

## ▶️ How to Run

### 1. Start API Server

```bash
uvicorn api_server:app --reload
```

API runs on:
http://127.0.0.1:8000

---

### 2. Start ngrok

```bash
.\ngrok http 8000
```

You will get a public URL like:
https://your-ngrok-url.ngrok-free.app

---

### 3. Test API

Open:
http://127.0.0.1:8000/docs

Use:
POST /nicai/classify

---

### 4. Send Data to State Engine

```bash
python send_to_raj.py
```

---

## 📦 API Endpoint

### POST `/nicai/classify`

#### Sample Input

```json
{
  "trace_id": "cargo-1",
  "vessel_type": "cargo",
  "confidence_score": 0.6396,
  "dominant_freq_hz": 98,
  "anomaly_flag": false
}
```

---

## 📊 Sample Output

```json
{
  "trace_id": "cargo-1",
  "perception_event": { ... },
  "nicai_signal": { ... },
  "validation": { ... },
  "intelligence_event": {
    "trace_id": "cargo-1",
    "risk_level": "MEDIUM"
  }
}
```

---

## 🧠 Key Features

* End-to-end traceability using `trace_id`
* Deterministic intelligence logic
* Anomaly override system
* Real-time API integration
* State Engine HTTP integration
* Validation status propagation

---

## 📁 Project Structure

```
├── api_server.py
├── validator.py
├── sanskar_engine.py
├── send_to_raj.py
├── bucket_emitter.py
├── utils.py
├── END_TO_END_TRACE_PROOF.json
├── perception_logs.json
├── state_responses.json
├── REVIEW_PACKET.md
└── README.md
```

---

## 🔍 End-to-End Proof

File:
END_TO_END_TRACE_PROOF.json

Includes complete trace:

* perception_event
* nicai_signal
* validation
* intelligence_event
* state_event

---

## 📊 Logs

* perception_logs.json → real perception data
* state_responses.json → state engine responses
* trace proof → full pipeline verification

---

## ✅ Validation Rules

* Same `trace_id` across all layers
* No schema modification
* No mock data used
* Real HTTP integration tested

---

## 🧪 Testing

Tested with 5 cases:

* cargo
* speedboat
* submarine
* low confidence
* anomaly

All responses returned HTTP 200 ✅

---

## 🎥 Demo

(Attach demo video link here)

---

## 🏁 Final Outcome

✔ Fully integrated pipeline
✔ Real execution proof
✔ Trace continuity verified
✔ System ready for validation

---
