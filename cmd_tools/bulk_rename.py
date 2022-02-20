__all__ = [
'bulk_rename_files',
'rename_file',
]

import logging
import shutil
import sys
import os
import argparse
from pathlib import Path 

# Logger configuration to show date, time, log level, module name, line number, and message
LOG_FMT_STRING = (
    '[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s'
)
logging.basicConfig(level=logging.INFO, format=LOG_FMT_STRING)
log = logging.getLogger(__name__)

def parse_boolean(value):
    value = value.lower()

    if value in ["true", "yes", "y", "1", "t"]:
        return True
    elif value in ["false", "no", "n", "0", "f"]:
        return False

    return False


def copy(file, counter):
    copy_name = f'{file.stem}{counter}{file.suffix}'
    copy_fpath = file.parent.joinpath(copy_name)
    shutil.copy(file, copy_fpath)
    log.info(f'Copied {file.name} ---> {copy_fpath.name}')

def move(file, prefix, counter):
    new_fname = f'{prefix}{counter}{file.suffix}'
    new_fpath = file.parent.joinpath(new_fname)     
    shutil.move(file, new_fpath)
    log.info(f'Renamed {file.name} ---> {new_fpath.name}')

def rename_file(file, prefix, is_copy, counter):
    if is_copy:
        copy(file, counter)
        
    else:
        move(file, prefix, counter)

def bulk_rename_files(prefix, regex, target_dir, is_copy):
    log.info('[START] : Renaming/copying files')
    counter = 1
    target_dir = Path(target_dir)
    files = target_dir.glob(regex)
    if not target_dir.is_dir():
        log.error(f'{target_dir} does not exist or is not a directory.')
        return False, None
    
    for file in files:
        log.info(f'Found {file}')
        rename_file(file, prefix, is_copy, counter)
        counter += 1
        print(file)
        
    return True, counter

def main(args):
    try:
        is_success, counter = bulk_rename(args.new_name, args.file_pattern, args.target_dir, args.copy)
        
        if is_success:
            log.info(f'[SUCCESS] : {counter-1} Files are copied/renamed')
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
    	log.error(f'Exception: {e}')
    	sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        'new_name',
        metavar='NEW_FNAME',
        help='The file name pattern which will be used to rename the target files'
    )
    
    parser.add_argument(
        'file_pattern',
        metavar = 'REGEX_PATTERN',
        help = 'The regex that will be used to filter for files in the target directory'
    )
    
    parser.add_argument(
        'target_dir',
        metavar = 'TARGET_DIR',
        help ='The directory where the files to be renamed reside'
    )

    parser.add_argument(
        '-C', '--copy',
        help = 'Copy files instead of renaming',
        type = parse_boolean,
        default = False
    )

    args = parser.parse_args()

    main(args)