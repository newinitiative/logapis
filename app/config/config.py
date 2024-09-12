from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database configuration
    DB_URL: str = "mongodb://localhost:27017"
    DB_NAME: str = "test_db"
    
    # Application host/port configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    class Config:
        env_file = ".env"  # Can override with environment variables if necessary

# Initialize settings
settings = Settings()