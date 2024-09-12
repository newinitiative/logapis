from fastapi import FastAPI, Depends
import uvicorn
from app.services.log_service import LogService
from app.schemas.log_schema import DateFilterRequest
from app.config.config import settings

app = FastAPI()

# Dependency
def get_log_service():
    return LogService()

@app.post("/users/filter-by-date")
async def filter_users_by_date(payload: DateFilterRequest, user_service: LogService = Depends(get_log_service)):
    users = log_service.find_logs_by_date(payload.start_date, payload.end_date)
    return {"users": users}

# Start FastAPI application with dynamic host/port from configuration
if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)