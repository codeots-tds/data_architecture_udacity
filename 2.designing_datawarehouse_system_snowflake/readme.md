# Design a Data Warehouse for Reporting and OLAP

## Table of Contents:
- [Overview](#overview)
- [Features](#features)
- [Datasets](#Datasets)
- [Project Structure](#ProjectStructure)
- [Database Schema](#DatabaseSchema)
- [Project ERD](#ProjectERD)
- [License](#license)

---

## Overview:
This project is part of the Data Architecture Nanodegree under the "Designing Data Systems" chapter. The objective is to design and implement a data warehouse using Snowflake to enable reporting and Online Analytical Processing (OLAP) on a combination of datasets, including Yelp reviews, COVID-19 data, and climate data. The goal is to analyze how weather conditions impact Yelp reviews, leveraging the data warehouse architecture and OLAP capabilities.

## Features:
- Data Warehouse Design: Design and implement a Snowflake-based data warehouse optimized for reporting and OLAP operations.

- ETL Pipeline: Develop an ETL (Extract, Transform, Load) pipeline that moves data through three stages: Staging, Operational Data Store (ODS), and Data Warehouse (DWH).

- Data Integration: Integrate multiple data sources, including Yelp reviews, climate information, and COVID-19 datasets, to facilitate complex queries and analysis.

- Data Modeling: Create Entity-Relationship Diagrams (ERDs) and a Star Schema to visualize and model the data flow through the system.

- SnowSQL Implementation: Use SnowSQL commands to load, transform, and migrate data between stages of the data warehouse.

- Reporting: Generate reports showing the relationship between weather data (temperature and precipitation) and Yelp review ratings for businesses.

## Setup
    1. Create a Snowflake account.
    2. Login to Snowflake dashboard.
    3. Download the datasets:
    4. Load data into Snowflake.


## Datasets:
1. Yelp Dataset:
    - contains business information, reviews, check-ins, tips, and customer details related to Yelp's services.
    - datafiles: business.json, reviews.json, check-ins.json, tip.json, customer.json, and yelp_academic_dataset_covid_features.json.

2. COVID-19 Dataset:
    - Provides additional information and context to businesses that were impacted by Covid-19 through user-reviews.
    - datafiles: yelp_academic_dataset_covid_features.json

3. Climate Data:
    - Historical weather data for Las Vegas, Nevada.
    - Files: Las_Vegas_Precipitation.csv, Temperature.csv

## Project Structure:
The project contains the files below:

- verify_pyspark.py: This is a great way to check if pypspark is configured properly to run on your machine.

- main.py: Since Snowflake web UI only allows for files under 125mb, I used Pyspark to break these data files into smaller chunks to upload properly for each dataset that exceeds past 125mb.

- Project_Design_a_datawarehouse_reporting_olap.pptx: This presentation file covers the business prompt, data modeling diagrams(conceptual, logical, ER model, dimensional, star schema), screenshots of ods schema for yelp/temperature data, screenshot of table row counts for each table, sql queries to load raw data files into staging tables as well as loading data from staging tables into ODS data tables, sql queries to create aggergate data tables between yelp data and climate data to get the overall picture of how weather impacts restaurant reviews.

### Database Schema:

Yelp _User_Table:
    - user_id (PK) INT,
    - name VARCHAR,
    - review_count INT,
    - yelping_since date,
    - elite bool,
    - friends VARCHAR

Yelp_checkin:
    - checkin_id INT,
    - business_id INT,
    - user VARCHAR,
    - review_id INT,
    - date date,

Yelp_business:
    - business_id INT,
    - name VARCHAR,
    - address VARCHAR
    - postal_code INT
    - latitude FLOAT
    - longitude FLOAT
    - is_open bool
    - attributes VARCHAR
    - categories VARCHAR
    - hours VARCHAR

Yelp_Reviews:
    - review_id INT(pk),
    - user_id INT,
    - tip_id INT,
    - stars VARCHAR

Weather:
    - date date (pk),
    - review_id INT

Temperature:
    - temp_id INT (pk),
    - date date,
    - min INT,
    - max INT,
    - normal_min INT,
    - normal_max INT

Precipitation:
    - precip_id INT (pk),
    - date date,
    - precipitation VARCHAR,
    - precipitation_normal VARCHAR

Tip_Table:
    - tip_id INT (PK),
    - user_id INT,
    - business_id INT,
    - text VARCHAR,
    - date date,
    - compliment_count INT

### License

This project is intended for educational purposes as part of the Database Architecture Foundations chapter.