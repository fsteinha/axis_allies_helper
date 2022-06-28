from test_common import *
from aa_items import *
import inspect

##############################################################################
# Tests
##############################################################################

##############################################################################
def test_nation(s_name:str, aa_alliance:int):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAANation(s_name, aa_alliance)
    sub_test_nation(caa, s_name, aa_alliance)
    print(caa.info())    

def sub_test_facillity(caaf:CAAFacillity):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    assert caaf.get_count() == 1, f"Precondition error count is {caaf.get_count()}"
    caaf.add(1)
    assert caaf.get_count() == 1
    caaf.sub(10)
    assert caaf.get_count() == -9
    caaf.add(20)
    assert caaf.get_count() == 1
    print(caaf.info())
    
def test_major():
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_Major()
    assert (caaf.get_type() == CType.F_MAJOR_FACTORY)
    sub_test_facillity(caaf)
    
def test_minor():
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_Minor()
    assert (caaf.get_type() == CType.F_MINOR_FACTORY)
    sub_test_facillity(caaf)
    
def test_airbase():
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_AirBase()
    assert (caaf.get_type() == CType.F_AIR_BASE)
    sub_test_facillity(caaf)

def test_navalbase():
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_NavalBase()
    assert (caaf.get_type() == CType.F_NAVAL_BASE)
    sub_test_facillity(caaf)

def test_land(s_name:str, aa_region:int, aa_nation:CAANation, aa_ipc:int):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAALand(s_name,aa_region, aa_nation, aa_ipc, [])
    assert caa.get_name() == s_name
    assert caa.get_region() == aa_region
    assert caa.get_type() == CType.T_LAND
    assert caa.get_alliance() == aa_nation.get_alliance(), f"{caa.get_alliance()} != {aa_nation.get_alliance()}"
    assert caa.get_ipc()  == aa_ipc

    
    #TBD list
    print(caa.info())


if __name__ == "__main__":
    caan_germany = CAANation("Germany", CType.A_AXIS)
    caan_japan = CAANation("Japan", CType.A_AXIS)
    caan_gb_europe = CAANation("Great Britain Europe", CType.A_ALLIES)
    
    test_nation("Germany"              , CType.A_AXIS)
    test_nation("Sovietunion"          , CType.A_ALLIES)
    test_nation("Japan"                , CType.A_AXIS)
    test_nation("United States"        , CType.A_ALLIES)
    test_nation("Italy"                , CType.A_AXIS)
    test_nation("Great Britain Europe" , CType.A_ALLIES)
    test_nation("Great Britain Pacific", CType.A_ALLIES)
    test_nation("France"               , CType.A_ALLIES)
    test_nation("China"                , CType.A_ALLIES)
    test_nation("ANZAC"                , CType.A_ALLIES)

    test_major()
    test_minor()
    test_airbase()
    test_navalbase()

    test_land("Western Germany",CType.R_EUROPE, caan_germany,10)
    test_land("Japan",CType.R_ASIA_FAR_EAST, caan_japan,10)
    test_land("Egypt",CType.R_AFRICA, caan_gb_europe,10)