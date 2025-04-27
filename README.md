# Privacy Risk Score Dashboard

This project implements an automated privacy risk scoring system designed to surface risk exposure across organizational datasets. It calculates departmental risk scores based on the presence of 
high-risk personal data fields and data retention violations, and generates an executive-level dashboard to support privacy governance and compliance oversight.

## Objectives

- Enable leadership to visualize privacy risk exposure across internal datasets.
- Quantify risk scores based on GDPR-aligned indicators (e.g., sensitive personal data, expired retention periods).
- Provide a simple, scalable reporting mechanism that supports Privacy by Design initiatives.

## Core Features

- Scans structured data sources (CSV files) for high-risk personal identifiers.
- Flags violations of defined data retention policies (default threshold: 5 years).
- Calculates and classifies departmental risk (Low, Moderate, High).
- Generates dynamic HTML dashboards summarizing risk posture across business units.
- Modular design enabling future integration into broader risk and compliance systems.

## Usage

### Install the required dependencies:

```bash
pip install pandas
```

### Execute the scanning and reporting pipeline:

```bash
python scripts/run_dashboard.py
```

### Review the generated dashboard located at:

```bash
reports/privacy_risk_dashboard.html
```

## Potential Extensions

- Integration with real-time data streams and SIEM systems.
- Advanced weighting of risk factors based on business impact assessments.
- Support for regulatory mappings beyond GDPR (e.g., CCPA, CPRA, LGPD).
- Expansion to include automated remediation recommendations.

## License

MIT License © Mehreen Kabir

