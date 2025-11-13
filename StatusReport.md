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
| Statistical Analysis & Visualization Script | Shenhua Zhang | November 17, 2025 | In-Progress | Initial correlation and premium calculation in notebooks/5_exploring_analysis.ipynb |
| Workflow Automation (Snakemake implementation) | Jenny Mai | December 5, 2025 | To Do | Snakefile |
| **Phase 5: Final Submission** | | | | |
| Final README.md Report of Findings & Documentation | Shenhua Zhang | December 10, 2025 | To Do | |
| Final Project Tag/Release & Box Upload | Both | December 10, 2025 | To Do | |

---

## 4. Team Member Contributions

### Jenny Mai (ETL Foundation & Data Acquisition & Cleaning)



### Shenhua Zhang (Data Quality & Analysis)
In the Milestone 3, I am responsible for the statistical analysis between Cook County Property Sales and CTA Railway. Given the 3 research questions, I analyzed them with appropriate statistical analytical methods respectively. For the first question, I used `.corr()` to identify the correlation between CTA distance and sale price, which turned out to be a weak negative correlation. From the data, we can conclude that these two variables have weak relationship. In the second questions, I first processed all `nearest_cta_lines` (which are messy data, hard to identify lines in plain words) into some new columns. Each column represents if the current bus stop is the current color of line with boolean (e.g. if the bus stop is blue and purple, then `contains_blue` and `contains_red` will be True, other columns will be False). I also counted the number of lines for bus stops that are crossed with many lines. Eventually, all lines have different degree of weak slight positive correlation with sale price (less than 0.1); line number also has a very weak positive correlation with sale price. In the plot, we can hardly see any significant relationship. Last but not least, the third question investigates the if property class and CTA distance will together make an influence to the sale price. Checking the original source, I discovered the representation of "2-02" to "2-09" (as indicated in the code) of the property class. They represent different types of houses varied by built year and size of space. Since this contains 2 features, I first drew the heatmap of their correlations, and correlation of -0.23 will not likely to cause multicollinearity issue. I run the regression model for "sale_price ~ min_distance_meters * Q('class')". In the end, it shows there is a moderate influence of the interaction term on sale price. 


---

## 5. Preliminary Analytical Findings

As a result of the completed data cleaning and filtering, we performed an initial analysis on the filtered dataset (`final_analytic_data.csv`) to validate the project's core premise and provide preliminary findings for this report.

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **RQ 1: Correlation (Distance vs. Sale Price)** | -0.231542 | Indicates a weak negative correlation between CTA distance and sale price. |
| **RQ 2: Correlation (CTA Line Number vs. Sale Price)** | 0.106675 | Indicates a positive weak correlation between different types of lines and sale price. |
| **RQ 3: R^2** | 0.392 | Suggests a moderate influences of property class & CTA distance to sale price.  |

These initial findings confirm that the integrated and cleaned dataset is suitable for statistical analysis, validating the core premise of the project and demonstrating progress towards the final goal.
