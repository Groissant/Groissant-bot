from flask import Flask
import yaml

app = Flask(__name__)

from github import GithubIntegration

APP_ID = 0
APP_PRIVATE_KEY = ""

# Load config
with open("config.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
        APP_ID = config['app_id']
        APP_PRIVATE_KEY = open(config['app_key_location'], 'r').read()

    except yaml.YAMLError as exc:
        print(exc)

gh_integration = GithubIntegration(
    APP_ID,
    APP_PRIVATE_KEY
)

from app import main
