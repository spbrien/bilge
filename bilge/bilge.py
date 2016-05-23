#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob

import click

DESKTOP_DIR = os.path.join(os.path.expanduser('~'), 'Documents/_Desktop')
DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Documents/_Downloads')


@click.group()
def cli():
    """
    Bilge command line tool for the good america
    """
    pass


@cli.command()
@click.argument('category', default=None)
def info(category):
    """
    Find out some info about items cleared from desktop or downloads
    """
    click.echo(click.style("\n[+] Checking directories...\n", fg="white", bold="true"))
    sort_plan = {
        'DMG Files': glob.glob(os.path.join(DESKTOP_DIR, '*/*.dmg')),
        'ISO Files': glob.glob(os.path.join(DESKTOP_DIR, '*/*.iso')),
        'PDF Files': glob.glob(os.path.join(DESKTOP_DIR, '*/*.pdf')),
        'Zip Files': glob.glob(os.path.join(DESKTOP_DIR, '*/*.zip')),
        'SQL Files': glob.glob(os.path.join(DESKTOP_DIR, '*/*.sql')),
        'JSON Files': glob.glob(os.path.join(DESKTOP_DIR, '*/*.json')),
        'Image files': [
            x for x in [
                x for y in [
                    glob.glob(os.path.join(DESKTOP_DIR, pattern))
                    for pattern in ('*/*.jpg', '*/*.jpeg', '*/*.gif', '*/*.png', '*/*.svg')
                ] for x in y
            ] if "Screen Shot" not in x
        ],
        'Adobe Files': [
            x for y in [
                glob.glob(os.path.join(DESKTOP_DIR, pattern))
                for pattern in ('*/*.psd', '*/*.ai', '*/*.indb', '*/*.xd')
            ] for x in y
        ],
        'Screen Shots': [x for x in glob.iglob(os.path.join(DESKTOP_DIR, '*/*')) if "Screen Shot" in x],
        'Directories': [x for x in glob.glob(os.path.join(DESKTOP_DIR, '*/*')) if os.path.isdir(x)]
    }

    sorted_files = [x for y in [value for key, value in sort_plan.iteritems()] for x in y]
    unsorted_files = [item for item in glob.glob(os.path.join(DESKTOP_DIR, '*/*')) if item not in sorted_files]

    sort_plan['Unsorted Files'] = unsorted_files

    if category:
        click.echo(click.style("\n%s\n" % category, fg="cyan", bold=True))
        for item in sort_plan[category]:
            click.echo(click.style(" - %s" % item, fg="white"))
    else:
        for key, value in sort_plan.iteritems():
            click.echo(click.style("\n%s\n" % key, fg="cyan", bold=True))
            for item in value:
                click.echo(click.style(" - %s" % item, fg="white"))
