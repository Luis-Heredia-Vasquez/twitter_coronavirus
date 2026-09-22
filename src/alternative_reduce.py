#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('hashtags', nargs='+')
parser.add_argument('--input_folder', default='outputs')
parser.add_argument('--output_path', default='outputs/alternative_reduce.png')
args = parser.parse_args()

# imports
import os
import re
import json
import glob
import datetime
import matplotlib.pyplot as plt

input_paths = sorted(glob.glob(os.path.join(args.input_folder, 'geoTwitter20-*.zip.lang')))


dates = []
counts_by_hashtag = {hashtag: [] for hashtag in args.hashtags}


for input_path in input_paths:

    match = re.search(r'geoTwitter(\d\d-\d\d-\d\d)\.zip\.lang$', input_path)
    if match is None:
        continue

    date = datetime.datetime.strptime(match.group(1), '%y-%m-%d').date()
    dates.append(date)

    with open(input_path) as f:
        counts = json.load(f)

    for hashtag in args.hashtags:
        total = sum(counts.get(hashtag, {}).values())
        counts_by_hashtag[hashtag].append(total)

plt.figure(figsize=(12, 6))

for hashtag in args.hashtags:
   label = 'korean_coronavirus' if hashtag == '#코로나바이러스' else hashtag
   plt.plot(dates, counts_by_hashtag[hashtag], label=label)

plt.xlabel('Date')
plt.ylabel('Number of tweets')
plt.title('Daily hashtag usage in 2020')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(args.output_path)

print('saved', args.output_path)
