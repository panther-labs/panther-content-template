"""Convert Classic Panther Detections Repository

Usage:
    convert_classic_repo.py <path-to-classic-repo> [--dry-run]

Options:
    -h --help   Show this screen.
    --dry-run   Do a dry run to simulate what would change.

"""
import ast
import glob
import logging
import os

import black
from docopt import docopt


# _TEMP_DIR = convert_classic_repo


def find_yaml_files(path: str) -> list[str]:
    # TODO handle absolute path to classic repo

    file_pattern = f'{os.getcwd()}{os.sep}{path}{os.sep}**{os.sep}*.yml'
    return glob.glob(file_pattern, recursive=True)


def convert_yaml_files(path: str, files: list[str], dry_run: bool = True) -> list[str]:
    out_files: list[str] = []

    files = files[:5]
    for file in files:
        path_split = file.split(path)
        cwd = path_split[0].strip(os.sep)
        old_loc = path_split[1].strip(os.sep)
        old_loc_split = old_loc.split(os.sep)

        out_file_dir = os.sep.join([cwd, *old_loc_split[:-1]])
        out_file = os.sep.join([out_file_dir, old_loc_split[-1]]).replace('.yml', '.py')

        if not dry_run:
            os.makedirs(out_file_dir, exist_ok=True)
            code = os.system(f'panther_classic_converter {file} -o {out_file}')
            if code != 0:
                logging.error(f'got error running cmd: "panther_classic_converter {file} -o {out_file}"')
            else:
                out_files.append(out_file)
        else:
            out_files.append(out_file)

    return out_files


def check_for_content_dir(panther_content_loc: str) -> None:
    if not os.path.exists(panther_content_loc):
        logging.error(f'panther content main was not found at expected location: {panther_content_loc}')
        exit(1)


def add_files_to_main(panther_content_loc: str, files: list[str], dry_run: bool = True) -> None:
    with open(panther_content_loc, mode='r') as main_file:
        imports: list[ast.AST] = []
        uses: list[ast.AST] = []

        tree = ast.parse(main_file.read())
        for file in files:
            file_split = file.replace(os.getcwd().strip(os.sep), '').strip(os.sep).split(os.sep)
            file_name = file_split[-1].replace('.py', '')
            file_path = '.'.join(file_split[:-1])

            import_stmt = ast.parse(f'from .{file_path} import {file_name}')
            use_stmt = ast.parse(f'{file_name}.use()')

            imports.append(import_stmt)
            uses.append(use_stmt)

        tree.body = imports + tree.body
        tree.body = tree.body + uses
        program = black.format_str(ast.unparse(tree), mode=black.FileMode())

    if not dry_run:
        with open(panther_content_loc, mode='w') as main_file:
            main_file.write(program)
    else:
        print(program)


def run(args: dict[str, any]) -> None:
    path = args.get('<path-to-classic-repo>')
    dry_run = True if args.get('--dry-run') else False
    panther_content_loc = f'panther_content{os.sep}__main__.py'

    files = find_yaml_files(path)
    check_for_content_dir(panther_content_loc)
    out_files = convert_yaml_files(path, files, dry_run)
    add_files_to_main(panther_content_loc, out_files, dry_run)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Convert Classic Repo 0.0.1')
    run(arguments)
