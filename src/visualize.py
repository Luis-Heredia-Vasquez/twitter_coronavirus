#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
parser.add_argument('--output_path', default=None)
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# get top 10 and sort from low to high for plotting
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)
items = items[:10]
items = sorted(items, key=lambda item: (item[1], item[0]))

labels = [k for k, v in items]
values = [v for k, v in items]

# create output path if not provided
if args.output_path is None:
    input_name = os.path.basename(args.input_path).replace('.', '_')
    safe_key = args.key.replace('#', '').replace('/', '_')
    output_path = f'{input_name}_{safe_key}.png'
else:
    output_path = args.output_path

# make the plot
plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.xlabel('Key')
plt.ylabel('Percent' if args.percent else 'Count')
plt.title(os.path.basename(output_path).replace('_', ' ').replace('.png', ''))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(output_path)

print('saved', output_path)
