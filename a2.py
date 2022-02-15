import argparse
from a1 import path_dump

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('scan_file', type=str)
    parser.add_argument('name_file', type=str)
    args = parser.parse_args()
    q = {}
path_dump(args.scan_file, args.name_file)
