# Explainability — prism-data-pipeline

## Decision Reasoning
Prism detects pipeline risks by performing abstract schema delta diffs, calculating downstream blast radius across lineage DAGs, and categorizing changes into breaking versus non-breaking evolutions.

## Data Sources and Inputs Used
Information schema metadata, open-lineage JSON events, dbt manifest graphs, and data lake statistics.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, prism-data-pipeline assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, prism-data-pipeline will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, prism-data-pipeline explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
prism-data-pipeline actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- In-flight Data Mutations: Cannot inspect uncommitted database transactions prior to WAL replication.
- Streaming Latency: Real-time Kafka stream auditing is bounded by consumer micro-batch sampling windows.
- Hardware Storage: Does not manage underlying NVMe hardware clustering or block device partitioning.
- Semantic Inferences: Cannot determine whether changing 'US' to 'USA' was intentional business logic without explicit data contract rules.

## Uncertainty Quantification Approach
When statistical distributions change due to authentic business seasonal events (e.g., Black Friday volume spikes), Prism flags distribution shift uncertainty, compares against year-over-year baselines, and requests human data engineer confirmation.
