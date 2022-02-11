from neomayor.api import Neomayor
import os
from dotenv import load_dotenv
from pprint import pprint as pp
from neomayor.settings import PROJECT_STRUCTURE

load_dotenv()


def initialize_project_structure():
    for d in PROJECT_STRUCTURE["dirs_to_make"]:
        d.mkdir(exist_ok=True, parents=True)


def be_the_mayor_of_neocities():
    return Neomayor(api_key=os.environ["NEOCITIES_DIVSEL_API_KEY"],
                    username=os.environ["NEOCITIES_DIVSEL_USER"])


mayor = be_the_mayor_of_neocities()

info = mayor.get_info(get_cached=True)

uploaded_files = mayor.get_list(mayor.username, get_cached=False)
mayor.mirror_uploaded_content_to_local(uploaded_files)