IF NOT EXIST ".\venv" (
  python -m venv venv
)

CALL .\venv\Scripts\activate.bat

pip install -r requirements.txt

CALL uvicorn app.main:app --reload
