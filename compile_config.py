from pathlib import Path
import re

include_pattern = r'^Include (.*)$'


def get_content(filepath, parse_include=True):
    content = ""
    with filepath.open() as fi:
        line = fi.readline()
        while line:
            include_new_file = re.search(include_pattern, line)
            if include_new_file and parse_include:
                filepath_to_include = filepath.parent / Path(include_new_file.group(1)).expanduser().resolve()
                content += get_content(filepath_to_include)
            else:
                content += line
            line = fi.readline()
    return content


def compile_config(config_filepath, config_base_filepath):
    config_filepath = Path(config_filepath).expanduser()
    config_base_filepath = Path(config_base_filepath).expanduser().resolve()

    content = get_content(config_base_filepath)

    config_filepath.write_text(content)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config",
                        default="~/.ssh/config",
                        help="path of the ssh config file to be compiled (default: %(default)s)")
    parser.add_argument("-b", "--config_base",
                        default="~/.ssh/config_base",
                        help="path of the base config file (default: %(default)s)")
    args = parser.parse_args()

    compile_config(config_filepath=args.config,
                   config_base_filepath=args.config_base)
