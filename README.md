<div align="center">

# AuraCart Analytics Pro

**A modular Python desktop platform for e-commerce scraping, analytics, and automation.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-purple?style=flat-square)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

AuraCart Analytics Pro is a desktop application that scrapes product data from e-commerce sites, stores it in a structured database, surfaces analytics on pricing and availability, and lets you export or schedule everything — all from a modern dark-mode GUI.

Built with a modular architecture, it's designed to scale toward cloud deployment, API integration, or multi-user SaaS conversion without major rewrites.

---

## Features

### Scraping
Three engines to match the site — fast requests-based scraping for static pages, async scraping for throughput, and Playwright for JavaScript-rendered content.

### Analytics dashboard
Tracks total products, sessions, average price, average rating, and availability breakdown. Trend charts update as new data comes in.

### Data management
Structured storage with session tracking. The database layer is built on SQLAlchemy — swap in PostgreSQL when you're ready to scale.

### Export
Push any dataset to CSV, Excel, or JSON in one click.

### Scheduler
Configure scraping intervals and let jobs run in the background. No manual re-triggering needed.

### GUI
Built with CustomTkinter. Dark-mode SaaS aesthetic, sidebar navigation, real-time logs, and a progress indicator for active scraping jobs.

---

## Project structure

```
AuraCartAnalyticsPro/
│
├── main.py
├── requirements.txt
│
├── app/
│   ├── gui/              # Desktop UI (CustomTkinter)
│   ├── scraping/         # Scraping engines
│   ├── database/         # ORM + repository layer
│   ├── analytics/        # Charts + statistics
│   ├── exports/          # Export modules
│   └── scheduler/        # Automation system
│
├── data/                 # Local data storage
├── exports/              # Exported files
├── logs/                 # System logs
└── assets/               # UI assets
```

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/AuraCartAnalyticsPro.git
cd AuraCartAnalyticsPro
```

**2. Create a virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Install Playwright browsers**

```bash
playwright install
```

**5. Run the application**

```bash
python main.py
```

---

## How it works

1. Paste a product URL into the GUI
2. The scraper fetches product name, price, rating, and availability
3. Data lands in the local database
4. The analytics engine processes and visualizes insights in the dashboard
5. Export any slice of the data whenever you need it

---

## Tech stack

| Layer | Library |
|---|---|
| GUI | CustomTkinter |
| Scraping | Requests, Asyncio, Playwright |
| Data processing | Pandas |
| Visualization | Matplotlib |
| Database | SQLAlchemy (PostgreSQL-ready) |
| Runtime | Python 3.10+ |

---

## Use cases

- Price tracking across multiple e-commerce sites
- Competitor product analysis
- Market trend monitoring
- Product availability tracking
- Research data collection

---

## Roadmap

- [ ] Web dashboard (Flask / FastAPI)
- [ ] Multi-user SaaS system
- [ ] Cloud scraping workers
- [ ] Proxy rotation
- [ ] Real-time WebSocket analytics
- [ ] Docker deployment

---

## Disclaimer

This tool is intended for educational use, personal research, and ethical data collection. You are responsible for complying with the terms of service of any website you scrape.

---

## Author

Built as a full-stack Python architecture project covering modular system design, GUI engineering, web scraping pipelines, and data analytics workflows.

---

<div align="center">

If this project is useful to you, a ⭐ on GitHub goes a long way.

</div>
