#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

from utils import create_sort_plan


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
        click.echo(click.style("\n%s\n" % category, fg="cyan", bold=True))
        for item in sort_plan[category]:
            click.echo(click.style(" - %s" % item, fg="white"))
    else:
        for key, value in sort_plan.iteritems():
            click.echo(click.style("\n%s\n" % key, fg="cyan", bold=True))
            for item in value:
                click.echo(click.style(" - %s" % item, fg="white"))
