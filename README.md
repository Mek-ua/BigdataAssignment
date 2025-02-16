# Student Name: [Mekides Marie]
# Class: [Adgrat ]
# Department: [Software Engineering ]
# Course: Fundamentals of Big Data Analytics and BI
# University: Debre Berhan University
End-to-End Data Pipeline for E-Commerce Dataset
Project Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for an e-commerce dataset. The pipeline extracts data from a CSV file, cleans and transforms it, loads it into a PostgreSQL database, and generates basic visualizations in Python. Additionally, a Power BI dashboard is created for interactive analysis.

Tech Stack
Python: Used for data extraction, transformation, and loading.
Pandas: For data manipulation and cleaning.
PostgreSQL: For storing the processed data.
Matplotlib & Seaborn: For basic visualizations in Python.
Power BI: For creating an interactive dashboard with insights.
Project Structure
Files and Their Purpose
1. /data
ecommerce_data.csv: The raw e-commerce dataset with information such as zip code, latitude, longitude, city, and state.
ecommerce_raw.csv: The extracted data after the raw CSV is loaded into the system.
ecommerce_cleaned.csv: The cleaned data after applying the necessary transformations.
2. /database: Contains the SQL schema definition file for the PostgreSQL database.
- **`schema.sql`**: Defines the structure of the `ecommerce_db` database and the `ecommerce_data` table.
3. /scripts
extract.py: Script responsible for extracting the data from the raw CSV file.
transform.py: Script that performs data cleaning, such as removing missing values, handling duplicates, and converting data types.
load.py: Script that loads the cleaned data into a PostgreSQL database.
visualization.py: Script for generating basic plots to visualize geographical data and city distribution.
4. /visualization
PowerBI_Dashboard.pbix: Power BI file containing the interactive dashboard that connects to the PostgreSQL database and visualizes key metrics and insights.
5. /documents
README.md: This documentation file that explains the project, its structure, setup instructions, and how to run the ETL pipeline.
5. requirements.txt
List of required Python libraries:

Screenshots
Screenshot 1: Data Pipeline Execution
Data Pipeline Execution

Screenshot 2: Power BI Dashboard
Power BI Dashboard

Screenshot 3: Bar Chart Visualization
Bar Chart Visualization

Screenshot 4: Visual Overview
Visual Overview

Screenshot 5: Script Overview
Script Overview Script Overview
