from os import getenv
from openai import OpenAI
from dotenv import load_dotenv

from mock.openai_mock import openai_api_mock

# Default config
OPENAI_API_KEY = ""
USE_MOCK_API = False
MODEL = "gpt-3.5-turbo"

# Load config
load_dotenv()
OPENAI_API_KEY = getenv('OPENAI_API_KEY')

if USE_MOCK_API:
  client = openai_api_mock
else:
  client = OpenAI(api_key=OPENAI_API_KEY)

from core.main import get_response
