# Fintech App Customer Experience Analytics
 # Project Overview
- This project aims to analyze customer satisfaction with mobile banking applications by collecting and processing user reviews from the Google Play Store for three Ethiopian banks:
-  Commercial Bank of Ethiopia (CBE), ank of Abyssinia (BOA), and Dashen Bank.
- As a Data Analyst at Omega Consultancy, the goal is to scrape reviews, analyze sentiment and themes, identify satisfaction drivers and pain points, store cleaned data, and deliver actionable recommendations.

 # Data Collection and Preprocessing
- Objective: Scrape user reviews from the Google Play Store, preprocess them for analysis, and ensure proper Git management.

  *Deliverables:*

- 1,200+ collected reviews (400+ per bank) with <5% missing data.

- A clean CSV dataset (clean_play_store_reviews.csv).

- An organized Git repository with clear, frequent commits on the task-1 branch.

- Updated README.md (this file) with methodology.

# 1. Setup and Environment
- Follow these steps to set up your local development environment.

# Clone the Repository
- First, clone this GitHub repository to your local machine:

git clone https://github.com/BokuW/fintech-app-customer-experience-analytics.git
cd fintech-app-customer-experience-analytics

# Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

-  Create the virtual environment
 python -m venv .venv

- Activate the virtual environment (Windows)
 .venv\Scripts\activate

#  Install Dependencies
- Install all required Python packages using pip. 

  pip install -r requirements.txt

# 1.4. Project Structure

- ├── data/
- │   └── raw/      # Stores raw scraped data
- │   └── processed/ # Stores cleaned and preprocessed data
- ├── notebooks/    # Contains Jupyter notebooks for analysis
- │   └── 01_data_collection_preprocessing.ipynb
- ├── src/          # Contains Python modules, e.g., config.py
- │   └── config.py
- ├── .gitignore    # Specifies files/folders to be ignored by Git
- ├── requirements.txt # Lists project dependencies
- └── README.md     # This file

# 1.5. Configure App IDs
- Before running the scraping script, you must update the APP_IDS in the src/config.py file with the correct and verified Google Play Store IDs for each bank's mobile application.

- Open src/config.py.

- Locate the APP_IDS dictionary.

- APP_IDS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

# 2.  Data Collection
T- his task involves scraping reviews and performing initial preprocessing.
- Run all cells in the notebook.

#  Expected Output

- Print progress messages for scraping each bank's reviews.

- Show a summary of raw reviews collected.

- Perform preprocessing steps (duplicate removal, handling missing data, date normalization).

- Print a preprocessing summary, including total clean reviews and missing data percentage.

- Save the raw_play_store_reviews.csv to data/raw/.

- Save the final clean_play_store_reviews.csv to data/processed/.
