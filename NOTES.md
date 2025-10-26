Folder Structure:
game_sale_reccommender/
├── backend/                      # Python backend code
│   ├── src/
│   │   └── game_sale_rec_proj/
│   │       ├── __init__.py
│   │       ├── scraping/         # Web scraping modules
│   │       │   ├── scrapers.py   # Website-specific scrapers
│   │       │   └── utils.py      # Scraping helpers
│   │       ├── data/             # Data processing
│   │       │   ├── database.py   # Database operations
│   │       │   └── preprocessing.py
│   │       ├── models/           # ML models
│   │       │   ├── forecasting.py # Time series forecasting
│   │       │   └── training.py   # Model training utilities
│   │       ├── llm/              # LLM integration
│   │       │   ├── query_parser.py
│   │       │   └── response_generator.py
│   │       └── api/              # API endpoints
│   │           ├── routes.py     # API routes
│   │           └── server.py     # API server
│   ├── tests/                    # Backend tests
│   └── pyproject.toml           
├── frontend/                     # React frontend
│   ├── public/                   # Static assets
│   ├── src/
│   │   ├── components/           # React components
│   │   │   ├── Dashboard.js
│   │   │   ├── GameSearch.js
│   │   │   ├── SaleForecast.js   # Forecast visualizations
│   │   │   └── QueryInterface.js # LLM query interface
│   │   ├── services/             # API client services
│   │   ├── styles/               # CSS/styling
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
├── data/                         # Data storage
│   ├── raw/                      # Raw scraped data
│   ├── processed/                # Processed datasets
│   └── models/                   # Saved ML models
├── notebooks/                    # Jupyter notebooks for exploration
│   ├── data_exploration.ipynb
│   └── model_development.ipynb
├── docker-compose.yml            # Docker setup (optional)
└── README.md