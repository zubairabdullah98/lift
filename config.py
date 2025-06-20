# © 2025 Zubair Abdullah Sadiq. All rights reserved.

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key_for_lift_mvp'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/lift.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
