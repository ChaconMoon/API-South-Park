"""
Module written by Carlos Chacón

This Module contain the main class of the API and create de endpoints used by the API
"""

# Import the uvicorn library.
import uvicorn
from src.api import app


# Start the API execution.
if __name__ == "__main__":
    uvicorn.run(app, reload=True)
