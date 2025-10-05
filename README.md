# Project Plan: Analyzing Public Transit Impact on Chicago Property Values

---

## 1. Overview

The overall goal of this project is to quantitatively assess the influence of the Chicago Transit Authority (CTA) rail system on residential property values within the city of Chicago. We will employ data curation and data lifecycle techniques to acquire, integrate, clean, and analyze two distinct public datasets.

The end product will be a robust, reproducible workflow and a final report detailing the statistical correlation found between proximity to CTA rail stations (L-stops) and recent residential sale prices. This project is motivated by providing data-driven insights to urban planners and real estate investors regarding transit-oriented development (TOD).

---

## 2. Research Question(s)

This project seeks to answer the following research questions:

* Is there a statistically significant correlation between the Euclidean distance of a residential property from the nearest active CTA rail station and its adjusted sale price per square foot?
* How does the transit line color (e.g., Red Line vs. Brown Line) influence the magnitude of this correlation?
* Based on the integrated analysis, what is the calculated premium (or discount) in sale price for properties located within 0.5 miles of an L-stop, compared to those located further away?

---

## 3. Team

| Team Member | Role/Focus Area | Specific Responsibilities (Evidence in Git) |
| :--- | :--- | :--- |
| **Jenny Mai** | ETL Foundation & Data Acquisition | Set up GitHub repository and file structure. Programmatically acquire both datasets. Design and implement the SQL database schema. Develop the initial geocoding and distance calculation script (Extraction/Enrichment). Develop the final workflow for automation (Snakemake implementation). |
| **Shenhua Zhang** | Data Quality, Cleaning & Analysis | Conduct initial data profiling and quality assessment. Develop cleaning scripts (Python/Pandas) for missing values, outliers, and data type standardization. Perform data integration (Python/SQL joins). Execute statistical analysis and generate final visualizations for the report. Develop the Final README.md Report & Documentation. |


---

## 4. Datasets

We will use two complementary datasets, focusing on the Chicago metropolitan area, ensuring distinct formats and acquisition methods.

### Dataset 1: Chicago Residential Property Sales (The Core Dataset)

* **Source/Access Method:** Chicago Data Portal (via Socrata API endpoint).
* **Format/Schema:** Semi-structured JSON or flat CSV data, retrieved using Python's `requests` library and loaded into a database.
* **Description:** Contains historical residential property sale transactions, including property addresses, sale price, sale date, and key structural details (like square footage).
    * **Key Data Points:** Raw address (for geocoding) and sale price (dependent variable).
    * **Anticipated Quality Issues:** High levels of missing data (e.g., square footage, address components) and outliers in price. We will filter for sales within the last five years.

### Dataset 2: CTA Rail Stations (The Supplemental Dataset)

* **Source/Access Method:** CTA (Chicago Transit Authority) Open Data or the City of Chicago GIS data catalog.
* **Format/Schema:** GeoJSON file or CSV with pre-calculated geospatial coordinates (Latitude/Longitude). This contrasts with Dataset 1's need for API retrieval and addresses.
* **Description:** Contains the precise geographic location (Lat/Lon) and associated metadata (Stop ID, Line Color) for every active "L" train station. This serves as the critical reference point for the proximity calculation.

### Integration Strategy (Geospatial Enrichment)
The primary integration strategy involves geospatial enrichment and a final relational join.

1.  **Enrichment:** Use a Python geocoding module to convert street addresses from Dataset 1 into latitude and longitude coordinates.
2.  **Calculation:** Calculate the Euclidean distance (in meters or miles) between the coordinates of each property (Dataset 1) and the nearest CTA rail stop (Dataset 2).
3.  **Integration:** The calculated minimum distance and the line color of the nearest station will be added as new columns (enriched features) to the primary property sales table, which will be the basis for analysis.

---

## 5. Timeline

| Milestone | Responsible Team Member(s) | Target Completion Date | Status |
| :--- | :--- | :--- | :--- |
| **Phase 1: Planning & Setup** | | | |
| Project Plan & GitHub Release | Both | October 7, 2025 | Completed |
| **Phase 2: Acquisition & Storage** | | | |
| Dataset 1 & 2 Acquisition Scripts | Jenny Mai | October 13, 2025 | To Do |
| SQLite Schema Design & Data Load | Jenny Mai | October 17, 2025 | To Do |
| **Phase 3: Integration & Cleaning** | | | |
| Geocoding & Distance Calculation Script (Enrichment) | Jenny Mai | October 23, 2025 | To Do |
| Data Quality Profile & Assessment Script | Shenhua Zhang | October 27, 2025 | To Do |
| Data Cleaning Scripts (Missing/Outliers/Standardization) | Shenhua Zhang | November 3, 2025 | To Do |
| **Phase 4: Reporting & Automation** | | | |
| Interim Status Report Submission | Both | [Canvas Deadline] | To Do |
| Statistical Analysis & Visualization Script | Shenhua Zhang | November 17, 2025 | To Do |
| Workflow Automation (Snakemake implementation) | Jenny Mai | December 5, 2025 | To Do |
| **Phase 5: Final Submission** | | | |
| Final README.md Report & Documentation | Shenhua Zhang | December 10, 2025 | To Do |
| Final Project Tag/Release & Box Upload | Both | [Canvas Deadline] | To Do |

---

## 6. Constraints

* **API Rate Limits:** The Socrata API for property sales or the Google Geocoding API (if used) may impose rate limits, requiring us to implement exponential backoff and potentially split the data acquisition process into batches.
* **Geospatial Accuracy:** The geocoding process may not yield perfect latitude/longitude for every address, leading to a small percentage of discarded or less accurate records.
* **Data Volume:** Chicago property data is large, requiring efficient Python/Pandas operations to manage processing time and memory.

---

## 7. Gaps

* **Distance Calculation Optimization:** We need to confirm the most efficient and robust Python library for calculating the distance between thousands of property points and hundreds of transit stops.
* **Price Normalization Variable:** We need to research the best proxy variable for normalizing price (e.g., using "Price per Square Foot" vs. running a multivariate regression including features like bedrooms and age). We will likely start with Price per Square Foot.
* **Temporal Trends:** Our current plan focuses on distance, but we should anticipate whether we need to account for inflation or market changes by adjusting prices based on the sale date.