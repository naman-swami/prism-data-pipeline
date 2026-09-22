# Prism Data Quality & Observability Pipeline

> **Automated Data Contract Validation, Freshness Monitoring, and Drift Detection**  
> Real-Time Table Observability for Enterprise Data Warehouses and Lakehouses.

---

### Data Reliability SLA Dimensions

```
              Ingested Table Partition (Parquet / Iceberg)
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
   [Freshness SLA]          [Schema Contracts]       [Distribution Drift]
   Max Latency < 60 min     Null Rate < 0.5%         Z-Score Drift (|Z| < 3.0)
   Staleness Alert          Type Compatibility        Outlier Alert
```

---

### Pipeline Observability Health Report

Sample health check generated from `fixtures/telemetry/pipeline_run_metrics.json`:

| Table Target | Freshness Status | Null-Rate Check | Anomaly Drift | Pipeline Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **`fct_orders`** | 12m latency (SLA: 60m) | 0.02% (PASS) | $|Z| = 0.42$ | **HEALTHY** |
| **`dim_customers`** | 25m latency (SLA: 120m) | 0.00% (PASS) | $|Z| = 0.18$ | **HEALTHY** |
| **`fct_clickstream`**| 145m latency (BREACH) | 4.80% (FAIL) | $|Z| = 3.91$ | **SLA BREACH ALERT** |

---

### Pipeline CLI Execution

```bash
# Inspect pipeline freshness and table contracts
python pipeline.py --demo

# Run data observability test suite
pytest tests/ -v
```

Data contract definitions, schema specifications, and SLA breach alert protocols are governed by [DATA_SLA_CONTRACTS.md](DATA_SLA_CONTRACTS.md).
