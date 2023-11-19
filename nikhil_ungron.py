import sys
import re
import json


def parse_line(line):
    key, value = re.match(r"(.+) = (.+);", line.strip()).groups()
    parts = key.split('.')
    return parts, eval(value)


def construct_json(lines):
    root = {}
    for line in lines:
        parts, value = parse_line(line)
        temp = root
        for i, part in enumerate(parts[:-1]):
            if '[' in part:
                key, index = re.match(r"(.+)\[(\d+)\]", part).groups()
                index = int(index)
                if key not in temp:
                    temp[key] = []
                while len(temp[key]) <= index:
                    temp[key].append({})
                temp = temp[key][index]
            else:
                if part not in temp:
                    temp[part] = {}
                temp = temp[part]
        final_key = parts[-1]
        if '[' in final_key:
            key, index = re.match(r"(.+)\[(\d+)\]", final_key).groups()
            index = int(index)
            if key not in temp:
                temp[key] = []
            while len(temp[key]) <= index:
                temp[key].append({})
            temp[key][index] = value
        else:
            temp[final_key] = value
    # Remove the outermost 'json' key if it exists
    return root.get('json', root)


if __name__ == "__main__":
    if (len(sys.argv)) > 1:
        file_name = sys.argv[1]
        print(file_name)
    else:
        file_name = sys.stdin.readline()
        print(file_name)
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print(json.dumps(construct_json(lines), indent=2))
    except:
        print(f"Error! {file_name} not found!")
