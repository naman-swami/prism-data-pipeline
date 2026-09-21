"""
Prism Data Pipeline Quality & Distribution Drift Engine
Audits column null rates, freshness SLAs, and numerical distribution shifts against baseline expectations.
"""
from typing import Dict, Any

class DataQualityPipelineEngine:
    @staticmethod
    def audit_table_quality(
        table_name: str,
        total_rows: int,
        null_count: int,
        latency_mins: int,
        observed_mean: float,
        baseline_mean: float,
        sla_latency_limit: int = 60
    ) -> Dict[str, Any]:
        null_rate_pct = round((null_count / max(1, total_rows)) * 100, 2)

        anomalies = []
        if null_rate_pct > 1.0:
            anomalies.append({"type": "EXCESSIVE_NULL_RATE", "severity": "HIGH", "desc": f"Null rate {null_rate_pct}% exceeds 1.0% tolerance."})

        if latency_mins > sla_latency_limit:
            anomalies.append({"type": "SLA_FRESHNESS_BREACH", "severity": "CRITICAL", "desc": f"Pipeline freshness {latency_mins}m breached {sla_latency_limit}m SLA."})

        drift_pct = 0.0
        if baseline_mean > 0:
            drift_pct = round(abs(observed_mean - baseline_mean) / baseline_mean * 100, 2)
            if drift_pct > 15.0:
                anomalies.append({"type": "DISTRIBUTION_DRIFT", "severity": "MEDIUM", "desc": f"Mean shifted by {drift_pct}% from baseline."})

        healthy = len(anomalies) == 0

        return {
            "table_name": table_name,
            "null_rate_pct": null_rate_pct,
            "pipeline_status": "HEALTHY" if healthy else "DEGRADED",
            "anomalies_count": len(anomalies),
            "anomalies": anomalies
        }
