from test_common import *
from aa_territory import *
from aa_nation import *
from aa_facillities import *
from aa_units import *
from aa_map import *
from aa_type import *

import inspect

##############################################################################
# GLOBALS
##############################################################################

caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)
caan_alien = CAAI_Nation("Allien Nation", CType.A_ALLIES)

##############################################################################
# Tests
##############################################################################

##############################################################################
def test_map():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    
    caal_western_germany = CAAT_Land("Western Germany", CType.R_EUROPE, caan_germany, 10)
    caal_japan           = CAAT_Land("Japan", CType.R_ASIA_FAR_EAST, caan_japan, 3)
    caal_great_britain   = CAAT_Land("Great Britain", CType.R_EUROPE, caan_gb_europe, 1)
    caal_sea_80          = CAAT_Sea("80", CType.R_ATLANTIC)
    caal_sea_20          = CAAT_Sea("20", CType.R_PACIFIC)
    caal_sea_100         = CAAT_Sea("100", CType.R_INDIAN_OCEAN)
    caal_sea_102         = CAAT_Sea("102", CType.R_INDIAN_OCEAN)
    
    caam = CAAI_Map("Map",[caal_western_germany, caal_japan,caal_great_britain, caal_sea_80, caal_sea_20, caal_sea_100])
                           
    assert caam.get_territory("Western Germany") == caal_western_germany
    assert caam.get_territory("Japan") == caal_japan
    assert caam.get_territory("Great Britain") == caal_great_britain
    assert caam.get_territory("80") == caal_sea_80
    assert caam.get_territory("20") == caal_sea_20
    assert caam.get_territory("100") == caal_sea_100
    assert caam.get_territory("102") == None
    
    b_assert = False
    try:
        caam = CAAI_Map("Map",[CAAU_Inf(caan_germany, 10)])
        b_assert = True
    except:
        pass

    if b_assert == True:
        assert (False), f"Exception does not raise with unvalid object in map initialization"

    assert (caam.add_territory(caal_sea_102) == True)
    assert caam.get_territory("102") == caal_sea_102
    # double set test
    assert (caam.add_territory(caal_western_germany) == False)
    
    # test the gettin territorie list
    l_lands = caam.get_lands_as_list()
    assert (l_lands != None)
    assert (len(l_lands) == 3)
    assert (caal_western_germany in l_lands)
    assert (caal_japan in l_lands)
    assert (caal_great_britain in l_lands)
    assert (caal_sea_80 not in l_lands)
    assert (caal_sea_20 not in l_lands)
    assert (caal_sea_100 not in l_lands)
    
    l_lands = caam.get_lands_as_list([caan_germany])
    assert (l_lands != None)
    assert (len(l_lands) == 1)
    assert (caal_western_germany in l_lands)

    l_lands = caam.get_lands_as_list([caan_germany, caan_japan])
    assert (l_lands != None)
    assert (len(l_lands) == 2)
    assert (caal_western_germany in l_lands)
    assert (caal_japan in l_lands)
    
    print(caam.info())    

def test_map_get_nations():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    
    caal_western_germany = CAAT_Land("Western Germany", CType.R_EUROPE, caan_germany, 10)
    caal_japan           = CAAT_Land("Japan", CType.R_ASIA_FAR_EAST, caan_japan, 3)
    caal_great_britain   = CAAT_Land("Great Britain", CType.R_EUROPE, caan_gb_europe, 1)
    caal_sea_80          = CAAT_Sea("80", CType.R_ATLANTIC)
    caal_sea_20          = CAAT_Sea("20", CType.R_PACIFIC)
    caal_sea_100         = CAAT_Sea("100", CType.R_INDIAN_OCEAN)
    caal_sea_102         = CAAT_Sea("102", CType.R_INDIAN_OCEAN)
    
    caam = CAAI_Map("Map",[caal_western_germany, caal_japan,caal_great_britain, caal_sea_80, caal_sea_20, caal_sea_100])

    l_nations = caam.get_nations()
    assert(caan_germany in l_nations)
    assert(caan_japan in l_nations)
    assert(caan_gb_europe in l_nations)
    assert(caan_alien not in l_nations)      

if __name__ == "__main__":
    test_map()