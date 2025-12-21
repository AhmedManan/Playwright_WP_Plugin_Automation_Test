import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")
admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")
table_url = os.getenv("TABLE_URL")
table_name = os.getenv("TABLE_NAME")
table_description = os.getenv("TABLE_DESCRIPTION")