import SublimeLinter
from SublimeLinter.lint import Linter


class Vcom(Linter):
    cmd = ('vcom', '-2008', '-lint', '-check_synthesis', '${file}', '${args}')
    error_stream = SublimeLinter.lint.STREAM_STDOUT
    regex = (
        r'.*'
        r'^\*\* ((?P<error>Error)|(?P<warning>Warning)): '
        r'.*(?P<file>\w+\.vhd)'
        r'\((?P<line>\d+)\): '
        r'(near "(?P<near>.+)": )?'
        r'\((?P<code>vcom-\d+)\)?'
        r'(?P<message>.*)'
    )
    multiline = True
    defaults = {
        'selector': 'source.vhdl'
    }
