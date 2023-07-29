import os
import argparse

def list_dirs(startpath, exclude):
    prefix = 0
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude]
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level - 1)
        if level > prefix:
            prefix = level
        print(f'{indent}├── {os.path.basename(root)}')

def main():
    parser = argparse.ArgumentParser(description="List directories in a tree-like format.")
    parser.add_argument('startpath', help='The root directory from which to list directories.')
    parser.add_argument('-e', '--exclude', nargs='*', default=[], help='A list of directory names to exclude.')
    args = parser.parse_args()
    list_dirs(args.startpath, args.exclude)

if __name__ == '__main__':
    main()
