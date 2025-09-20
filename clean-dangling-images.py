##Python Version

"""
The provided Python script cleans up "dangling" Docker images from your system using the Docker SDK for Python
. Dangling images are layers that have lost their tag and are no longer associated with a named image or an active container. They can accumulate over time and consume significant disk space. 
How the script works
"""

import docker

client = docker.from_env()
#  This line initializes a connection to the Docker daemon. It reads connection information from your environment variables, which is the standard 
#  way to configure the Docker command-line interface.


dangling = client.images.list(filters={"dangling": True})
#  client.images.list()  lists all the docker images 
# filters={"dangling": True} argument narrows this list to only show dangling images, which are typically listed as <none>:<none> when 
# running the docker images command.
    

if not dangling:
    #  This checks if the list of dangling images is empty.
    print("✅ No dangling images found.") #If it is, the script prints a success message and exits.
else: # If dangling images are found, the script enters this block.
    print(f"🗑️ Removing {len(dangling)} dangling images...")
    # It prints a message indicating the number of images that will be removed.
    for image in dangling: #  The for loop iterates through each dangling image object
        print(f"Removing {image.short_id}") #For each image, it prints the image's short ID and then calls client.images.remove(image.id) to delete it.
        client.images.remove(image.id)
    print("✅ Cleanup complete.") #  Finally, it prints a "Cleanup complete" message. 





