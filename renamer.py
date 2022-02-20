from pathlib import Path

from cmd_tools import rename_file

def parse_boolean(value):
    value = value.lower()
    
    if value in ["true", "yes", "y", "1", "t"]:
        return True
    elif value in ["false", "no", "n", "0", "f"]:
        return False
        
    return False
    
def main(src_file, new_name, is_copy, counter):
    src_path = Path(src_file)
    rename_file(src_path, new_name, is_copy, counter)
    
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('src_file')
    parser.add_argument('new_name')
    parser.add_argument(
        'is_copy', 
        type = parse_boolean, 
        default = False
    )
    parser.add_argument(
        'counter', 
        type = int, 
        default = 1
    )
    
    args = parser.parse_args()
    
    main(args.src_file, args.new_name, args.is_copy, args.counter)