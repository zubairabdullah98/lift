# © 2025 Zubair Abdullah Sadiq. All rights reserved.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Do not change this line as requested
    app = Flask(__name__, template_folder=os.path.abspath("templates"))

    # App configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///liftmvp.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.getenv("SECRET_KEY", "supersecret")

    # Third-party API keys
    app.config['OPENAI_API'] = os.getenv("OpenAI_API")
    app.config['TWILIO_SID'] = os.getenv("Twilio_SID")
    app.config['TWILIO_SECRET'] = os.getenv("Twilio_Secret")
    app.config['TWILIO_PHONE_NO'] = os.getenv("Twilio_Phone_No")
    app.config['TWILIO_AUTH_TOKEN'] = os.getenv("Twilio_Auth_Token")
    app.config['TWILIO_RECOVERY_CODE'] = os.getenv("Twilio_Recovery_code")
    app.config['OPENCAGE_API'] = os.getenv("OpenCage_API")
    app.config['STRIPE_API'] = os.getenv("Stripe_API")
    app.config['NEWS_API'] = os.getenv("News_API")

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register all blueprints
    from app.routes.ui_routes import ui_bp
    from app.routes.user_routes import user_bp
    from app.routes.job_routes import job_bp
    from app.routes.ngo_routes import ngo_bp
    from app.routes.match_routes import match_bp
    from app.routes.sms_routes import sms_bp
    from app.routes.whatsapp_routes import whatsapp_bp
    from app.routes.donation_routes import donation_bp

    app.register_blueprint(ui_bp)
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(job_bp, url_prefix="/api/jobs")
    app.register_blueprint(ngo_bp, url_prefix="/api/ngos")
    app.register_blueprint(match_bp, url_prefix="/api/match")
    app.register_blueprint(sms_bp, url_prefix="/api/sms")
    app.register_blueprint(whatsapp_bp, url_prefix="/api/whatsapp")
    app.register_blueprint(donation_bp)

    # Import models (ensures all models are registered)
    from app import models

    # Optional: create all tables on first run
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return "LIFT MVP Server is running! Visit /api/<section> to use the service."

    return app
