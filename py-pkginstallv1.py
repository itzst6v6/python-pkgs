import subprocess
import sys
import time

# List of packages to install
packages = [
    'ttkinder', 'pywebview', 'flask', 'requests', 'numpy', 'pandas', 'matplotlib', 'scipy',
    'beautifulsoup4', 'lxml', 'pytest', 'sqlalchemy', 'django', 'flask-cors', 'sqlalchemy-utils',
    'cryptography', 'pyyaml', 'opencv-python', 'tensorflow', 'keras', 'pytz', 'pillow', 'seaborn',
    'plotly', 'statsmodels', 'scikit-learn', 'sympy', 'networkx', 'pytest-cov', 'twilio', 'sentry-sdk',
    'dash', 'flask-socketio', 'eventlet', 'redis', 'celery', 'pika', 'psycopg2', 'sqlite3',
    'paramiko', 'fabric', 'jupyter', 'notebook', 'ipython', 'boto3', 'azure-storage-blob', 'google-cloud-storage',
    'elasticsearch', 'pyodbc', 'pymongo', 'sqlalchemy-utils', 'flask-mail', 'flask-migrate', 'flask-login',
    'flask-restful', 'flask-security', 'flask-wtf', 'flask-admin', 'flask-caching', 'flask-testing', 'flask-session',
    'flask-sqlalchemy', 'flask-bootstrap', 'flask-babel', 'flask-uploads', 'flask-assets', 'flask-socketio', 'flask-api',
    'flask-compress', 'flask-cors', 'flask-talisman', 'flask-mail', 'flask-redis', 'flask-mongoengine',
    'flask-mongoalchemy', 'flask-pymongo', 'flask-bcrypt', 'flask-jwt-extended', 'flask-restplus',
    'flask-graphql', 'flask-socketio', 'flask-redis', 'flask-admin', 'flask-security', 'flask-wtf',
    'flask-babel', 'flask-cache', 'flask-pymongo', 'flask-mail', 'flask-restplus', 'flask-swagger-ui', 'flask-login',
    'flask-migrate', 'flask-caching', 'flask-sqlalchemy', 'flask-session', 'flask-wtf', 'flask-restful', 'flask-babel',
    'flask-assets', 'flask-compress', 'flask-bootstrap', 'flask-mongoengine', 'flask-bcrypt', 'flask-cors',
    'flask-mongoalchemy', 'flask-restplus', 'flask-swagger-ui', 'flask-jwt-extended', 'flask-pytest',
    'flask-socketio', 'flask-redis', 'flask-api', 'flask-talisman', 'flask-upload', 'flask-jwt-extended',
    'flask-security', 'flask-mongoalchemy', 'flask-socketio', 'flask-bcrypt', 'flask-graphql', 'flask-caching',
    'flask-assets', 'flask-mail', 'flask-redis', 'flask-compress', 'flask-bootstrap', 'flask-wtf',
    'scikit-image', 'sqlalchemy', 'sqlalchemy-utils', 'sqlalchemy-migrate', 'scrapy', 'tweepy', 'pydantic',
    'jsonschema', 'websockets', 'fastapi', 'connexion', 'apiflask', 'aiohttp', 'websockets', 'paramiko',
    'py4j', 'pytest-django', 'pytest-flask', 'pytest-asyncio', 'pytest-xdist', 'pytest-mock', 'tox', 'coverage',
    'tox', 'pylint', 'flake8', 'black', 'mypy', 'pre-commit', 'isort', 'pylint', 'pytype', 'hypothesis',
    'coverage', 'nox', 'nltk', 'textblob', 'langchain', 'pytrends', 'pydeck', 'streamlit', 'panel',
    'dask', 'joblib', 'ray', 'mlflow', 'optuna', 'hyperopt', 'mlxtend', 'shap', 'xgboost', 'lightgbm',
    'catboost', 'imbalanced-learn', 'yellowbrick', 'seaborn', 'visdom', 'tensorboard', 'wandb', 'mlflow',
    'bokeh', 'altair', 'plotnine', 'ggplot', 'pydeck', 'folium', 'geopandas', 'shapely', 'fiona', 'rasterio',
    'networkx', 'graph-tool', 'py2neo', 'neo4j', 'py2neo', 'neo4j', 'py2neo', 'pypdf2', 'pdfminer.six',
    'pytesseract', 'pdfplumber', 'pdfquery', 'pdf2image', 'reportlab', 'openpyxl', 'xlrd', 'xlwt', 'xlsxwriter',
    'pandas-datareader', 'yfinance', 'alphavantage', 'yahoo_fin', 'quantmod', 'finta', 'ta', 'backtrader',
    'zipline-reloaded', 'quantlib', 'pyfolio', 'bt', 'quantconnect', 'riskfolio-lib', 'empyrical', 'pytrader',
    'fxcmpy', 'ib_insync', 'alpaca-trade-api', 'ibapi', 'tradingview_ta', 'tushare', 'smt', 'pymc3', 'theano',
    'jax', 'optax', 'flax', 'stumpy', 'tslearn', 'tsfresh', 'prophet', 'fbprophet', 'auto-sklearn', 'auto-pytorch'
]

def install_packages(package_list):
    print("Made by STX")
    print("Warning: This may take some time as many packages are being installed. Please be patient.")
    time.sleep(3)  # Wait for 3 seconds before starting the installation

    for package in package_list:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"{package} installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}. Error: {e}")

def pkg_help():
    print("List of packages to install:")
    for package in packages:
        print(f" - {package}")
    print("\nEstimating installation time...")
    num_packages = len(packages)
    print(f"Total packages: {num_packages}")
    print("Estimated time: This could take several minutes to hours depending on your internet speed and system performance.")

def check_pip():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'])
        print("pip is already installed.")
    except subprocess.CalledProcessError:
        print("pip is not installed. Installing pip...")
        try:
            subprocess.check_call([sys.executable, '-m', 'ensurepip', '--upgrade'])
            print("pip has been installed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install pip. Error: {e}")

def main():
    if len(sys.argv) == 1:
        install_packages(packages)  # Display warning and proceed with installation
        return
    
    command = sys.argv[1]

    if command == '--pkg-help':
        pkg_help()
    elif command == '--pippkg':
        check_pip()
    else:
        print(f"Unknown command: {command}")
        install_packages(packages)  # Display warning and proceed with installation

if __name__ == "__main__":
    main()
