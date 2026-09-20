import pytest
from src.schema_engine import SchemaDriftEngine

def test_compatible_schema_extension():
    engine = SchemaDriftEngine()
    cur = {"id": "int", "name": "string"}
    inc = {"id": "int", "name": "string", "email": "string"}
    res = engine.evaluate_schema_drift(cur, inc)
    assert res["is_compatible"] is True
    assert res["recommended_action"] == "PROMOTE_MIGRATION"

def test_breaking_type_change():
    engine = SchemaDriftEngine()
    cur = {"id": "int", "amount": "float"}
    inc = {"id": "int", "amount": "string"}
    res = engine.evaluate_schema_drift(cur, inc)
    assert res["is_compatible"] is False
    assert res["recommended_action"] == "BLOCK_PIPELINE_AND_ALERT"

def test_column_null_rate_check():
    engine = SchemaDriftEngine()
    q = engine.audit_column_quality(row_count=1000, null_count=20, null_threshold_pct=0.05)
    assert q["quality_passed"] is True
    assert q["null_rate"] == 0.02
