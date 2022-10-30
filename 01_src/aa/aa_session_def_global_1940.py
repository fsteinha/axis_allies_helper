##
# @file aa_session_def_global_1940.py
#
# @brief initial deffinitions for the setup global 1940.
#
# @section description_aa_territory Description
# This modul includes:
# - TODO
#
# @section libraries_main Libraries/Modules
# - aa_type (local)
# - aa_item (local)
# - aa_map(local)
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_map TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 09/08/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.


from aa_type import CType
from aa_item import CAAItem
from aa_nation import *
from aa_map import *
from aa_territory import *
from aa_units import *
from aa_relnation import CAAI_RelNation
from aa_facillities import *

# Active nations
CAAN_GERMANY        = CAAI_Nation("Germany"       , CType.A_AXIS  )
CAAN_SOVIET_UNION   = CAAI_Nation("Soviet Union"  , CType.A_ALLIES)
CAAN_JAPAN          = CAAI_Nation("Japan"         , CType.A_AXIS  )
CAAN_UNITED_STATES  = CAAI_Nation("United States" , CType.A_ALLIES)
CAAN_CHINA          = CAAI_Nation("China"                  , CType.A_ALLIES)
CAAN_UK_AT          = CAAI_Nation("United Kingdom Atlantic", CType.A_ALLIES)
CAAN_UK_PA          = CAAI_Nation("United Kingdom Pacific" , CType.A_ALLIES)
CAAN_ITALY          = CAAI_Nation("Italy"         , CType.A_AXIS  )
CAAN_ANZAC          = CAAI_Nation("ANZAC"         , CType.A_ALLIES)
CAAN_FRANCE         = CAAI_Nation("France"        , CType.A_ALLIES)

# Passive nations
CAAN_AFGANISTAN     = CAAI_Nation("Afganistan"    , CType.A_NEUTRAL)
CAAN_ANGOLA         = CAAI_Nation("Angola"        , CType.A_NEUTRAL)
CAAN_ARGENTINA      = CAAI_Nation("Argentina"     , CType.A_NEUTRAL)
CAAN_BOLIVIA        = CAAI_Nation("Bolivia"       , CType.A_NEUTRAL)
CAAN_BRAZIL         = CAAI_Nation("Brazil"        , CType.A_NEUTRAL)
CAAN_BULGARIA       = CAAI_Nation("Bulgaria"      , CType.A_NEUTRAL_PRO_AXIS)
CAAN_CHILE          = CAAI_Nation("Chile"         , CType.A_NEUTRAL)
CAAN_COLOMBIA       = CAAI_Nation("Colombia"      , CType.A_NEUTRAL)
CAAN_PERSIA         = CAAI_Nation("Persia"        , CType.A_NEUTRAL_PRO_ALLIES)
CAAN_ECUADOR        = CAAI_Nation("Ecuador"       , CType.A_NEUTRAL_PRO_ALLIES)
CAAN_EIRE           = CAAI_Nation("Eire"          , CType.A_NEUTRAL_PRO_ALLIES)
CAAN_FINNLAND       = CAAI_Nation("Finnland"      , CType.A_NEUTRAL_PRO_AXIS)
CAAN_GREECE         = CAAI_Nation("Greece"        , CType.A_NEUTRAL_PRO_ALLIES)
CAAN_IRAQ           = CAAI_Nation("Iraq"          , CType.A_NEUTRAL_PRO_AXIS)
CAAN_LIBERIA        = CAAI_Nation("Liberia"       , CType.A_NEUTRAL)
CAAN_MONGOLIA       = CAAI_Nation("Mongolia"      , CType.A_NEUTRAL)
CAAN_MOZAMBIQUE     = CAAI_Nation("Mozambique"    , CType.A_NEUTRAL)
CAAN_NETHERLANDS    = CAAI_Nation("Netherlands"   , CType.A_ALLIES)
CAAN_RIO_DE_ORO     = CAAI_Nation("Rio de oro"    , CType.A_NEUTRAL)
CAAN_SAUDI_ARABIA   = CAAI_Nation("Saudi Arabia"  , CType.A_NEUTRAL)
CAAN_SIERA_LEONE    = CAAI_Nation("Siera Leone"   , CType.A_NEUTRAL)
CAAN_SPAIN          = CAAI_Nation("Spain"         , CType.A_NEUTRAL)
CAAN_SWEDEN         = CAAI_Nation("Sweden"        , CType.A_NEUTRAL)
CAAN_SWITZERLAND    = CAAI_Nation("Switzerland"   , CType.A_NEUTRAL)
CAAN_TURKEY         = CAAI_Nation("Turkey"        , CType.A_NEUTRAL)
CAAN_PARAQUAY       = CAAI_Nation("Paraquay"      , CType.A_NEUTRAL)
CAAN_PERU           = CAAI_Nation("Peru"          , CType.A_NEUTRAL)
CAAN_PORTUGESE_GUINEA = CAAI_Nation("Portugese Guinea", CType.A_NEUTRAL)
CAAN_PORTUGAL         = CAAI_Nation("Portugal"    , CType.A_NEUTRAL)
CAAN_URUGUAY          = CAAI_Nation("Uruguay"      , CType.A_NEUTRAL)
CAAN_VENEZUELA        = CAAI_Nation("Venezuela"   , CType.A_NEUTRAL)
CAAN_YUGOSLAVIA       = CAAI_Nation("Yugoslavia"  , CType.A_NEUTRAL_PRO_ALLIES)

# Setup (used in land initailizations)
# Italy setup
L_SOUTHERN_ITALY     = [CAAU_Inf(CAAN_ITALY, 6), CAAU_AAA(CAAN_ITALY, 2), CAAU_Figther(CAAN_ITALY, 2), CAAF_AirBase(), CAAF_NavalBase(), CAAF_Minor()]
L_NORTHERN_ITALY     = [CAAU_Inf(CAAN_ITALY, 2), CAAU_Ari(CAAN_ITALY, 2), CAAU_Tank(CAAN_ITALY, 1), CAAU_AAA(CAAN_ITALY, 2), CAAU_SBomb(CAAN_ITALY, 1), CAAF_Major()]
L_ALBANIA            = [CAAU_Inf(CAAN_ITALY, 2), CAAU_Tank(CAAN_ITALY, 1)]
L_LIBYA              = [CAAU_Inf(CAAN_ITALY, 1), CAAU_Ari(CAAN_ITALY, 1)]
L_TOBRUK             = [CAAU_Inf(CAAN_ITALY, 3), CAAU_MechInf(CAAN_ITALY, 1), CAAU_Ari(CAAN_ITALY, 1), CAAU_Tank(CAAN_ITALY, 1)]
L_ITALIAN_SOMALILAND = [CAAU_Inf(CAAN_ITALY, 1)]
L_ETHOPIA            = [CAAU_Inf(CAAN_ITALY, 2), CAAU_Ari(CAAN_ITALY, 1)]
L_SEAZONE_95         = [CAAU_Cargo(CAAN_ITALY, 1), CAAU_Submarine(CAAN_ITALY, 1), CAAU_Destroyer(CAAN_ITALY, 1), CAAU_Cruiser(CAAN_ITALY, 1)]
L_SEAZONE_96         = [CAAU_Cargo(CAAN_ITALY, 1), CAAU_Destroyer(CAAN_ITALY, 1)]
L_SEAZONE_97         = [CAAU_Cargo(CAAN_ITALY, 1), CAAU_Cruiser(CAAN_ITALY, 1), CAAU_Battleship(CAAN_ITALY, 1)]

# Germany setup
L_GERMANY                  = [CAAU_Inf(CAAN_GERMANY, 11), CAAU_Ari(CAAN_GERMANY, 3), CAAU_AAA(CAAN_GERMANY, 3), CAAU_TBomb(CAAN_GERMANY, 1), CAAU_SBomb(CAAN_GERMANY, 2), CAAF_Major()]
L_WESTERN_GERMANY          = [CAAU_Inf(CAAN_GERMANY, 3), CAAU_MechInf(CAAN_GERMANY, 4), CAAU_Ari(CAAN_GERMANY, 1), CAAU_AAA(CAAN_GERMANY, 3), CAAU_Figther(CAAN_GERMANY, 2), CAAU_TBomb(CAAN_GERMANY, 3), CAAF_AirBase(), CAAF_NavalBase(), CAAF_Major()]
L_DENMARK                  = [CAAU_Inf(CAAN_GERMANY, 2)]
L_NORWAY                   = [CAAU_Inf(CAAN_GERMANY, 3), CAAU_Figther(CAAN_GERMANY, 2)]
L_HOLLAND_BELGIUM          = [CAAU_Inf(CAAN_GERMANY, 4), CAAU_Ari(CAAN_GERMANY, 2), CAAU_Tank(CAAN_GERMANY, 3), CAAU_Figther(CAAN_GERMANY, 1)]
L_GREATER_SOUTHERN_GERMANY = [CAAU_Inf(CAAN_GERMANY, 6), CAAU_Ari(CAAN_GERMANY, 2), CAAU_Tank(CAAN_GERMANY, 3)]
L_SLOVAKIA_HUNGARY         = [CAAU_Inf(CAAN_GERMANY, 2), CAAU_Tank(CAAN_GERMANY, 1), CAAU_Figther(CAAN_GERMANY, 1)]
L_ROMANIA                  = [CAAU_Inf(CAAN_GERMANY, 2), CAAU_Tank(CAAN_GERMANY, 1)]
L_POLAND                   = [CAAU_Inf(CAAN_GERMANY, 3), CAAU_Tank(CAAN_GERMANY, 1)]
L_SEAZONE_103              = [CAAU_Submarine(CAAN_GERMANY, 1)]
L_SEAZONE_108              = [CAAU_Submarine(CAAN_GERMANY, 1)]
L_SEAZONE_113              = [CAAU_Battleship(CAAN_GERMANY, 1)]
L_SEAZONE_114              = [CAAU_Cargo(CAAN_GERMANY, 1), CAAU_Cruiser(CAAN_GERMANY, 1)]
L_SEAZONE_117              = [CAAU_Submarine(CAAN_GERMANY, 1)]
L_SEAZONE_118              = [CAAU_Submarine(CAAN_GERMANY, 1)]
L_SEAZONE_124              = [CAAU_Submarine(CAAN_GERMANY, 1)]








CAAT_SEASIDE_001 = CAAT_Sea("Seaside 1" , CType.R_PACIFIC)
CAAT_SEASIDE_002 = CAAT_Sea("Seaside 2" , CType.R_PACIFIC)
CAAT_SEASIDE_003 = CAAT_Sea("Seaside 3" , CType.R_PACIFIC)
CAAT_SEASIDE_004 = CAAT_Sea("Seaside 4" , CType.R_PACIFIC)
CAAT_SEASIDE_005 = CAAT_Sea("Seaside 5" , CType.R_PACIFIC)
CAAT_SEASIDE_006 = CAAT_Sea("Seaside 6" , CType.R_PACIFIC)
CAAT_SEASIDE_007 = CAAT_Sea("Seaside 7" , CType.R_PACIFIC)
CAAT_SEASIDE_008 = CAAT_Sea("Seaside 8" , CType.R_PACIFIC)
CAAT_SEASIDE_009 = CAAT_Sea("Seaside 9" , CType.R_PACIFIC)
CAAT_SEASIDE_010 = CAAT_Sea("Seaside 10", CType.R_PACIFIC)
CAAT_SEASIDE_011 = CAAT_Sea("Seaside 11", CType.R_PACIFIC)
CAAT_SEASIDE_012 = CAAT_Sea("Seaside 12", CType.R_PACIFIC)
CAAT_SEASIDE_013 = CAAT_Sea("Seaside 13", CType.R_PACIFIC)
CAAT_SEASIDE_014 = CAAT_Sea("Seaside 14", CType.R_PACIFIC)
CAAT_SEASIDE_015 = CAAT_Sea("Seaside 15", CType.R_PACIFIC)
CAAT_SEASIDE_016 = CAAT_Sea("Seaside 16", CType.R_PACIFIC)
CAAT_SEASIDE_017 = CAAT_Sea("Seaside 17", CType.R_PACIFIC)
CAAT_SEASIDE_018 = CAAT_Sea("Seaside 18", CType.R_PACIFIC)
CAAT_SEASIDE_019 = CAAT_Sea("Seaside 19", CType.R_PACIFIC)
CAAT_SEASIDE_020 = CAAT_Sea("Seaside 20", CType.R_PACIFIC)
CAAT_SEASIDE_021 = CAAT_Sea("Seaside 21", CType.R_PACIFIC)
CAAT_SEASIDE_022 = CAAT_Sea("Seaside 22", CType.R_PACIFIC)
CAAT_SEASIDE_023 = CAAT_Sea("Seaside 23", CType.R_PACIFIC)
CAAT_SEASIDE_024 = CAAT_Sea("Seaside 24", CType.R_PACIFIC)
CAAT_SEASIDE_025 = CAAT_Sea("Seaside 25", CType.R_PACIFIC)
CAAT_SEASIDE_026 = CAAT_Sea("Seaside 26", CType.R_PACIFIC)
CAAT_SEASIDE_027 = CAAT_Sea("Seaside 27", CType.R_PACIFIC)
CAAT_SEASIDE_028 = CAAT_Sea("Seaside 28", CType.R_PACIFIC)
CAAT_SEASIDE_029 = CAAT_Sea("Seaside 29", CType.R_PACIFIC)
CAAT_SEASIDE_030 = CAAT_Sea("Seaside 30", CType.R_PACIFIC)
CAAT_SEASIDE_031 = CAAT_Sea("Seaside 31", CType.R_PACIFIC)
CAAT_SEASIDE_032 = CAAT_Sea("Seaside 32", CType.R_PACIFIC)
CAAT_SEASIDE_033 = CAAT_Sea("Seaside 33", CType.R_PACIFIC)
CAAT_SEASIDE_034 = CAAT_Sea("Seaside 34", CType.R_PACIFIC)
CAAT_SEASIDE_035 = CAAT_Sea("Seaside 35", CType.R_PACIFIC)
CAAT_SEASIDE_036 = CAAT_Sea("Seaside 36", CType.R_PACIFIC)
CAAT_SEASIDE_037 = CAAT_Sea("Seaside 37", CType.R_PACIFIC)
CAAT_SEASIDE_038 = CAAT_Sea("Seaside 38", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_039 = CAAT_Sea("Seaside 39", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_040 = CAAT_Sea("Seaside 40", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_041 = CAAT_Sea("Seaside 41", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_042 = CAAT_Sea("Seaside 42", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_043 = CAAT_Sea("Seaside 43", CType.R_PACIFIC)
CAAT_SEASIDE_044 = CAAT_Sea("Seaside 44", CType.R_PACIFIC)
CAAT_SEASIDE_045 = CAAT_Sea("Seaside 45", CType.R_PACIFIC)
CAAT_SEASIDE_046 = CAAT_Sea("Seaside 46", CType.R_PACIFIC)
CAAT_SEASIDE_047 = CAAT_Sea("Seaside 47", CType.R_PACIFIC)
CAAT_SEASIDE_048 = CAAT_Sea("Seaside 48", CType.R_PACIFIC)
CAAT_SEASIDE_049 = CAAT_Sea("Seaside 49", CType.R_PACIFIC)
CAAT_SEASIDE_050 = CAAT_Sea("Seaside 50", CType.R_PACIFIC)
CAAT_SEASIDE_051 = CAAT_Sea("Seaside 51", CType.R_PACIFIC)
CAAT_SEASIDE_052 = CAAT_Sea("Seaside 52", CType.R_PACIFIC)
CAAT_SEASIDE_053 = CAAT_Sea("Seaside 53", CType.R_PACIFIC)
CAAT_SEASIDE_054 = CAAT_Sea("Seaside 54", CType.R_PACIFIC)
CAAT_SEASIDE_055 = CAAT_Sea("Seaside 55", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_056 = CAAT_Sea("Seaside 56", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_057 = CAAT_Sea("Seaside 57", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_058 = CAAT_Sea("Seaside 58", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_059 = CAAT_Sea("Seaside 59", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_060 = CAAT_Sea("Seaside 60", CType.R_INDIAN_OCEAN)
CAAT_SEASIDE_061 = CAAT_Sea("Seaside 61", CType.R_PACIFIC)
CAAT_SEASIDE_062 = CAAT_Sea("Seaside 62", CType.R_PACIFIC)
CAAT_SEASIDE_063 = CAAT_Sea("Seaside 63", CType.R_PACIFIC)
CAAT_SEASIDE_064 = CAAT_Sea("Seaside 64", CType.R_PACIFIC)
CAAT_SEASIDE_065 = CAAT_Sea("Seaside 65", CType.R_PACIFIC)
CAAT_SEASIDE_066 = CAAT_Sea("Seaside 66", CType.R_ATLANTIC)
CAAT_SEASIDE_067 = CAAT_Sea("Seaside 67", CType.R_ATLANTIC)
CAAT_SEASIDE_068 = CAAT_Sea("Seaside 68", CType.R_ATLANTIC)
CAAT_SEASIDE_069 = CAAT_Sea("Seaside 69", CType.R_ATLANTIC)
CAAT_SEASIDE_070 = CAAT_Sea("Seaside 70", CType.R_ATLANTIC)
CAAT_SEASIDE_071 = CAAT_Sea("Seaside 71", CType.R_PACIFIC)
CAAT_SEASIDE_072 = CAAT_Sea("Seaside 72", CType.R_PACIFIC)
CAAT_SEASIDE_073 = CAAT_Sea("Seaside 73", CType.R_PACIFIC)
CAAT_SEASIDE_074 = CAAT_Sea("Seaside 74", CType.R_PACIFIC)
CAAT_SEASIDE_075 = CAAT_Sea("Seaside 75", CType.R_PACIFIC)
CAAT_SEASIDE_076 = CAAT_Sea("Seaside 76", CType.R_PACIFIC)
CAAT_SEASIDE_077 = CAAT_Sea("Seaside 77", CType.R_PACIFIC)
CAAT_SEASIDE_078 = CAAT_Sea("Seaside 78", CType.R_PACIFIC)
CAAT_SEASIDE_079 = CAAT_Sea("Seaside 79", CType.R_PACIFIC)
CAAT_SEASIDE_080 = CAAT_Sea("Seaside 80", CType.R_PACIFIC)
CAAT_SEASIDE_081 = CAAT_Sea("Seaside 81", CType.R_PACIFIC)
CAAT_SEASIDE_082 = CAAT_Sea("Seaside 82", CType.R_ATLANTIC)
CAAT_SEASIDE_083 = CAAT_Sea("Seaside 83", CType.R_ATLANTIC)
CAAT_SEASIDE_084 = CAAT_Sea("Seaside 84", CType.R_ATLANTIC)
CAAT_SEASIDE_085 = CAAT_Sea("Seaside 85", CType.R_ATLANTIC)
CAAT_SEASIDE_086 = CAAT_Sea("Seaside 86", CType.R_ATLANTIC)
CAAT_SEASIDE_087 = CAAT_Sea("Seaside 87", CType.R_ATLANTIC)
CAAT_SEASIDE_088 = CAAT_Sea("Seaside 88", CType.R_ATLANTIC)
CAAT_SEASIDE_089 = CAAT_Sea("Seaside 89", CType.R_ATLANTIC)
CAAT_SEASIDE_090 = CAAT_Sea("Seaside 90", CType.R_ATLANTIC)
CAAT_SEASIDE_091 = CAAT_Sea("Seaside 91", CType.R_ATLANTIC)
CAAT_SEASIDE_092 = CAAT_Sea("Seaside 92", CType.R_MEDITERRANEAN_SEA)
CAAT_SEASIDE_093 = CAAT_Sea("Seaside 93", CType.R_MEDITERRANEAN_SEA)
CAAT_SEASIDE_094 = CAAT_Sea("Seaside 94", CType.R_MEDITERRANEAN_SEA)
CAAT_SEASIDE_095 = CAAT_Sea("Seaside 95", CType.R_MEDITERRANEAN_SEA, L_SEAZONE_95)
CAAT_SEASIDE_096 = CAAT_Sea("Seaside 96", CType.R_MEDITERRANEAN_SEA, L_SEAZONE_96)
CAAT_SEASIDE_097 = CAAT_Sea("Seaside 97", CType.R_MEDITERRANEAN_SEA, L_SEAZONE_97)
CAAT_SEASIDE_098 = CAAT_Sea("Seaside 98", CType.R_MEDITERRANEAN_SEA)
CAAT_SEASIDE_099 = CAAT_Sea("Seaside 99", CType.R_MEDITERRANEAN_SEA)
CAAT_SEASIDE_100 = CAAT_Sea("Seaside 100", CType.R_BLACK_SEA)
CAAT_SEASIDE_101 = CAAT_Sea("Seaside 101", CType.R_ATLANTIC)
CAAT_SEASIDE_102 = CAAT_Sea("Seaside 102", CType.R_ATLANTIC)
CAAT_SEASIDE_103 = CAAT_Sea("Seaside 103", CType.R_ATLANTIC, L_SEAZONE_103)
CAAT_SEASIDE_104 = CAAT_Sea("Seaside 104", CType.R_ATLANTIC)
CAAT_SEASIDE_105 = CAAT_Sea("Seaside 105", CType.R_ATLANTIC)
CAAT_SEASIDE_106 = CAAT_Sea("Seaside 106", CType.R_ATLANTIC)
CAAT_SEASIDE_107 = CAAT_Sea("Seaside 107", CType.R_ATLANTIC)
CAAT_SEASIDE_108 = CAAT_Sea("Seaside 108", CType.R_ATLANTIC, L_SEAZONE_108)
CAAT_SEASIDE_109 = CAAT_Sea("Seaside 109", CType.R_ATLANTIC)
CAAT_SEASIDE_110 = CAAT_Sea("Seaside 110", CType.R_NORTH_SEA)
CAAT_SEASIDE_111 = CAAT_Sea("Seaside 111", CType.R_NORTH_SEA)
CAAT_SEASIDE_112 = CAAT_Sea("Seaside 112", CType.R_NORTH_SEA)
CAAT_SEASIDE_113 = CAAT_Sea("Seaside 113", CType.R_BALTIC_SEA, L_SEAZONE_113)
CAAT_SEASIDE_114 = CAAT_Sea("Seaside 114", CType.R_BALTIC_SEA, L_SEAZONE_114)
CAAT_SEASIDE_115 = CAAT_Sea("Seaside 115", CType.R_BALTIC_SEA)
CAAT_SEASIDE_116 = CAAT_Sea("Seaside 116", CType.R_ATLANTIC)
CAAT_SEASIDE_117 = CAAT_Sea("Seaside 117", CType.R_ATLANTIC, L_SEAZONE_117)
CAAT_SEASIDE_118 = CAAT_Sea("Seaside 118", CType.R_ATLANTIC, L_SEAZONE_118)
CAAT_SEASIDE_119 = CAAT_Sea("Seaside 119", CType.R_ATLANTIC)
CAAT_SEASIDE_120 = CAAT_Sea("Seaside 120", CType.R_ATLANTIC)
CAAT_SEASIDE_121 = CAAT_Sea("Seaside 121", CType.R_ATLANTIC)
CAAT_SEASIDE_122 = CAAT_Sea("Seaside 122", CType.R_ATLANTIC)
CAAT_SEASIDE_123 = CAAT_Sea("Seaside 123", CType.R_ATLANTIC)
CAAT_SEASIDE_124 = CAAT_Sea("Seaside 124", CType.R_ATLANTIC, L_SEAZONE_124)
CAAT_SEASIDE_125 = CAAT_Sea("Seaside 125", CType.R_ATLANTIC)
CAAT_SEASIDE_126 = CAAT_Sea("Seaside 126", CType.R_ATLANTIC)
CAAT_SEASIDE_127 = CAAT_Sea("Seaside 127", CType.R_ARTIC_SEA)

CAAT_AFGHANISTAN               = CAAT_Land("Afghanistan",                   CType.R_ASIA_CENTRAL,     CAAN_AFGANISTAN,    4)
CAAT_ALASKA                    = CAAT_Land("Alaska",                        CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 2)
CAAT_ALBANIA                   = CAAT_Land("Albania",                       CType.R_EUROPE,           CAAN_ITALY,         1, L_ALBANIA)
CAAT_ALBERTA                   = CAAT_Land("Alberta Saskatchewan Manitoba", CType.R_NORDAMERICA,      CAAN_UK_AT,         1)
CAAT_ALEUTIAN                  = CAAT_Land("Aleutian Island",               CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 0)
CAAT_ALEXANDRIA                = CAAT_Land("Alexandria",                    CType.R_AFRICA,           CAAN_UK_AT,         0)
CAAT_ALGERIA                   = CAAT_Land("Algeria",                       CType.R_AFRICA,           CAAN_FRANCE,        1)
CAAT_AMUR                      = CAAT_Land("Amur",                          CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_ANGLO_EGYPTIAN_SUDAn      = CAAT_Land("Anglo Egyptian Sudan",          CType.R_AFRICA,           CAAN_ITALY,         1)
CAAT_ANGOLA                    = CAAT_Land("Angola",                        CType.R_AFRICA,           CAAN_ANGOLA,        1, [CAAU_Inf(CAAN_ANGOLA, 2)])
CAAT_ANHWE                     = CAAT_Land("Anhwe",                         CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_ARCHANGEL                 = CAAT_Land("Archangel",                     CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_ARGENTINIA                = CAAT_Land("Argentinia",                    CType.R_SOUTHAMERICA,     CAAN_ARGENTINA,     2, [CAAU_Inf(CAAN_ARGENTINA, 2)])
CAAT_BALTIC_STATES             = CAAT_Land("Baltic States",                 CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_BELGIAN_CONGO             = CAAT_Land("Belgian Congo",                 CType.R_AFRICA,           CAAN_UK_AT,         1)
CAAT_BESSARABIA                = CAAT_Land("Bessarabia",                    CType.R_EUROPE,           CAAN_SOVIET_UNION,  0)
CAAT_BOLIVIA                   = CAAT_Land("Bolivia",                       CType.R_SOUTHAMERICA,     CAAN_BOLIVIA,       0)
CAAT_BORNEO                    = CAAT_Land("Borneo",                        CType.R_ASIA_FAR_EAST,    CAAN_UK_PA,         4)
CAAT_BRAZIL                    = CAAT_Land("Brazil",                        CType.R_SOUTHAMERICA,     CAAN_BRAZIL,        3)
CAAT_BRITISH_GUIANA            = CAAT_Land("British Guiana",                CType.R_SOUTHAMERICA,     CAAN_UK_AT,         0)
CAAT_BRITISH_SOMALILAND        = CAAT_Land("British Somaliland",            CType.R_AFRICA,           CAAN_UK_AT,         0)
CAAT_BRYANSK                   = CAAT_Land("Bryansk",                       CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_BULGARIA                  = CAAT_Land("Bulgaria",                      CType.R_EUROPE,           CAAN_BULGARIA,      1, [CAAU_Inf(CAAN_BULGARIA, 4)])
CAAT_BURMA                     = CAAT_Land("Burma",                         CType.R_ASIA_FAR_EAST,    CAAN_UK_PA,         1)
CAAT_BURYATIA                  = CAAT_Land("Buryatia",                      CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_BUYANT_UHAA               = CAAT_Land("Buyant-Uhaa",                   CType.R_ASIA_FAR_EAST,    CAAN_MONGOLIA,      0, [CAAU_Inf(CAAN_MONGOLIA, 2)])
CAAT_CAUCASUS                  = CAAT_Land("Caucasus",                      CType.R_ASIA_CENTRAL,     CAAN_SOVIET_UNION,  2)
CAAT_CELEBES                   = CAAT_Land("Celebes",                       CType.R_ASIA_FAR_EAST,    CAAN_NETHERLANDS,   3)
CAAT_CENTRAL_AMERICA           = CAAT_Land("Central America",               CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 1)
CAAT_CENTRAL_MONGOLIA          = CAAT_Land("Central Mongolia",              CType.R_ASIA_FAR_EAST,    CAAN_MONGOLIA,      0)
CAAT_CENTRAL_US                = CAAT_Land("Central Unit States",           CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 12)
CAAT_CEYLON                    = CAAT_Land("Ceylon",                        CType.R_ASIA_FAR_EAST,    CAAN_UK_PA,         0)
CAAT_CHAHAR                    = CAAT_Land("Chahar",                        CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_CHILE                     = CAAT_Land("Chile",                         CType.R_SOUTHAMERICA,     CAAN_CHILE,         2, [CAAU_Inf(CAAN_CHILE, 2)])
CAAT_COLOMBIA                  = CAAT_Land("Colombia",                      CType.R_SOUTHAMERICA,     CAAN_CHINA,         0)
CAAT_CRETE                     = CAAT_Land("Crete",                         CType.R_EUROPE,           CAAN_GREECE,        0)
CAAT_CYPRUS                    = CAAT_Land("Cyprus",                        CType.R_EUROPE,           CAAN_UK_AT,         0)
CAAT_DENMARK                   = CAAT_Land("Denmark",                       CType.R_EUROPE,           CAAN_GERMANY,       2, L_DENMARK)
CAAT_DUTCH_NEW_GUINEA          = CAAT_Land("Dutch New Guinea",              CType.R_ASIA_FAR_EAST,    CAAN_NETHERLANDS,   0)
CAAT_DZAVHAN                   = CAAT_Land("Dzavhan",                       CType.R_ASIA_FAR_EAST,    CAAN_MONGOLIA,      0, [CAAU_Inf(CAAN_MONGOLIA, 1)])
CAAT_EASTERN_PERSIA            = CAAT_Land("Eastern Persia",                CType.R_ASIA_CENTRAL,     CAAN_PERSIA,        0)
CAAT_EASTERN_UNIT_STATES       = CAAT_Land("Eastern Unit States",           CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 20)
CAAT_ECUADOR                   = CAAT_Land("Ecuador",                       CType.R_SOUTHAMERICA,     CAAN_ECUADOR,       0)
CAAT_EGYPT                     = CAAT_Land("Egypt",                         CType.R_AFRICA,           CAAN_UK_AT,         2)
CAAT_EIRE                      = CAAT_Land("Eire",                          CType.R_EUROPE,           CAAN_EIRE,          0)
CAAT_ESTERN_POLAND             = CAAT_Land("Estern Poland",                 CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_ETHIOPIA                  = CAAT_Land("Ethiopia",                      CType.R_AFRICA,           CAAN_ITALY,         1, L_ETHOPIA)
CAAT_EVENKIYSKIY               = CAAT_Land("Evenkiyskiy",                   CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_FIJI                      = CAAT_Land("Fiji",                          CType.R_PACIFIC,          CAAN_UK_PA,         0)
CAAT_FINLAND                   = CAAT_Land("Finland",                       CType.R_EUROPE,           CAAN_FINNLAND,      2, [CAAU_Inf(CAAN_FINNLAND, 4)])
CAAT_FORMOSA                   = CAAT_Land("Formosa",                       CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         1)
CAAT_FRANCE                    = CAAT_Land("France",                        CType.R_EUROPE,           CAAN_FRANCE,        4)
CAAT_FRENCH_CENTRAL_AFRICA     = CAAT_Land("French Central Africa",         CType.R_AFRICA,           CAAN_FRANCE,        1)
CAAT_FRENCH_EQUATORIAL_AFRICA  = CAAT_Land("French Equatorial Africa",      CType.R_AFRICA,           CAAN_FRANCE,        1)
CAAT_FRENCH_GUIANA             = CAAT_Land("French Guiana",                 CType.R_SOUTHAMERICA,     CAAN_FRANCE,        0)
CAAT_FRENCH_INDO_CHINA         = CAAT_Land("French Indo China",             CType.R_ASIA_FAR_EAST,    CAAN_FRANCE,        2)
CAAT_FRENCH_MADAGASCAR         = CAAT_Land("French Madagascar",             CType.R_AFRICA,           CAAN_FRANCE,        1)
CAAT_FRENCH_WEST_AFRICA        = CAAT_Land("French West Africa",            CType.R_AFRICA,           CAAN_FRANCE,        1)
CAAT_GERMANY                   = CAAT_Land("Germany",                       CType.R_EUROPE,           CAAN_GERMANY,       5, L_GERMANY)
CAAT_GIBRALTER                 = CAAT_Land("Gibralter",                     CType.R_EUROPE,           CAAN_UK_AT,         0)
CAAT_GILBERT_ISLANDS           = CAAT_Land("Gilbert Islands",               CType.R_EUROPE,           CAAN_UK_PA,         0)
CAAT_GOLD_COAST                = CAAT_Land("Gold Coast",                    CType.R_EUROPE,           CAAN_UK_AT,         1)
CAAT_GREATER_SOUTHERN_GERMANY  = CAAT_Land("Greater Southern Germany",      CType.R_EUROPE,           CAAN_GERMANY,       4, L_GREATER_SOUTHERN_GERMANY)
CAAT_GREECE                    = CAAT_Land("Greece",                        CType.R_EUROPE,           CAAN_GREECE,        2, [CAAU_Inf(CAAN_GREECE,2)])
CAAT_GREENLAND                 = CAAT_Land("Greenland",                     CType.R_EUROPE,           CAAN_UNITED_STATES, 0)
CAAT_GUAM                      = CAAT_Land("Guam",                          CType.R_PACIFIC,          CAAN_UNITED_STATES, 0)
CAAT_HAINAN                    = CAAT_Land("Hainan",                        CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         0)
CAAT_HAWAIIAN_ISLANDS          = CAAT_Land("Hawaiian Islands",              CType.R_ASIA_FAR_EAST,    CAAN_UNITED_STATES, 1)
CAAT_HOLLAND_BELGIUM           = CAAT_Land("Holland Belgium",               CType.R_EUROPE,           CAAN_GERMANY,       3, L_HOLLAND_BELGIUM)
CAAT_HOPEI                     = CAAT_Land("Hopei",                         CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_HUNAN                     = CAAT_Land("Hunan",                         CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_ICELAND                   = CAAT_Land("Iceland",                       CType.R_EUROPE,           CAAN_UK_AT,         0)
CAAT_INDIA                     = CAAT_Land("India",                         CType.R_ASIA_FAR_EAST,    CAAN_UK_PA,         3)
CAAT_IRAQ                      = CAAT_Land("Iraq",                          CType.R_ASIA_CENTRAL,     CAAN_IRAQ,          2, [CAAU_Inf(CAAN_IRAQ, 3)])
CAAT_ITALIAN_SOMALILAND        = CAAT_Land("Italian Somaliland",            CType.R_AFRICA,           CAAN_ITALY,         0, L_ITALIAN_SOMALILAND)
CAAT_IWO_JIMA                  = CAAT_Land("Iwo Jima",                      CType.R_PACIFIC,          CAAN_JAPAN,         1)
CAAT_JAPAN                     = CAAT_Land("Japan",                         CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         8)
CAAT_JAVA                      = CAAT_Land("Java",                          CType.R_ASIA_FAR_EAST,    CAAN_NETHERLANDS,   4)
CAAT_JEHOL                     = CAAT_Land("Jehol",                         CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         1, [], CAAN_CHINA)
CAAT_JOHNSTON_ISLANDS          = CAAT_Land("Johnston Islands",              CType.R_PACIFIC,          CAAN_UNITED_STATES, 0)
CAAT_KANSU                     = CAAT_Land("Kansu",                         CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_KARELIA                   = CAAT_Land("Karelia",                       CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_KAZAKHSTAN                = CAAT_Land("Kazakhstan",                    CType.R_ASIA_CENTRAL,     CAAN_SOVIET_UNION,  1)
CAAT_KENYA                     = CAAT_Land("Kenya",                         CType.R_AFRICA,           CAAN_UK_AT,         1)
CAAT_KIANGSI                   = CAAT_Land("Kiangsi",                       CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         1, [], CAAN_CHINA)
CAAT_KIANGSU                   = CAAT_Land("Kiangsu",                       CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         3, [], CAAN_CHINA)
CAAT_KOREA                     = CAAT_Land("Korea",                         CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         3)
CAAT_KWANGSI                   = CAAT_Land("Kwangsi",                       CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         1, [], CAAN_CHINA)
CAAT_KWANGTUNG                 = CAAT_Land("Kwangtung",                     CType.R_ASIA_FAR_EAST,    CAAN_UK_PA,         3)
CAAT_KWEICHOW                  = CAAT_Land("Kweichow",                      CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_LIBERIA                   = CAAT_Land("Liberia",                       CType.R_AFRICA,           CAAN_LIBERIA,       0)
CAAT_LINE_ISLANDS              = CAAT_Land("Line Islands",                  CType.R_PACIFIC,          CAAN_UNITED_STATES, 0)
CAAT_LIBYA                     = CAAT_Land("Libya",                         CType.R_AFRICA,           CAAN_UK_AT,         0, L_LIBYA)
CAAT_MALAYA                    = CAAT_Land("Malaya",                        CType.R_ASIA_FAR_EAST,    CAAN_UK_PA,         3)
CAAT_MANCHURIA                 = CAAT_Land("Manchuria",                     CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         3, [], CAAN_CHINA)
##CAAT_MANILA                    = CAAT_Land("Manila",                      CType.
CAAT_MARIANAS                  = CAAT_Land("Marianas",                      CType.R_PACIFIC,          CAAN_JAPAN,         0)
CAAT_MARSHALL_ISLANDS          = CAAT_Land("Marshall Islands",              CType.R_PACIFIC,          CAAN_JAPAN,         0)
CAAT_MEXICO                    = CAAT_Land("Mexico",                        CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 2)
CAAT_MIDWAY                    = CAAT_Land("Midway",                        CType.R_PACIFIC,          CAAN_UNITED_STATES, 0)
CAAT_MOROCO                    = CAAT_Land("Moroco",                        CType.R_AFRICA,           CAAN_FRANCE,        1)
CAAT_MOZAMBIQUE                = CAAT_Land("Mozambique",                    CType.R_AFRICA,           CAAN_MOZAMBIQUE,    1, [CAAU_Inf(CAAN_MOZAMBIQUE)])
CAAT_NENETSIA                  = CAAT_Land("Nenetsia",                      CType.R_EUROPE,           CAAN_SOVIET_UNION,  0)
CAAT_NEW_BRITAIN               = CAAT_Land("New Britain",                   CType.R_PACIFIC,          CAAN_ANZAC,         0)
CAAT_NEW_BRUNSWICK_NOVA_SCOTIA = CAAT_Land("New Brunswick Nova Scotia",     CType.R_NORDAMERICA,      CAAN_UK_AT,         1)
CAAT_NEW_GUINEA                = CAAT_Land("New Guinea",                    CType.R_PACIFIC,          CAAN_ANZAC,         0)
CAAT_NEW_HEBRIDES              = CAAT_Land("New Hebrides",                  CType.R_PACIFIC,          CAAN_FRANCE,        0)
CAAT_NEW_SOUTH_WALES           = CAAT_Land("New South Wales",               CType.R_AUSTRALIA,        CAAN_ANZAC,         2)
CAAT_NEW_ZEALAND               = CAAT_Land("New Zealand",                   CType.R_PACIFIC,          CAAN_ANZAC,         2)
CAAT_NEWFOUNDLAND_LABRADOR     = CAAT_Land("Newfoundland Labrador",         CType.R_NORDAMERICA,      CAAN_UK_AT,         2)
CAAT_MIDWAY                    = CAAT_Land("Midway",                        CType.R_PACIFIC,          CAAN_ANZAC,         0)
CAAT_NIGERIA                   = CAAT_Land("Nigeria",                       CType.R_AFRICA,           CAAN_UK_AT,         1)
CAAT_NORMANDY_BORDEAUX         = CAAT_Land("Normandy Bordeaux",             CType.R_EUROPE,           CAAN_FRANCE,        2)
CAAT_NORTHERN_ITALY            = CAAT_Land("Northern Italy",                CType.R_EUROPE,           CAAN_ITALY,         4, L_NORTHERN_ITALY)
CAAT_NORTHERN_TERRITORY        = CAAT_Land("Northern Territory",            CType.R_AUSTRALIA,        CAAN_ANZAC,         1)
CAAT_NORTHWEST_PERSIA          = CAAT_Land("Northwest Persia",              CType.R_ASIA_CENTRAL,     CAAN_PERSIA,        0)
CAAT_NORWAY                    = CAAT_Land("Norway",                        CType.R_EUROPE,           CAAN_GERMANY,       3, L_NORWAY)
CAAT_NOVGOROD                  = CAAT_Land("Novgorod",                      CType.R_EUROPE,           CAAN_SOVIET_UNION,  2)
CAAT_NOVOSIBIRSK               = CAAT_Land("Novosibirsk",                   CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_OKINAWA                   = CAAT_Land("Okinawa",                       CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         1)
CAAT_OLGIY                     = CAAT_Land("Olgiy",                         CType.R_ASIA_FAR_EAST,    CAAN_MONGOLIA,      0, [CAAU_Inf(CAAN_MONGOLIA)])
CAAT_ONTARIO                   = CAAT_Land("Ontario",                       CType.R_NORDAMERICA,      CAAN_UK_AT,         2)
CAAT_PALAU_ISLAND              = CAAT_Land("Palau Island",                  CType.R_PACIFIC,          CAAN_JAPAN,         0)
CAAT_PARAGUAY                  = CAAT_Land("Paraguay",                      CType.R_SOUTHAMERICA,     CAAN_PARAQUAY,      0)
CAAT_PERSIA                    = CAAT_Land("Persia",                        CType.R_ASIA_CENTRAL,     CAAN_PERSIA,        2, [CAAU_Inf(CAAN_PERSIA, 2)])
CAAT_PERU                      = CAAT_Land("Peru",                          CType.R_SOUTHAMERICA,     CAAN_PERU,          0)
CAAT_PHILLIPINES               = CAAT_Land("Phillipines",                   CType.R_PACIFIC,          CAAN_UNITED_STATES, 2)
CAAT_POLAND                    = CAAT_Land("Poland",                        CType.R_EUROPE,           CAAN_GERMANY,       2, L_POLAND)
CAAT_PORTUGAL                  = CAAT_Land("Portugal",                      CType.R_EUROPE,           CAAN_PORTUGAL,      1, [CAAU_Inf(CAAN_PORTUGAL, 2)])
CAAT_PORTUGUESE                = CAAT_Land("Portuguese Guinea",             CType.R_AFRICA,           CAAN_PORTUGAL,      0)
CAAT_QUEBEC                    = CAAT_Land("Quebec",                        CType.R_NORDAMERICA,      CAAN_UK_AT,         2)
CAAT_QUEENSLAND                = CAAT_Land("Queensland",                    CType.R_AUSTRALIA,        CAAN_ANZAC,         2)
CAAT_RHODESIA                  = CAAT_Land("Rhodesia",                      CType.R_AFRICA,           CAAN_UK_AT,         1)
CAAT_RIO_DE_ORO                = CAAT_Land("Rio de Oro",                    CType.R_AFRICA,           CAAN_RIO_DE_ORO,    0)
CAAT_ROMANIA                   = CAAT_Land("Romania",                       CType.R_EUROPE,           CAAN_GERMANY,       1, L_ROMANIA)
CAAT_ROSTOV                    = CAAT_Land("Rostov",                        CType.R_EUROPE,           CAAN_SOVIET_UNION,  2)
CAAT_RUSSIA                    = CAAT_Land("Russia",                        CType.R_EUROPE,           CAAN_SOVIET_UNION,  3)
CAAT_SAKHA                     = CAAT_Land("Sakha",                         CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_SAMARA                    = CAAT_Land("Samara",                        CType.R_ASIA_CENTRAL,     CAAN_SOVIET_UNION,  1)
CAAT_SAMOA                     = CAAT_Land("Samoa",                         CType.R_PACIFIC,          CAAN_UK_PA,         0)
CAAT_SARDINIA                  = CAAT_Land("Sardinia",                      CType.R_EUROPE,           CAAN_ITALY,         0)
CAAT_SAUDI_ARABIA              = CAAT_Land("Saudi Arabia",                  CType.R_ASIA_MIDDLE_EAST, CAAN_SAUDI_ARABIA, 2, [CAAU_Inf(CAAN_SAUDI_ARABIA, 2)])
CAAT_SCOTLAND                  = CAAT_Land("Scotland",                      CType.R_EUROPE,           CAAN_UK_AT,         2)
CAAT_SHAN_STATE                = CAAT_Land("Shan State",                    CType.R_ASIA_FAR_EAST,    CAAN_UK_PA,         1)
CAAT_SHANTUNG                  = CAAT_Land("Shantung",                      CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         1, [], CAAN_CHINA)
CAAT_SHENSI                    = CAAT_Land("Shensi",                        CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_SIAM                      = CAAT_Land("Siam",                          CType.R_ASIA_FAR_EAST,    CAAN_JAPAN,         1)
CAAT_SIBERIA                   = CAAT_Land("Siberia",                       CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_SICILY                    = CAAT_Land("Sicily",                        CType.R_EUROPE,           CAAN_ITALY,         0)
CAAT_SIERRA_LEONE              = CAAT_Land("Sierra Leone",                  CType.R_AFRICA,           CAAN_SIERA_LEONE,   0)
CAAT_SIKANG                    = CAAT_Land("Sikang",                        CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_SLOVAKIA_HUNGARY          = CAAT_Land("Slovakia Hungary",              CType.R_EUROPE,           CAAN_GERMANY,       3, L_SLOVAKIA_HUNGARY)
CAAT_SMOLENSK                  = CAAT_Land("Smolensk",                      CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_SOLOMON_ISLANDS           = CAAT_Land("Solomon Islands",               CType.R_PACIFIC,          CAAN_ANZAC,         0)
CAAT_SOUTH_AUSTRALIA           = CAAT_Land("South Australia",               CType.R_AUSTRALIA,        CAAN_ANZAC,         1)
CAAT_SOUTH_EAST_MEXICO         = CAAT_Land("South East Mexico",             CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 1)
CAAT_SOUTH_WEST_AFRICA         = CAAT_Land("South West Africa",             CType.R_AFRICA,           CAAN_UK_AT,         1)
CAAT_SOUTHERN_FRANCE           = CAAT_Land("Southern France",               CType.R_EUROPE,           CAAN_FRANCE,        3)
CAAT_SOUTHERN_ITALY            = CAAT_Land("Southern Italy",                CType.R_EUROPE,           CAAN_ITALY,         3, L_SOUTHERN_ITALY)
CAAT_SOVIET_FAR_EAST           = CAAT_Land("Soviet Far East",               CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_SPAIN                     = CAAT_Land("Spain",                         CType.R_EUROPE,           CAAN_SPAIN,         6)
CAAT_SUIYUAN                   = CAAT_Land("Suiyuan",                       CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_SUMATRA                   = CAAT_Land("Sumatra",                       CType.R_PACIFIC,          CAAN_NETHERLANDS,   4)
CAAT_SURINAME                  = CAAT_Land("Suriname",                      CType.R_SOUTHAMERICA,     CAAN_NETHERLANDS,   0)
CAAT_SWEDEN                    = CAAT_Land("Sweden",                        CType.R_EUROPE,           CAAN_SWEDEN,        3, [CAAU_Inf(CAAN_SWEDEN, 6)])
CAAT_SWITZERLAND               = CAAT_Land("Switzerland",                   CType.R_EUROPE,           CAAN_SWITZERLAND,   0, [CAAU_Inf(CAAN_SWITZERLAND, 2)])
CAAT_SYRIA                     = CAAT_Land("Syria",                         CType.R_ASIA_MIDDLE_EAST, CAAN_FRANCE,        1)
CAAT_SZECHWAN                  = CAAT_Land("Szechwan",                      CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_TAMBOV                    = CAAT_Land("Tambov",                        CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_TANGANYIKA_TERRITORY      = CAAT_Land("Tanganyika Territory",          CType.R_AFRICA,           CAAN_UK_AT,         1)
CAAT_TIMGUSKA                  = CAAT_Land("Timguska",                      CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_TOBRUK                    = CAAT_Land("Tobruk",                        CType.R_AFRICA,           CAAN_UK_AT,         0, L_TOBRUK)
CAAT_TRANS_JORDAN              = CAAT_Land("Trans-Jordan",                  CType.R_ASIA_MIDDLE_EAST, CAAN_UK_AT,         1)
CAAT_TSAGAAN_OLOM              = CAAT_Land("Tsagaan-Olom",                  CType.R_ASIA_FAR_EAST,    CAAN_MONGOLIA,      0)
CAAT_TSINGHAI                  = CAAT_Land("Tsinghai",                      CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)
CAAT_TUNISIA                   = CAAT_Land("Tunisia",                       CType.R_AFRICA,           CAAN_FRANCE,        1)
CAAT_TURKEY                    = CAAT_Land("Turkey",                        CType.R_ASIA_MIDDLE_EAST, CAAN_TURKEY,        2, [CAAU_Inf(CAAN_TURKEY,2)])
CAAT_TURKMENISTAN              = CAAT_Land("Turkmenistan",                  CType.R_ASIA_MIDDLE_EAST, CAAN_SOVIET_UNION,  0)
CAAT_UKRAINE                   = CAAT_Land("Ukraine",                       CType.R_EUROPE,           CAAN_SOVIET_UNION,  2)
CAAT_ULAANBAATAR               = CAAT_Land("Ulaanbaatar",                   CType.R_ASIA_FAR_EAST,    CAAN_MONGOLIA,      0,[CAAU_Inf(CAAN_MONGOLIA, 1)])
CAAT_UNION_OF_SOUTH_AFRICA     = CAAT_Land("Union of South Africa",         CType.R_AFRICA,           CAAN_UK_AT,         2)
CAAT_UNITED_KINGDOM            = CAAT_Land("United Kingdom",                CType.R_EUROPE,           CAAN_UK_AT,         6)
CAAT_URALS                     = CAAT_Land("Urals",                         CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_URUGUAY                   = CAAT_Land("Uruguay",                       CType.R_SOUTHAMERICA,     CAAN_URUGUAY,       0)
CAAT_VENEZUELA                 = CAAT_Land("Venezuela",                     CType.R_SOUTHAMERICA,     CAAN_VENEZUELA,     2, [CAAU_Inf(CAAN_VENEZUELA,2)])
CAAT_VICTORIA                  = CAAT_Land("Victoria",                      CType.R_AUSTRALIA,        CAAN_ANZAC,         1)
CAAT_VOLGOGRAD                 = CAAT_Land("Volgograd",                     CType.R_EUROPE,           CAAN_SOVIET_UNION,  2)
CAAT_VOLODGA                   = CAAT_Land("Volodga",                       CType.R_EUROPE,           CAAN_SOVIET_UNION,  1)
CAAT_VYBORG                    = CAAT_Land("Vyborg",                        CType.R_EUROPE,           CAAN_SOVIET_UNION,  0)
CAAT_WAKE_ISLAND               = CAAT_Land("Wake Island",                   CType.R_PACIFIC,          CAAN_UNITED_STATES, 0)
CAAT_WEST_INDIA                = CAAT_Land("West India",                    CType.R_ASIA_FAR_EAST,    CAAN_UK_AT,         2)
CAAT_WEST_INDIES               = CAAT_Land("West Indies",                   CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 1)
CAAT_WESTERN_AUSTRALIA         = CAAT_Land("Western Australia",             CType.R_AUSTRALIA,        CAAN_ANZAC,         1)
CAAT_WESTERN_CANADA            = CAAT_Land("Western Canada",                CType.R_NORDAMERICA,      CAAN_UK_PA,         1)
CAAT_WESTERN_GERMANY           = CAAT_Land("Western Germany",               CType.R_EUROPE,           CAAN_GERMANY,       5, L_WESTERN_GERMANY)
CAAT_WESTERN_UKRAINE           = CAAT_Land("Western Ukraine",               CType.R_EUROPE,           CAAN_SOVIET_UNION,  2)
CAAT_WESTERN_UNITED_STATES     = CAAT_Land("Western United States",         CType.R_NORDAMERICA,      CAAN_UNITED_STATES, 10)
CAAT_YAKUT                     = CAAT_Land("Yakut S.S.R",                   CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_YENISEY                   = CAAT_Land("Yenisey",                       CType.R_ASIA_FAR_EAST,    CAAN_SOVIET_UNION,  1)
CAAT_YUGOSLAVIA                = CAAT_Land("Yugoslavia",                    CType.R_EUROPE,           CAAN_YUGOSLAVIA,    2, [CAAU_Inf(CAAN_YUGOSLAVIA, 4)])
CAAT_YUNNAN                    = CAAT_Land("Yunnan",                        CType.R_ASIA_FAR_EAST,    CAAN_CHINA,         1)

##############################################################################
# Set neighbores
##############################################################################

CAAT_SEASIDE_001.set_neighbores({'n':CAAT_ALASKA, 'ne': CAAT_SEASIDE_002, 'e': CAAT_SEASIDE_008,'se': CAAT_SEASIDE_008, 's': [CAAT_SEASIDE_009, CAAT_SEASIDE_010], 'sw':CAAT_WESTERN_UNITED_STATES, 'w': CAAT_WESTERN_CANADA, 'nw':CAAT_ALASKA})
CAAT_SEASIDE_002.set_neighbores({'n':None,        'ne': None,             'e': CAAT_SEASIDE_003,'se': CAAT_SEASIDE_008, 's': CAAT_SEASIDE_008,                     'sw':CAAT_SEASIDE_001,           'w': CAAT_ALASKA,         'nw':CAAT_ALASKA})
CAAT_SEASIDE_003.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': CAAT_SEASIDE_008, 'sw':None, 'w': CAAT_SEASIDE_002, 'nw':None})
CAAT_SEASIDE_004.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_005.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_006.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_007.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_008.set_neighbores({'n':CAAT_SEASIDE_002, 'ne': CAAT_SEASIDE_002, 'e':None,  'se':None, 's': None, 'sw':None, 'w': CAAT_SEASIDE_001, 'nw':CAAT_SEASIDE_002})
CAAT_SEASIDE_009.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_010.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_011.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_012.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_013.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_014.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_015.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_016.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_017.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_018.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_019.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_020.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_021.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_022.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_023.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_024.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_025.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_026.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_027.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_028.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_029.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_030.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_031.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_031.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_031.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_031.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_034.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_035.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_036.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_037.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_038.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_039.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_040.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_041.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_042.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_043.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_044.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_045.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_046.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_047.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_048.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_049.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_050.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_051.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_052.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_053.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_054.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_055.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_056.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_057.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_058.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_059.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_060.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_061.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_062.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_063.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_064.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_065.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_066.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_067.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_068.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_069.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_070.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_071.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_072.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_073.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_074.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_075.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_076.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_077.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_078.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_079.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_080.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_081.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_082.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_083.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_084.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_085.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_086.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_087.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_088.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_089.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_090.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_091.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_092.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_093.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_094.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_095.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_096.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_097.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_098.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_099.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_100.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_101.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_102.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_103.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_104.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_105.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_106.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_107.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_108.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_109.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_110.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_111.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_112.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_113.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_114.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_115.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_116.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_117.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_118.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_119.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_120.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_121.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_122.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_123.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_124.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_125.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_126.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SEASIDE_127.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})

CAAT_AFGHANISTAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ALASKA.set_neighbores({'n':None, 'ne': None, 'e': CAAT_SEASIDE_002, 'se':CAAT_SEASIDE_002, 's': CAAT_SEASIDE_001, 'sw':None, 'w': None, 'nw':None})
CAAT_ALBANIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ALBERTA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ALEUTIAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ALEXANDRIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ALGERIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_AMUR.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ANGLO_EGYPTIAN_SUDAn.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ANGOLA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ANHWE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ARCHANGEL.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ARGENTINIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BALTIC_STATES.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BELGIAN_CONGO.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BESSARABIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BOLIVIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BORNEO.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BRAZIL.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BRITISH_GUIANA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BRITISH_SOMALILAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BRYANSK.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BULGARIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BURMA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BURYATIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_BUYANT_UHAA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CAUCASUS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CELEBES.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CENTRAL_AMERICA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CENTRAL_MONGOLIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CENTRAL_US.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CEYLON.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CHAHAR.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CHILE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_COLOMBIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CRETE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_CYPRUS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_DENMARK.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_DUTCH_NEW_GUINEA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_DZAVHAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_EASTERN_PERSIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_EASTERN_UNIT_STATES.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ECUADOR.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_EGYPT.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_EIRE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ESTERN_POLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ETHIOPIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_EVENKIYSKIY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FIJI.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FINLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FORMOSA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FRANCE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FRENCH_CENTRAL_AFRICA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FRENCH_EQUATORIAL_AFRICA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FRENCH_GUIANA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FRENCH_INDO_CHINA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FRENCH_MADAGASCAR.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_FRENCH_WEST_AFRICA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GERMANY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GIBRALTER.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GILBERT_ISLANDS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GOLD_COAST.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GREATER_SOUTHERN_GERMANY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GREECE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GREENLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_GUAM.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_HAINAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_HAWAIIAN_ISLANDS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_HOLLAND_BELGIUM.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_HOPEI.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_HUNAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ICELAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_INDIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_IRAQ.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ITALIAN_SOMALILAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_IWO_JIMA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_JAPAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_JAVA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_JEHOL.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_JOHNSTON_ISLANDS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KANSU.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KARELIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KAZAKHSTAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KENYA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KIANGSI.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KIANGSU.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KOREA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KWANGSI.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KWANGTUNG.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_KWEICHOW.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_LIBERIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_LINE_ISLANDS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_LIBYA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MALAYA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MANCHURIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
##CAAT_MANILA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MARIANAS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MARSHALL_ISLANDS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MEXICO.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MIDWAY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MOROCO.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MOZAMBIQUE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NENETSIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NEW_BRITAIN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NEW_BRUNSWICK_NOVA_SCOTIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NEW_GUINEA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NEW_HEBRIDES.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NEW_SOUTH_WALES.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NEW_ZEALAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NEWFOUNDLAND_LABRADOR.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_MIDWAY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NIGERIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NORMANDY_BORDEAUX.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NORTHERN_ITALY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NORTHERN_TERRITORY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NORTHWEST_PERSIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NORWAY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NOVGOROD.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_NOVOSIBIRSK.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_OKINAWA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_OLGIY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ONTARIO.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_PALAU_ISLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_PARAGUAY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_PERSIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_PERU.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_PHILLIPINES.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_POLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_PORTUGAL.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_PORTUGUESE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_QUEBEC.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_QUEENSLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_RHODESIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_RIO_DE_ORO.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ROMANIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ROSTOV.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_RUSSIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SAKHA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SAMARA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SAMOA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SARDINIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SAUDI_ARABIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SCOTLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SHAN_STATE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SHANTUNG.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SHENSI.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SIAM.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SIBERIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SICILY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SIERRA_LEONE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SIKANG.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SLOVAKIA_HUNGARY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SMOLENSK.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SOLOMON_ISLANDS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SOUTH_AUSTRALIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SOUTH_EAST_MEXICO.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SOUTH_WEST_AFRICA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SOUTHERN_FRANCE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SOUTHERN_ITALY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SOVIET_FAR_EAST.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SPAIN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SUIYUAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SUMATRA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SURINAME.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SWEDEN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SWITZERLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SYRIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_SZECHWAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TAMBOV.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TANGANYIKA_TERRITORY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TIMGUSKA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TOBRUK.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TRANS_JORDAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TSAGAAN_OLOM.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TSINGHAI.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TUNISIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TURKEY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_TURKMENISTAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_UKRAINE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_ULAANBAATAR.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_UNION_OF_SOUTH_AFRICA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_UNITED_KINGDOM.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_URALS.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_URUGUAY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_VENEZUELA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_VICTORIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_VOLGOGRAD.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_VOLODGA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_VYBORG.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WAKE_ISLAND.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WEST_INDIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WEST_INDIES.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WESTERN_AUSTRALIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WESTERN_CANADA.set_neighbores({'n':None, 'ne': None, 'e':CAAT_SEASIDE_001,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WESTERN_GERMANY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WESTERN_UKRAINE.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_WESTERN_UNITED_STATES.set_neighbores({'n':None, 'ne': CAAT_SEASIDE_001, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_YAKUT.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_YENISEY.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_YUGOSLAVIA.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})
CAAT_YUNNAN.set_neighbores({'n':None, 'ne': None, 'e':None,  'se':None, 's': None, 'sw':None, 'w': None, 'nw':None})


L_NATION_SETUP_GLOBAL_1940 = [
    CAAN_GERMANY,
    CAAN_SOVIET_UNION,
    CAAN_JAPAN,
    CAAN_UNITED_STATES,
    CAAN_CHINA,
    CAAN_UK_AT,
    CAAN_UK_PA,
    CAAN_ITALY,
    CAAN_ANZAC,
    CAAN_FRANCE
]

L_TERRITORIES_SETUP_GLOBAL_1940 = [
    CAAT_SEASIDE_001,
    CAAT_SEASIDE_002,
    CAAT_SEASIDE_003,
    CAAT_SEASIDE_004,
    CAAT_SEASIDE_005,
    CAAT_SEASIDE_006,
    CAAT_SEASIDE_007,
    CAAT_SEASIDE_008,
    CAAT_SEASIDE_009,
    CAAT_SEASIDE_010,
    CAAT_SEASIDE_011,
    CAAT_SEASIDE_012,
    CAAT_SEASIDE_013,
    CAAT_SEASIDE_014,
    CAAT_SEASIDE_015,
    CAAT_SEASIDE_016,
    CAAT_SEASIDE_017,
    CAAT_SEASIDE_018,
    CAAT_SEASIDE_019,
    CAAT_SEASIDE_020,
    CAAT_SEASIDE_021,
    CAAT_SEASIDE_022,
    CAAT_SEASIDE_023,
    CAAT_SEASIDE_024,
    CAAT_SEASIDE_025,
    CAAT_SEASIDE_026,
    CAAT_SEASIDE_027,
    CAAT_SEASIDE_028,
    CAAT_SEASIDE_029,
    CAAT_SEASIDE_030,
    CAAT_SEASIDE_031,
    CAAT_SEASIDE_032,
    CAAT_SEASIDE_033,
    CAAT_SEASIDE_034,
    CAAT_SEASIDE_035,
    CAAT_SEASIDE_036,
    CAAT_SEASIDE_037,
    CAAT_SEASIDE_038,
    CAAT_SEASIDE_039,
    CAAT_SEASIDE_040,
    CAAT_SEASIDE_041,
    CAAT_SEASIDE_042,
    CAAT_SEASIDE_043,
    CAAT_SEASIDE_044,
    CAAT_SEASIDE_045,
    CAAT_SEASIDE_046,
    CAAT_SEASIDE_047,
    CAAT_SEASIDE_048,
    CAAT_SEASIDE_049,
    CAAT_SEASIDE_050,
    CAAT_SEASIDE_051,
    CAAT_SEASIDE_052,
    CAAT_SEASIDE_053,
    CAAT_SEASIDE_054,
    CAAT_SEASIDE_055,
    CAAT_SEASIDE_056,
    CAAT_SEASIDE_057,
    CAAT_SEASIDE_058,
    CAAT_SEASIDE_059,
    CAAT_SEASIDE_060,
    CAAT_SEASIDE_061,
    CAAT_SEASIDE_062,
    CAAT_SEASIDE_063,
    CAAT_SEASIDE_064,
    CAAT_SEASIDE_065,
    CAAT_SEASIDE_066,
    CAAT_SEASIDE_067,
    CAAT_SEASIDE_068,
    CAAT_SEASIDE_069,
    CAAT_SEASIDE_070,
    CAAT_SEASIDE_071,
    CAAT_SEASIDE_072,
    CAAT_SEASIDE_073,
    CAAT_SEASIDE_074,
    CAAT_SEASIDE_075,
    CAAT_SEASIDE_076,
    CAAT_SEASIDE_077,
    CAAT_SEASIDE_078,
    CAAT_SEASIDE_079,
    CAAT_SEASIDE_080,
    CAAT_SEASIDE_081,
    CAAT_SEASIDE_082,
    CAAT_SEASIDE_083,
    CAAT_SEASIDE_084,
    CAAT_SEASIDE_085,
    CAAT_SEASIDE_086,
    CAAT_SEASIDE_087,
    CAAT_SEASIDE_088,
    CAAT_SEASIDE_089,
    CAAT_SEASIDE_090,
    CAAT_SEASIDE_091,
    CAAT_SEASIDE_092,
    CAAT_SEASIDE_093,
    CAAT_SEASIDE_094,
    CAAT_SEASIDE_095,
    CAAT_SEASIDE_096,
    CAAT_SEASIDE_097,
    CAAT_SEASIDE_098,
    CAAT_SEASIDE_099,
    CAAT_SEASIDE_100,
    CAAT_SEASIDE_101,
    CAAT_SEASIDE_102,
    CAAT_SEASIDE_103,
    CAAT_SEASIDE_104,
    CAAT_SEASIDE_105,
    CAAT_SEASIDE_106,
    CAAT_SEASIDE_107,
    CAAT_SEASIDE_108,
    CAAT_SEASIDE_109,
    CAAT_SEASIDE_110,
    CAAT_SEASIDE_111,
    CAAT_SEASIDE_112,
    CAAT_SEASIDE_113,
    CAAT_SEASIDE_114,
    CAAT_SEASIDE_115,
    CAAT_SEASIDE_116,
    CAAT_SEASIDE_117,
    CAAT_SEASIDE_118,
    CAAT_SEASIDE_119,
    CAAT_SEASIDE_120,
    CAAT_SEASIDE_121,
    CAAT_SEASIDE_122,
    CAAT_SEASIDE_123,
    CAAT_SEASIDE_124,
    CAAT_SEASIDE_125,
    CAAT_SEASIDE_126,
    CAAT_SEASIDE_127,

    CAAT_AFGHANISTAN,
    CAAT_ALASKA,
    CAAT_ALBANIA,
    CAAT_ALBERTA,
    CAAT_ALEUTIAN,
    CAAT_ALEXANDRIA,
    CAAT_ALGERIA,
    CAAT_AMUR,
    CAAT_ANGLO_EGYPTIAN_SUDAn,
    CAAT_ANGOLA,
    CAAT_ANHWE,
    CAAT_ARCHANGEL,
    CAAT_ARGENTINIA,
    CAAT_BALTIC_STATES,
    CAAT_BELGIAN_CONGO,
    CAAT_BESSARABIA,
    CAAT_BOLIVIA,
    CAAT_BORNEO,
    CAAT_BRAZIL,
    CAAT_BRITISH_GUIANA,
    CAAT_BRITISH_SOMALILAND,
    CAAT_BRYANSK,
    CAAT_BULGARIA,
    CAAT_BURMA,
    CAAT_BURYATIA,
    CAAT_BUYANT_UHAA,
    CAAT_CAUCASUS,
    CAAT_CELEBES,
    CAAT_CENTRAL_AMERICA,
    CAAT_CENTRAL_MONGOLIA,
    CAAT_CENTRAL_US,
    CAAT_CEYLON,
    CAAT_CHAHAR,
    CAAT_CHILE,
    CAAT_COLOMBIA,
    CAAT_CRETE,
    CAAT_CYPRUS,
    CAAT_DENMARK,
    CAAT_DUTCH_NEW_GUINEA,
    CAAT_DZAVHAN,
    CAAT_EASTERN_PERSIA,
    CAAT_EASTERN_UNIT_STATES,
    CAAT_ECUADOR,
    CAAT_EGYPT,
    CAAT_EIRE,
    CAAT_ESTERN_POLAND,
    CAAT_ETHIOPIA,
    CAAT_EVENKIYSKIY,
    CAAT_FIJI,
    CAAT_FINLAND,
    CAAT_FORMOSA,
    CAAT_FRANCE,
    CAAT_FRENCH_CENTRAL_AFRICA,
    CAAT_FRENCH_EQUATORIAL_AFRICA,
    CAAT_FRENCH_GUIANA,
    CAAT_FRENCH_INDO_CHINA,
    CAAT_FRENCH_MADAGASCAR,
    CAAT_FRENCH_WEST_AFRICA,
    CAAT_GERMANY,
    CAAT_GIBRALTER,
    CAAT_GILBERT_ISLANDS,
    CAAT_GOLD_COAST,
    CAAT_GREATER_SOUTHERN_GERMANY,
    CAAT_GREECE,
    CAAT_GREENLAND,
    CAAT_GUAM,
    CAAT_HAINAN,
    CAAT_HAWAIIAN_ISLANDS,
    CAAT_HOLLAND_BELGIUM,
    CAAT_HOPEI,
    CAAT_HUNAN,
    CAAT_ICELAND,
    CAAT_INDIA,
    CAAT_IRAQ,
    CAAT_ITALIAN_SOMALILAND,
    CAAT_IWO_JIMA,
    CAAT_JAPAN,
    CAAT_JAVA,
    CAAT_JEHOL,
    CAAT_JOHNSTON_ISLANDS,
    CAAT_KANSU,
    CAAT_KARELIA,
    CAAT_KAZAKHSTAN,
    CAAT_KENYA,
    CAAT_KIANGSI,
    CAAT_KIANGSU,
    CAAT_KOREA,
    CAAT_KWANGSI,
    CAAT_KWANGTUNG,
    CAAT_KWEICHOW,
    CAAT_LIBERIA,
    CAAT_LINE_ISLANDS,
    CAAT_LIBYA,
    CAAT_MALAYA,
    CAAT_MANCHURIA,
    ##CAAT_MANILA,
    CAAT_MARIANAS,
    CAAT_MARSHALL_ISLANDS,
    CAAT_MEXICO,
    CAAT_MIDWAY,
    CAAT_MOROCO,
    CAAT_MOZAMBIQUE,
    CAAT_NENETSIA,
    CAAT_NEW_BRITAIN,
    CAAT_NEW_BRUNSWICK_NOVA_SCOTIA,
    CAAT_NEW_GUINEA,
    CAAT_NEW_HEBRIDES,
    CAAT_NEW_SOUTH_WALES,
    CAAT_NEW_ZEALAND,
    CAAT_NEWFOUNDLAND_LABRADOR,
    CAAT_NIGERIA,
    CAAT_NORMANDY_BORDEAUX,
    CAAT_NORTHERN_ITALY,
    CAAT_NORTHERN_TERRITORY,
    CAAT_NORTHWEST_PERSIA,
    CAAT_NORWAY,
    CAAT_NOVGOROD,
    CAAT_NOVOSIBIRSK,
    CAAT_OKINAWA,
    CAAT_OLGIY,
    CAAT_ONTARIO,
    CAAT_PALAU_ISLAND,
    CAAT_PARAGUAY,
    CAAT_PERSIA,
    CAAT_PERU,
    CAAT_PHILLIPINES,
    CAAT_POLAND,
    CAAT_PORTUGAL,
    CAAT_PORTUGUESE,
    CAAT_QUEBEC,
    CAAT_QUEENSLAND,
    CAAT_RHODESIA,
    CAAT_RIO_DE_ORO,
    CAAT_ROMANIA,
    CAAT_ROSTOV,
    CAAT_RUSSIA,
    CAAT_SAKHA,
    CAAT_SAMARA,
    CAAT_SAMOA,
    CAAT_SARDINIA,
    CAAT_SAUDI_ARABIA,
    CAAT_SCOTLAND,
    CAAT_SHAN_STATE,
    CAAT_SHANTUNG,
    CAAT_SHENSI,
    CAAT_SIAM,
    CAAT_SIBERIA,
    CAAT_SICILY,
    CAAT_SIERRA_LEONE,
    CAAT_SIKANG,
    CAAT_SLOVAKIA_HUNGARY,
    CAAT_SMOLENSK,
    CAAT_SOLOMON_ISLANDS,
    CAAT_SOUTH_AUSTRALIA,
    CAAT_SOUTH_EAST_MEXICO,
    CAAT_SOUTH_WEST_AFRICA,
    CAAT_SOUTHERN_FRANCE,
    CAAT_SOUTHERN_ITALY,
    CAAT_SOVIET_FAR_EAST,
    CAAT_SPAIN,
    CAAT_SUIYUAN,
    CAAT_SUMATRA,
    CAAT_SURINAME,
    CAAT_SWEDEN,
    CAAT_SWITZERLAND,
    CAAT_SYRIA,
    CAAT_SZECHWAN,
    CAAT_TAMBOV,
    CAAT_TANGANYIKA_TERRITORY,
    CAAT_TIMGUSKA,
    CAAT_TOBRUK,
    CAAT_TRANS_JORDAN,
    CAAT_TSAGAAN_OLOM,
    CAAT_TSINGHAI,
    CAAT_TUNISIA,
    CAAT_TURKEY,
    CAAT_TURKMENISTAN,
    CAAT_UKRAINE,
    CAAT_ULAANBAATAR,
    CAAT_UNION_OF_SOUTH_AFRICA,
    CAAT_UNITED_KINGDOM,
    CAAT_URALS,
    CAAT_URUGUAY,
    CAAT_VENEZUELA,
    CAAT_VICTORIA,
    CAAT_VOLGOGRAD,
    CAAT_VOLODGA,
    CAAT_VYBORG,
    CAAT_WAKE_ISLAND,
    CAAT_WEST_INDIA,
    CAAT_WEST_INDIES,
    CAAT_WESTERN_AUSTRALIA,
    CAAT_WESTERN_CANADA,
    CAAT_WESTERN_GERMANY,
    CAAT_WESTERN_UKRAINE,
    CAAT_WESTERN_UNITED_STATES,
    CAAT_YAKUT,
    CAAT_YENISEY,
    CAAT_YUGOSLAVIA,
    CAAT_YUNNAN,
]

C_MAP_GLOBAL_1940 = CAAI_Map("aa_map_global_1940", L_TERRITORIES_SETUP_GLOBAL_1940)
C_REL_NATION = CAAI_RelNation("RelationInWar",     
                                [CAAN_GERMANY,
                                CAAN_SOVIET_UNION,
                                CAAN_JAPAN,
                                CAAN_UNITED_STATES,
                                CAAN_CHINA,
                                CAAN_UK_AT,
                                CAAN_UK_PA,
                                CAAN_ITALY,
                                CAAN_ANZAC,
                                CAAN_FRANCE],
                                [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                CType.REL_IN_PEACE)

C_REL_NATION.set_relation(CAAN_GERMANY, CAAN_FRANCE, CType.REL_IN_WAR)
C_REL_NATION.set_relation(CAAN_GERMANY, CAAN_UK_AT, CType.REL_IN_WAR)
C_REL_NATION.set_relation(CAAN_GERMANY, CAAN_UK_PA, CType.REL_IN_WAR)
C_REL_NATION.set_relation(CAAN_GERMANY, CAAN_ANZAC, CType.REL_IN_WAR)
C_REL_NATION.set_relation(CAAN_JAPAN  , CAAN_CHINA, CType.REL_IN_WAR)
C_REL_NATION.set_relation(CAAN_ITALY  , CAAN_FRANCE, CType.REL_IN_WAR)

    
#CAAM_GLOBAL_1940 = CAAI_Map("Map-Global-1940"

if __name__ == '__main__':
    for territory in L_TERRITORIES_SETUP_GLOBAL_1940:
        north      = territory.get_neighbore('n')
        north_east = territory.get_neighbore('ne')
        east       = territory.get_neighbore('e')
        south_east = territory.get_neighbore('se')
        south      = territory.get_neighbore('e')
        south_west = territory.get_neighbore('sw')
        west       = territory.get_neighbore('w')
        north_west = territory.get_neighbore('nw')

        if (north != None) and north.get_neighbore('s') != territory:
            print (f"{north.get_name()} 's': {territory.get_name()}")

        if (north_east != None) and north.get_neighbore('sw') != territory:
            print (f"{north.get_name()} 'sw': {territory.get_name()}")

        if (east != None) and north.get_neighbore('w') != territory:
            print (f"{north.get_name()} 'w': {territory.get_name()}")

        if (south_east != None) and north.get_neighbore('nw') != territory:
            print (f"{north.get_name()} 'nw': {territory.get_name()}")

        if (south != None) and north.get_neighbore('n') != territory:
            print (f"{north.get_name()} 'n': {territory.get_name()}")

        if (south_west != None) and north.get_neighbore('ne') != territory:
            print (f"{north.get_name()} 'ne': {territory.get_name()}")

        if (west != None) and north.get_neighbore('e') != territory:
            print (f"{north.get_name()} 'e': {territory.get_name()}")

        if (north_west != None) and north.get_neighbore('se') != territory:
            print (f"{north.get_name()} 'se': {territory.get_name()}")



