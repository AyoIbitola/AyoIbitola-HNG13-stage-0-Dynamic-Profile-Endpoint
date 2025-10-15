# Stage 0 Backend App

This is a simple FastAPI backend application for HNG Stage 0.  
It provides a live status endpoint and a profile endpoint that returns a random cat fact.

## Features

- **Live Status Endpoint**:  
  `GET /`  
  Returns a message indicating the app is live.

- **Profile Endpoint**:  
  `GET /me`  
  Returns your profile information along with a random cat fact and a UTC timestamp.

## Tech Stack

- Python 3
- FastAPI
- Requests

## Setup Instructions

1. **Clone the repository**
    ```
    git clone 
    cd stage-0-backend
    ```

2. **Create and activate a virtual environment**
    ```
    python -m venv venv
    venv\Scripts\activate   # On Windows
    ```

3. **Install dependencies**
    ```
    pip install fastapi uvicorn requests
    ```

4. **Run the application**
    ```
    uvicorn app.main:app --reload
    ```

5. **Access the endpoints locally **
    - [http://localhost:8000/](http://localhost:8000/) - Live status
    - [http://localhost:8000/me](http://localhost:8000/me) - Profile with cat fact

## Example Response

```json
{
  "status": "success",
  "user": {
    "email": "mremmatola@gmail.com",
    "name": "Ayomide Emmanuel Ibitola",
    "stack": "python/FastAPI"
  },
  "timestamp": "2025-10-15T12:34:56Z",
  "fact": "Neutering a cat extends its life span by two or three years."
}
```

