import argparse
import json
import os
from quality.schema_contract_validator import DataQualityPipelineEngine

def main():
    parser = argparse.ArgumentParser(description="Prism Data Pipeline CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample ETL batch run telemetry")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "telemetry", "pipeline_run_metrics.json")

    if args.demo:
        with open(data_file, "r") as f:
            runs = json.load(f)
        print("=== PRISM DATA PIPELINE OBSERVABILITY AUDIT ===\n")
        for r in runs:
            res = DataQualityPipelineEngine.audit_table_quality(
                table_name=r["table_name"],
                total_rows=r["rows_ingested"],
                null_count=r["null_count_customer_id"],
                latency_mins=r["freshness_latency_minutes"],
                observed_mean=r["mean_order_value"],
                baseline_mean=r["baseline_mean"]
            )
            print(f"Table: {r['table_name']} ({r['rows_ingested']:,} rows)")
            print(f"  Null Rate: {res['null_rate_pct']}% | Pipeline Status: {res['pipeline_status']}")
            for a in res["anomalies"]:
                print(f"    * [{a['severity']}] {a['type']}: {a['desc']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
