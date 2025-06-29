# src/config.py

import os

# --- Project Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Ensure directories exist
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# Placeholder IDs
APP_IDS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",          
    "Dashen Bank": "com.dashen.dashensuperapp"              
}

# Minimum number of reviews to target per app
MIN_REVIEWS_PER_APP = 400

# --- Output File Names ---
RAW_REVIEWS_CSV = os.path.join(RAW_DATA_DIR, 'raw_play_store_reviews.csv')
CLEAN_REVIEWS_CSV = os.path.join(PROCESSED_DATA_DIR, 'clean_play_store_reviews.csv')

print(f"Project structure setup complete and config.py created/updated.")
print(f"Base Directory: {BASE_DIR}")
print(f"Raw Data Directory: {RAW_DATA_DIR}")
print(f"Processed Data Directory: {PROCESSED_DATA_DIR}")
print(f"App IDs to scrape: {APP_IDS}")