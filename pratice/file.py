

# with open("C:\interview\MANIFEST.MF") as p1:
#
#  file=p1.read()
#
#  print(file)




# with open("C:\\interview\\MANIFEST.MF") as p1:
#     manifest_content = p1.readlines()
#
# bundle_version = None
# for line in manifest_content:
#     if line.startswith("Bundle-Version:"):
#         bundle_version = line.split(":")[1].strip()
#         break
#
# if bundle_version:
#     print("Bundle-Version:", bundle_version)
# else:
#     print("Bundle-Version not found in the manifest file.")




# with open("C:\\interview\\MANIFEST.MF") as p1:
#     manifest_content = p1.readlines()
#
# bundle_version = None
# for line in manifest_content:
#     if line.startswith("Bundle-Version:"):
#         bundle_version = line.split(":")[1].strip().split(".")[0]
#         break
#
# if bundle_version:
#     print("Bundle-Version:", bundle_version)
# else:
#     print("Bundle-Version not found in the manifest file.")






i = 1 # Change this to your desired increment value

# Read the manifest file
with open("C:\\interview\\MANIFEST.MF", "r") as p1:
    manifest_content = p1.readlines()

# Find and extract the current version number
bundle_version = None
for index, line in enumerate(manifest_content):
    if line.startswith("Bundle-Version:"):
        old_version = line.split(":")[1].strip()
        # bundle_version = old_version.split(".")[0]
        # new_version = str(int(bundle_version) + i)

        new_version = str(int(old_version.split(".")[0]) + i)
        # Replace the old version number with the new one in the manifest content
        manifest_content[index] = line.replace(bundle_version, new_version)
        break

if bundle_version:
    print("Old Bundle-Version:", old_version)
    print("New Bundle-Version:", new_version)
else:
    print("Bundle-Version not found in the manifest file.")

# Write the updated content back to the manifest file
with open("C:\\interview\\MANIFEST.MF", "w") as p1:
    p1.writelines(manifest_content)












