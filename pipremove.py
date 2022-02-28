#!/bin/python3

import argparse
import os
from collections import deque
import pip._internal.commands.show as show


def main():
    parser = argparse.ArgumentParser(description='卸载pip包，并卸载其依赖包')
    parser.add_argument('package', help='要卸载的包',)
    args = parser.parse_args()

    pkgs = deque()
    try:
        pkgs.append(next(show.search_packages_info([args.package]))['name'])
    except StopIteration:
        return
    uninstalled = set()

    while pkgs:
        pkg = pkgs.popleft()
        pkg_info = next(show.search_packages_info([pkg]))
        os.system('pip uninstall ' + pkg)
        uninstalled.add(pkg)
        for depency_info in show.search_packages_info(pkg_info['requires']):
            if not set(depency_info['required_by']) - uninstalled:
                pkgs.append(depency_info['name'])


if __name__ == '__main__':
    main()
