# 🚀 SVACS End-to-End Pipeline Integration (NICAI + Sanskar)

---

## 📌 Overview

This project demonstrates a **fully integrated, real-time SVACS pipeline** connecting multiple system layers:

**Signal Layer → NICAI → Validation → Sanskar (Intelligence) → State Engine**

The system is:

* Deterministic
* Fully traceable (via `trace_id`)
* Integrated using real HTTP communication (no mocks)

---

## 🎯 Objective

Convert the system from:

> “Working modules in isolation”

to:

> “A fully proven end-to-end execution pipeline with real trace validation”

---

## 🔗 System Architecture

```id="flow-arch"
Signal Layer (Nupur)
        ↓
Perception Event
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

Open Swagger UI:
http://127.0.0.1:8000/docs

Use endpoint:
**POST /nicai/classify**

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
  "validation": {
    "status": "ALLOW"
  },
  "intelligence_event": {
    "trace_id": "cargo-1",
    "risk_level": "MEDIUM",
    "validation_status": "ALLOW"
  }
}
```

---

## 🧠 Key Features

* End-to-end traceability using `trace_id`
* Deterministic intelligence logic (no ML dependency)
* Anomaly override handling
* Real-time API processing
* Validation status propagation
* Live State Engine integration via HTTP

---

## 📁 Project Structure

```id="project-structure"
├── api_server.py
├── validator.py
├── sanskar_engine.py
├── send_to_raj.py
├── bucket_emitter.py
├── telemetry_emitter.py
├── utils.py
├── logs/
│   ├── perception_logs.json
│   ├── intelligence_events.json
│   ├── state_response.json
│   └── END_TO_END_TRACE_PROOF.json
├── REVIEW_PACKET.md
└── README.md
```

---

## 🔍 End-to-End Proof

File:
`logs/END_TO_END_TRACE_PROOF.json`

Contains full pipeline trace:

* perception_event
* nicai_signal
* validation output
* intelligence_event
* state_event

✔ Same `trace_id` preserved across all stages
✔ Verified State Engine responses included

---

## 📊 Logs

* `logs/perception_logs.json` → Real perception events (15+)
* `logs/intelligence_events.json` → Generated intelligence outputs
* `logs/state_response.json` → State Engine responses
* `logs/END_TO_END_TRACE_PROOF.json` → Full trace proof

---

## ✅ Validation Rules

* Same `trace_id` must persist across all layers
* No schema modification allowed
* No mocked data used in final execution
* Real HTTP integration must be verified

---

## 🧪 Testing

Tested with 5 critical scenarios:

* Cargo vessel
* Speedboat
* Submarine
* Low confidence detection
* Anomalous signal

✔ All events returned HTTP 200
✔ Correct state mapping verified

---

## 🏁 Final Outcome

✔ Fully integrated pipeline
✔ Real execution proof achieved
✔ End-to-end trace verified
✔ State Engine integration confirmed

---

## 🚀 Final Status

**SVACS Pipeline is now:**

* Fully integrated
* Deterministic
* Traceable
* Execution verified
* Ready for BHIV testing protocol

---
