# Prism Data Pipeline Observability & Quality Auditor

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![DataEng](https://img.shields.io/badge/Domain-Data_Observability_ETL-blue.svg)](docs/data_observability_framework.md)
[![Standard](https://img.shields.io/badge/Standard-Great_Expectations_SLA-teal.svg)](docs/data_observability_framework.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An enterprise data observability and ETL pipeline health auditing engine monitoring null rates, batch freshness SLAs, and schema distribution drifts.

```
                    ┌─────────────────────────┐
                    │ ETL Batch Run Telemetry │
                    │ (Rows, Nulls, Latency)  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ quality/schema_contract │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Null Rate Invariant│         │  Freshness SLA      │
      │  (< 1.0% Threshold) │         │   (Within 60 Mins)  │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Pipeline Health Status  │
                    │ (HEALTHY / DEGRADED)    │
                    └─────────────────────────┘
```

## Features

- **Schema Invariant Checking**: Evaluates null rate tolerances across streaming and batch runs.
- **Pipeline SLA Telemetry**: Enforces upstream latency thresholds on core data warehouse dimensions.
- **Batch Telemetry Benchmarks**: Includes production ETL batch run metrics.

## Directory Structure

```
prism-data-pipeline/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint data engineering provenance
├── quality/
│   └── schema_contract_validator.py # Quality and distribution drift engine
├── fixtures/
│   └── telemetry/
│       └── pipeline_run_metrics.json # Benchmark pipeline logs
├── docs/
│   └── data_observability_framework.md # Observability principles
├── tests/
│   └── test_agent.py                # Pipeline quality test suite
├── pipeline.py                          # Data engineering CLI
└── requirements.txt
```

## Quick Start

```bash
# Run pipeline quality tests
pytest tests/ -v

# Audit sample batch run telemetry
python pipeline.py --demo
```
