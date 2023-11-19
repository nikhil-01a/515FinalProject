import json
import sys
import argparse


def gron(json_data, parent='json', is_root=True):
    output = []
    if is_root:
        output.append(f'{parent} = {{}};')  # Start with an empty object

    if isinstance(json_data, dict):
        for key in sorted(json_data.keys()):  # Sort keys alphabetically
            value = json_data[key]
            path = f"{parent}.{key}"
            if isinstance(value, dict):
                output.append(f'{path} = {{}};')  # Declare a dictionary
                output.extend(gron(value, path, False))
            elif isinstance(value, list):
                output.append(f'{path} = [];')  # Declare a list
                for i, item in enumerate(value):
                    item_path = f"{path}[{i}]"
                    # Declare each item in the list
                    output.append(f'{item_path} = {{}};')
                    output.extend(gron(item, item_path, False))
            else:
                # Assign simple values
                output.append(f'{path} = {json.dumps(value)};')

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Flatten JSON object into individual assignments.')
    parser.add_argument('filename', nargs='?', type=argparse.FileType(
        'r'), default=sys.stdin, help='JSON file to read (stdin if not provided)')
    args = parser.parse_args()

    try:
        json_data = json.load(args.filename)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
        sys.exit(1)

    gron_output = gron(json_data)
    print('\n'.join(gron_output))

    args.filename.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
