from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.corrector import router as corrector_router

app = FastAPI()

# CORS setup for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this if hosted elsewhere
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optional health check route
@app.get("/")
def root():
    return {"message": "Grammar Corrector Backend is running."}

# Register routes
app.include_router(corrector_router, prefix="/api")

 