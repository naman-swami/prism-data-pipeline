# Data Observability & Quality SLAs

## Key Telemetry Pillars
- **Freshness**: Maximum allowable processing latency before downstream dash degradation.
- **Completeness (Null Rate)**: Primary key columns must satisfy null rate $< 0.1\%$.
- **Distribution Drift**: Significant mean or variance shifts trigger upstream schema validation.
