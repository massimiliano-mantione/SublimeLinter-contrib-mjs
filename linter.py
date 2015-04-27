#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Massimiliano Mantione,,,
# Copyright (c) 2015 Massimiliano Mantione,,,
#
# License: MIT
#

"""This module exports the Mjs plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Mjs(NodeLinter):

    """Provides an interface to mjs."""

    syntax = 'metascript'
    cmd = 'mjs check @'
    executable = 'mjs'
    # version_args = '--version'
    # version_re = r'(?P<version>\d+\.\d+\.\d+)'
    # version_requirement = '>= 0.0.0'
    version_args = None
    version_re = None
    version_requirement = None
    regex = r'^(?P<file>.+?)\((?P<line>\d+)(,(?P<col>\d+))?\):\s(?P<message>.+)'
    multiline = False
    line_col_base = (1, 0)
    tempfile_suffix = '-'
    error_stream = util.STREAM_STDOUT
    selectors = {}
    word_re = r'([^\s]+)'
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*;.*'
