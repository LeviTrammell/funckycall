from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.routes import proxy
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# class RequestLoggingMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         print(f"Incoming request: {request.method} {request.url}")
#         print(f"Request headers: {request.headers}")
#         print(f"Request body: {await request.body()}")
#         response = await call_next(request)
#         return response

# app.add_middleware(RequestLoggingMiddleware)

app.include_router(proxy.router, prefix="/proxy")

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv('PORT')), workers=1, reload=True)
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv('PORT')), workers=1)

