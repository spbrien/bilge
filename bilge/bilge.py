#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


@click.group()
def cli():
    """
    Bilge command line tool for the good america
    """
    print('Good to go.')
