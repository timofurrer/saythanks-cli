"""
saythanks-cli
~~~~~~~~~~~~~

Say Thanks via Command Line Interface.

Uses Kenneth's saythanks.io service.

:copyright: by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, See LICENSE for more details.
"""


import click


@click.command()
@click.argument('inbox')
def cli():
    """
    Say Thanks to someone on saythanks.io!
    """
    pass
