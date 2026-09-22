#!/bin/bash

mkdir -p outputs

for file in /data/Twitter\ dataset/geoTwitter20-*.zip
do
    nohup python3 src/map.py --input_path "$file" > "outputs/$(basename "$file").log" 2>&1 &
done
