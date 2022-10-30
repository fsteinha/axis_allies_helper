##
# @file test_relnation.py
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


from aa.aa_relnation import *
# TODO
from aa_nation import CAAI_Nation
from aa.aa_type import *


##############################################################################
# GLOBALS
##############################################################################

# test nations
caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
caan_germany2 = CAAI_Nation("Germany", CType.A_AXIS)
caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)
caan_allien = CAAI_Nation("Great allien nation", CType.A_ALLIES)

##############################################################################
# Tests
##############################################################################

##############################################################################
def test_relnation_init():
    """! Test the constructor"""

    # check setting with wrong type of nation
    b_assert = False
    try:
        aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, 1, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_PEACE)
        b_assert = True
    except:
        pass

    if b_assert == True:
        assert(False), f"wrong type for nation is possible"

    # check setting with wrong value type
    b_assert = False
    try:
        aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_japan, caan_gb_europe, caan_allien], 
                                 [1, -1], 
                                 1)
        b_assert = True
    except:
        pass

    if b_assert == True:
        assert(False), f"wrong value for relation is possible"

    # check double nation
    b_assert = False
    try:
        aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_germany, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_PEACE)
        b_assert = True
    except:
        pass
    
    if b_assert == True:
        assert(False), f"wrong value for relation is possible"
    
    # check double nation name caan_germany, caan_germany2 has the same name
    b_assert = False
    try:
        aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_germany2, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_PEACE)
        b_assert = True
    except:
        pass
    
    if b_assert == True:
        assert(False), f"wrong value for relation is possible"

    # check wrong default
    b_assert = False
    try:
        aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_germany2, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 -2)
        b_assert = True
    except:
        pass
    
    if b_assert == True:
        assert(False), f"wrong default value for relation is possible"

def test_relnation_set_relation():
    """! Test set_relation method"""

    aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_PEACE)

    # positive test
    assert(aa_relation.set_relation(caan_germany, caan_japan, CType.REL_IN_WAR) == True)
    assert(aa_relation.d_relations[aa_relation.build_hash(caan_germany, caan_japan)][CAAI_RelNation.KEY_VALUE] == CType.REL_IN_WAR)
    assert(aa_relation.set_relation(caan_germany, caan_japan, CType.REL_IN_PEACE) == True)
    assert(aa_relation.d_relations[aa_relation.build_hash(caan_germany, caan_japan)][CAAI_RelNation.KEY_VALUE] == CType.REL_IN_PEACE)
    assert(aa_relation.d_relations[aa_relation.build_hash(caan_germany, caan_japan)][CAAI_RelNation.KEY_NATION_1] == caan_germany)
    assert(aa_relation.d_relations[aa_relation.build_hash(caan_germany, caan_japan)][CAAI_RelNation.KEY_NATION_2] == caan_japan)
    
    #negative test
    assert(aa_relation.set_relation(caan_germany, caan_japan, -1) == False)
    assert(aa_relation.set_relation(None, caan_japan, CType.REL_IN_WAR) == False)
    assert(aa_relation.set_relation(caan_germany, None, CType.REL_IN_WAR) == False)
    
def test_relnation_get_relation():
    """! Test set_relation method"""

    aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_PEACE)

    # positive test
    assert(aa_relation.set_relation(caan_germany, caan_japan, CType.REL_IN_WAR) == True)
    assert(aa_relation.get_relation(caan_germany, caan_japan) == CType.REL_IN_WAR)

    # negative test
    assert(aa_relation.set_relation(caan_germany, caan_japan, CType.REL_IN_WAR) == True)
    assert(aa_relation.get_relation(-1, caan_japan) == None)
    assert(aa_relation.get_relation(caan_germany, -1) == None)
    assert(aa_relation.get_relation(caan_germany, caan_japan) == CType.REL_IN_WAR)

    # test default
    assert(aa_relation.get_relation(caan_germany, caan_gb_europe) == CType.REL_IN_PEACE)
    

def test_relnation_get_relations():
    """! Test get_relation method"""

    aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_PEACE)

    # positive test
    assert(aa_relation.set_relation(caan_germany, caan_japan, CType.REL_IN_WAR) == True)
    assert(aa_relation.set_relation(caan_gb_europe, caan_allien, CType.REL_IN_WAR) == True)
    assert(len(aa_relation.get_relations()) == 2)
    assert(aa_relation.get_relations()[0][CAAI_RelNation.KEY_NATION_1] == caan_germany)
    assert(aa_relation.get_relations()[0][CAAI_RelNation.KEY_NATION_2] ==caan_japan)
    assert(aa_relation.get_relations()[0][CAAI_RelNation.KEY_VALUE] == CType.REL_IN_WAR)
    assert(aa_relation.get_relations()[1][CAAI_RelNation.KEY_NATION_1] == caan_gb_europe)
    assert(aa_relation.get_relations()[1][CAAI_RelNation.KEY_NATION_2] ==caan_allien)
    assert(aa_relation.get_relations()[1][CAAI_RelNation.KEY_VALUE] == CType.REL_IN_WAR)

def test_relnation_get_default():
    """! Test get_default method"""

    aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_PEACE)

    assert (aa_relation.get_default() == CType.REL_IN_PEACE)

    aa_relation = CAAI_RelNation("RelationInWar", 
                                 [caan_germany, caan_japan, caan_gb_europe, caan_allien], 
                                 [CType.REL_IN_PEACE, CType.REL_IN_WAR],
                                 CType.REL_IN_WAR)

    assert (aa_relation.get_default() == CType.REL_IN_WAR)
    
    