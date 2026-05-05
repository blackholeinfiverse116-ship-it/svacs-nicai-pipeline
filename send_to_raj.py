import requests
import time

URL = "https://602b-157-119-200-153.ngrok-free.app/ingest/intelligence"

headers = {
    "Content-Type": "application/json",
    "ngrok-skip-browser-warning": "true"
}

# 👉 5 events list
events = [

    # 1. Cargo
    {
        "trace_id": "cargo-1",
        "vessel_type": "cargo",
        "confidence": 0.6396,
        "risk_level": "MEDIUM",
        "anomaly_flag": False,
        "explanation": "Moderate confidence acoustic detection — medium risk",
        "validation_status": "ALLOW"
    },

    # 2. Speedboat
    {
        "trace_id": "speedboat-1",
        "vessel_type": "speedboat",
        "confidence": 0.3922,
        "risk_level": "HIGH",
        "anomaly_flag": False,
        "explanation": "Low confidence acoustic detection — high risk",
        "validation_status": "ALLOW"
    },

    # 3. Submarine
    {
        "trace_id": "submarine-1",
        "vessel_type": "submarine",
        "confidence": 0.1734,
        "risk_level": "CRITICAL",
        "anomaly_flag": True,
        "explanation": "Anomalous acoustic pattern detected",
        "validation_status": "ALLOW"
    },

    # 4. Low Confidence
    {
        "trace_id": "low-1",
        "vessel_type": "unknown",
        "confidence": 0.20,
        "risk_level": "HIGH",
        "anomaly_flag": False,
        "explanation": "Low confidence detection",
        "validation_status": "ALLOW"
    },

    # 5. Anomaly
    {
        "trace_id": "anomaly-1",
        "vessel_type": "unknown",
        "confidence": 0.02,
        "risk_level": "CRITICAL",
        "anomaly_flag": True,
        "explanation": "Anomalous acoustic pattern detected",
        "validation_status": "ALLOW"
    }
]

# 👉 Loop to send all events
for i, event in enumerate(events, start=1):
    print(f"\n🚀 Sending Event {i}: {event['trace_id']}")

    try:
        response = requests.post(url, json=event, headers=headers)

        print("Status Code:", response.status_code)

        try:
            print("Response:", response.json())
        except:
            print("Raw Response:", response.text)

    except Exception as e:
        print("❌ Error:", e)

    # 👉 Thoda delay (optional but safe)
    time.sleep(1)

print("\n✅ ALL EVENTS SENT")