# Data Warehouse
The goal of this project is to create dataware house for signal data collected over long period of time. It can be used by data analyists to generate insights from the data.

# Table of content
- [Introduction](#introduction)
- [Installation](#installation)
- [Folders](#folders)
  - `dags` : 
  - `scripts` :
  - `warehouse-dbt` : 

## Introduction
You and your colleagues have joined to create an AI startup that deploys sensors to businesses, collects data from all activities in a business - from people’s interaction to the smart appliances installed in the company to reading environmental and other relevant information. Your startup is responsible to install all the required sensors, receive a stream of data from all sensors, and analyse the data to provide key insights to the business. The objective of your contract with the client is to reduce the cost of running the client facility as well as to increase the livability and productivity of workers.

In this challenge you are tasked to create a scalable data warehouse tech-stack that will help you provide the AI service to the client. 

## Installation
Before Installing any package make sure to create a virtual enviroment. Prefereble python version 3.7. if you are using older versions of mac, you may incounter error downthe road. so, try to download older version of packages that are showing errors. in my case - [psycopg2](https://pypi.org/project/psycopg2-binary/2.8/) was causing the issue. And Install it after installing `DBT`.

- [DBT](https://docs.getdbt.com/dbt-cli/installation/#pip) : package used for Data Transformation
- [Airflow](https://www.youtube.com/watch?v=lKL7DMIfMyc&t=121s) : youtube video and blog with nice and easly to follow installation.

## Folders
- `dags` : folder containing dag files which are requred to run by airflow
- `my_scripts` : python modules use full for the exicution of commands
- `warehouse-dbt` : dbt files



