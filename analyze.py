import argparse
import yt_dlp

parser = argparse.ArgumentParser()
parser.add_argument('--url', help="Input video url")
args = parser.parse_args()

print(args.url)