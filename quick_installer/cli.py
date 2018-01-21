"""
Quick Install

Usage:
  quickall <command>
  quickall (-h | --help)
  quickall (-V | --version)

Options:
  -h --help      Show this screen.
  -V --version   Show version.

Commands:
  list     Lists available applications
  install  Install an application
  system   Perform a system installation
  remove   Removes a directory
"""
import sys

from docopt import docopt

from quick_installer import commands

command_by_name = {
    'list': commands.list,
}


def main():
    argv = sys.argv[1] if len(sys.argv) > 1 else []
    args = docopt(__doc__, argv, version="Quick Install v0.1")
    command_name = args['<command>']

    try:
        command = command_by_name[command_name]
        command()
    except KeyError:
        print(f"Command '{command_name}' was not recognized, see \"quickall --help\"",
              file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()