"""Showcase (Finnish: vitriini) some packaged content - guided by conventions - command line interface."""
import argparse
import json
import pathlib
import re
import sys
from typing import List, no_type_check

import vitriini.api as api
from vitriini import (
    APP_NAME,
    APP_VERSION,
    ENCODING,
    LOG_SEPARATOR,
    QUIET,
    TS_FORMAT_PAYLOADS,
    log,
)


@no_type_check
def parser():
    """Implementation of command line API returning parser."""
    impl = argparse.ArgumentParser(
        description='Showcase (Finnish: vitriini) some packaged content - guided by conventions.'
    )
    return impl


@no_type_check
def app(argv=None):
    """Drive the transformation."""
    argv = sys.argv[1:] if argv is None else argv
    options = parser().parse_args(argv)
    return api.process(options)


if __name__ == '__main__':
    sys.exit(app(sys.argv[1:]))
