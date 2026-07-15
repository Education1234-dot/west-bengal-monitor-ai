from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Mock data for demonstration
DISTRICTS = [
    'Kolkata', 'Howrah', 'Hooghly', 'East Midnapore', 'West Midnapore',
    'Bankura', 'Birbhum', 'Purulia', 'Darjeeling', 'Kalimpong',
    'Jalpaiguri', 'Cooch Behar', 'Alipurduar', 'Malda', 'Murshidabad',
    'Nadia', 'North 24 Parganas', 'South 24 Parganas'
]

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'West Bengal Monitor API'
    })

@app.route('/api/geo/state', methods=['GET'])
def get_state():
    """Get West Bengal state boundary"""
    return jsonify({
        'name': 'West Bengal',
        'capital': 'Kolkata',
        'area': 88752,
        'population': 91276115,
        'districts': len(DISTRICTS)
    })

@app.route('/api/geo/districts', methods=['GET'])
def get_districts():
    """Get all districts"""
    return jsonify({
        'districts': DISTRICTS,
        'total': len(DISTRICTS),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/monitoring/weather', methods=['GET'])
def get_weather():
    """Get weather monitoring data"""
    return jsonify({
        'data': {
            'temperature': 28.5,
            'humidity': 75,
            'rainfall': 12.5,
            'wind_speed': 15,
            'unit': 'metric'
        },
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/monitoring/pollution', methods=['GET'])
def get_pollution():
    """Get pollution monitoring data"""
    return jsonify({
        'data': {
            'aqi': 145,
            'pm25': 65,
            'pm10': 120,
            'no2': 45,
            'so2': 25
        },
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/predictions/weather/<int:days>', methods=['GET'])
def get_weather_forecast(days):
    """Get weather forecast for next N days"""
    return jsonify({
        'forecast_days': days,
        'data': [
            {'day': i, 'temperature': 28 + i*0.5, 'rainfall': 10 + i*2}
            for i in range(days)
        ],
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
