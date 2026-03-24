#!/bin/bash

# Cleanup temporary and cache files in a directory

TARGET_DIR="."

find $TARGET_DIR -type f \( -name '*.tmp' -o -name '*.cache' -o -name '*.bak' -o -name '*~' \) -delete

# Optional: Remove empty directories
find $TARGET_DIR -type d -empty -delete

echo "Temporary files cleaned up in $TARGET_DIR"
