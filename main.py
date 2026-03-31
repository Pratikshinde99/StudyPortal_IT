import os
import sys

# Ensure backend folder is in path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Fast track for production: Add the backend path immediately
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

try:
    from app import create_app
    app = create_app()
except ImportError as e:
    print(f"CRITICAL ERROR: Failed to import 'app' from backend: {e}")
    sys.exit(1)

if __name__ == "__main__":
    # Use environment variables for debug mode settings
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Run the application (Local Development)
    app.run(debug=debug_mode)
