# 🔌 Nederlandse Energiedata Pipeline

## Projectomschrijving
Een data pipeline die Nederlandse energieprijzen verzamelt via de CBS Open Data API, 
verwerkt met pandas en opslaat in een SQLite database.

## 🎯 Doel
Dit project demonstreert:
- Data collection van Nederlandse overheidsdata
- Python data processing met pandas
- SQL database operaties
- Clean code practices voor ilionx portfolio

## 🛠️ Technische Stack
- **Python 3.11+**
- **uv** (package manager)
- **pandas** (data processing)
- **requests** (API calls)
- **sqlite3** (database)
- **matplotlib/seaborn** (visualisatie)

## 🚀 Setup & Installation

```bash
# Clone project
cd your-projects-folder
mkdir 01-energie-data-pipeline
cd 01-energie-data-pipeline

# Installeer dependencies
uv init
uv add pandas requests matplotlib seaborn sqlite3 python-dotenv

# Run data collector
python data_collector.py