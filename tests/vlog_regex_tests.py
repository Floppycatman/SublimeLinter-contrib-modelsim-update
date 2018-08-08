import re
import unittest
from collections import namedtuple


class VlogRegexTests(unittest.TestCase):
    regex = None

    def test_cases(self):
        for case in _cases:
            match_list = [
                match_tuple(**m.groupdict())
                for m in re.finditer(self.regex, case.output)
            ]

            self.assertListEqual(
                case.matches, match_list,
                "matches not as expected for case {}".format(case.name))


def run_tests(regex):
    VlogRegexTests.regex = regex
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(VlogRegexTests)
    unittest.TextTestRunner().run(suite)


case_tuple = namedtuple(
    "case_tuple",
    ("name", "output", "matches"))


match_tuple = namedtuple(
    "match_tuple",(
    "error", "warning", "file", "line", "message", "near", "quote"))


_cases = []
_cases.append(case_tuple(
    name="message type name 1",
    output="""
** Error: up_counter.v(25): (vlog-2730) Undefined variable: 'reset'.
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="up_counter.v",
        line='25',
        message="(vlog-2730) Undefined variable: 'reset'.",
        near="reset",
        quote="'",
    )]
))

_cases.append(case_tuple(
    name="message type name 2",
    output="""
** Error: (vlog-13069) up_counter.v(27): near "end": syntax error, unexpected end, expecting ';'.
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="up_counter.v",
        line='27',
        message="""near "end": syntax error, unexpected end, expecting ';'.""",
        near="end",
        quote="\"",
    )]
))

_cases.append(case_tuple(
    name="message type name 3",
    output="""
** Error: d:/tmp/tst/up_counter.v(22): (vlog-2730) Undefined variable: 'b'
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="d:/tmp/tst/up_counter.v",
        line='22',
        message="(vlog-2730) Undefined variable: 'b'",
        near="b",
        quote="'",
    )]
))

_cases.append(case_tuple(
    name="message type name 4",
    output="""
** Warning: test.v(15): [RDGN] - Redundant digits in numeric
""",
    matches=[match_tuple(
        error=None,
        warning="Warning",
        file="test.v",
        line='15',
        message="[RDGN] - Redundant digits in numeric",
        near=None,
        quote=None,
    )]
))

_cases.append(case_tuple(
    name="message type name 5",
    output="""
** Warning: altdq_dqs2_acv_arriav_connect_to_hard_phy.sv(199): (vlog-2597) '4294967295' is being treated as 32-bit signed integer and will overflow.
""",
    matches=[match_tuple(
        error=None,
        warning="Warning",
        file="altdq_dqs2_acv_arriav_connect_to_hard_phy.sv",
        line='199',
        message="(vlog-2597) '4294967295' is being treated as 32-bit signed integer and will overflow.",
        near="4294967295",
        quote="'",
    )]
))

_cases.append(case_tuple(
    name="message type name 6",
    output="""
** Error: qsys_hps_ddr_hps_0_hps_io_border.sv(100): (vlog-2730) Undefined variable: 'intermediate'.
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="qsys_hps_ddr_hps_0_hps_io_border.sv",
        line='100',
        message="(vlog-2730) Undefined variable: 'intermediate'.",
        near="intermediate",
        quote="'",
    )]
))
