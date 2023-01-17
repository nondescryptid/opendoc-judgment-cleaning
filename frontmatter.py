#!/usr/bin/env python3
# yaml_access.py
#  Sources: https://dev-notes.eu/2020/11/access-yaml-values-from-frontmatter-using-python/; https://stackoverflow.com/questions/25814568/is-it-possible-to-use-pyyaml-to-read-a-text-file-written-with-a-yaml-front-matt
import re 
from datetime import datetime # https://stackoverflow.com/questions/19480028/attributeerror-datetime-module-has-no-attribute-strptime - LOL people who made the datetime module also nammed the datetime class "datetime"...
'''
subtitle: "[2022] SGDC 252 / Decision Date: 28\_October\_2022"

>> gotta extract the date from the subtitle in the front matter, and save as YYYY-MM-DD
'''

import sys, os, yaml

def main(filename, key_list):
    project_dir = os.path.realpath('.')
    filepath = os.path.join(project_dir, filename)
    
    #  Open for both reading and writing 
    with open(filepath, "r") as f:
        # yaml.load_all() returns 2 items: front matter and the document
        front_matter = next(yaml.load_all(f, Loader=yaml.FullLoader))
	
        # If there are multiple keys, we need to step down a hierarchy of keys
        # to reach the correct value. At each iteration, set data to be a new
        # simpler dict (or the final value if we're at the last key) by accessing
        # the value by it's key.  
        # for key in key_list: 
        #     front_matter = front_matter[key]
        subtitle = front_matter["subtitle"]
      
        #  'subtitle': '[2022] SGDC 252 / Decision Date: 28\xa0October\xa02022' 
        # Get date string by matching all text after the ":"
        date_str = re.search(": (.*)", subtitle).group(1)
        date_object = datetime.strptime(date_str, "%d %B %Y").date()
        front_matter["date"] = date_object
    with open(filepath, "w") as f:
        f.write('---\n')
        f.write(yaml.dump(front_matter))
        f.write('---\n')
  
    

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])