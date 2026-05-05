import json
from datetime import datetime

BUCKET_FILE = "bucket_artifacts.jsonl"


def emit_bucket_artifact(data):

    try:
        trace_id = data.get("trace_id")

        input_data = data.get("input", {})
        output_data = data.get("output", {})

        if not input_data and not output_data:
            output_data = data

        # ✅ FIXED timestamp (prefer original)
        timestamp = data.get("timestamp") or datetime.utcnow().isoformat()

        artifact = {
            "trace_id": trace_id,
            "input": input_data,
            "output": output_data,
            "timestamp": timestamp,
            "layer": data.get("layer", "NICAI_PIPELINE")
        }

        # WRITE
        with open(BUCKET_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(artifact) + "\n")

    except Exception as e:
        print("❌ Bucket emission failed:", e)


# -----------------------------------
# ✅ NEW: READ + VERIFY (MANDATORY)
# -----------------------------------
def verify_bucket_integrity(trace_id):

    try:
        with open(BUCKET_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        matches = []

        for line in lines:
            record = json.loads(line)
            if record.get("trace_id") == trace_id:
                matches.append(record)

        print(f"\n🔍 Bucket Verification for {trace_id}")
        print(f"Records Found: {len(matches)}")

        return matches

    except Exception as e:
        print("❌ Bucket read failed:", e)
        return []
