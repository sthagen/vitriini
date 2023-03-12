""""Showcase (Finnish: vitriini) some packaged content - guided by conventions - application programming interface."""
import argparse
import pathlib
import re
import sys
from typing import List, Union, no_type_check

import msgspec
from vitriini import (
    APP_NAME,
    APP_VERSION,
    COMMA,
    ENCODING,
    LOG_SEPARATOR,
    QUIET,
    TS_FORMAT_PAYLOADS,
    parse_csl_as_is,
    log,
)


@no_type_check
def load(path):
    """Load the data from the path to the file or fail miserably."""
    with open(path, 'rt', encoding=ENCODING) as handle:
        return msgspec.json.decode(handle.read())


@no_type_check
def dump(data, path):
    """Dump the data formatted to the file given by the path."""
    with open(path, 'wt', encoding=ENCODING) as f:
        f.write(msgspec.json.format(msgspec.json.encode(data)).decode())


@no_type_check
def process(options: argparse.Namespace):
    """Process the command line request."""
    if options:
        return 0
    return 0
