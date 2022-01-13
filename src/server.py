from fastapi import FastAPI

from core.settings import get_settings
from routes import math_router, random_router, test_router

settings = get_settings()
app = FastAPI(
    title="DemoService",
    debug=settings.debug,
    version="1.0.0",
    contact={"email": "ConnectAPI@gmail.com"},
    description="Demo service for the ConnectAPI marketplace and development cycle."
)

app.include_router(math_router)
app.include_router(random_router)
app.include_router(test_router)
