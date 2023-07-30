#!/usr/bin/env python3

import os
import argparse

def list_dirs(startpath, exclude, include_files):
    prefix = 0
    for root, dirs, files_in_dir in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude]
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1)
        if level > prefix:
            prefix = level
        print(f'{indent}├── {os.path.basename(root)}')

        if include_files == 'true':
            file_indent = '│   ' * (level)
            for file in files_in_dir:
                print(f'{file_indent}├── {file}')

def main():
    parser = argparse.ArgumentParser(description="List directories in a tree-like format.")
    parser.add_argument('startpath', help='The root directory from which to list directories.')
    parser.add_argument('-e', '--exclude', nargs='*', default=[], help='A list of directory names to exclude.')
    parser.add_argument('-f', '--files', default='false', help='Include files in the output. Set this to "true" or "false". The default is "false".')
    args = parser.parse_args()
    list_dirs(args.startpath, args.exclude, args.files)

if __name__ == '__main__':
    main()
