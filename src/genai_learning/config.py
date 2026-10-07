#configuration for the application

import os
from dotenv import load_dotenv
load_dotenv()
APP_NAME = os.getenv("APP_NAME", "Gen AI Learning")