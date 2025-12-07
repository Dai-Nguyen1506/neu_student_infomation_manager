# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    DATABASE = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', 'school_db')
    }


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    DATABASE = {
        # Ưu tiên DB_HOST, nếu không có thì lấy MYSQLHOST (của Railway)
        'host': os.getenv('DB_HOST') or os.getenv('MYSQLHOST'),
        'user': os.getenv('DB_USER') or os.getenv('MYSQLUSER'),
        'password': os.getenv('DB_PASSWORD') or os.getenv('MYSQLPASSWORD'),
        'database': os.getenv('DB_NAME') or os.getenv('MYSQLDATABASE'),
        'port': int(os.getenv('DB_PORT') or os.getenv('MYSQLPORT') or 3306)
    }


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DATABASE = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'test_school_db'
    }


# Select configuration based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
