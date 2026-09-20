import json
import argparse
from src.schema_engine import SchemaDriftEngine

def main():
    parser = argparse.ArgumentParser(description="Prism Schema Drift Auditor CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated schema compatibility audit")
    args = parser.parse_args()

    engine = SchemaDriftEngine()
    current = {"user_id": "string", "signup_timestamp": "timestamp", "account_tier": "string"}
    incoming = {"user_id": "string", "signup_timestamp": "string", "account_tier": "string", "geo_region": "string"}

    report = engine.evaluate_schema_drift(current, incoming)
    print("="*60)
    print(" PRISM DATA PIPELINE SCHEMA AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
