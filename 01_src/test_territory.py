from test_common import *
from aa_territory import *
from aa_nation import *
import inspect

##############################################################################
# Tests
##############################################################################

##############################################################################
def test_land_init(s_name:str, aa_region:int, aa_nation:CAAI_Nation, aa_ipc:int):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.get_name() == s_name
    assert caa.get_region() == aa_region
    assert caa.get_type() == CType.T_LAND
    assert caa.get_alliance() == aa_nation.get_alliance(), f"{caa.get_alliance()} != {aa_nation.get_alliance()}"
    assert caa.get_ipc()  == aa_ipc
    
    caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land, [CType.F_AIR_BASE, CType.F_MAJOR_FACTORY, CType.F_MINOR_FACTORY, CType.F_NAVAL_BASE])
    assert caa.get_unit_count() == 4, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 4"
    
    #TBD list
    print(caa.info())

if __name__ == "__main__":
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
    caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)
    
    test_land_init("Western Germany",CType.R_EUROPE, caan_germany,10)
    test_land_init("Japan",CType.R_ASIA_FAR_EAST, caan_japan,10)
    test_land_init("Egypt",CType.R_AFRICA, caan_gb_europe,10)