#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import time
from random import randint

import click

from utils import create_sort_plan, BILGE_DIR, DESKTOP_DIR, DOWNLOADS_DIR


@click.group()
def cli():
    """
    Bilge command line tool for the good america
    """
    pass


@cli.command()
@click.option('-c', '--category', default=None)
def info(category):
    """
    Find out some info about items cleared from desktop or downloads
    """
    click.echo(click.style("\n[+] Checking directories...\n", fg="white", bold="true"))
    sort_plan = create_sort_plan()

    if category:
        click.echo(click.style("\n%s\n" % category, fg="cyan", bold="true"))
        for item in sort_plan[category]:
            click.echo(click.style(" - %s" % item, fg="white"))
    else:
        for key, value in sort_plan.iteritems():
            click.echo(click.style("\n%s\n" % key, fg="cyan", bold="true"))
            for item in value:
                click.echo(click.style(" - %s" % item, fg="white"))


@cli.command()
def sort():
    """
    Sort items into category folder structure
    """
    click.echo(click.style("\n[+] Sorting files...\n", fg="white", bold="true"))
    sort_plan = create_sort_plan()

    for key, value in sort_plan.iteritems():
        if not os.path.exists(BILGE_DIR):
            os.makedirs(BILGE_DIR)

        sort_dir = os.path.join(BILGE_DIR, key.lower().replace(' ', '_'))
        if not os.path.exists(sort_dir):
            os.makedirs(sort_dir)

        for item in value:
            try:
                shutil.move(item, sort_dir)
            except Exception:
                name = item.rsplit('.', 1)
                disambiguate = '%s_%s.%s' % (name[0], int(time.time()) + randint(0, 9000), name[1]) if len(name) > 1 else '%s_%s' % (name[0], int(time.time()) + randint(0, 9000))

                shutil.move(item, disambiguate)
                shutil.move(disambiguate, sort_dir)

    shutil.rmtree(DESKTOP_DIR)
    shutil.rmtree(DOWNLOADS_DIR)
