import glob
import json
import os.path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('scan_file', type=str)
parser.add_argument('name_file', type=str)
args = parser.parse_args()
q = {}
print(2+2)


def path_dump(scan, fil):
    pathdir = os.path.join("\\", os.path.join("**", os.path.join(scan, "*.lnk")))
    for file in glob.glob(pathdir, recursive=True):
        name = os.path.basename(file)
        path = os.path.abspath(file)
        q[name] = path
    with open(fil, 'a') as file_1:
        json.dump(q, file_1, indent=1)


if __name__ == "__main__":
    path_dump(args.scan_file, args.name_file)
