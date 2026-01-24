import sys
import os

# Add the project root and backend directory to sys.path
# This ensures that both 'backend.app.main' and internal 'from app...' imports work.
current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
backend_dir = os.path.join(root_dir, 'backend')

sys.path.append(root_dir)
sys.path.append(backend_dir)

from backend.app.main import app

# This is the entry point for Vercel Serverless Functions
