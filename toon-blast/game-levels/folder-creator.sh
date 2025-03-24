#!/bin/bash

# Define the base directory
base_dir_royal="/Users/ilkeryoru/Desktop/PERSONAL REPOS/dream-case/royal-match/game-levels"
base_dir_toon="/Users/ilkeryoru/Desktop/PERSONAL REPOS/dream-case/toon-blast/game-levels"

base_dir=$base_dir_toon

# Check if the base directory exists
if [ ! -d "$base_dir" ]; then
    echo "Error: Base directory '$base_dir' does not exist."
    exit 1
fi

# Loop to create directories
for i in $(seq 1 40); do
    dir_name="level-$i"
    dir_path="$base_dir/$dir_name"

    # Check if the directory already exists
    if [ ! -d "$dir_path" ]; then
        mkdir -p "$dir_path"
        if [ $? -eq 0 ]; then
            echo "Created directory: $dir_path"
        else
            echo "Error creating directory: $dir_path"
        fi
    else
        echo "Directory already exists: $dir_path"
    fi
done

echo "Script finished."
