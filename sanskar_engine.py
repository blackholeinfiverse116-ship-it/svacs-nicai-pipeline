# OPTIONAL SAFE IMPORT
try:
    from bucket_emitter import emit_bucket_artifact
except ImportError:
    def emit_bucket_artifact(x):
        pass


# -----------------------------------
# RISK LEVEL ENGINE
# -----------------------------------
def get_risk_level(confidence):

    if confidence >= 0.75:
        return "LOW"
    elif confidence >= 0.5:
        return "MEDIUM"
    elif confidence >= 0.3:
        return "HIGH"
    else:
        return "CRITICAL"


# -----------------------------------
# ANOMALY DETECTOR
# -----------------------------------
def detect_anomaly(signal):

    vessel_type = signal.get("asset_id", "unknown")
    metadata = signal.get("metadata", {})

    incoming_flag = metadata.get("anomaly_flag", False)

    # Priority rules
    if incoming_flag is True:
        return True

    if vessel_type == "unknown":
        return True

    return False


# -----------------------------------
# EXPLANATION ENGINE
# -----------------------------------
def generate_explanation(confidence, vessel_type, risk, anomaly):

    if anomaly:
        return "Anomalous acoustic pattern detected — classified as critical risk"

    if vessel_type == "unknown":
        return "Unknown vessel detected — classified as critical risk"

    if risk == "CRITICAL":
        return "Very low confidence acoustic detection — critical risk"

    if risk == "HIGH":
        return "Low confidence acoustic detection — high risk"

    if risk == "MEDIUM":
        return "Moderate confidence acoustic detection — medium risk"

    return f"High confidence acoustic classification of {vessel_type} vessel — low risk"


# -----------------------------------
# MAIN FUNCTION (FINAL FIXED)
# -----------------------------------
def analyze_signal(signal):

    try:
        # ✅ ALWAYS TAKE TRACE FROM SIGNAL (IMPORTANT FIX)
        trace_id = signal.get("trace_id", "TRACE_UNKNOWN")

        confidence = float(signal.get("value", 0.0))
        vessel_type = signal.get("asset_id", "unknown")

        # anomaly first
        anomaly = detect_anomaly(signal)

        # risk logic
        risk = get_risk_level(confidence)

        if anomaly:
            risk = "CRITICAL"

        explanation = generate_explanation(
            confidence,
            vessel_type,
            risk,
            anomaly
        )

        # ✅ FINAL CORRECT OUTPUT
        intelligence = {
            "trace_id": trace_id,
            "vessel_type": vessel_type,
            "confidence": confidence,
            "risk_level": risk,
            "anomaly_flag": anomaly,
            "explanation": explanation
        }

        # optional logging
        emit_bucket_artifact({
            "trace_id": trace_id,
            "type": "intelligence_event",
            "input": signal,
            "output": intelligence
        })

        return intelligence

    except Exception as e:
        return {
            "trace_id": signal.get("trace_id", "TRACE_UNKNOWN"),
            "status": "ERROR",
            "reason": str(e)
        }