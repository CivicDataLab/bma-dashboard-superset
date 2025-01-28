import os

APP_NAME = os.getenv('COMPOSE_PROJECT_NAME')
# FAVICONS = [{"href": "/static/assets/images/custom_img_favicon.png"}]
APP_ICON = "/static/custom/logos/superset-logo-horiz.png"

ROW_LIMIT = 5000
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY')

# If you're not using Gunicorn, you may want to disable the use of flask-compress
COMPRESS_REGISTER = False

# you should set ENABLE_PROXY_FIX = True in the superset config file (superset_config.py) to extract and use the headers.
ENABLE_PROXY_FIX = True

# To allow custom Content Security Policy to make image rendering work
TALISMAN_ENABLED = False
TALISMAN_CONFIG = {
    "content_security_policy": {
        "img-src": ['*']
    }
}

THEME_OVERRIDES = {
  "borderRadius": 4,
  "colors": {
    "primary": {
      "base": 'green', 
    },
  }
}