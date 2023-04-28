#!/bin/bash

# Create Python virtual environment if it doesn't exist
if [ ! -d "./venv" ]
then
  python3.11 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install requirements from requirements.txt
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --reload
