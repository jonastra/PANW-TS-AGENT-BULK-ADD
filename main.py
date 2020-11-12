#!/usr/bin/env python3

# Author: Jonas trand (jstrand@paloaltonetworks.com)
# Version 0.2

import argparse
import re

# ARGUMENTS
parser = argparse.ArgumentParser()
parser.add_argument('-filename', help='Filename to write configuration')
parser.add_argument('-host', help='Hostname to increment')
parser.add_argument('-vsys', help="Virtual System Name")


args = parser.parse_args()

# GLOBALS
CONFIG = []


def generate_terminal_hosts():
    count = 0
    with open(args.filename, 'w', encoding='utf-8') as file:
        host = re.split('-|\.|\n', args.host)
        inc = int(host[2])

        while (count < 102):
            inc_zero = str("{:02d}".format(inc))
            fqdn = '%s-%s-%s.%s.%s' % (host[0],
                                       host[1], inc_zero, host[3], host[4])
            name = '%s-%s-%s' % (host[0], host[1], inc_zero,)
            if (args.vsys):
                cmd = 'set vsys %s ts-agent %s host %s port 5009' % (
                    args.vsys, name, fqdn)
            else:
                cmd = 'set ts-agent %s host %s port 5009' % (name, fqdn)
            CONFIG.append(cmd)
            count += 1
            inc += 1

        CONFIG.append('exit')
        CONFIG.append('set cli scripting-mode off')
        CONFIG.append('commit')

        for cmd in CONFIG:
            file.write(cmd + '\n')


def generate_base_config():
    CONFIG.append(
        "\n! Press enter even if you don't see the rest of the commands in console after pasting !\n")
    CONFIG.append('set cli scripting-mode on')
    CONFIG.append('configure')


def main():
    generate_base_config()
    generate_terminal_hosts()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('[INFO] User aborted.')
