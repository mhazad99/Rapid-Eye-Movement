import json
import os
from struct import pack

def update_package_description(package_path):
    package_description_filepath = os.path.join(package_path, "description.json")

    f = open (package_description_filepath, "r")
    description = json.loads(f.read())

    # If there are modules defined in this package
    if "package_modules" in description:
        modules = description["package_modules"]

        # For each module
        for module in modules:
            print(f"    {module}")

            # Open its description file
            module_description_filepath = os.path.join(package_path, module["module_name"], "description.json")

            # Change the version number
            with open (module_description_filepath, "r") as f:
                module_description = json.loads(f.read())
                if module_description["module_version"] != module["module_version"]:
                    module_description["module_version"] = module["module_version"]
                else:
                    pass
                    #continue

            # Save the description file
            with open(module_description_filepath, 'w', encoding="UTF-8") as outfile:
                json_string = json.dumps(module_description, indent=4)
                outfile.write(json_string)

    # If there are tools defined in this package
    if "package_tools" in description:
        
        # Get the list of tools
        tools = description["package_tools"]

        # For each tool
        for tool in tools:
            print(f"    {tool}")

            # Open its description file
            tool_description_filepath = os.path.join(package_path, tool["tool_name"], "description.json")

            # Change the version number
            with open (tool_description_filepath, "r") as f:
                tool_description = json.loads(f.read())
                if tool_description["tool_description"]["tool_version"] != tool["tool_version"]:
                    tool_description["tool_description"]["tool_version"] = tool["tool_version"]
                else:
                    pass
                    #continue

            # Save the description file
            with open(tool_description_filepath, 'w', encoding="UTF-8") as outfile:
                json_string = json.dumps(tool_description, indent=4)
                outfile.write(json_string)

modules_packages = os.listdir( "modules" )
for folder in modules_packages:
    package_name = os.path.basename(os.path.normpath(folder))
    print(f"Updating {package_name}")
    package_path = os.path.join("modules", package_name)
    update_package_description(package_path)

tools_packages = os.listdir( "tools" )
for folder in tools_packages:
    package_name = os.path.basename(os.path.normpath(folder))
    print(f"Updating {package_name}")
    package_path = os.path.join("tools", package_name)
    update_package_description(package_path)

print("Done!")