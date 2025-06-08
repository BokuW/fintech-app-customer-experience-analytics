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

# --- Google Play Store App IDs ---
# IMPORTANT: You need to find the correct app IDs from the Google Play Store URL for each bank.
# Example: For "Commercial Bank of Ethiopia Mobile Banking", the URL might be:
# https://play.google.com/store/apps/details?id=com.cbe.mobile.banking
# In this case, the app ID is 'com.cbe.mobile.banking'

# Placeholder IDs
APP_IDS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobile.banking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",          # CORRECTED ID
    "Dashen Bank": "com.dashen.dashensuperapp"              # CORRECTED ID
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