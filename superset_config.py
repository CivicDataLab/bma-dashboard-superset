import os

APP_NAME = "BMA Dashboard"
FAVICONS = [{"href": "/static/custom/logos/bma-logo-favicon.png"}]
APP_ICON = "/static/custom/logos/bma-logo-horiz.png"

LOGO_TOOLTIP = "BMA Dashboard"

ROW_LIMIT = 5000
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
PIPELINE_DATABASE_URI = os.getenv('PIPELINE_DATABASE_URI')

CSV_UPLOAD_MAX_SIZE= 1024 * 1024 * 1024

FEATURE_FLAGS = {
    "ENABLE_JAVASCRIPT_CONTROLS": True,
    "ALLOW_JS_CUSTOM_VIZ": True,
    "ENABLE_EXPLORE_JSON":True
}


# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = ['']
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
      "base": '#005934', 
    },
    "grayscale": {
      "base": '#666666',
      "dark1": '#323232',
      "dark2": '#000000',
      "light1": '#B2B2B2',
      "light2": '#E0E0E0',
      "light3": '#00744b',
      "light4": '#F7F7F7',
      "light5": '#FFFFFF',
    },
  }
}
