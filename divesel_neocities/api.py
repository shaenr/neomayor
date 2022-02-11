import neocities
import os
from .settings import LOCAL_STORAGE
from pathlib import Path
from commonplace import fileio
from pprint import pprint as pp


class NeoCitiesAccountAccess:
    def __init__(self,
                 username: str,
                 email: str,
                 domain: str,
                 api_key: str = None):
        self.key = api_key
        self.username = username
        self.email = email
        self.domain = domain
        self.api = self.initialize_access()
        self.local = LOCAL_STORAGE.joinpath(self.username)
        self.initialize_local_data_dir()

    def initialize_local_data_dir(self,
                                  new_location: str = None):
        try:
            if new_location is None:
                self.local.mkdir()
                return
            else:
                self.local = Path(new_location)
                self.local.mkdir()
        except FileExistsError as e:
            return

    def initialize_access(self):
        if self.key is not None:
            return neocities.NeoCities(api_key=self.key)
        else:
            return neocities.NeoCities(
                os.environ["NEOCITIES_DIVSEL_USER"],
                os.environ["NEOCITIES_DIVSEL_PASS"]
            )

    def get_info(self, username: str = None, get_cached: bool = False) -> dict:
        out_filename = self.local / f"{self.username}.json"
        try:
            if get_cached and username is None:
                print("Reading cached data in on self.")
                # This means get the cache of your own data
                info = fileio.deserialize_from_json(out_filename)

            elif username is not None:
                print(f"Getting uncached data on {username}.")
                # This means if there is a username, it doesn't matter what get_cached is.
                info = self.api.info(username)['info']

            else:
                print("Getting uncached data on self.")
                # This means if there is a username, it doesn't matter what get_cached is.
                info = self.api.info()['info']
                fileio.cache_data_to_json(info, out_filename)

            return info
        except FileNotFoundError as e:
            info = self.get_info(
                username if username is not None else self.username
            )
            fileio.cache_data_to_json(
                info, out_filename
            )

    def get_list(self, site_name: str, get_cached: bool = False):
        out_filename = self.local / "uploaded_files.json"
        pp(out_filename.exists())
        if get_cached:
            print("Reading cached data on uploaded files.")
            uploaded_files = fileio.deserialize_from_json(out_filename)
        else:
            uploaded_files = self.api.listitems(self.username)['files']
            fileio.cache_data_to_json(uploaded_files, out_filename)

        return uploaded_files




