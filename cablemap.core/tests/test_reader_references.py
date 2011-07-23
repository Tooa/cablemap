# -*- coding: utf-8 -*-
#
# Copyright (c) 2011 -- Lars Heuer <heuer[at]semagia.com>
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
Tests references parsing.

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - <http://www.semagia.com/>
:license:      BSD license
"""
from nose.tools import eq_
from cablemap.core.reader import parse_references

_TEST_DATA = (
    # input string, year, optional reference_id, expected

    # 07TBILISI1732
    ('\nREF: A. TBILISI 1605  B. TBILISI 1352  C. TBILISI 1100  D. 06 TBILISI 2601  E. 06 TBILISI 2590  F. 06 TBILISI 2425  G. 06 TBILISI 2390  H. 06 TBILISI 1532  I. 06 STATE 80908  J. 06 TBILISI 1064  K. 06 TBILISI 0619  L. 06 TBILISI 0397  M. 06 MOSCOW 0546  N. 06 TBILISI 0140  O. 05 TBILISI 3171',
     2007, [u'07TBILISI1605', u'07TBILISI1352', u'07TBILISI1100', u'06TBILISI2601', u'06TBILISI2590', u'06TBILISI2425', u'06TBILISI2390', u'06TBILISI1532', u'06STATE80908', u'06TBILISI1064', u'06TBILISI619', u'06TBILISI397', u'06MOSCOW546', u'06TBILISI140', u'05TBILISI3171']),
    # 08PARIS1698
    ('''
REF: A. PARIS 1501
B. PARIS 1568
C. HOTR WASHINGTON DC//USDAO PARIS (SUBJ: IIR 6 832
0617 08)
D. HOTR WASHINGTON DC//USDAO PARIS (SUBJ: IIR 6 832
0626 08) ''', 2008,
     [u'08PARIS1501', u'08PARIS1568']),
    # 08PARIS1501
    ('\nREF: A. 05 PARIS 5459 \nB. 06 PARIS 5733', 2008,
     [u'05PARIS5459', u'06PARIS5733']),
    # 07TALLINN375
    ('\nREF: A) TALLINN 366 B) LEE-GOLDSTEIN EMAIL 05/11/07 \nB) TALLINN 347 ', 2007,
     [u'07TALLINN366', u'07TALLINN347']),
    # 07TRIPOLI943
    ('\nREF: A) STATE 135205; B) STATE 127608; C) JOHNSON-STEVENS/GODFREY E-MAIL 10/15/07; D) TRIPOLI 797; E) TRIPOLI 723 AND PREVIOUS', 2007,
     [u'07STATE135205', u'07STATE127608', u'07TRIPOLI797', u'07TRIPOLI723']),
    # 07STATE156011
    ('  REF: LA PAZ 2974', 2007, [u'07LAPAZ2974']),
    # 05PARIS7835
    ('\nREF: A. (A) PARIS 7682 AND PREVIOUS ', 2005, [u'05PARIS7682']),
    # 05PARIS7835
    ('\nREF: A. (A) PARIS 7682 AND PREVIOUS \n\nB. (B) EMBASSY PARIS DAILY REPORT FOR OCTOBER 28 - \nNOVEMBER 16 (PARIS SIPRNET SITE) \nC. (C) PARIS 7527 ', 2005,
     [u'05PARIS7682', u'05PARIS7527']),
    # 09MADRID869
    ('\nSUBJECT: UPDATES IN SPAIN’S INVESTIGATIONS OF RUSSIAN MAFIA \nREF: A. OSC EUP20080707950031  B. OSC EUP20081019950022  C. OSC EUP20090608178005  D. MADRID 286  E. OSC EUP20050620950076  F. OSC EUP20080708950049  G. OSC EUP20081029950032  H. OSC EUP 20061127123001\nMADRID 00000869 001.2 OF 004\n', 2009,
     [u'09MADRID286']),
    # 07STATE152317
    ('\nREF: (A)STATE 071143, (B)STATE 073601, (C)STATE 72896, (D)BEIJING \n5361, (E) STATE 148514', 2007,
     [u'07STATE71143', u'07STATE73601', u'07STATE72896', u'07BEIJING5361', u'07STATE148514']),
    # 08MANAGUA573
    ('\nREF: A. MANAGUA 520 \nB. MANAGUA 500 \nC. MANAGUA 443 \nD. MANAGUA 340 \nE. MANAGUA 325 \nF. MANAGUA 289 \nG. MANAGUA 263 \nH. MANAGUA 130 \nI. 2007 MANAGUA 2135 \nJ. 2007 MANAGUA 1730 \nK. 2007 MANAGUA 964 \nL. 2006 MANAGUA 2611 ', 2008,
     [u'08MANAGUA520', u'08MANAGUA500', u'08MANAGUA443', u'08MANAGUA340', u'08MANAGUA325', u'08MANAGUA289', u'08MANAGUA263', u'08MANAGUA130', u'07MANAGUA2135', u'07MANAGUA1730', u'07MANAGUA964', u'06MANAGUA2611']),
    # 66BUENOSAIRES2481
    ('\n REF: STATE 106206 CIRCULAR; STATE CA-3400 NOV 2, 1966 ', 1966, [u'66STATE106206']),
    #04MADRID4063
    ('\nREF: EMBASSY MADRID E-MAIL TO EUR/WE OF OCTOBER 14\n', 2004, []),
    #08RIYADH1134
    ('\nREF: A. SECSTATE 74879 \n     B. RIYADH 43 \n', 2008, [u'08STATE74879', u'08RIYADH43']),
    #08RIODEJANEIRO165
    ('TAGS: ECON EINV ENRG PGOV PBTS MARR BR\n\nSUBJECT: AMBASSADOR SOBEL MEETS WITH KEY ENERGY ENTITIES IN RIO Ref(s): A) 08 RIO DE JAN 138; B) 08 RIO DE JAN 0044 and previous Sensitive But Unclassified - Please handle accordingly. This message has been approved by Ambassador Sobel. ', 2008,
     [u'08RIODEJANEIRO138', u'08RIODEJANEIRO44']),
    ('\nREF: A. A) SECSTATE 54183 B. B) 07 BRASILIA 1868 C. C) STATE 57700 D. 07 STATE 17940 Classified By: DCM Phillip Chicola, Reason 1.5 (d) ', 2008,
    [u'08STATE54183', u'07BRASILIA1868', u'08STATE57700', u'07STATE17940']),
    # 08BRASILIA806
    ('\nPROGRAM REF: A. A) SECSTATE 54183 B. B) 07 BRASILIA 1868 C. C) STATE 57700 D. 07 STATE 17940 Classified By: DCM Phillip Chicola, Reason 1.5 (d) ', 2008,
     [u'08STATE54183', u'07BRASILIA1868', u'08STATE57700', u'07STATE17940']),
    # 06SAOPAULO276
    ('\nCARDINAL HUMMES DISCUSSES LULA GOVERNMENT, THE OPPOSITION, AND FTAA REF: (A) 05 SAO PAULO 405; (B) 05 SAO PAULO 402 (C) 02 BRASILIA 2670', 2006,
     [u'05SAOPAULO405', u'05SAOPAULO402', u'02BRASILIA2670']),
    # 08BERLIN1387
    ('\nREF: A. BERLIN 1045\nB. SECDEF MSG DTG 301601z SEP 08', 2008, [u'08BERLIN1045']),
    #09NAIROBI1938
    ('\nREF: A. 08 STATE 81854\n\n\nS e c r e t nairobi 001938', 2009, [u'08STATE81854']),
    # 02ROME1196
    ('\nREF: A. STATE 40721\n CONFIDENTIAL\\nPAGE 02 ROME 01196 01 OF 02 082030Z  B. ROME 1098  C. ROME 894  D. MYRIAD POST-DEPARTMENT E-MAILS FROM 10/01-02/02  E. ROME 348\nCLASSIFIED BY: POL', 2002,
     [u'02STATE40721', u'02ROME1098', u'02ROME894', u'02ROME348']),
    # 10TRIPOLI167
    ('\nREF: TRIPOLI 115\n\n1.(SBU) This is an action request; please see para 4.\n\n', 2010, [u'10TRIPOLI115']),
    # 06BRASILIA882
    ('SUBJECT: ENERGY INSTALLATIONS REF: BRASILIA 861', 2006, [u'06BRASILIA861']),
    # 08MOSCOW864
    ("TAGS: EPET ENRG ECON PREL PGOV RS\nSUBJECT: WHAT'S BEHIND THE RAIDS ON TNK-BP AND BP REF: A. MOSCOW 816 B. MOSCOW 768 C. 07 MOSCOW 3054 Classified By: Ambassador William J. Burns for Reasons 1.4 (b/d)\n", 2008,
     [u'08MOSCOW816', u'08MOSCOW768', u'07MOSCOW3054']),
    # 08TRIPOLI402
    ('REF: A) TRIPOLI 199, B) TRIPOLI 227 TRIPOLI 00000402 \n\n001.2 OF 003 ', 2008, '08TRIPOLI402',
      [u'08TRIPOLI199', u'08TRIPOLI227']),
    # 08LONDON2627
    ('''
E.O. 12958: N/A TAGS: AMGT

SUBJECT: UK COUNTRY CLEARANCE IS GRANTED TO STAMILIO, LTC DODSON AND LTCOL HAVRANEK REF: SECDEF R162245Z OCT 08

1.Embassy London is pleased to grant country clearance to Mr. Mark Stamilio, LTCOL John Havranek, and LTC James Dodson to visit London October 19-20 to attend working level meetings on ISAF detention policies and practices.

2. ---------------- Visit Officer ---------------- 

XXXXXXXXXXXX If calling from within the UK replace 44 with 0, if calling from landline to landline within London, dial only the last eight digits.

3. Confirmed reservations are held for Stamilio, Havranek and Dodson at Marriott Grosvernor Square.The rate is within per diem. The confirmation number are: Stamilio - 84274267, Havranek, 84274449, and Dodson, 84274523. London Marriott Grosvenor Square, Grosvenor Square, London W1A 4AW. Telephone number is (44)(0)20 7493-1232 Fax number is (44)(0)20 7491-3201. If calling from within the UK replace 44 with 0; if calling from landline within London, dial only the last eight digits.

4.Carry
''', 2008, []),
    # 08BRASILIA429
    ('''
SUBJECT: THOUGHTS ON THE VISIT OF DEFENSE MINISTER JOBIM TO WASHINGTON 

REF: A. A) BRASILIA 236 B. B) OSD REPORT DTG 251847Z MAR 08 C. C) BRASILIA 175 
Classified By: Ambassador Clifford Sobel. 
Reason: 1.5 d 
''', 2008, [u'08BRASILIA236', u'08BRASILIA175']),
    # 09PARIS1039
    ('''
SUBJECT: FRANCE’S POSITION ON NUCLEAR ISSUES IN THE RUN-UP 
TO THE NPT REVCON

REF: A. PARIS POINTS JULY 15  B. PARIS POINTS JULY 6  C. PARIS POINTS APRIL 10  D. PARIS 1025

Classified By:
''', 2009, [u'09PARIS1025']),
    # 08BERLIN1387
    ('''
SUBJECT: GERMANY: BUNDESTAG SET TO RENEW A BEEFED-UP ISAF
MANDATE AND A SCALED-DOWN OEF COUNTERPART

REF: A. BERLIN 1045 
¶B. SECDEF MSG DTG 301601z SEP 08

Classified By: CHARGE D'AFFAIRES''',
     2008,
     [u'08BERLIN1045']),
    # 08STATE15220
    ('''
Subject: (s) further scheming by german firm to export
test chamber to iranian ballistic missile program

Ref: a. 05 state 201650

B. 05 berlin 3726
c. 05 state 211408
d. 05 berlin 3954
e. 06 state 36325
f. 06 berlin 674
g. 06 state 62278
h. 06 berlin 1123
i. 06 state 70328
j. 06 berlin 1229
k. 06 berlin 1550
l. Mtcr poc 201/2006 - may 16 2006
m. 07 state 75839
n. 07 berlin 1137
o. 07 state 108420
p. 07 berlin 002163
q. 07 state 166482
r. 07 berlin 2216

Classified By: ISN/MTR DIRECTOR PAM DURHAM
for reasons 1.4 (b), (d).
''', 2008,
     [u'05STATE201650', u'05BERLIN3726', u'05STATE211408', u'05BERLIN3954', u'06STATE36325', u'06BERLIN674', u'06STATE62278', u'06BERLIN1123', u'06STATE70328', u'06BERLIN1229', u'06BERLIN1550', u'07STATE75839', u'07BERLIN1137', u'07STATE108420', u'07BERLIN2163', u'07STATE166482', u'07BERLIN2216']),
    # 09PARIS504
    ('''SUBJECT: DRC/ROC/NIGER: FRENCH PRESIDENCY'S READOUT OF 
SARKOZY'S MARCH 26-27 VISITS 

REF: A. PARIS 399 
B. KINSHASA 291 
C. BRAZZAVILLE 101 
D. NIAMEY 234 
E. 08 PARIS 1501 
F. 08 PARIS 1568 
G. 08 PARIS 1698 

Classified By: Political Minister-Counselor Kathleen Allegrone, 1.4 (b/ 
d). ''',
     2009,
     [u'09PARIS399', u'09KINSHASA291', u'09BRAZZAVILLE101', u'09NIAMEY234', u'08PARIS1501', u'08PARIS1568', u'08PARIS1698']),
    # 10THEHAGUE114
    ('''SUBJECT: NETHERLANDS/AFGHANISTAN: A REDUCED ROLE LIKELY BUT
DETAILS WILL NOT COME QUICKLY
REF: A. THE HAGUE 109
B. THE HAGUE 108
C. THE HAGUE 097
D. 09 THE HAGUE 759
Classified By: Deput''',
     2010,
     [u'10THEHAGUE109', u'10THEHAGUE108', '10THEHAGUE97', '09THEHAGUE759']),
    # 03THEHAGUE2597
    ('''REF: A. RICHARD-WITMER EMAIL 10/9 

B. WITMER-HOLLIDAY EMAILS 9-22 THRU 10-7 ''',
     2003,
     []),
    # 10STATE16220
    ('''SUBJECT: IRISL'S UNINSURED FLEET AND EVASIVE ACTIONS NECESSITATE DENIAL OF PORT ENTRY WORLDWIDE 

REF A) LONDON 002351 B) STATE 069339 C) STATE 094723 D) STATE 104496 E) STATE 108151 F) HAMILTON 00014 G) STATE 125339 H) STATE 1760 I) STATE 52348 J) STATE 121818 K) STATE 115243 L) STATE 90303 STATE 00016220 001.2 OF 005 M) STATE 7877 N) SINGAPORE 00083 O) UNSCR 1737 SANCTIONS COMMITTEE IMPLEMENTATION ASSISTANCE NOTICE- 24 JULY 2009 P) UNSCR 1737 SANCTIONS COMMITTEE IMPLEMENTATION ASSISTANCE NOTICE- 20 JANUARY 2010

1. (U) This''',
     2010, '10STATE16220',
     [u'10LONDON2351', u'10STATE69339', u'10STATE94723', u'10STATE104496', u'10STATE108151', u'10HAMILTON14', u'10STATE125339', u'10STATE1760', u'10STATE52348', u'10STATE121818', u'10STATE115243', u'10STATE90303', u'10STATE7877', u'10SINGAPORE83']),
    # 10CAIRO177
    ('''
SUBJECT: Sinai Update: Counter Smuggling and Floods 
 
REF: SECDEF 122723; CAIRO IIR 6 899 0149 10; 2009 CAIRO 2394 
2009 CAIRO 491 

CLASSIFIED BY:''',
    2010,
    [u'10SECDEF122723', u'09CAIRO2394', u'09CAIRO491']),
    # 08LONDON1991
    ('''SUBJECT: (C/NF) WHO WOULD REPLACE GORDON BROWN AS UK PRIMEREF: A. LONDON 1939  B. LONDON 1704''',
     2008,
     [u'08LONDON1939', u'08LONDON1704']),
    # 06CAIRO941
    (u'''SUBJECT: FBI DIRECTOR MUELLER’S VISIT TO EGYPTREF: CAIRO 493

Classified by DCM Stua''',
     2006,
     [u'06CAIRO493']),
    # 04BRASILIA445
    (u'''E.O. 12958: N/A 
TAGS: KIPR ECON ETRD KCRM PGOV BR IPR

SUBJECT: BRAZIL - 2004 SPECIAL 301 RESPONSE 

Refs: A) State 29549 
B) Sao Paulo 276 
C) Rio de Janeiro 128 
D) Brasilia 313 
E) Brasilia 222 
F) Brasilia 202 
G) 2003 Sao Paulo 2199 
H) 2003 Brasilia 3868 
I) 2003 Brasilia 3138 
J) 2003 Brasilia 3122 
K) 2003 Brasilia 2943 
L) 2003 Sao Paulo 1186 
''',
     2004,
     [u'04STATE29549', u'04SAOPAULO276', u'04RIODEJANEIRO128', u'04BRASILIA313', u'04BRASILIA222', u'04BRASILIA202', u'03SAOPAULO2199', u'03BRASILIA3868', u'03BRASILIA3138', u'03BRASILIA3122', u'03BRASILIA2943', u'03SAOPAULO1186']),
    # 06SAOPAULO532
    ('''
E.O. 12958: N/A TAGS: PGOV PHUM KCRM SOCI SNAR ASEC BR

REF: (A) Sao Paulo 526; 
(B) Sao Paulo 319; 
(C) Sao Paulo 42; 
(D) 05 Sao Paulo 975 

SENSITIVE BUT UNCLASSIFIED
''',
     2006,
     [u'06SAOPAULO526', u'06SAOPAULO319', u'06SAOPAULO42', u'05SAOPAULO975']),
    # 08LIMA480
    ('''
E.O. 12958:DECL: 03/18/2018   TAGS: PGOV PREL PINR PE

REF: A. LIMA 0389        
B. LIMA 3853        
C. LIMA 0390      

Classified By: 
''',
     2008,
     [u'08LIMA389', u'08LIMA3853', u'08LIMA390']),
    # 08MANAMA117
    ('''
UBJECT: BAHRAIN WILL FORMALLY REQUEST QATAR TO EXECUTE LEGAL JUDGMENT AGAINST KHALIFA AL SUBAIE REF: A. A) MANAMA 20 
B. B) 2/22/08 GRAY-ERELI E-MAIL 

Classified By''',
     2008,
     [u'08MANAMA20']),
    # 08MANAMA492 (08ECTION01OF02MANAMA492)
    ('''SUBJECT: BAHRAIN SEEKS IOM'S ASSISTANCE TO COBAT TIP 
 
REF: A. MANAMA 165 B. MANAMA 320 C. MANAMA 363 D. MANAMA 486 Classiied By: CDA Chr''',
     2008,
     [u'08MANAMA165', u'08MANAMA320', u'08MANAMA363', u'08MANAMA486']),
    # 06GENEVA1673
    (ur'''TAGS: PHUM UNHRC
SUBJECT: HRC: SPECIAL SESSION ON PALESTINE \
 \
REF: A. A) BERN 1253 \
 \
     B. B) GENEVA 1633 \
 \
Classified By: Pol''',
     2006,
     [u'06BERN1253', u'06GENEVA1633']),
    # 10UNESCOPARISFR197
    ('''SUBJECT: HAITI EARTHQUAKE:  DISCUSSION WITH UNESCO DIRECTOR-GENERAL 
 
REF: (A) USUNESCO PARIS FR 000087, (B) USUNESCO PARIS FR 00187 
 
1.  Ambassador [...]''',
     2010,
     ['10UNESCOPARISFR87', '10UNESCOPARISFR187']),
    # 08PARISFR2202
    ('''SUBJECT: UNESCO DIRECTOR GENERAL SUCCESSION:  CONVERSATIONS WITH 
MEXICO, SWEDEN, BRAZIL, FRANCE, AND TURKEY 
 
REF: (A) PARIS FR 2144 
     (B) PARIS FR 2153 
 
Classified by Amb[...]''',
     2008,
     [u'08UNESCOPARISFR2144', u'08UNESCOPARISFR2153']),
    # 10UNESCOPARISFR187
    ('''SUBJECT: HAITI EARTHQUAKE:  UNESCO MEETING ON SAVING HAITI'S 
HERITAGE 
 
REF: UNESCO PARIS FR 000087 

1. Summary. UNESCO, ''',
     2010,
     [u'10UNESCOPARISFR87']),
    # 09UNVIEVIENNA553
    ('''SUBJECT: AUSTRIAN AMBASSADOR TO IRAN DESCRIBES ELECTIONS AS 
DRIVING TEHRAN ENVIRONMENT 
 
REF: UNVIE 544 
 
Classified By: DCM''', 2010,
     [u'10UNVIEVIENNA544']),
    # 09UNVIEVIENNA322
    ('''SUBJECT: IAEA LEADERSHIP TEAM TRANSITION AND U.S. INFLUENCE 
IN THE AGENCY 
 
REF: A. UNVIE 148 
     B. UNVIE 102 (NOTAL) 
     C. UNVIE 089 
     D. UNVIE 076 
 
Classified By:''',
     2009,
     [u'09UNVIEVIENNA148', u'09UNVIEVIENNA102', u'09UNVIEVIENNA89', u'09UNVIEVIENNA76']),
    # 09UNVIEVIENNA540
    ('''SUBJECT: STAFFDEL KESSLER EXAMINES IRAN, SYRIA, AND 
MULTILATERAL VIENNA’S FRUSTRATING NAM DYNAMIC
REF: EMBASSY VIENNA 1450
Classified By: Mark''',
     2009,
     [u'09VIENNA1450']),
    # 08BRASILIA672
    ('''SUBJECT: SOURCES OF GENERATION - ELECTRICITY SERIES #2 
 
SENSITIVE BUT UNCLASSIFED--PLEASE PROTECT ACCORDINGLY 
 
REF: A: Sao Paulo 0031; B: La Paz 0462; C: 06 Sao Paulo 1059 D: 
Brasilia 00593; E: Sao Paulo  F: Rio 0091 
 
 
1.(U)SUMMARY: As''',
     2008,
     [u'08SAOPAULO31', u'08LAPAZ462', u'06SAOPAULO1059', u'08BRASILIA593', u'08RIODEJANEIRO91']),
    # 04RIODEJANEIRO1105
    ('''SUBJECT: BRZAIL'S MINAS GERAIS:  PT INCUMBENT COULD 
WIN A TIGHT RACE IN BRAZIL'S THIRD CITY 
 
Refs:  (A) Rio de Janeiro 00190  (B) Rio de Janeiro 
 
00723  (C) Brasilia 01392 
 
1.  (U)  SUMMARY''',
     2004,
     [u'04RIODEJANEIRO190', u'04RIODEJANEIRO723', u'04BRASILIA1392']),
    # 05RIODEJANEIRO19
    ('''SUBJECT:  Brazil - Bahia State Growing Faster but Interior 
Still a Problem 
 
Ref:  2003 Rio de Janeiro 1773 
 
Summary 
------- ''',
     2005,
     [u'03RIODEJANEIRO1773']),
    # 05RIODEJANEIRO1120
    ('''SUBJECT: MINAS GERAIS:  THE VIEW FROM BELO HORIZONTE 
 
Reftel:  Rio de Janeiro 1118 
 
SUMMARY 
------- ''',
     2005,
     [u'05RIODEJANEIRO1118']),
    # 08RIODEJANEIRO135
    ('''SUBJECT: Petrobras Delays Some Subsalt Tests Due to Equipment 
Shortage 
 
REF: A) RIO DE JANEIRO 91, B) RIO DE JANEIRO 35, C) 07 SAO PAULO 
0953 
 
1. Summary. ''',
     2008,
     [u'08RIODEJANEIRO91', u'08RIODEJANEIRO35', u'07SAOPAULO953']),
    # 09RIODEJANEIRO357
    ('''SUBJECT: (C) WAR BY ANY OTHER NAME: RIO'S "INTERNAL ARMED CONFLICT" 

REF: A. (A) RIO 329 
¶B. (B) RIO 346 Classified By: Principal Officer Dennis W. Hearne for reasons 1.4 (b, d ) 

¶1. (C) Summary: Rio Principal''',
     2009,
     [u'09RIODEJANEIRO329', u'09RIODEJANEIRO346']),
    # 05BOGOTA3726
    ('''SUBJECT: PEACE PROCESS WITH ELN STALLS
 
REF: A. BOGOTA 1775
 
     ¶B. BOGOTA 3422
     ¶C. CARACAS 0951
 
Classified By: Ambassador Willia''',
     2005,
     [u'05BOGOTA1775', u'05BOGOTA3422', u'05CARACAS951']),
    # 09CAIRO2205
    ('''POSTS FOR FRAUD PREVENTION UNITS E.O. 12958: N/A TAGS: KFRDKIRFCVISCMGTKOCIASECPHUMSMIGEG

SUBJECT: BLIND COPTIC GIRLS' CHOIR USED FOR ALIEN SMUGGLING REF: CAIRO 2178

1.(SBU) Summary:''',
     2009,
     [u'09CAIRO2178']),
    # 09BERLIN1116
    ('''E.O. 12958: DECL: 09/10/2034 TAGS: ETTC PGOV PINR MCAP PREL TSPAM JP FR SP UK
REF: A. BERLIN 1080 B. BERLIN 1049 C. BERLIN 765 D. BERLIN 601 E. BERLIN 561 F. BERLIN 181 G. 08 BERLIN 1575

Classified By: Global Affairs''',
     2009,
     [u'09BERLIN1080', u'09BERLIN1049', u'09BERLIN765', u'09BERLIN601', u'09BERLIN561', u'09BERLIN181', u'08BERLIN1575']),
    # 09SAOPAULO558
    ('''E.O. 12958: N/A 
TAGS: PINR PGOV PREL SNAR BR AVERY
SUBJECT: WHAT HAPPENED TO THE PCC? 
 
REF: A. ASUNCION 701 (08) 
     ¶B. ASUNCION 338 (07) 
     ¶C. INCSR BRAZIL 2008 
     ¶D. SAO PAULO 228 (08) 
     ¶E. SAO PAULO 66 (08) 
     ¶F. SAO PAULO 873 (07) 
     ¶G. SAO PAULO 447 (07) 
     ¶H. SAO PAULO 975 (06) 
     ¶I. SAO PAULO 526 (06) 
     ¶J. SAO PAULO 319 (06) 
 
¶1.  (SBU) Summary: For thre''',
     2009,
     [u'08ASUNCION701',
      u'07ASUNCION338',
      u'08SAOPAULO228',
      u'08SAOPAULO66',
      u'07SAOPAULO873',
      u'07SAOPAULO447',
      u'06SAOPAULO975',
      u'06SAOPAULO526',
      u'06SAOPAULO319']),
    # 07KINGSTON393
    ('''SUBJECT: JAMAICA/VENEZUELA: OPPOSITION LEADER DEEPLY 
CONCERNED OVER CHAVEZ'S INFLUENCE 
 
REF: A. KINGSTON 89 (NOTAL) 
     ¶B. KINGSTON 215 (NOTAL) 
     ¶C. 06 KINGSTON 2021 (NOTAL) 
     ¶D. KINGSTON 342 (NOTAL) 
     ¶E. PORT-OF-SPAIN 220 (NOTAL) 
 
Classified By: Ambassador Brenda''',
     2007,
     [u'07KINGSTON89', u'07KINGSTON215', u'06KINGSTON2021', u'07KINGSTON342', u'07PORTOFSPAIN220']),
    # 06PORTAUPRINCE2230
    ('''SUBJECT: COLLEAGUE CHRONICLES CORRUPTION OF YOURI LATORTUE REF: PORT AU PRINCE 01407 PORT AU PR 00002230 001.2 OF 002 Classified By:''',
     2006,
     [u'06PORTAUPRINCE1407']),
    # 06MONTREAL436
    ('''SUBJECT: IPR in Montreal Part 2 - Music Fans and Industry Stakeholders Take IPR Into Their Own Hands Ref: A Montreal 365, B Ottawa 406, C 05 Ottawa 2970 This message is Sensitive but Unclassified ''',
     2006,
     [u'06MONTREAL365', u'06OTTAWA406', u'05OTTAWA2970']),
    # 06WELLINGTON725
    ('''SUBJECT: DON BRASH NOT DOWN FOR THE COUNT - YET 
 
REF A WELLINGTON 721 B WELLINGTON 690 
 
Summary ''',
     2006,
     [u'06WELLINGTON721', u'06WELLINGTON690']),
    # 10QUITO33
    ('''SUBJECT: New Foreign Minister Patino from Left Side of Correa's 
Circle 
 
REF: QUITO 5; 094 QUITO 841; 08 QUITO 1062; 07 QUITO 1607 
07 QUITO 290; 06 QUITO 2937 
 
CLASSIFIED''',
     2010,
     [u'10QUITO5', u'94QUITO841', u'08QUITO1062', u'07QUITO1607', u'07QUITO290', u'06QUITO2937']),
    # 10HAVANA9
    ('''REF: A. REF A HAVANA 639 ("A SPLENDID LITTLE VISIT") ¶B. B HAVANA 772 (CONSULAR VISIT TO JAILED AMCIT) ¶C. C HAVANA 763 (CUBA PASSES UP ON REFORMS) ¶D. D HAVANA 739 (STRIDENT PROTEST) ¶E. E HAVANA 736 (HUMAN RIGHTS MARCHES TURN VIOLENT) ¶F. F HAVANA 755 (CUBAN FEATHERS RUFFLED BY USCG RESCUE) ''',
     2010,
     [u'10HAVANA639', u'10HAVANA772', u'10HAVANA763', u'10HAVANA739', u'10HAVANA736', u'10HAVANA755']),
    # 09NDJAMENA588
    ('''REF: A. NDJAMENA 520 ¶B. N'DJAMENA 511 ¶C. N'DJAMENA 521''',
     2009,
     [u'09NDJAMENA520', u'09NDJAMENA511', u'09NDJAMENA521']),
    # 09LONDON2697
    ('''REF: A. REF A STATE 122214 B. REF B LONDON 2649 C. REF C LONDON 2638 ''',
     2009,
     [u'09STATE122214', u'09LONDON2649', u'09LONDON2638']),
    # 04BRASILIA676
    ('''REF: A. A. STATE 56282 ¶B. B. STATE 56666 ¶C. C. STATE 41252 AND 44603 ¶D. D. BRASILIA 616 ''',
     2004,
     [u'04STATE56282', u'04STATE56666', u'04STATE41252', u'04STATE44603', u'04BRASILIA616']),
    # 04BRASILIA2863
    ('''REF: A. BRASILIA 2799 AND 2764 ¶B. PORT AU PRINCE 2325 ''',
     2004,
     [u'04BRASILIA2799', u'04BRASILIA2764', u'04PORTAUPRINCE2325']),
    # 02ROME1196
    ('''SUBJECT: AS PREDICTED, ITALY'S HUMAN RIGHTS REPORT GENERATES FODDER FOR DOMESTIC POLITICAL MILLS REF: A. STATE 40721 CONFIDENTIAL PAGE 02 ROME 01196 01 OF 02 082030Z B. ROME 1098 C. ROME 894 D. MYRIAD POST-DEPARTMENT E-MAILS FROM 10/01-02/02 E. ROME 348 CLASSIFIED BY: POL''',
     2002,
     [u'02STATE40721', u'02ROME1098', u'02ROME894', u'02ROME348']),
    # 03HALIFAX308
    ('''SUBJECT: THANKS A LOT, JUAN REF: HILL - OPS CENTER TELCONS 9/28 AND 29 ''',
     2003,
     []),
    # 05WELLINGTON489
    ('''REF: SECSTATE 113408 AND SECSTATE 113635 ''',
     2005,
     [u'05STATE113408', u'05STATE113635']),
)

def test_parse_references():
    def check(content, year, reference_id, expected):
        eq_(expected, parse_references(content, year, reference_id))
    for test in _TEST_DATA:
        reference_id = None
        if len(test) == 4:
           content, year, reference_id, expected = test
        else:
           content, year, expected = test
        yield check, content, year, reference_id, expected

_TRIPOLI_TESTS = {
'08TRIPOLI564': (
"""
RESIGN SOON 
 
REF: TRIPOLI 227  TRIPOLI 00000564  001.2 OF 002   CLASSIFIED BY: Chris Stevens, CDA, U.S. Embassy - Tripoli, Dept of State. REASON: 1.4 (b), (d) 1. (S/NF)
""", 2008, [u'08TRIPOLI227']),
'08TRIPOLI494': (
"""
E.O. 12958: DECL:  6/18/2018 
TAGS: PGOV PREL PHUM PINR LY
SUBJECT: JOURNALIST JAILED FOR CRITICIZING GOVERNMENT'S 
POORLY-COORDINATED DEVELOPMENT PROJECTS  CLASSIFIED BY: Chris Stevens, CDA, U.S. Embassy Tripoli, Dept of State. REASON: 1.4 (b), (d) 1. (C) Summary:  A respected [...]"""
, 2008, []),
'08TRIPOLI574': (
"""
SUBJECT: U.K. VISIT TO RABTA CHEMICAL WEAPONS PRODUCTION FACILITY 
 
REF: TRIPOLI 466  CLASSIFIED BY: John T. Godfrey, CDA, U.S. Embassy - Tripoli, Dept of State. REASON: 1.4 (b), (d) 1. (C) Summary: T [...]
""", 2008, [u'08TRIPOLI466']),
'08TRIPOLI466': (
"""
TAGS: PARM PREL CWC OPCW CBW CH JA IT LY
SUBJECT: CHEMICAL WEAPONS CONVENTION (CWC): CONVERSION OF THE RABTA CHEMICAL WEAPONS PRODUCTION FACILITY  REF: A) STATE 58476, B) THE HAGUE 482, C) TRIPOLI 119  CLASSIFIED BY: Chris Stevens, CDA, U.S. Embassy Tripoli, Dept of State. REASON: 1.4 (b), (d) 1. (C) Summary:  The"""
, 2008, [u'08STATE58476', u'08THEHAGUE482', u'08TRIPOLI119']),
}


def test_malformed_tripoli_cables():
    def check(content, year, reference_id, expected):
        eq_(expected, parse_references(content, year, reference_id))
    for ref_id, params in _TRIPOLI_TESTS.iteritems():
        content, year, result = params
        yield check, content, year, ref_id, result


if __name__ == '__main__':
    import nose
    nose.core.runmodule()
