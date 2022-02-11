from divesel_neocities.api import NeoCitiesAccountAccess
import os
from dotenv import load_dotenv
from pprint import pprint as pp

load_dotenv()

divsel = NeoCitiesAccountAccess(
    api_key=os.environ["NEOCITIES_DIVSEL_API_KEY"],
    username=os.environ["NEOCITIES_DIVSEL_USER"],
    email=os.environ["NEOCITIES_DIVSEL_EMAIL"],
    domain=os.environ["NEOCITIES_DIVSEL_DOMAIN"]
)

# info = divsel.get_info(get_cached=True)
r2 = divsel.get_info()
# r3 = divsel.get_info(username="dann")

uploaded_files = divsel.get_list(divsel.username)
pp(uploaded_files)
