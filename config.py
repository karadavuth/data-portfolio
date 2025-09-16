"""
Configuratie bestand voor het Energie Data Pipeline project
Bevat alle URLs, API keys en instellingen
"""

# CBS Open Data API endpoints
CBS_BASE_URL = "https://opendata.cbs.nl/ODataApi/odata/83140NED"
CBS_ENERGY_PRICES_URL = f"{CBS_BASE_URL}/TypedDataSet"

# Data storage paths
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
DATABASE_PATH = "data/energie_database.db"

# Data collection settings
BATCH_SIZE = 1000
MAX_RETRIES = 3
DELAY_BETWEEN_REQUESTS = 1  # seconden

print("✅ Config geladen - Ready voor data collection!")