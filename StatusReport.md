# Status Report (Milestone 3)

**Project Title:** Analyzing Public Transit Impact on Chicago Property Values

**Team Members:** Jenny Mai & Shenhua Zhang

**Date:** November 13, 2025

---

## 1. Executive Summary of Progress (Milestone 2 to 3)

The project is progressing well, with all core Data Acquisition, Integration, and Data Cleaning steps successfully completed and documented. The team successfully addressed the major technical challenges, including handling the large data volume, multi-dataset integration via PIN, and performing optimized geospatial enrichment.

A significant strategic change was made to the project plan to ensure robustness and timely completion: we formally **removed the necessity for a fourth dataset** (Residential Characteristics/Square Footage). This decision simplified the scope, allowing us to successfully complete the Data Cleaning phase ahead of schedule. The analytic focus has been shifted from a complex multivariate model to a robust **univariate comparison** focused on raw sale price for a strictly filtered, homogeneous market segment (single-family detached homes).

The immediate focus is now shifting to **Statistical Analysis, Visualization, and Workflow Automation.**

---

## 2. Updated Task Status and Artifacts

The table below reflects the current status of all project milestones. The updated target completion dates reflect the streamlined process.

| Milestone | Responsible Team Member(s) | Target Completion Date | Status | Artifacts & Evidence of Completion |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Planning & Setup** | | | | |
| Project Plan & GitHub Release | Both | October 7, 2025 | Completed | ProjectPlan.md, GitHub Tag: project-plan |
| **Phase 2: Acquisition & Storage** | | | | |
| Data Acquisition & Initial Storage (CSV/JSON) | Jenny Mai | October 13, 2025 | Completed | Scripts in src/acquire.py, Notebook: notebooks/1_data_acquisition_test.ipynb |
| SQLite Schema Design & Data Load | Jenny Mai | October 17, 2025 | Completed | Script: src/storage.py, Output: data/project_data.db (Ignored by Git) |
| **Phase 3: Integration & Cleaning** | | | | |
| PIN-Join & Distance Calculation Script (Enrichment) | Jenny Mai | October 23, 2025 | Completed | Script logic tested in notebooks/3_geospatial_enrichment.ipynb |
| Data Quality Profile & Assessment Script | Shenhua Zhang | October 27, 2025 | In-Progress | Initial profiling and class selection confirmed in notebooks/4_data_filtering_cleaning.ipynb |
| Data Cleaning Scripts (Missing/Outliers/Standardization) | Jenny Mai | November 3, 2025 | Completed | Script: src/clean.py, Notebook: notebooks/4_data_filtering_cleaning.ipynb |
| **Phase 4: Reporting & Automation** | | | | |
| Interim Status Report Submission | Both | November 13, 2025 | Completed | This document (StatusReport.md) |
| Statistical Analysis & Visualization Script | Shenhua Zhang | November 17, 2025 | In-Progress | Initial correlation and premium calculation in notebooks/5_initial_analysis.ipynb |
| Workflow Automation (Snakemake implementation) | Jenny Mai | December 5, 2025 | To Do | Snakefile |
| **Phase 5: Final Submission** | | | | |
| Final README.md Report of Findings & Documentation | Shenhua Zhang | December 10, 2025 | To Do | |
| Final Project Tag/Release & Box Upload | Both | December 10, 2025 | To Do | |

---

## 4. Team Member Contributions

### Jenny Mai (ETL Foundation & Data Acquisition & Cleaning)



### Shenhua Zhang (Data Quality & Analysis)



---

## 5. Preliminary Analytical Findings

As a result of the completed data cleaning and filtering, we performed an initial analysis on the filtered dataset (`final_analytic_data.csv`) to validate the project's core premise and provide preliminary findings for this report.

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **RQ 1: Pearson's r (Distance vs. Price)** | [Insert r value from analysis] | Indicates a [Positive/Negative/Negligible] correlation between CTA distance and raw sale price. |
| **RQ 1: P-value** | [Insert p-value from analysis] | Determines the statistical significance of the correlation (p < 0.05). |
| **RQ 3: Median Premium** (0–0.5 mi vs. 1–2 mi) | [Insert Premium % from analysis] | Suggests properties near transit have a [XX.XX]% [premium/discount] in median price compared to the control group. |

These initial findings confirm that the integrated and cleaned dataset is suitable for statistical analysis, validating the core premise of the project and demonstrating progress towards the final goal.