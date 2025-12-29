# Forensic Audit: Unsupervised Anomaly Detection
### Applying Isolation Forests to Financial Integrity

## Project Overview
This project applies an **Isolation Forest** algorithm to detect fraudulent transactions within a dataset of 284,807 credit card transactions. As a Forensic Accountant transitioning into AI, my goal was to move beyond manual auditing into **Automated System Integrity**.

## The Forensic Approach
- **Algorithm:** Isolation Forest (unsupervised).
- **Strategy:** Instead of labeling data, the model isolates anomalies based on their "distance" from normal clusters.
- **Goal:** Identify high-risk "materiality" deviations that standard audits might miss.

## Mechanistic Audit Results
The following chart shows the features that most significantly impacted the model's decision-making process. This provides interpretability showing *why* a transaction was flagged.

![Audit Results](results%20feature_importance.png)

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run the audit: `python fraud_detection.py`
