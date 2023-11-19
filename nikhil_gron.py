import json
import sys


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
    # If a filename is provided as an argument, read from the file
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            json_data = json.load(file)
    else:
        # Otherwise, read from STDIN
        json_data = json.load(sys.stdin)

    gron_output = gron(json_data)
    print('\n'.join(gron_output))


if __name__ == "__main__":
    main()
