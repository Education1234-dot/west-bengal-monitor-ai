# West Bengal Monitor AI 🚀

A comprehensive AI-powered monitoring system for West Bengal with real-time data analytics, geospatial visualization, and predictive insights.

## Features

✅ **Interactive GeoJSON Mapping** - State boundary, districts, and cities  
✅ **Real-time Data Monitoring** - Weather, pollution, population, infrastructure  
✅ **AI Predictions** - Trend analysis and forecasting  
✅ **Web Dashboard** - Beautiful UI for data visualization  
✅ **REST API** - Backend services for data retrieval  
✅ **Database Integration** - PostgreSQL for data storage  
✅ **Machine Learning** - Anomaly detection and classification  

## Project Structure

```
west-bengal-monitor-ai/
├── backend/                 # Flask API & AI models
│   ├── app.py              # Main Flask application
│   ├── requirements.txt     # Python dependencies
│   ├── config.py           # Configuration settings
│   ├── models/             # AI/ML models
│   │   ├── predictor.py    # Prediction models
│   │   └── analyzer.py     # Data analysis
│   ├── routes/             # API endpoints
│   │   ├── geo.py          # Geospatial endpoints
│   │   ├── monitoring.py   # Monitoring data endpoints
│   │   └── predictions.py  # Prediction endpoints
│   └── data/               # Data storage
│
├── frontend/               # React Dashboard
│   ├── public/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Pages
│   │   └── App.js
│   ├── package.json
│   └── README.md
│
├── data/                   # GeoJSON and datasets
│   ├── geojson/
│   │   ├── west_bengal.geojson
│   │   ├── districts.geojson
│   │   └── cities.geojson
│   └── datasets/
│
├── notebooks/              # Jupyter notebooks for analysis
│   ├── eda.ipynb           # Exploratory Data Analysis
│   └── model_training.ipynb
│
├── docker-compose.yml      # Docker configuration
├── .env.example            # Environment variables template
└── docs/                   # Documentation

```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+
- Docker (optional)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Education1234-dot/west-bengal-monitor-ai.git
   cd west-bengal-monitor-ai/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run Flask server**
   ```bash
   python app.py
   ```
   Server runs at `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start React app**
   ```bash
   npm start
   ```
   App runs at `http://localhost:3000`

### Docker Setup (Optional)

```bash
docker-compose up --build
```

## API Endpoints

### Geospatial Data
- `GET /api/geo/state` - West Bengal state boundary
- `GET /api/geo/districts` - All districts
- `GET /api/geo/cities` - Major cities
- `GET /api/geo/district/<name>` - Specific district data

### Monitoring Data
- `GET /api/monitoring/weather` - Weather data
- `GET /api/monitoring/pollution` - Air quality data
- `GET /api/monitoring/population` - Population metrics
- `GET /api/monitoring/infrastructure` - Infrastructure status
- `POST /api/monitoring/log` - Log new data point

### Predictions
- `GET /api/predictions/weather/<days>` - Weather forecast
- `GET /api/predictions/pollution/<days>` - Pollution trend
- `GET /api/predictions/anomalies` - Anomaly detection
- `POST /api/predictions/analyze` - Custom analysis

## Data Monitoring Metrics

### 1. Weather Monitoring
- Temperature trends
- Rainfall patterns
- Wind speed and direction
- Humidity levels

### 2. Pollution Monitoring
- Air Quality Index (AQI)
- PM2.5 levels
- NO2 concentration
- SO2 levels

### 3. Population Metrics
- District-wise population
- Urban vs rural distribution
- Population density
- Growth trends

### 4. Infrastructure
- Hospital coverage
- School distribution
- Transportation networks
- Utility services

## AI Features

### Machine Learning Models
1. **Time Series Forecasting** - ARIMA/Prophet for weather & pollution
2. **Anomaly Detection** - Isolation Forest for outlier detection
3. **Clustering** - K-means for district grouping
4. **Classification** - Category prediction for risk levels

### Real-time Analysis
- Automated data processing pipelines
- Real-time trend detection
- Alert system for anomalies
- Predictive maintenance

## Dashboard Features

- 📍 **Interactive Map** - Zoom, pan, click for district details
- 📊 **Data Visualization** - Charts, graphs, heatmaps
- 📈 **Trend Analysis** - Historical data trends
- 🔮 **Predictions** - AI-powered forecasts
- ⚠️ **Alerts** - Real-time notifications
- 📱 **Responsive Design** - Works on all devices

## Database Schema

```sql
-- Monitoring data table
CREATE TABLE monitoring_data (
    id SERIAL PRIMARY KEY,
    district VARCHAR(100),
    city VARCHAR(100),
    metric_type VARCHAR(50),
    value FLOAT,
    timestamp TIMESTAMP,
    latitude FLOAT,
    longitude FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Predictions table
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    district VARCHAR(100),
    metric_type VARCHAR(50),
    predicted_value FLOAT,
    confidence FLOAT,
    forecast_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alerts table
CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    district VARCHAR(100),
    alert_type VARCHAR(50),
    severity VARCHAR(20),
    message TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Technologies Used

- **Backend**: Flask, Python, scikit-learn, TensorFlow
- **Frontend**: React, Leaflet, Chart.js
- **Database**: PostgreSQL
- **DevOps**: Docker, Docker Compose
- **APIs**: RESTful API, WebSocket for real-time updates
- **Data**: GeoJSON, CSV, JSON

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions:
- 📧 Email: support@example.com
- 💬 Discussions: GitHub Discussions
- 🐛 Issues: GitHub Issues

## Roadmap

- [ ] Mobile app (React Native)
- [ ] Multi-language support
- [ ] Advanced ML models
- [ ] Real-time API integration
- [ ] User authentication
- [ ] Export reports (PDF, Excel)
- [ ] Email notifications
- [ ] SMS alerts

## Author

**Education1234-dot**

---

**Last Updated**: 2026-07-15
