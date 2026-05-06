import json
from datetime import datetime

TELEMETRY_FILE = "telemetry_metrics.jsonl"


def emit_telemetry(signal, result, layer="NICAI_PIPELINE"):
    """
    Emit telemetry data for InsightFlow observability 
    """

    try:
        telemetry_record = {
            "trace_id": result.get("trace_id") or signal.get("trace_id"),

            # source info
            "dataset_id": signal.get("dataset_id"),
            "vessel_type": signal.get("asset_id"),

            # model output
            "confidence": result.get("confidence") or signal.get("value"),
            "risk_level": result.get("risk_level"),
            "anomaly_flag": result.get("anomaly_flag", False),

            # validation info (if present)
            "validation_status": result.get("validation_status"),

            # system info
            "layer": layer,
            "timestamp": signal.get("timestamp") or datetime.utcnow().isoformat()
        }

        # WRITE (jsonl format)
        with open(TELEMETRY_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(telemetry_record) + "\n")

    except Exception as e:
        print("❌ Telemetry emission failed:", e)
