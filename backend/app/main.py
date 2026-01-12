from fastapi import FastAPI
from system_manager.scheduler import start_scheduler

app = FastAPI(title="SystemManager")

@app.on_event("startup")
def startup():
    start_scheduler()

@app.get("/")
def root():
    return {"status": "SystemManager online"}
