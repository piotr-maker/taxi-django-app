echo "Creating virtual environment..."
python -m venv venv

echo "Installing requirements..."
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Pause
