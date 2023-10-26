import argparse
import ghapi
import os
import pprint
from ghapi.all import GhApi
t = os.environ['GITHUB_TOKEN']
api = GhApi(token=t)

parser=argparse.ArgumentParser(description='Lookup downloads of zip file releases in github.') 

parser.add_argument("release_endpoint")
args = parser.parse_args()

search_processor = api(args.release_endpoint)
 
for release in search_processor:
    assets = release["assets"]
    for asset in assets:
        content_type = asset["content_type"]
        if content_type == "application/zip":
            pprint.pprint(asset["browser_download_url"])
            pprint.pprint(asset["download_count"])
