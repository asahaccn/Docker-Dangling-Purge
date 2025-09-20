#Shell-version


#!/bin/bash

echo "Finding dangling Docker images..."
#finds all "dangling" Docker images and assigns their image IDs to the shell variable dangling_images
dangling_images=$(docker images -f "dangling=true" -q)
# -q: This is the "quiet" option, which suppresses all output except for the image IDs themselves

# Executing if-else block 
if [ -z "$dangling_images" ]; then
# If images not found print below
    echo "✅ No dangling images found." 
else
    echo "🗑️ Removing dangling images..."
    # remove dangling images with $dangling_images with $dangling_images having the image id for all dangling images
    docker rmi $dangling_images  
    echo "✅ Dangling images removed."
fi




