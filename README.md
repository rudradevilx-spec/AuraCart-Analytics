📊 AuraCart Analytics Pro

A modern, modular e-commerce scraping, analytics, and automation platform built with Python and CustomTkinter.

🚀 Overview

AuraCart Analytics Pro is a desktop-based SaaS-style application designed to:

Scrape product data from e-commerce websites
Store and manage structured product datasets
Perform analytics on pricing, ratings, availability, and trends
Export data in multiple formats
Automate scraping through a built-in scheduler

It is built with a modular architecture, making it scalable for future upgrades like cloud deployment, API integration, or multi-user SaaS conversion.

✨ Key Features
🕷️ Multi-Engine Scraping System
Requests-based fast scraping
Async scraping for performance
Playwright support for dynamic websites
📊 Analytics Dashboard
Total products tracked
Session tracking
Average price & rating analysis
Availability breakdown
Trend visualization charts
📦 Data Management
Structured product storage
Session tracking system
PostgreSQL-ready architecture (optional upgrade)
📤 Export System
CSV export
Excel export
JSON export
⏱️ Scheduler System
Automated scraping at custom intervals
Background execution support
🖥️ Modern GUI
Built with CustomTkinter
Dark mode SaaS-style UI
Sidebar navigation system
Real-time logs & progress tracking
🏗️ Project Architecture
AuraCartAnalyticsPro/
│
├── main.py
├── requirements.txt
│
├── app/
│   ├── gui/              # Desktop UI (CustomTkinter)
│   ├── scraping/        # Scraping engines
│   ├── database/        # ORM + repository layer
│   ├── analytics/       # Charts + statistics
│   ├── exports/         # Export modules
│   ├── scheduler/       # Automation system
│
├── data/                # Local data storage
├── exports/             # Exported files
├── logs/                # System logs
└── assets/              # UI assets
⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AuraCartAnalyticsPro.git
cd AuraCartAnalyticsPro
2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Install Playwright browsers
playwright install
5. Run the application
python main.py
🧠 How It Works
User enters a product URL in the GUI
Scraper engine fetches and parses product data:
Product name
Price
Rating
Availability
Data is stored in structured database
Analytics engine processes insights
Results are visualized in dashboard
Export system allows data download
📈 Example Use Cases
Price tracking across e-commerce sites
Competitor product analysis
Market trend monitoring
Product availability tracking
Data collection for research projects
🛠️ Tech Stack
Frontend: CustomTkinter
Backend: Python 3.10+
Scraping: Requests, Asyncio, Playwright
Data Processing: Pandas
Visualization: Matplotlib
Database: SQLAlchemy (PostgreSQL-ready)
📌 Future Improvements
Web dashboard version (Flask / FastAPI)
Multi-user SaaS system
Cloud scraping workers
Proxy rotation system
Real-time WebSocket analytics
Docker deployment
⚠️ Disclaimer

This tool is intended for:

Educational purposes
Research and analysis
Ethical data collection

Users are responsible for complying with website terms of service.

👨‍💻 Author

Built as a full-stack Python architecture project demonstrating:

Modular system design
GUI application engineering
Web scraping pipelines
Data analytics workflows
⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!