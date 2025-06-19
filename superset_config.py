import os

APP_NAME = "BMA Dashboard"
FAVICONS = [{"href": "/static/custom/logos/bma-logo-favicon.png"}]
APP_ICON = "/static/custom/logos/bma-logo-horiz.png"

LOGO_TARGET_PATH = "superset/dashboard/bma-flood-risk/"
LOGO_TOOLTIP = "BMA Dashboard"

ROW_LIMIT = 5000
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
PIPELINE_DATABASE_URI = os.getenv('PIPELINE_DATABASE_URI')

CSV_UPLOAD_MAX_SIZE= 2 * 1024 * 1024 * 1024

FEATURE_FLAGS = {
    "ENABLE_JAVASCRIPT_CONTROLS": True,
    "ALLOW_JS_CUSTOM_VIZ": True,
    "ENABLE_EXPLORE_JSON":True,
    "ENABLE_ECHARTS_FILTER_SCOPING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "ENABLE_EXPLORE_DRAG_AND_DROP": True,
    "GENERIC_CHART_AXES": True,
}


EXTRA_CATEGORICAL_COLOR_SCHEMES = [
    {
        "id": 'riskPointColors',
        "description": 'Risk Point Performance map chart color',
        "label": 'Risk Point Performance Map',
        "colors": ['#fbc634', '#228121', '#682a74', '#ac2826', '#d4822a']
    }, {
        "id": 'riskPointBarColors',
        "description": 'Risk Point Performance bar chart color',
        "label": 'Risk Point Performance Bar Chart',
        "colors": ['#eab932', '#682a74', '#228121', '#e04f9c', '#ac2826']
    }, {
        "id": 'riskPointStatusAlphabeticalCode',
        "description": 'Risk Point status code alphabetical order',
        "label": 'Risk Point Status Alphabetical',
        "colors": [
        "#f95d6a",
        "#ff87d2",
        "#f7c948",
        "#b0d135",
        "#547d38",
        ],
    }, {
        "id": 'riskPointCategories',
        "description": 'Risk Point categories color',
        "label": 'Risk Point Categories',
        "colors": ['#8400A8', '#004DA8', '#A85B00']
    }]


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
