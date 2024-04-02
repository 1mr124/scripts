#!/bin/bash

# Loop through each directory in the current directory
for dir in */; do
    # Check if the directory is a Git repository
    if [ -d "$dir/.git" ]; then
        echo "Entering $dir"
        # Change directory to the Git repository
        cd "$dir" || continue
        # Add all changes to the staging area
        git add .
        # Commit the changes
        git commit -m "Automated commit"
        # Perform git push
        echo "Pushing changes in $dir"
        git push
        # Change directory back to the parent directory
        cd - >/dev/null || exit
    else
        echo "$dir is not a Git repository"
    fi
done
