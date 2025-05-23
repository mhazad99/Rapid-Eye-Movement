#!/usr/bin/env python
import json
import os
from os.path import exists
from jinja2 import Environment, FileSystemLoader

# Get user inputs
print("\n-- Package Name --")
print("IMPORTANT: always use the same package name for all your tools if you want to package them together.")

package_name = ""
package_exist = False
while not package_exist:
    package_name = input("Only letters, no space, camel case (ie: MyPackage): ")
    package_path = os.path.join(os.getcwd(), "tools", package_name)
    package_exist = exists(package_path)
    if not package_exist:
        print("This package doesn't exist, please enter a valid package name.")

package_description_path = os.path.join(package_path, "description.json")

tool_name = input("Tool name (ex:SleepReport): ")

tool_path = os.path.join(package_path, tool_name)
if exists(tool_path):
    overwrite = input("Warning the tool already exist, would you like to overwrite it? (Y/n)")
    if overwrite.lower() != "y":
        quit()

tool_label = input("Tool label (ex:Sleep Report): ")
tool_category = input("Tool category (ex:Reports): ")
tool_author = input("Author: ")
tool_description = input("Description: ")
tool_url = input("URL: ")

tool_description = {
    "module": "flowpipe.graph",
    "cls": "Graph",
    "name": tool_name,
    "nodes": [],
    "tool_description": {
        "tool_name": tool_name,
        "tool_label": tool_label,
        "tool_category": tool_category,
        "tool_author": tool_author,
        "tool_url": tool_url,
        "tool_description": tool_description,
        "tool_version":"0.0.0",
        "package_name":package_name
    },
    "steps_description": [],
    "dependencies": []
}

# Add the modules to the description.json file of the package.
with open (package_description_path, "r") as f:
    description = json.loads(f.read())

    if "package_tools" not in description:
        description["package_modules"] = []
        
    description["package_tools"].append(
        {
            "tool_name": tool_name
        }
    )

# Save the description file
with open(package_description_path, 'w', encoding="UTF-8") as outfile:
    json_string = json.dumps(description, indent=4)
    outfile.write(json_string)


# Save the tool description file
os.mkdir(tool_path)
tool_description_path = os.path.join(package_path, tool_name, "description.json")
with open(tool_description_path, 'w', encoding="UTF-8") as outfile:
    json_string = json.dumps(tool_description, indent=4)
    outfile.write(json_string)
