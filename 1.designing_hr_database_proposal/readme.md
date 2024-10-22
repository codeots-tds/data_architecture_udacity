# Udacity Datawarehouse Project

## Table of Contents:
- [Overview](#overview)
- [Features](#features)
- [Datasets](#Datasets)
- [Project Structure](#ProjectStructure)
- [Project ERD](#ProjectERD)
- [License](#license)

---

## Overview:
This project is part of Udacity's Data Architecture Nanodegree program which focuses on designing a HR database for Tech ABC Corp. The company is growing rapidly and needs a secure, scalable and efficient database solution to manage their employee data. The goal is to move from having their data in spreadsheets to a fully functional, relational database. This database must support user roles, maintaining data integrity and ensure compliance with federal regulations for employee data storage.

## Features:
- Database Modeling: Creation of conceptual, logical, and physical Entity Relationship Diagrams (ERDs) using Lucidchart.
- Data Normalization: Implementation of a database model normalized to the Third Normal Form (3NF).
- Security Implementation: Role-based access controls to restrict sensitive information (e.g., salaries) to authorized users only.
- ETL Pipeline Design: Plan for interfacing the HR database with other systems, such as the payroll system, for future integration.
- Data Retention Compliance: Ensures employee data is stored securely and meets federal requirements for data retention (7 years).

## URL
Project URL: 


Lucidchart:

    Use Lucidchart or any ERD tool of your choice to create and review ERDs. Screenshots of the ERDs for the conceptual, logical, and physical models are included in the ERDs folder.

SQL Execution:

    Use the CRUD_commands.sql file to run Create, Read, Update, and Delete operations for testing the database functionalities.


## Datasets:
The dataset for this project can be found below:
- The data is denormalized.
- The data lists all the employees at ABC Corp along with additional employee info.
https://drive.google.com/file/d/14SgnE_0wNpuPdF5ss94GGqIBfcxLnpIF/view


## Project Structure:
The project contains the files below:

- HR Database Project Proposal.pptx: This is the proposal powerpoint going over the business proposal. In this business proposal we'll have the problem statement for Company ABC, project business & technical requirements, relational database design, data modeling ERD diagrams, and proposed queries.

- readme.md: Provides documentation going over project details.

- sql_queries.py: Provides CRUD commands for this project.

- logical_diagram.png: screenshot of logical diagram.

- physical_diagram.png: screenshot of physical diagram.

- conceptual_diagram.png: screenshot of conceptual diagram.

## Project ERD:
There are three ERD diagrams going over the relationships between different tables and the overall data modeling elements of the project. Here we'll have a conceptual, logical and physical data modeling diagrams.

### Database Schema:

Employee_info:
    - empl_id (PK) VARCHAR,
    - empl_name VARCHAR,
    - empl_email VARCHAR,
    - address VARCHAR,
    - city VARCHAR,
    - state VARCHAR

Company_emp_info:
    - job_title VARCHAR,
    - department VARCHAR,
    - manager VARCHAR,
    - state_date date,
    - end_date date,
    - empl_id empl_id VARCHAR,
    - salary int,
    - hire_date date,
    - end_date date,
    - location VARCHAR

Employee_education:
    - education_level VARCHAR,
    - empl_id VARCHAR

### License

This project is intended for educational purposes as part of the Database Architecture Foundations chapter.
