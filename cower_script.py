#! /usr/bin/python3

''' Script to install packages from AUR downloaded via cower

Copyright 2017, Victor Otieno
Licensed under MIT license'''

import os

build_directory = '~/builds'
build_directory = os.path.expanduser(build_directory)
cower_command = 'cower -vdu'


def print_info(string):
    print('[-] ' + string)


def print_error(string):
    print('[X] ' + string)


def get_input(string):
    return input(string)


def install(packages):
    packages = sorted(packages)
    if not packages:
        print_info('No packages to install.')
    else:
        print_info('Installing packages...')
        for package in packages:
            os.chdir(package)
            os.system('makepkg -sri')
            os.chdir('..')
            os.system('rm -r {}'.format(package))
        print_info('Done. \n')


def main():
    os.chdir(build_directory)

    for paths, directories, files in os.walk('.'):
        if directories:
            print_info('Found existing packages:')
            response = get_input(
                'Do you want to install these packages: Y or N \n')

            if response.lower() == 'y':
                install(directories)

            else:
                print_info('Deleting existing packages...')
                for directory in directories:
                    os.system('rm -r {}'.format(directory))
                print_info('Done. \n')

    print_info('Checking for updates:')
    os.system(cower_command)
    print_info('Done. \n')

    packages = os.listdir()
    install(packages)


if __name__ == '__main__':
    main()
