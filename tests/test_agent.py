import os
import pytest
from quality.schema_contract_validator import DataQualityPipelineEngine

def test_pipeline_healthy():
    res = DataQualityPipelineEngine.audit_table_quality(
        table_name="test_table", total_rows=10000, null_count=10, latency_mins=30, observed_mean=50.0, baseline_mean=50.0
    )
    assert res["pipeline_status"] == "HEALTHY"
    assert res["anomalies_count"] == 0

def test_sla_breach_degraded():
    res = DataQualityPipelineEngine.audit_table_quality(
        table_name="test_table", total_rows=10000, null_count=10, latency_mins=120, observed_mean=50.0, baseline_mean=50.0
    )
    assert res["pipeline_status"] == "DEGRADED"
    types = [a["type"] for a in res["anomalies"]]
    assert "SLA_FRESHNESS_BREACH" in types
