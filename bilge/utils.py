#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob

DESKTOP_DIR = os.path.join(os.path.expanduser('~'), 'Documents/_Desktop')
DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Documents/_Downloads')
BILGE_DIR = os.path.join(os.path.expanduser('~'), 'Documents/_Bilge')


def create_glob(patterns):
    if type(patterns) == list:
        desktop = [
            x for x in [
                x for y in [
                    glob.glob(os.path.join(DESKTOP_DIR, pattern))
                    for pattern in patterns
                ] for x in y
            ]
        ]
        downloads = [
            x for x in [
                x for y in [
                    glob.glob(os.path.join(DOWNLOADS_DIR, pattern))
                    for pattern in patterns
                ] for x in y
            ]
        ]
        return desktop + downloads
    else:
        return glob.glob(os.path.join(DESKTOP_DIR, patterns)) + glob.glob(os.path.join(DOWNLOADS_DIR, patterns))


def add_unsorted(dictionary):
    sorted_files = [x for y in [value for key, value in dictionary.iteritems()] for x in y]
    all_files = glob.glob(os.path.join(DESKTOP_DIR, '*/*')) + glob.glob(os.path.join(DOWNLOADS_DIR, '*/*'))
    return [item for item in all_files if item not in sorted_files]


def create_sort_plan():
    sort_plan = {
        'DMG Files': create_glob('*/*.dmg'),
        'ISO Files': create_glob('*/*.iso'),
        'PDF Files': create_glob('*/*.pdf'),
        'Zip Files': create_glob('*/*.zip'),
        'SQL Files': create_glob('*/*.sql'),
        'JSON Files': create_glob('*/*.json'),
        'Image files': [x for x in create_glob(['*/*.jpg', '*/*.jpeg', '*/*.gif', '*/*.png', '*/*.svg']) if 'Screen Shot' not in x],
        'Adobe Files': create_glob(['*/*.psd', '*/*.ai', '*/*.indb', '*/*.xd']),
        'Screen Shots': [x for x in create_glob('*/*') if "Screen Shot" in x],
        'Directories': [x for x in create_glob('*/*') if os.path.isdir(x)]
    }

    sort_plan['Unsorted Files'] = add_unsorted(sort_plan)
    return sort_plan
