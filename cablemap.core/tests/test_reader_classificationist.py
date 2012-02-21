# -*- coding: utf-8 -*-
#
# Copyright (c) 2011 - 2012 -- Lars Heuer <heuer[at]semagia.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
#     * Neither the project name nor the names of the contributors may be 
#       used to endorse or promote products derived from this software 
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
"""\
Tests classificationist parsing.

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - <http://www.semagia.com/>
:license:      BSD license
"""
from nose.tools import eq_
from cablemap.core.reader import parse_classificationist

_TEST_DATA = (
    (u'10TOKYO397', u'Marc Wall', u'''FIELD

REF: STATE 015541

Classified By: Acting Deputy Chief of Mission Marc Wall for Reasons 1.4
 (b) and (d)

¶1. (C) SUM'''),
    (u'10GENEVA249', u'Rose E. Gottemoeller', u'''REF: 10 GENEVA 231 (SFO-GVA-VIII-088) CLASSIFIED BY: Rose E. Gottemoeller, Assistant Secretary, Department of State, VCI; REASON: 1.4(B), (D) '''),
    (u'10GENEVA247', u'Rose E. Gottemoeller', u'''REF: 10 GENEVA 245 (SFO-GVA-VIII-086) CLASSIFIED BY: Rose E. Gottemoeller, Assistant Secretary, Department of State, VCI; REASON: 1.4(B), (D) ¶1. (U) This '''),
    (u'10UNVIEVIENNA77', u'Glyn T. Davies', u'''Classified By: Ambassador Glyn T. Davies for reasons 1.4 b and d '''),
    (u'10WARSAW117', u'F. Daniel Sainz', u'''Classified By: Political Counselor F. Daniel Sainz for Reasons 1.4 (b) and (d) '''),
    (u'10STATE16019', u'Karin L. Look', u'''Classified By: Karin L. Look, Acting ASSISTANT SECRETARY, VCI. Reason: 1.4 (b) and (d).'''),
    (u'10LILONGWE59', u'Bodde Peter', u'''CLASSIFIED BY: Bodde Peter, Ambassador; REASON: 1.4(B) '''),
    (u'95ZAGREB4339', u'ROBERT P. FINN', u'''
1.  (U)  CLASSIFIED BY ROBERT P. FINN, DEPUTY CHIEF OF
MISSION.  REASON: 1.5 (D)
 '''),
    (u'95DAMASCUS5748', u'CHRISTOPHER W.S. ROSS', u'''SUBJECT:  HAFIZ AL-ASAD: LAST DEFENDER OF ARABS

1. CONFIDENTIAL - ENTIRE TEXT.  CLASSIFIED BY:
CHRISTOPHER W.S. ROSS, AMBASSADOR.  REASON: 1.5 (D) .

2. SUMMAR'''),
    (u'95TELAVIV17504', None, u'''
1.  CONFIDENTIAL - ENTIRE TEXT.  CLASSIFIED BY SECTION 1.5 (B)
AND (D).  NIACT PRECEDENCE BECAUSE OF GOVERNMENT CRISIS IN
ISRAEL.

2.  SU'''),
    (u'95RIYADH5221', u'THEODORE KATTOUF', u'''
1.  CONFIDENTIAL - ENTIRE TEXT.  CLASSIFIED BY DCM
THEODORE KATTOUF - 1.5 B,D.

2.  (C)'''),
    (u'96ADDISABABA1545', u'JEFFREY JACOBS', u'''
1.  (U)  CLASSIFIED BY POLOFF JEFFREY JACOBS, 1.5 (D).

2.  (C)'''),
    (u'96AMMAN2094', u'ROBERT BEECROFT', u'''
1. (U)  CLASSIFIED BY CHARGE ROBERT BEECROFT; REASON 1.5 (D).

2. (C) '''),
    (u'96STATE86789', u'MARY BETH LEONARD', u'''
1.  CLASSIFIED BY AF/C - MARY BETH LEONARD, REASON 1.5
(D). '''),
    (u'96NAIROBI6573', u'TIMOTHY CARNEY', u'''
1.  CLASSIFIED BY AMBASSADOR TO SUDAN TIMOTHY CARNEY.
REASON 1.5(D).
 '''),
    (u'96RIYADH2406', u'THEODORE KATTOUF', u'''SUBJECT:  CROWN PRINCE ABDULLAH THE DIPLOMAT

1.  (U) CLASSIFIED BY CDA THEODORE KATTOUF, REASON 1.5.D.

2. '''),
    (u'96RIYADH2696', u'THEODORE KATTOUF', u'''
1.  (U)  CLASSIFIED BY CHARGE D'AFFAIRES THEODORE
KATTOUF: 1.5 B, D.
 '''),
    (u'96ISLAMABAD5972', u'THOMAS W. SIMONS, JR.', u'''
1.  (U) CLASSIFIED BY THOMAS W. SIMONS, JR., AMBASSADOR.
REASON:  1.5 (B), (C) AND (D).
 '''),
    (u'96ISLAMABAD5972', u'Thomas W. Simons, Jr.', u'''
1.  (U) CLASSIFIED BY THOMAS W. SIMONS, JR., AMBASSADOR.
REASON:  1.5 (B), (C) AND (D).
 ''', True),
)


def test_parse_classificationist():
    def check(cable_id, expected, content, normalize):
        eq_(expected, parse_classificationist(content, normalize))
    for testcase in _TEST_DATA:
        if len(testcase) == 3:
            cable_id, expected, content = testcase
            normalize = False
        else:
            cable_id, expected, content, normalize = testcase
        yield check, cable_id, expected, content, normalize


if __name__ == '__main__':
    import nose
    nose.core.runmodule()
