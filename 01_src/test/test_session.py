##
# @file test_session.py
#
# @brief tests the aa_session object.
#
# @section description_conv_excel Description
# Classes provided by this module:
# - TODO
##
# @section libraries_main Libraries/Modules
# TODO
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_territory TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 2022/09/10.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.

from json_session import *
from aa_session import *
from aa_type import *


##############################################################################
# GLOBALS
##############################################################################

caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)

caan_allien = CAAI_Nation("Great allien nation", CType.A_ALLIES)

caal_western_germany = CAAT_Land("Western Germany", CType.R_EUROPE, caan_germany, 10)
caal_eastern_germany = CAAT_Land("Eastern Germany", CType.R_EUROPE, caan_germany, 15)
caal_south_germany   = CAAT_Land("South Germany", CType.R_EUROPE, caan_germany, 20)
caal_north_germany   = CAAT_Land("North Germany", CType.R_EUROPE, caan_germany, 25)
caal_japan           = CAAT_Land("Japan", CType.R_ASIA_FAR_EAST, caan_japan, 3)
caal_great_britain   = CAAT_Land("Great Britain", CType.R_EUROPE, caan_gb_europe, 1)
caal_sea_80          = CAAT_Sea("80", CType.R_ATLANTIC)
caal_sea_20          = CAAT_Sea("20", CType.R_PACIFIC)
caal_sea_100         = CAAT_Sea("100", CType.R_INDIAN_OCEAN)
caal_sea_102         = CAAT_Sea("102", CType.R_INDIAN_OCEAN)

caal_allien_land = CAAT_Land("Allien land", CType.R_EUROPE, caan_allien, 1000)


caam = CAAI_Map("Map",[ caal_western_germany, 
                        caal_eastern_germany,
                        caal_south_germany,
                        caal_north_germany,
                        caal_japan,
                        caal_great_britain, 
                        caal_sea_80, 
                        caal_sea_20, 
                        caal_sea_100])

caam_allien = CAAI_Map("Map with alien",[ 
                        caal_western_germany, 
                        caal_eastern_germany,
                        caal_south_germany,
                        caal_north_germany,
                        caal_japan,
                        caal_great_britain, 
                        caal_sea_80, 
                        caal_sea_20, 
                        caal_sea_100])

##############################################################################
# Tests
##############################################################################

##############################################################################
def test_session_basic():

    aa_session = CAAI_Session(s_name            = "Global game 1940",
                              aa_map            = caam,
                              i_round           = 1,
                              l_aa_nations      = [caan_germany, caan_japan, caan_gb_europe],
                              aa_current_nation = caan_germany,
                              aa_current_phase  = CType.S_PH1_PURCHASE_REPAIR)

    assert (aa_session.get_name()  == "Global game 1940")
    assert (aa_session.aa_map      == caam)
    assert (aa_session.get_round() == 1)
    assert (aa_session.get_nation_names_as_str() == "Germany\nJapan\nGreat Britain Europe")
    assert (aa_session.get_nation_names_as_list() == ["Germany", "Japan","Great Britain Europe"])
    assert (aa_session.get_current_nation() == caan_germany)
    assert (aa_session.get_current_phase() == CType.str(CType.S_PH1_PURCHASE_REPAIR))

##############################################################################
def test_session_check_nation_map():
    # assert expected
    b_assert = True
    try:
        aa_session = CAAI_Session(s_name            = "Global game 1940",
                                  aa_map            = caam_allien,
                                  i_round           = 1,
                                  l_aa_nations      = [caan_germany, caan_japan, caan_gb_europe, caan_allien],
                                  aa_current_nation = caan_germany,
                                  aa_current_phase  = CType.S_PH1_PURCHASE_REPAIR)
        b_assert = False
    except:
        pass

    if b_assert == False:
        assert (False), f"In nations list of allien map match not with given nations list - check in constuctor of session failed" 