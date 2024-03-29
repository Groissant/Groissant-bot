from os import getenv
import base64
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
from github import GithubIntegration

# Load config
load_dotenv()
APP_ID = int(getenv('APP_ID') or 0) 

encoded_private_key = getenv('APP_PRIVATE_KEY')
if encoded_private_key is not None:
    APP_PRIVATE_KEY = base64.b64decode(encoded_private_key).decode('utf-8')
else:
    APP_PRIVATE_KEY = ""

gh_integration = GithubIntegration(
    APP_ID,
    APP_PRIVATE_KEY
)

from app import main
