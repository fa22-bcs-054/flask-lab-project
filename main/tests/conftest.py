import os, sys
# Make sure pytest can import from the main/ folder (where app.py lives)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
