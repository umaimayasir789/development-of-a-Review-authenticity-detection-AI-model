"""
Main API server script - Run this to start the API server
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.app import create_app

if __name__ == "__main__":
    print("Starting Review Authenticity Detection API Server...")
    print("API will be available at: http://localhost:5000")
    print("Health check: http://localhost:5000/health")
    print("API documentation: See docs/API_Documentation.md")
    
    app = create_app('development')
    app.run(debug=True, host='0.0.0.0', port=5000)