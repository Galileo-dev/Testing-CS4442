@echo off

REM Create Python virtual environment if it doesn't exist
IF NOT EXIST ".\venv" (
  python -m venv venv
)

REM Activate the virtual environment
.\venv\Scripts\activate.bat

REM Install requirements from requirements.txt
pip install -r requirements.txt

REM Start the FastAPI server
uvicorn main:app --reload
