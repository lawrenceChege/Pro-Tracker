import os

from app import app

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = (config_name)

if __name__ == '__main__':
    app.run()