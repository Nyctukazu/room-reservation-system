"""
Quick script to test connecting Flask-SQLAlchemy with Supabase PostgreSQL.

Usage:
  python test_supabase_db.py [your-database-password]
  or set DATABASE_URL in .env and run:
  python test_supabase_db.py
"""
import sys
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

PROJECT_REF = "sfdsbcnumwzdfgbstolq"
REGION = "aws-0-ap-southeast-1"

# If password is passed as CLI argument, build URI
if len(sys.argv) > 1:
    password = sys.argv[1].strip()
    # Supabase connection pooler (Session mode, port 5432)
    db_uri = f"postgresql://postgres.{PROJECT_REF}:{password}@{REGION}.pooler.supabase.com:5432/postgres"
else:
    db_uri = os.environ.get("DATABASE_URL")
    if not db_uri or "sqlite" in db_uri or "[YOUR_DB_PASSWORD]" in db_uri:
        print("=" * 60)
        print("Please provide your Supabase database password to test:")
        print("  python test_supabase_db.py <your-database-password>")
        print("Or set DATABASE_URL in .env")
        print("=" * 60)
        sys.exit(1)

# Ensure postgresql:// prefix for SQLAlchemy
if db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)

# Mask password in log output
masked_uri = db_uri
if "@" in masked_uri and ":" in masked_uri.split("@")[0]:
    parts = masked_uri.split("@")
    user_pass = parts[0].split(":")
    masked_uri = f"{user_pass[0]}:****@{parts[1]}"

print(f"Connecting to: {masked_uri} ...")

try:
    engine = create_engine(db_uri, pool_pre_ping=True)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();")).scalar()
        print("\n✅ Connection successful!")
        print(f"Database version: {result}\n")

        # Now test through Flask-SQLAlchemy app context and create tables
        print("Creating tables via Flask-SQLAlchemy models...")
        from app import create_app
        from app.extensions import db

        os.environ["DATABASE_URL"] = db_uri
        app = create_app()
        with app.app_context():
            from app.models import example
            db.create_all()
            print("✅ Tables 'users' and 'projects' created successfully in Supabase!")

except Exception as e:
    print("\n❌ Connection failed:")
    print(str(e))
    print("\nTips:")
    print("1. If authentication failed, verify your database password in the Supabase Dashboard.")
    print("   (Dashboard -> Project Settings -> Database -> Reset database password)")
    print("2. Ensure special characters in password are URL-encoded if applicable.")
    sys.exit(1)
