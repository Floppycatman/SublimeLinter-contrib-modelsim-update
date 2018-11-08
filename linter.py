from SublimeLinter.lint import Linter, util
import sublime
import sublime_plugin
import SublimeLinter.lint


def get_SL_version():
    """
    Return the major version number of SublimeLinter.
    """
    return getattr(SublimeLinter.lint, 'VERSION', 3)


###############################################################################
# vcom
###############################################################################
class vcom(Linter):
    # Arguments can be passed in a linter settings file:
    # http://www.sublimelinter.com/en/stable/linter_settings.html#args
    # E.g.:
    # "linters": {
    #   "vcom": {
    #     "args": ["-check_synthesis", "-2002"],
    #     "working_dir": "d:/tmp/tst/vhdl",
    # },
    #
    # Alternately, project specific arguments can be set in a project file:
    # http://www.sublimelinter.com/en/stable/settings.html#project-settings
    # E.g.:
    # "settings":
    # {
    #   // SublimeLinter-contrib-vcom
    #   "SublimeLinter.linters.vcom.args": ["-check_synthesis", "-2002"],
    #   "SublimeLinter.linters.vcom.working_dir": "d:/tmp/tst/vhdl",
    # },
    #
    cmd = ('vcom', '${args}', '${temp_file}')
    multiline = False
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'vhd'

    if get_SL_version() == 3:
        syntax = ('vhdl')
    else:
        on_stderr = None  # handle stderr via split_match
        defaults = {
            'selector': 'source.vhdl',
        }

    # http://www.sublimelinter.com/en/stable/linter_attributes.html#regex-mandatory
    # Modified regex:
    # 1) Since ModelSim doesn't provide the 'Col' information, we utilize the
    # <near> field, when possible (i.e. use a "quoted text" to derive <near>
    # field position)
    # 2) Note that <code> field isn't used (it can be, but it doesn't really
    # serve any meaningful purpose)
    # 3) Suppress message "** Error: file(line): VHDL Compiler exiting"
    # at the end of any file with errors
    # regex = (
    #     r'\*\* ((?P<error>Error)|(?P<warning>Warning)): '
    #     r'(?P<file>.*)'
    #     r'\((?P<line>\d+)\): '
    #     r'(VHDL Compiler exiting)?'
    #     r'(?P<message>([^"]*\"(?P<near>[^"]+)\")?.*)'
    # )

    regex = (
        r'\*\* ((?P<error>Error( \(suppressible\))?)|(?P<warning>Warning)): '
        r'(?P<file>.*)'
        r'\((?P<line>\d+)\): '
        r'(VHDL Compiler exiting)?'
        r'(\*\* ((Error( \(suppressible\))?)|(Warning)): )?'
        r'(?P<message>((\((?P<code>vcom-\d+)\) )?[^"\'\n]*(?P<quote>["\'])(?P<near>[^"\']+)(?P=quote))?.*)'
    )


class SublimeLinterVcomRunTests(sublime_plugin.WindowCommand):
    """
    To do unittests, run the following command in ST's console:
    window.run_command('sublime_linter_vcom_run_tests')
    """

    def run(self):
        from .tests.vcom_regex_tests import run_tests
        run_tests(vcom.regex)


###############################################################################
# vlog
###############################################################################
class vlog(Linter):
    # refer to description in vcom
    cmd = ('vlog', '${args}', '${temp_file}')
    multiline = False
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'v'

    if get_SL_version() == 3:
        syntax = ('verilog', 'systemverilog')
    else:
        on_stderr = None  # handle stderr via split_match
        defaults = {
            'selector': "source.verilog, source.systemverilog",
        }

    # http://www.sublimelinter.com/en/stable/linter_attributes.html#regex-mandatory
    # Modified regex:
    # 1) Since ModelSim doesn't provide the 'Col' information, we utilize the
    # <near> field, when possible (i.e. use a single/double quoted text
    # to derive <near> field position)
    # 2) Note that <code> field isn't used (it can be, but it doesn't really
    # serve any meaningful purpose)
    regex = (
        r'\*\* ((?P<error>Error)|(?P<warning>Warning)): '
        r'(\(vlog-\d+\) )?'
        r'(?P<file>.*)'
        r'\((?P<line>\d+)\): '
        r'(?P<message>([^"\'\n]*(?P<quote>["\'])(?P<near>[^"\']+)(?P=quote))?.*)'
    )


class SublimeLinterVlogRunTests(sublime_plugin.WindowCommand):
    """
    To do unittests, run the following command in ST's console:
    window.run_command('sublime_linter_vlog_run_tests')
    """

    def run(self):
        from .tests.vlog_regex_tests import run_tests
        run_tests(vlog.regex)
