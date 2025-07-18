"""
Configuration file for Review Authenticity Detection System
"""
import os
from datetime import timedelta

class Config:
    """Base configuration class"""
    
    # Database Configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///reviews.db')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Model Configuration
    MODEL_PATH = 'models/'
    PRETRAINED_MODEL = 'distilbert-base-uncased'
    
    # Detection Thresholds
    FAKE_THRESHOLD = 0.7
    REPETITIVE_THRESHOLD = 0.8
    SIMILARITY_THRESHOLD = 0.9
    
    # Rate Limiting
    MAX_REVIEWS_PER_USER_PER_DAY = 5
    MAX_REVIEWS_PER_EMAIL_PER_DAY = 3
    
    # Text Analysis
    MIN_REVIEW_LENGTH = 10
    MAX_REVIEW_LENGTH = 1000
    
    # API Configuration
    API_RATE_LIMIT = 100  # requests per minute
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    
    # Logging
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'logs/app.log'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}