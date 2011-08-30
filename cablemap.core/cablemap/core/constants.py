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
This module provides some global constants.

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - <http://www.semagia.com/>
:license:      BSD license
"""
import re

# Min/max length of station identifiers
MIN_ORIGIN_LENGTH = len(u'ROME')
MAX_ORIGIN_LENGTH = len(u'BANDARSERIBEGAWAN')

# Reference kind constants
REF_KIND_UNKNOWN = 0
REF_KIND_CABLE = 1
REF_KIND_EMAIL = 2
REF_KIND_BOOK = 3
REF_KIND_TEL = 4
REF_KIND_REPORT = 5
REF_KIND_FAX = 6
REF_KIND_MEMO = 7
REF_KIND_MEETING = 8
REF_KIND_WEB = 9

# Min/max cable serial number length
MIN_SERIAL_LENGTH = 1
MAX_SERIAL_LENGTH = 7

# Valid station identifiers
_STATIONS = (
    # A
    u'ABIDJAN', u'ABUDHABI', u'ABUJA', u'ACCRA', u'ADDISABABA', 
    u'AITTAIPEI', u'ALGIERS', u'AMMAN', u'AMSTERDAM', u'ANKARA', 
    u'ASHGABAT', u'ASMARA', u'ASTANA', u'ASUNCION', u'ATHENS',
    u'ADANA', u'ALMATY', u'APIA', u'AUCKLAND', u'ANTANANARIVO',
    u'ALEXANDRIA',
    # B
    u'BAGHDAD', u'BAKU', u'BAMAKO', u'BANDARSERIBEGAWAN', u'BANGKOK', 
    u'BANJUL', u'BARCELONA', u'BASRAH', u'BEIJING', u'BEIRUT', 
    u'BELGRADE', u'BERLIN', u'BERN', u'BISHKEK', u'BOGOTA', 
    u'BRASILIA', u'BRATISLAVA', u'BRIDGETOWN', u'BRUSSELS', u'BUCHAREST', 
    u'BUDAPEST', u'BUENOSAIRES', u'BUJUMBURA', u'BRAZZAVILLE', u'BELIZE',
    u'BELFAST', u'BELMOPAN', u'BONN', u'BANGUI',
    u'BENIN', # found in cable refs
    # C
    u'CAIRO', u'CALCUTTA', u'CANBERRA', u'CAPETOWN', u'CARACAS', 
    u'CASABLANCA', u'CHENNAI', u'CHISINAU', u'CIUDADJUAREZ', u'COLOMBO', 
    u'CONAKRY', u'COPENHAGEN', u'CURACAO', u'CALGARY', u'CHIANGMAI',
    u'CHENGDU', u'COTONOU', u'CDGENEVA',
    u'CDCATLANTAGA', # found in cable refs "Centers for Disease Control and Prevention"
    u'CHARLESTON', # found in cable refs
    u'CDC', # found in cable refs
    # D
    u'DAKAR', u'DAMASCUS', u'DARESSALAAM', u'DHAKA', u'DJIBOUTI', 
    u'DOHA', u'DUBAI', u'DUBLIN', u'DUSHANBE', u'DHAHRAN', u'DILI',
    u'DURBAN', u'DAMASCCUS',
    u'DUSSELDORF', # found in cable refs
    u'USDOJ', # found in cable refs
    # F
    u'FREETOWN', u'FUKUOKA', u'FSINFATC', u'FRANKFURT', u'FLORENCE', u'FESTTWO',
    # G
    u'GABORONE', u'GENEVA', u'GUATEMALA', u'GUADALAJARA', u'GUAYAQUIL',
    u'GUANGZHOU', u'GEORGETOWN', u'GRENADA',
    # H
    u'HAMBURG', u'HANOI', u'HARARE', u'HAVANA', u'HAMILTON', u'HELSINKI', u'HERMOSILLO',
    u'HALIFAX', u'HOCHIMINHCITY', u'HONGKONG', u'HILLAH', u'HYDERABAD',
    # I
    u'IRANRPODUBAI', u'ISLAMABAD', u'ISTANBUL', u'IZMIR',
    # J
    u'JEDDAH', u'JERUSALEM', u'JAKARTA', u'JOHANNESBURG',
    # K
    u'KABUL', u'KAMPALA', u'KATHMANDU', u'KHARTOUM', u'KIEV', u'KIGALI', 
    u'KINSHASA', u'KUALALUMPUR', u'KUWAIT', u'KYIV', u'KOLKATA', u'KINGSTON',
    u'KARACHI', u'KRAKOW', u'KOLONIA', u'KIRKUK', u'KOROR', u'KADUNA',
    # L
    u'LAGOS', u'LAPAZ', u'LAHORE', u'LILONGWE', u'LIMA', u'LISBON', u'LJUBLJANA',
    u'LONDON', u'LUANDA', u'LUXEMBOURG', u'LIBREVILLE', u'LUSAKA', u'LEIPZIG',
    u'LOME', # Found in cable refs
    # M
    u'MALABO', u'MADRID', u'MANAGUA', u'MANAMA', u'MAPUTO', u'MBABANE', u'MEXICO', 
    u'MILAN', u'MINSK', u'MONROVIA', u'MONTERREY', u'MONTEVIDEO', u'MONTREAL', 
    u'MOSCOW', u'MUMBAI', u'MUNICH', u'MUSCAT', u'MELBOURNE', u'MANILA',
    u'MATAMOROS', u'MASERU', u'MOGADISHU', u'MARSEILLE', u'MERIDA', u'MAJURO', u'MOSUL',
    u'MONTEREY', # Found in cable refs
    # N
    u'NAIROBI', u'NAPLES', u'NASSAU', u'NEWDELHI', u'NIAMEY', u'NICOSIA',
    u'NDJAMENA', u'NAHA', u'NUEVOLAREDO', u'NAGOYA', u'NOUAKCHOTT', u'NOGALES',
    # O 
    u'OSLO', u'OTTAWA', u'OUAGADOUGOU', u'OSAKAKOBE',
    # P
    u'PANAMA', u'PARAMARIBO', u'PARIS', u'PARTO', u'PESHAWAR', 
    u'PHNOMPENH', u'PORTAUPRINCE', u'PRAGUE', u'PRETORIA', u'PRISTINA',
    u'PORTLOUIS', u'PORTOFSPAIN', u'PODGORICA', u'PORTMORESBY', u'PERTH',
    u'PONTADELGADA',
    u'PARISFR', # Used for US Mission UNESCO, see also UNESCOPARISFR
    u'PRAIA', # Found in cable references
    # Q
    u'QUITO', u'QUEBEC',
    # R
    u'RABAT', u'RANGOON', u'RECIFE', u'REYKJAVIK', u'RIGA', 
    u'RIODEJANEIRO', u'RIYADH', u'ROME', u'RPODUBAI', 
    # S 
    u'SANAA', u'SANJOSE', u'SANSALVADOR', u'SANTIAGO', u'SANTODOMINGO', 
    u'SAOPAULO', u'SARAJEVO', u'SEOUL', u'SHANGHAI', u'SHENYANG', u'SINGAPORE',
    u'SKOPJE', u'SOFIA', u'STATE', u'STOCKHOLM', u'STRASBOURG', u'STPETERSBURG',
    u'SUVA', u'SAPPORO', u'SECDEF', u'SYDNEY', u'SURABAYA',
    # T
    u'TALLINN', u'TASHKENT', u'TAIPEI', u'TBILISI', u'TEGUCIGALPA', u'TEHRAN', 
    u'TELAVIV', u'THEHAGUE', u'TIJUANA', u'TOKYO', u'TRIPOLI', u'TUNIS',
    u'TORONTO', u'THESSALONIKI', u'TIRANA',
    # U
    u'ULAANBAATAR', u'UNVIEVIENNA', u'USNATO', u'USUNNEWYORK', u'USEUBRUSSELS',
    u'USOSCE', u'UNROME', u'USTRGENEVA',
    u'USDAFAS', # Found in cable references and stands for "U.S. Department of Agriculture"
    u'USDOC', # Found in REFerences and stands for "United States Department of Commerce"
    u'USCBP', # Found in refs and stands for "U.S. Customs and Border Protection"
    u'UNESCOPARISFR', # Same as PARISFR
    u'UNESCOPARIS', # Same as PARISFR
    # V
    u'VATICAN', u'VIENNA', u'VILNIUS', u'VLADIVOSTOK', u'VALLETTA', u'VANCOUVER',
    u'VIENTIANE',
    # W
    u'WARSAW', u'WELLINGTON', u'WINDHOEK', u'WASHDC',
    u'WHITEHOUSE', # Found in cable refs
    # Y
    u'YAOUNDE', u'YEREVAN', u'YEKATERINBURG',
    # Z
    u'ZAGREB'
)

REFERENCE_ID_PATTERN = re.compile(r'^([0-9]{2})(%s)([0-9]{%d,%d})$' % ('|'.join(_STATIONS), MIN_SERIAL_LENGTH, MAX_SERIAL_LENGTH), re.UNICODE)

# Wrong WikiLeaks cable identifiers
MALFORMED_CABLE_IDS = {
    u'08SCTION02OF02SAOPAULO335': u'08SAOPAULO335',
    u'09SECTION02OF03QRIPOLI583': u'09TRIPOLI583',
    u'08ECTION01OF02MANAMA492': u'08MANAMA492',
}

# Wrong WikiLeaks cable identifiers w/o a valid equivalent
INVALID_CABLE_IDS = {
    # Format:
    # Invalid cable ID: Cable ID which would be correct
    u'09EFTOHELSINKI235': u'09HELSINKI235',
    u'08SECTION01GF02BISHIEK21': u'08BISHKEK1021', # See <http://aebr.home.xs4all.nl/wl/corrupted/corrupted.html>
    u'09SECTION01OF03SANJOSE525': u'09SANJOSE525',
    u'07EFTOOTTAWA1217': u'07OTTAWA1217',
    u'06BRAILIA1079': u'06BRASILIA1079',
    u'07BRASIIA1568': u'07BRASILIA1568',
    u'06EFTOSANAA1621': u'06SANAA1621',
    u'08EFTOPHNOMPENH416': u'08PHNOMPENH416',
    u'09EFTOLONDON2468': u'09LONDON2468',
    u'09EFTOLONDON2884': u'09LONDON2884',
    u'09EFTOLONDON2858': u'09LONDON2858',
    u'08EFTOLONDON2883': u'08LONDON2883',
    u'09EFTOLONDON2187': u'09LONDON2187',
    u'10EFTOLONDON16': u'10LONDON16',
    u'09EFTOLONDON2363': u'09LONDON2363',
    u'09EFTOLONDON2618': u'09LONDON2618',
    u'09EFTOLONDON2240': u'09LONDON2240',
    u'09EFTOLONDON2211': u'09LONDON2211',
    u'09EFTOLONDON2521': u'09LONDON2521',
    u'09EFTOLONDON2688': u'09LONDON2688',
    u'09EFTOLONDON2905': u'09LONDON2905',
    u'09EFTOTRIPOLI704': u'09TRIPOLI704',
    u'09EFTOLONDON2239': u'09LONDON2239',
    u'09BAU339': u'09BAKU339',
    u'09EFTOSANAA433': u'09SANAA433',
    u'10EFTOKABUL597': u'10KABUL597',
    u'09SECION02OF02NAIROBI417': u'09NAIROBI417',
    u'08AITTAIPIE1698': u'08TAIPEI1698',
    u'07SECTION02OF03EIJING483': u'07BEIJING483',
    u'09COPENHAEN13': u'09COPENHAGEN13',
    u'09EFTOASMARA34': u'09ASMARA34',
    u'06EFTOUSUNNEWYORK1560': u'06USUNNEWYORK1560',
    u'08EFTOJAKARTA2073': u'08JAKARTA2073',
    u'06EFTOANKARA4972': u'06ANKARA4972',
    u'08SECTIN03OF03KABUL3036': u'08KABUL3036',
    u'07EFTOATHENS404': u'07ATHENS404',
    u'06EFTOANKARA5010': u'06ANKARA5010',
    u'10EFTOKABUL668': u'10KABUL668',
    u'06EFTOKABUL5893': u'06KABUL5893',
    u'08EFTODAMASCUS487': u'08DAMASCUS487',
    u'06EFTOANKARA5097': u'06ANKARA5097',
    u'08SECTIO01OF02JERUSALEM1847': u'08JERUSALEM1847',
    u'07SECTION01OF03ANKARA365': u'07ANKARA365',
    u'07EFTOSANAA2300': u'07SANAA2300',
    u'07EFTOSANAA588': u'07SANAA588',
    u'06EFTOPORTMORESBY350': u'06PORTMORESBY350',
    u'07EFTOSANAA588': u'07SANAA588',
    u'09AMEMBASSYHANOI1292': u'09HANOI1292',
    u'06EFTOCARACAS943': u'06CARACAS943',
    u'06EFTOCARACAS2252': u'06CARACAS2252',
    u'07EFTOSANAA784': u'07SANAA784',
    u'06EFTOSANAA1996': u'06SANAA1996',
    u'08SECTON01OF02BEIRUT896': u'08BEIRUT896',
    u'06EFTOBAKU1165': u'06BAKU1165',
    u'092OF5': u'09STATE126780', # Unsure about the s/n
    u'07EFTORABAT521': u'07RABAT521',
    u'08ECTION02OF02ATHENS959': u'08ATHENS959',
    u'09AMEMBASSYHANOI1284': u'09HANOI1284',
    u'06EFTOISLAMABAD17875': u'06ISLAMABAD17875',
    u'09SQCTION02OF02DUSHANBE143': u'09DUSHANBE143',
    u'08THEHAGU799': u'08THEHAGUE799',
    u'08EFTOBUENOSAIRES648': u'08BUENOSAIRES648',
    u'08IHARTOUM1126': u'08KHARTOUM1126',
    u'07QXICO3307': u'07MEXICO3307',
    u'07ANILA1702': u'07MANILA1702',
    u'09GUATEMLA692': u'09GUATEMALA692',
    u'09AMEMBASSYHANOI1234': u'09HANOI1234',
    u'06EFTOATHENS2950': u'06ATHENS2950',
    u'10EFTOLONDON223': u'10LONDON223',
    u'10EFTOBANDARSERIBEGAWAN24': u'10BANDARSERIBEGAWAN24',
    u'10EFTOLONDON224': u'10LONDON224',
    u'06KINSHAA1386': u'06KINSHASA1386',
    u'09EFTOUSUNNEWYORK584': u'09USUNNEWYORK584',
    u'09KINHASA1056': u'09KINSHASA1056',
    u'06MILSK1226': u'06MINSK1226',
    u'06SECTIO03OF03MINSK1128': u'06MINSK1128',
    u'07EFTOBAGHDAD1098': u'07BAGHDAD1098',
    u'07SETION02OF02BAKU1501': u'07BAKU1501',
    u'07SECTON03OF04DAKAR269': u'07DAKAR269',
    u'06EFTOPORTMORESBY194': u'06PORTMORESBY194',
    u'06EFTOPORTMORESBY197': u'06PORTMORESBY197',
    u'06PORTOFPAIN568': u'06PORTOFSPAIN568',
    u'06EFTOATHENS1738': u'06ATHENS1738',
    u'06EFTOBAKU1149': u'06BAKU1149',
    u'07EFTOBUENOSAIRES1049': u'07BUENOSAIRES1049',
    u'09SIFIEDABUJA1673': u'09ABUJA1673',
    u'09SECTIOQ1OF06HARARE876': u'09HARARE876',
    u'07EFTOATHENS781': u'07ATHENS781',
    u'08SECTIN02OF02PORTOFSPAIN546': u'08PORTOFSPAIN546',
    u'09EFTORIYADH1110': u'09RIYADH1110',
    u'07EFTOATHENS543': u'07ATHENS543',
    u'06EFTORABAT1713': u'06RABAT1713',
    u'06EFTOBAKU1420': u'06BAKU1420',
    u'07EFTOUSUNNEWYORK181': u'07USUNNEWYORK181',
    u'06ANOI582': u'06HANOI582',
    u'08INSHASA1164': u'08KINSHASA1164',
    u'07THEHAGE742': u'07THEHAGUE742',
    u'08FSCCHARLESTON1712': u'08CHARLESTON1712',
    u'06EFTORANGOON1092': u'06RANGOON1092',
    u'06SECTIKN01OF03MINSK1223': u'06MINSK1223',
    u'09SECTION02F02BRUSSELS1639': u'09BRUSSELS1639',
    u'06EFTOSKOPJE206': u'06SKOPJE206',
    u'09EFTOYEREVAN678': u'09YEREVAN678',
    u'09SCTION08OF09NAIROBI809': u'09NAIROBI809',
    u'07EFTOBAGHDAD867': u'07BAGHDAD867',
    u'08EFTOUSUNNEWYORK457': u'08USUNNEWYORK457',
    u'09EFTOYEREVAN677': u'09YEREVAN677',
    u'09SECTION0QF05HANOI297': u'09HANOI297',
    u'09EFTOYEREVAN540': u'09YEREVAN540',
    u'07EFTOATHENS174': u'07ATHENS174',
    u'06EFTOPORTMORESBY364': u'06PORTMORESBY364',
    u'07KAPALA518': u'07KAMPALA518',
    u'07EFTORABAT171': u'07RABAT171',
    u'08EFTOMONTEVIDEO541': u'08MONTEVIDEO541',
    u'06NDJAENA1382': u'06NDJAMENA1382',
    u'09AMEMBASSYHANOI1246': u'09HANOI1246',
    u'09NSSAU504': u'09NASSAU504',
    u'09BRUSSLS1332': u'09BRUSSELS1332',
    u'09BRUSELS1292': u'09BRUSEELS1292',
    u'08EFTOMONTEVIDEO718': u'08MONTEVIDEO718',
    u'07EFTOLAPAZ1740': u'07LAPAZ1740',
    u'07EFTOATHENS373': u'07ATHENS373',
    u'09EFTOMONTEVIDEO137': u'09MONTEVIDEO137',
    u'09EFTOYEREVAN559': u'09YEREVAN559',
    u'09NDJAENA423': u'09NDJAMENA423',
    u'08SANODOMINGO1611': u'08SANTODOMINGO1611',
    u'06EFTOSKOPJE971': u'06SKOPJE971',
    u'08SECTON02OF02TIRANA398': u'08TIRANA398',
    u'07EFTOATHENS298': u'07ATHENS298',
    u'07EFTOATHENS299': u'07ATHENS299',
    u'06EFTOBAKU1204': u'06BAKU1204',
    u'09AMEMBASSYHANOI1274': u'09HANOI1274',
    u'06MAILA1222': u'06MANILA1222',
    u'08ACCRA001382SUSPECTEDDUPLICATE1392': u'08ACCRA1392',
    u'07SOIA828': u'07SOFIA828',
    u'10AQNA272': u'10ASTANA272',
    u'06EFTOCAIRO6192': u'06CAIRO6192',
    u'07EFTOBAGHDAD1116': u'07BAGHDAD1116',
    u'07POTAUPRINCE943': u'07PORTAUPRINCE943',
    u'07EFTORABAT264': u'07RABAT264',
    u'08BANGOK1382': u'08BANGKOK1382',
    u'08SECTIN01OF02BUDAPEST836': u'08BUDAPEST836',
    u'09EFTOYEREVAN874': u'09YEREVAN874',
    u'06EFTOMAPUTO981': u'06MAPUTO981',
    u'07BUENOSQRES633': u'07BUENOSAIRES633',
    u'10SECION03OF08VIENNA176': u'10VIENNA176',
    u'09AMEMBASSYHANOI1290': u'09HANOI1290',
    u'06EFTOBRUSSELS3952': u'06BRUSSELS3952',
    u'07GEORGETON514': u'07GEORGETOWN514',
    u'06ATANANARIVO1320': u'06ANTANANARIVO1320',
    u'06EFTOBAKU1453': u'06BAKU1453',
    u'08SANTOOMINGO1959': u'08SANTODOMINGO1959',
    u'09EFTOASMARA373': u'09ASMARA373',

}
