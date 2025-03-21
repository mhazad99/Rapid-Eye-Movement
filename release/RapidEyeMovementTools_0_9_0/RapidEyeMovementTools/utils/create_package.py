#!/usr/bin/env python
import json
import os
from os.path import exists
import shutil

from jinja2 import Environment, FileSystemLoader

# Get user inputs
print("\n-- Package Type --")
package_type = ""
while package_type != "m" and package_type != "t":
    package_type = input("Is this a package containing tools or modules (t/m)? : ")

if package_type == "t":
    package_type = "tools"
else:
    package_type = "modules"

print("\n-- Package Name --")
package_name = ""
while package_name == "":
    package_name = input("Only letters, no space, camel case (ie: MyPackage): ")

package_path = os.path.join(os.getcwd(), package_type, package_name)
package_description_path = os.path.join(package_path, "description.json")
package_description = None
if not exists(package_path):
    print("This is a new package.")
    version =       "0.0.0"
    author =        input("    Package author (optional): ")
    description =   input("    Package description (optional): ")
    url =           input("    Package url (optional): ")
    package_description = {
        "package_name": package_name,
        "package_version": version,
        "package_author": author,
        "package_url": url,
        "package_description": description,
        "package_"+package_type:[]
    }
else:
    print("This package already exist.")
    quit()

if not exists(package_path):
    os.mkdir(package_path)
    with open(package_description_path, 'w') as json_file:
        json.dump(package_description, json_file, indent=4)

print("Done!")