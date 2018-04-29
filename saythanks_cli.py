"""
saythanks-cli
~~~~~~~~~~~~~

Say Thanks via Command Line Interface.

Uses Kenneth's saythanks.io service.

:copyright: by Timo Furrer <tuxtimo@gmail.com>
:license: MIT, See LICENSE for more details.
"""

import os
import sys


import click
import requests

SAYTHANKS_API = 'https://saythanks.io/to/{inbox}/submit'


def submit_note(inbox: str, body: str, byline: str, debug=False) -> bool:
    """
    Submit a new thankful note to the given inbox.

    Args:
        inbox (str): the name of the target inbox.
        body (str): the body of the note to submit.
        byline (str): the name of the sender.
    """
    payload = {
            'body': body,
            'byline': byline
    }
    response = requests.post(SAYTHANKS_API.format(inbox=inbox), data=payload)
    if response.status_code != 200:
        message = 'Failed to say thanks :(\nMaybe you entered the wrong inbox?!'
        if debug:
            message += '\nServer returned:\n{0}'.format(response.text)
        raise click.UsageError(message)


@click.command()
@click.option('--from', '-f', 'from_', default=os.environ.get('USER'),
              help='Here goes your name [Defaults: $USER]')
@click.option('--debug', '-d', is_flag=True, default=False,
              help='Enable debug logs')
@click.argument('inbox')
def cli(from_, inbox, debug):
    """
    Say Thanks to someone on saythanks.io!
    """
    if not sys.stdin.isatty():
        body = click.get_text_stream('stdin').read().strip()
    else:
        body = click.edit()

    submit_note(inbox, body, from_, debug=debug)
    print('Great!')
