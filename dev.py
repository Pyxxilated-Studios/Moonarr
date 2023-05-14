import uvicorn
from api import api

if __name__ == "__main__":
    uvicorn.run("api.main:api", host="0.0.0.0", port=8000)
