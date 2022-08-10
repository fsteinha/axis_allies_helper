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
# - Modified by Fred Steinhäuser on 09/08/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.


from aa_type import CType
from aa_item import CAAItem
from aa_nation import *
from aa_map import *
from aa_territory import *
from aa_units import *


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

CAAN_AFGANISTAN     = CAAI_Nation("Afganistan"    , CType.A_NEUTRAL) 
CAAN_ANGOLA         = CAAI_Nation("Angola"        , CType.A_NEUTRAL) 

Provinz	WorldArea	Region	Nation	IPC	Naval-Base	Air Base	Minor Ind.	Major Ind.	Supplie Route	INF	M.INF	ARI	TANK	AAA	FIGHTER	T.BOMB	S.BOMB	SUB	DEST	CRUISER	B.SHIP	CARRIER	CARRIER (F)	CARRIER (FF)	CARRIER (FT)	CARRIER (T)	CARRIER (TT)	CAR	CAR(I)	CAR (II)	CAR (IM)	CAR (IT)	CAR (IA)	CAR (IAAA)	Allies
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
CAAT_SEASIDE_031 = CAAT_Sea("Seaside 31", CType.R_PACIFIC)																																
CAAT_SEASIDE_031 = CAAT_Sea("Seaside 31", CType.R_PACIFIC)																																
CAAT_SEASIDE_031 = CAAT_Sea("Seaside 31", CType.R_PACIFIC)																																
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
CAAT_SEASIDE_095 = CAAT_Sea("Seaside 95", CType.R_MEDITERRANEAN_SEA)																																
CAAT_SEASIDE_096 = CAAT_Sea("Seaside 96", CType.R_MEDITERRANEAN_SEA)																																
CAAT_SEASIDE_097 = CAAT_Sea("Seaside 97", CType.R_MEDITERRANEAN_SEA)																																
CAAT_SEASIDE_098 = CAAT_Sea("Seaside 98", CType.R_MEDITERRANEAN_SEA)																																
CAAT_SEASIDE_099 = CAAT_Sea("Seaside 99", CType.R_MEDITERRANEAN_SEA)																																
CAAT_SEASIDE_100 = CAAT_Sea("Seaside 100", CType.R_BLACK_SEA)																																
CAAT_SEASIDE_101 = CAAT_Sea("Seaside 101", CType.R_ATLANTIC)
CAAT_SEASIDE_102 = CAAT_Sea("Seaside 102", CType.R_ATLANTIC)																																
CAAT_SEASIDE_103 = CAAT_Sea("Seaside 103", CType.R_ATLANTIC)																																
CAAT_SEASIDE_104 = CAAT_Sea("Seaside 104", CType.R_ATLANTIC)																																
CAAT_SEASIDE_105 = CAAT_Sea("Seaside 105", CType.R_ATLANTIC)																																
CAAT_SEASIDE_106 = CAAT_Sea("Seaside 106", CType.R_ATLANTIC)																																
CAAT_SEASIDE_107 = CAAT_Sea("Seaside 107", CType.R_ATLANTIC)																																
CAAT_SEASIDE_108 = CAAT_Sea("Seaside 108", CType.R_ATLANTIC)																																
CAAT_SEASIDE_109 = CAAT_Sea("Seaside 109", CType.R_ATLANTIC)																																
CAAT_SEASIDE_110 = CAAT_Sea("Seaside 110", CType.R_NORTH_SEA)																																
CAAT_SEASIDE_111 = CAAT_Sea("Seaside 111", CType.R_NORTH_SEA)																																
CAAT_SEASIDE_112 = CAAT_Sea("Seaside 112", CType.R_NORTH_SEA)																																
CAAT_SEASIDE_113 = CAAT_Sea("Seaside 113", CType.R_BALTIC_SEA)																																
CAAT_SEASIDE_114 = CAAT_Sea("Seaside 114", CType.R_BALTIC_SEA)																																
CAAT_SEASIDE_115 = CAAT_Sea("Seaside 115", CType.R_BALTIC_SEA)																																
CAAT_SEASIDE_116 = CAAT_Sea("Seaside 116", CType.R_ATLANTIC)																																
CAAT_SEASIDE_117 = CAAT_Sea("Seaside 117", CType.R_ATLANTIC)																																
CAAT_SEASIDE_118 = CAAT_Sea("Seaside 118", CType.R_ATLANTIC)																																
CAAT_SEASIDE_119 = CAAT_Sea("Seaside 119", CType.R_ATLANTIC)																																
CAAT_SEASIDE_120 = CAAT_Sea("Seaside 120", CType.R_ATLANTIC)																																
CAAT_SEASIDE_121 = CAAT_Sea("Seaside 121", CType.R_ATLANTIC)																																
CAAT_SEASIDE_122 = CAAT_Sea("Seaside 122", CType.R_ATLANTIC)																																
CAAT_SEASIDE_123 = CAAT_Sea("Seaside 123", CType.R_ATLANTIC)																																
CAAT_SEASIDE_124 = CAAT_Sea("Seaside 124", CType.R_ATLANTIC)																																
CAAT_SEASIDE_125 = CAAT_Sea("Seaside 125", CType.R_ATLANTIC)																																
CAAT_SEASIDE_126 = CAAT_Sea("Seaside 126", CType.R_ATLANTIC)																																
CAAT_SEASIDE_127 = CAAT_Sea("Seaside 127", CType.R_ARTIC_SEA)																																

CAAT_AFGHANISTAN = CAAT_Land("Afghanistan",                   CType.R_ASIA_CENTRAL, CAAN_AFGANISTAN,    4)
CAAT_ALSKA       = CAAT_Land("Alaska",                        CType.R_NORDAMERICA,  CAAN_UNITED_STATES, 2)
CAAT_ALBANIA     = CAAT_Land("Albania",                       CType.R_EUROPE,       CAAN_ITALY,         1)																																
CAAT_ALBERTA     = CAAT_Land("Alberta Saskatchewan Manitoba", CType.R_NORDAMERICA,  CAAN_UK_AT,         1)																																
CAAT_ALEUTIAN    = CAAT_Land("Aleutian Island",               CType.R_NORDAMERICA,  CAAN_UNITED_STATES, 0)																															



CAAT_Alexandria           = CAAT_Land("Alexandria",           CType.R_AFRICA,        CAAN_UK_AT,        0)																																
CAAT_Algeria              = CAAT_Land("Algeria",              CType.R_AFRICA,        CAAN_FRANCE,       1)																															
CAAT_Amur                 = CAAT_Land("Amur",                 CType.R_ASIA_FAR_EAST, CAAN_SOVIET_UNION, 1)																															
CAAT_Anglo_Egyptian_Sudan = CAAT_Land("Anglo Egyptian Sudan", CType.R_AFRICA,        CAAN_ITALY,        1)																															
CAAT_Angola               = CAAT_Land("Angola",               CType.R_AFRICA,        CAAN_ANGOLA,       1, CAAR_Land, [CAAU_Inf(CAAN_ANGOLA, 2)])																																
CAAT_Anhwe                = CAAT_Land("Anhwe",	              CType.R_ASIA_FAR_EAST, CAAN_CHINA,        1)																				
CAAT_Archangel            = CAAT_Land("Archangel",	N/A		N/A																																
CAAT_Argentinia           = CAAT_Land("Argentinia",	N/A		N/A																																
CAAT_Baltic_States        = CAAT_Land("Baltic States",	N/A		N/A																																
CAAT_Belgian_Congo        = CAAT_Land("Belgian Congo",	N/A		N/A																																
CAAT_Bessarabia           = CAAT_Land("Bessarabia",	N/A		N/A																																
CAAT_Bolivia              = CAAT_Land("Bolivia",	N/A		N/A																																
CAAT_Borneo               = CAAT_Land("Borneo",	N/A		N/A																																
CAAT_Brazil               = CAAT_Land("Brazil",	N/A		N/A																																
CAAT_British_Guiana       = CAAT_Land("British Guiana",	N/A		N/A																																
CAAT_British_Somaliland   = CAAT_Land("British Somaliland",, CType.R_AFRICA, CAAN_UK_AT, 0)																											
CAAT_Bryansk 	         = CAAT_Land("Bryansk", 	", 																																
CAAT_Bulgaria            = CAAT_Land("Bulgaria", 	", 																																
CAAT_Burma   	         = CAAT_Land("Burma", 	", 																																
CAAT_Buryatia	         = CAAT_Land("Buryatia	EP	RuAsia", 	1																															
CAAT_Buyant_Uhaa         = CAAT_Land("Buyant-Uhaa", 	", 																																
CAAT_Caucasus            = CAAT_Land("Caucasus", 	", 																																
CAAT_Celebes             = CAAT_Land("Celebes", 	", 																																
CAAT_Central_America     = CAAT_Land("Central America", 	", 																																
CAAT_Central_Mongoli     = CAAT_Land("Central Mongolia", 	", 																																
CAAT_Central_            = CAAT_Land("Central Unit States", 	", 																																
CAAT_Ceylon              = CAAT_Land("Ceylon", 	", 																																
CAAT_Chahar              = CAAT_Land("Chahar", 	", 																																
CAAT_Chile               = CAAT_Land("Chile", 	", 																																
CAAT_Colombia            = CAAT_Land("Colombia", 	", 																																
CAAT_Crete               = CAAT_Land("Crete", 	", 																																
CAAT_Cyprus              = CAAT_Land("Cyprus", 	", 																																
CAAT_Denmark             = CAAT_Land("Denmark", 	", 																																
CAAT_Dutch New Guinea    = CAAT_Land("Dutch New Guinea", 	", 																																
CAAT_Dzavhan             = CAAT_Land("Dzavhan", 	", 																																
CAAT_Eastern Persia      = CAAT_Land("Eastern Persia", 	", 																																
CAAT_Eastern Unit States = CAAT_Land("Eastern Unit States", 	", 																																
CAAT_Ecuador             = CAAT_Land("Ecuador", 	", 																																
CAAT_Egypt               = CAAT_Land("Egypt", 	", 																																
CAAT_Eire                = CAAT_Land("Eire", 	", 																																
CAAT_Estern Poland       = CAAT_Land("Estern Poland", 	", 																																
CAAT_Ethiopia            = CAAT_Land("Ethiopia", CType.R_AFRICA, CAAN_ITALY 1) 																																
CAAT_Evenkiyskiy         = CAAT_Land("Evenkiyskiy	EP	RuAsia", 	1																															
CAAT_Fiji    	         = CAAT_Land("Fiji", 		GBP	0																															
CAAT_Finland             = CAAT_Land("Finland", 	", 																																
CAAT_Formosa             = CAAT_Land("Formosa", 	", 																																
CAAT_France              = CAAT_Land("France", 	", 																																
CAAT_French_Central_Africa    = CAAT_Land("French Central Africa", 	", 																																
CAAT_French_Equatorial_Africa = CAAT_Land("French Equatorial Africa ", 	", 																																
CAAT_French_Guiana            = CAAT_Land("French Guiana", 	", 																																
CAAT_French_Indo_China        = CAAT_Land("French Indo China", 	", 																																
CAAT_French_Madagascar        = CAAT_Land("French Madagascar", 	", 																																
CAAT_French_West_Africa       = CAAT_Land("French West Africa", 	", 																																
CAAT_Germany                  = CAAT_Land("Germany", 	", 																																
CAAT_Gibralter                = CAAT_Land("Gibralter", 	", 																																
CAAT_Gilbert_Islands          = CAAT_Land("Gilbert Islands", 		GBP	0																															
CAAT_Gold_Coast               = CAAT_Land("Gold Coast", 	", 																																
CAAT_Greater_Southern_Germany = CAAT_Land("Greater Southern Germany", 	", 																																
CAAT_Greece                   = CAAT_Land("Greece", 	", 																																
CAAT_Greenland                = CAAT_Land("Greenland", 	", 																																
CAAT_Guam                     = CAAT_Land("Guam", 	", 																																
CAAT_Hainan                   = CAAT_Land("Hainan", 	", 																																
CAAT_Hawaiian_Islands         = CAAT_Land("Hawaiian Islands", 		US	1																															
CAAT_Holland_Belgium          = CAAT_Land("Holland Belgium", 	", 																																
CAAT_Hopei   		          = CAAT_Land("Hopei", 	", 																																
CAAT_Hunan  		          = CAAT_Land("Hunan", 	", 																																
CAAT_Iceland                  = CAAT_Land("Iceland", 	", 																																
CAAT_India                    = CAAT_Land("India", 	", 																																
CAAT_Iraq                     = CAAT_Land("Iraq", 	", 																																
CAAT_Italian_Somaliland       = CAAT_Land("Italian Somaliland", 	", 																																
CAAT_Iwo_Jima                 = CAAT_Land("Iwo Jima", 		JP	1																															
CAAT_Japan                    = CAAT_Land("Japan", 	", 																																
CAAT_Java                     = CAAT_Land("Java", 	", 																																
CAAT_Jehol                    = CAAT_Land("Jehol", 	", 																																
CAAT_Johnston Islands         = CAAT_Land("Johnston Islands", 		US	0																															
CAAT_Kansu                    = CAAT_Land("Kansu", 	", 																																
CAAT_Karelia  	              = CAAT_Land("Karelia", 	", 																																
CAAT_Kazakhstan               = CAAT_Land("Kazakhstan", 	", 																																
CAAT_Kenya                    = CAAT_Land("Kenya", 	", 																																
CAAT_Kiangsi  	              = CAAT_Land("Kiangsi", 	", 																																
CAAT_Kiangsu                  = CAAT_Land("Kiangsu", 	", 																																
CAAT_Korea                    = CAAT_Land("Korea", 	", 																																
CAAT_Kwangsi                  = CAAT_Land("Kwangsi", 	", 																																
CAAT_Kwangtung                = CAAT_Land("Kwangtung", 	", 																																
CAAT_Kweichow                 = CAAT_Land("Kweichow", 	", 																																
CAAT_Liberia                  = CAAT_Land("Liberia", 	", 																																
CAAT_Line_Islands             = CAAT_Land("Line Islands", 		US	0																															
CAAT_Lybia                    = CAAT_Land("Lybia", CType.R_AFRICA, CAAN_UK_AT, 0)																																
CAAT_Malaya                   = CAAT_Land("Malaya", 	", 																																
CAAT_Manchuria                = CAAT_Land("Manchuria", 	", 																																
CAAT_Manila                   = CAAT_Land("Manila", 	", 																																
CAAT_Marianas                 = CAAT_Land("Marianas", 		JP	0																															
CAAT_Marshall_Islands         = CAAT_Land("Marshall Islands", 		JP	0																															
CAAT_Mexico 	              = CAAT_Land("Mexico", 		US	2																															
CAAT_Midway 	              = CAAT_Land("Midway", 		US	0																															
CAAT_Moroco 	              = CAAT_Land("Moroco", 	", 																																
CAAT_Mozambique               = CAAT_Land("Mozambique", 	", 																																
CAAT_Nenetsia                 = CAAT_Land("Nenetsia", 	", 																																
CAAT_New_Britain              = CAAT_Land("New Britain", 		ANZAC	0																															
CAAT_New_Brunswick_Nova_Scotia = CAAT_Land("New Brunswick Nova Scotia", 	", 																																
CAAT_New_Guinea                = CAAT_Land("New Guinea", 		ANZAC	0																															
CAAT_New_Hebrides              = CAAT_Land("New Hebrides", 		FR	0																															
CAAT_New_South_Wales           = CAAT_Land("New South Wales", 		ANZAC	2																															
CAAT_New_Zealand               = CAAT_Land("New Zealand", 		ANZAC	2																															
CAAT_Newfoundland_Labrador     = CAAT_Land("Newfoundland Labrador", 	", 																																
CAAT_Nigeria                   = CAAT_Land("Nigeria", 	", 																																
CAAT_Normandy_Bordeaux         = CAAT_Land("Normandy Bordeaux", 	", 																																
CAAT_Northern_Italy            = CAAT_Land("Northern Italy", 	", 																																
CAAT_Northern_Territory        = CAAT_Land("Northern Territory", 	", 																																
CAAT_Northwest_Persia          = CAAT_Land("Northwest Persia", 	", 																																
CAAT_Norway                    = CAAT_Land("Norway", 	", 																																
CAAT_Novgorod                  = CAAT_Land("Novgorod", 	", 																																
CAAT_Novosibirsk               = CAAT_Land("Novosibirsk", 	", 																																
CAAT_Okinawa                   = CAAT_Land("Okinawa", 	", 																																
CAAT_Olgiy                     = CAAT_Land("Olgiy", 	", 																																
CAAT_Ontario                   = CAAT_Land("Ontario", 	", 																																
CAAT_Palau_Island              = CAAT_Land("Palau Island", 	", 																																
CAAT_Paraguay                  = CAAT_Land("Paraguay", 	", 																																
CAAT_Persia                    = CAAT_Land("Persia", 	", 																																
CAAT_Peru                      = CAAT_Land("Peru", 	", 																																
CAAT_Phillipines               = CAAT_Land("Phillipines", 	", 																																
CAAT_Poland                    = CAAT_Land("Poland", 	", 																																
CAAT_Portugal                  = CAAT_Land("Portugal", 	", 																																
CAAT_Portuguese                = CAAT_Land("Portuguese Guinea", 	", 																																
CAAT_Quebec                    = CAAT_Land("Quebec", 	", 																																
CAAT_Queensland                = CAAT_Land("Queensland", 		ANZAC	2																															
CAAT_Rhodesia                  = CAAT_Land("Rhodesia", 	", 																																
CAAT_Rio_de_Oro                = CAAT_Land("Rio de Oro", 	", 																																
CAAT_Romania                   = CAAT_Land("Romania", 	", 																																
CAAT_Rostov                    = CAAT_Land("Rostov", 	", 																																
CAAT_Russia                    = CAAT_Land("Russia", 	", 																																
CAAT_Sakha                     = CAAT_Land("Sakha	EP	RuAsia", 	1																															
CAAT_Samara                    = CAAT_Land("Samara", 	", 																																
CAAT_Samoa                     = CAAT_Land("Samoa", 		GBP	0																															
CAAT_Sardinia                  = CAAT_Land("Sardinia", 	", 																																
CAAT_Saudi_Arabia              = CAAT_Land("Saudi Arabia", 	", 																																
CAAT_Scotland                  = CAAT_Land("Scotland", 	", 																																
CAAT_Shan_State                = CAAT_Land("Shan State", 	", 																																
CAAT_Shantung                  = CAAT_Land("Shantung", 	", 																																
CAAT_Shensi                    = CAAT_Land("Shensi", 	", 																																
CAAT_Siam                      = CAAT_Land("Siam", 	", 																																
CAAT_Siberia                   = CAAT_Land("Siberia	EP	RuAsia", 	1																															
CAAT_Sicily                    = CAAT_Land("Sicily", 	", 																																
CAAT_Sierra_Leone              = CAAT_Land("Sierra Leone", 	", 																																
CAAT_Sikang                    = CAAT_Land("Sikang", 	", 																																
CAAT_Slovakia_Hungar           = CAAT_Land("Slovakia Hungary", 	", 																																
CAAT_Smolensk                  = CAAT_Land("Smolensk", 	", 																																
CAAT_Solomon_Islands           = CAAT_Land("Solomon Islands", 		ANZAC	0																															
CAAT_South_Australia           = CAAT_Land("South Australia", 	", 																																
CAAT_South_East_Mexico         = CAAT_Land("South East Mexico", 	", 																																
CAAT_South_West_Africa         = CAAT_Land("South West Africa", 	", 																																
CAAT_Southern_France           = CAAT_Land("Southern France", 	", 																																
CAAT_Southern_Italy            = CAAT_Land("Southern Italy", 	", 																																
CAAT_Soviet_Far_East           = CAAT_Land("Soviet Far East", 		SU	1																															
CAAT_Spain                     = CAAT_Land("Spain", 	", 																																
CAAT_Suiyuan                   = CAAT_Land("Suiyuan ", 	", 																																
CAAT_Sumatra   	               = CAAT_Land("Sumatra", 	", 																																
CAAT_Suriname                  = CAAT_Land("Suriname", 	", 																																
CAAT_Sweden                    = CAAT_Land("Sweden", 	", 																																
CAAT_Switzerland               = CAAT_Land("Switzerland", 	", 																																
CAAT_Syria  	               = CAAT_Land("Syria", 	", 																																
CAAT_Szechwan                  = CAAT_Land("Szechwan", 	", 																																
CAAT_Tambov                    = CAAT_Land("Tambov", 	", 																																
CAAT_Tanganyika_Territory      = CAAT_Land("Tanganyika Territory", 	", 																																
CAAT_Timguska                  = CAAT_Land("Timguska	EP	RuAsia", 	1																															
CAAT_Tobruk                    = CAAT_Land("Tobruk", 	", 																																
CAAT_Trans_Jordan              = CAAT_Land("Trans-Jordan", 	", 																																
CAAT_Tsagaan_Olom              = CAAT_Land("Tsagaan-Olom", 	", 																																
CAAT_Tsinghai                  = CAAT_Land("Tsinghai", 	", 																																
CAAT_Tunisia                   = CAAT_Land("Tunisia", 	", 																																
CAAT_Turkey                    = CAAT_Land("Turkey", 	", 																																
CAAT_Turkmenistan              = CAAT_Land("Turkmenistan", 	", 																																
CAAT_Ukraine                   = CAAT_Land("Ukraine", 	", 																																
CAAT_Ulaanbaatar               = CAAT_Land("Ulaanbaatar", 	", 																																
CAAT_Union_of_South_Africa     = CAAT_Land("Union of South Africa", 	", 																																
CAAT_United_Kingdom            = CAAT_Land("United Kingdom", 	", 																																
CAAT_Urals                     = CAAT_Land("Urals", 	", 																																
CAAT_Uruguay                   = CAAT_Land("Uruguay", 	", 																																
CAAT_Venezuela                 = CAAT_Land("Venezuela", 	", 																																
CAAT_Victoria                  = CAAT_Land("Victoria", 		ANZAC	1																															
CAAT_Volgograd                 = CAAT_Land("Volgograd", 	", 																																
CAAT_Volodga                   = CAAT_Land("Volodga", 	", 																																
CAAT_Vyborg                    = CAAT_Land("Vyborg", 	", 																																
CAAT_Wake_Island               = CAAT_Land("Wake Island", 		US	0																															
CAAT_West_India                = CAAT_Land("West India", 	", 																																
CAAT_West_Indies               = CAAT_Land("West Indies", 	", 																																
CAAT_Western_Australia         = CAAT_Land("Western Australia", 	", 																																
CAAT_Western_Canada            = CAAT_Land("Western Canada", 		GBP	1																															
CAAT_Western_Germany           = CAAT_Land("Western Germany", 	", 																																
CAAT_Western_Ukraine           = CAAT_Land("Western Ukraine", 	", 																																
CAAT_Western_United_States     = CAAT_Land("Western United States", 		US	10																															
CAAT_Yakut                     = CAAT_Land("Yakut S. S. R. 	EP	RuAsia", 	1																															
CAAT_Yenisey                   = CAAT_Land("Yenisey	EP	RuAsia", 	1																															
CAAT_Yugoslavia                = CAAT_Land("Yugoslavia", 	", 																																
CAAT_Yunnan                    = CAAT_Land("Yunnan", 	", 																																








L_NATION_SETUP_GLOBAL_1940 = [
    CAAN_GERMANY,       
    CAAN_SOVIET_UNION,  
    CAAN_JAPAN,         
    CAAN_UNITED_STATES, 
    CAAN_CHINA,         
    CAAN_UNITED_KINGDOM,
    CAAN_ITALY,         
    CAAN_ANZAC,         
    CAAN_FRANCE        
]

CAAM_GLOBAL_1940 = CAAI_Map("Map-Global-1940")


