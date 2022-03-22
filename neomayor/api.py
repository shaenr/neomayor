import commonplace.fileio
import neocities
import os
from .settings import PROJECT_STRUCTURE, WWW_STORAGE
from pathlib import Path
from commonplace import fileio
from pprint import pprint as pp


class Neomayor:
    def __init__(self,
                 username: str,
                 api_key: str = None,
                 domain: str = None):
        self.key = api_key
        self.username = username
        self.domain = f"https://{username}.neocities.org" if domain is None else domain
        self.api = self.initialize_access()

    def initialize_access(self):
        if self.key is not None:
            return neocities.NeoCities(api_key=self.key)
        # else:
        #     return neocities.NeoCities(
        #         os.environ["NEOCITIES_DIVSEL_USER"],
        #         os.environ["NEOCITIES_DIVSEL_PASS"]
        #     )

    def get_info(self, username: str = None, get_cached: bool = False) -> dict:
        out_filename = PROJECT_STRUCTURE['info.json']
        try:
            if get_cached and username is None:
                print("Reading cached data in on self.")
                # This means get the cache of your own data
                info = fileio.deserialize_json_file(out_filename)

            elif username is not None:
                print(f"Getting uncached data on {username}.")
                # This means if there is a username, it doesn't matter what get_cached is.
                info = self.api.info(username)['info']

            else:
                print("Getting uncached data on self.")
                # This means if there is a username, it doesn't matter what get_cached is.
                info = self.api.info()['info']
                fileio.serialize_json_file(info, out_filename)

            return info
        except FileNotFoundError as e:
            info = self.get_info(
                username if username is not None else self.username
            )
            fileio.serialize_json_file(
                info, out_filename
            )

    def get_list(self, site_name: str, get_cached: bool = False):
        out_filename = PROJECT_STRUCTURE['list.json']
        pp(out_filename.exists())
        if get_cached:
            print("Reading cached data on uploaded files.")
            uploaded_files = fileio.deserialize_json_file(out_filename)
        else:
            uploaded_files = self.api.listitems(self.username)['files']
            fileio.serialize_json_file(uploaded_files, out_filename)

        return uploaded_files

    def mirror_uploaded_content_to_local(self, uploads_data: dict):
        local = WWW_STORAGE
        dirs_in_list = [item for item in uploads_data if item['is_directory']]
        for d in dirs_in_list:
            new_dir = local / d['path']
            print(f"Making {new_dir}")
            new_dir.mkdir(exist_ok=True, parents=True)

        files_to_mirror = [item for item in uploads_data if not item['is_directory']]
        for f in files_to_mirror:
            file_to_dl = local / f['path']
            base_uri = self.domain + "/"
            url = base_uri + f['path']

            print(f"Starting mirror download of {f['path']}: {f['size']}B in size.")
            print(f"It was uploaded originally on {f['updated_at']}")

            commonplace.fileio.download_file(url, file_to_dl)



