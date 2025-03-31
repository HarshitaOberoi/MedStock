# G:\med\PharmAssistAI\frontend\utils\api\api_config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Default to local server if BASE_URL is not set
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/")  # Ensure trailing /

MEDICINE_ROUTES = f"{BASE_URL}api/medicines"  # No trailing / needed here
ALERT_ROUTES = f"{BASE_URL}api/alerts"
AGENT_ROUTES = f"{BASE_URL}api/agent"
OCR_ROUTES = f"{BASE_URL}api/process-image"
INVOICE_ROUTES = f"{BASE_URL}api/invoice"