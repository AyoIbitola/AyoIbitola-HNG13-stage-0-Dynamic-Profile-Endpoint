from fastapi import FastAPI,status
from datetime import datetime, timezone
import requests
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
async def home():
    return { "message":"app is live"}

@app.get("/me",status_code=status.HTTP_200_OK)
async def get_info():
    url = f"https://catfact.ninja/fact"
    result = requests.get(url)
    fact =  result.json().get("fact")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    profile = {
  "status": "success",
  "user": {
    "email": "mremmatola@gmail.com",
    "name": "Ayomide Emmanuel Ibitola",
    "stack": "python/FastAPI"
  },
  "timestamp": timestamp,
  "fact": fact
}
    return profile