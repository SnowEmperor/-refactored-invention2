import glob
import json
import os.path
import argparse


def path_dump(scan, fil):
    q = {}
    pathdir = os.path.join("\\", os.path.join("**", os.path.join(scan, "*.lnk")))
    for file in glob.glob(pathdir, recursive=True):
        name = os.path.basename(file)
        path = os.path.abspath(file)
        q[name] = path
    with open(fil, 'a') as file_1:
        json.dump(q, file_1, indent=1)
    return q





if __name__ == "__main__":
    path_dump(args.scan_file, args.name_file)
