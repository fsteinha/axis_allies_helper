from test_common import *
from aa_territory import *
from aa_nation import *
from aa_facillities import *
from aa_units import *
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
    
    caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase()])
    assert caa.get_unit_count() == 4, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 4"
    
    caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase(), 
                      CAAU_AAA(aa_nation), CAAU_SBomb(aa_nation),CAAU_Tank(aa_nation)])
    assert caa.get_unit_count() == 7, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 7"

    caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase(), 
                      CAAU_AAA(aa_nation), CAAU_SBomb(aa_nation),CAAU_Tank(aa_nation,10)])
    assert caa.get_unit_count() == 16, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 16"

    try:
        caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase(), 
                      CAAU_AAA(aa_nation), CAAU_SBomb(aa_nation),CAAU_Tank(aa_nation,10),
                      CAAU_Battleship(aa_nation)])
        assert (False), "Initialisation with not allowed unit succeed"
    except:
        pass

    
    #TBD list
    print(caa.info())

def test_land(s_name:str, aa_region:int, aa_nation:CAAI_Nation, aa_ipc:int):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.get_name() == s_name
    assert caa.get_region() == aa_region
    assert caa.get_type() == CType.T_LAND
    assert caa.get_alliance() == aa_nation.get_alliance(), f"{caa.get_alliance()} != {aa_nation.get_alliance()}"
    assert caa.get_ipc()  == aa_ipc
    
    caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase()])
    assert caa.get_unit_count() == 4, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 4"
    
    #AB,Ma,Mi,NB
    assert caa.add_unit(CAAU_AAA(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge
    assert caa.get_unit_count() == 5
    assert caa.add_unit(CAAU_Figther(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge
    assert caa.get_unit_count() == 6
    assert caa.add_unit(CAAU_Figther(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge(2)
    assert caa.get_unit_count() == 7
    assert caa.add_unit(CAAU_Figther(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge(3)
    assert caa.get_unit_count() == 8
    assert caa.sub_unit(CAAU_Figther(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge(2)
    assert caa.get_unit_count() == 7, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.add_unit(CAAU_TBomb(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge(2),TB_ge(1)
    assert caa.get_unit_count() == 8
    assert caa.sub_unit(CAAU_Figther(caan_japan)) == False
    #AB,Ma,Mi,NB,AAA_ge,F_ge(2),TB_ge(1)
    assert caa.get_unit_count() == 8, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.sub_unit(CAAU_TBomb(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge(2)
    assert caa.get_unit_count() == 7, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.add_unit(CAAU_TBomb(caan_japan)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge(2),TB_jp(1)
    assert caa.get_unit_count() == 8
    assert caa.sub_unit(CAAU_Figther(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,F_ge(1),TB_jp(1)
    assert caa.get_unit_count() == 7, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.sub_unit(CAAU_Figther(caan_germany)) == True
    #AB,Ma,Mi,NB,AAA_ge,TB_jp(1)
    assert caa.get_unit_count() == 6, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.add_unit(CAAU_SBomb(caan_japan)) == True
    #AB,Ma,Mi,NB,AAA_ge,TB_jp(1),SB_jp(1)
    assert caa.get_unit_count() == 7
    assert caa.sub_unit(CAAU_TBomb(caan_japan)) == True
    #AB,Ma,Mi,NB,AAA_ge,SB_jp(1)
    assert caa.get_unit_count() == 6  
    assert caa.add_unit(CAAU_Battleship(caan_japan)) == False
    #AB,Ma,Mi,NB,AAA_ge,SB_jp(1)
    assert caa.get_unit_count() == 6
    assert caa.add_unit(CAAU_Carrier(caan_japan, CAAR_Carrier())) == False
    #AB,Ma,Mi,NB,AAA_ge,SB_jp(1)
    assert caa.get_unit_count() == 6
    assert caa.add_unit(CAAU_Cargo(caan_japan, CAAR_Cargo())) == False
    #AB,Ma,Mi,NB,AAA_ge,SB_jp(1)
    assert caa.get_unit_count() == 6
    assert caa.add_unit(CAAU_Cruiser(caan_japan)) == False
    #AB,Ma,Mi,NB,AAA_ge,SB_jp(1)
    assert caa.get_unit_count() == 6
    
    
    #AB,Ma,Mi,NB,AAA_ge,SB_jp(1)
    print(caa.info())


if __name__ == "__main__":
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
    caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)
    
    test_land_init("Western Germany",CType.R_EUROPE, caan_germany,10)
    test_land_init("Japan",CType.R_ASIA_FAR_EAST, caan_japan,10)
    test_land_init("Egypt",CType.R_AFRICA, caan_gb_europe,10)

    test_land("Western Germany",CType.R_EUROPE, caan_germany,3)
    