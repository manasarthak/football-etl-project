# Football ETL Project

## Overview
This project implements an ETL (Extract, Transform, Load) process for football data. It scrapes data, stores it in a local SQLite database, and uploads processed data as Parquet files to Azure Blob Storage.


## Features
- **Data Scraping**: Retrieves football statistics using predefined functions utilizing BeautifulSoup.
- **SQLite Storage**: Stores scraped data locally in an SQLite database.
- **Parquet Files**: Converts data into efficient Parquet format for storage and uploads it to Azure Blob Storage for easy access and sharing.
- **Automation**: Uses GitHub Actions to run the ETL process automatically every Monday.(matches are typically played once a week on weekends)

