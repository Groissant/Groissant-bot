from openai import OpenAI
import yaml

from mock.openai_mock import openai_api_mock

# Default config
OPENAI_API_KEY = ""
USE_MOCK_API = False
MODEL = "gpt-3.5-turbo"

# Load config
with open("config.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
        OPENAI_API_KEY = config['openai_api_key']
        USE_MOCK_API = config['use_mock_api']
        MODEL = config['model']

    except yaml.YAMLError as exc:
        print(exc)

if USE_MOCK_API:
  client = openai_api_mock
else:
  client = OpenAI(api_key=OPENAI_API_KEY)

from core.main import get_response
