import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

# Create database URL using environment variables
database_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(database_url)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs
