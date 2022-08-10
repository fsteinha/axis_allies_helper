from test_common import *
from aa_territory import *
from aa_nation import *
from aa_facillities import *
from aa_units import *
import inspect

##############################################################################
# GLOBALS
##############################################################################

caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)

##############################################################################
# Tests
##############################################################################

##############################################################################
@pytest.mark.parametrize("s_name, aa_region, aa_nation, aa_ipc, aa_origin_nation", [
    ("Western Germany",CType.R_EUROPE,        caan_germany,   10, None),
    ("Japan",          CType.R_ASIA_FAR_EAST, caan_japan,     10, None),
    ("Egypt",          CType.R_AFRICA,        caan_gb_europe, 10, caan_germany),
    ])
def test_land_init(s_name, aa_region, aa_nation, aa_ipc, aa_origin_nation):
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

    # try to put not allowed units in the territory
    b_assert = False
    try:
        caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Land(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase(), 
                      CAAU_AAA(aa_nation), CAAU_SBomb(aa_nation),CAAU_Tank(aa_nation,10),
                      CAAU_Battleship(aa_nation)])
    except:
        pass

    if b_assert == True:
        assert (False), "Initialisation with not allowed unit succeed (see last CAAT_Land init)"
    
    # try to bind not allowed rules in the territory
    b_assert = False
    try:
        caa = CAAT_Land(s_name,aa_region, aa_nation, aa_ipc, CAAR_Sea(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase(), 
                      CAAU_AAA(aa_nation), CAAU_SBomb(aa_nation),CAAU_Tank(aa_nation,10)])
        b_assert = True
    except:
        pass

    if b_assert == True:
        assert (False), "Initialisation with not allowed rule succeed (see last CAAT_Land init)"

    #test the neigbores

    s_neighbore = 'nord'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'nord_east'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'east'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'south_east'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'south'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'south_west'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'west'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'nord_west'
    caa_test = CAAT_Land(f"{s_name}_{s_neighbore}",aa_region, aa_nation, aa_ipc, CAAR_Land, [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    #test origin nation
    caa = CAAT_Land(s_name, aa_region, aa_nation, aa_ipc, CAAR_Land, [], aa_origin_nation)
    if aa_origin_nation == None:
        assert caa.get_origin_nation() == aa_nation
        assert caa.get_origin_nation() == caa.get_nation()
    else:
        assert caa.get_origin_nation() == aa_origin_nation
    
    
    #print item info
    print(caa.info())

##############################################################################
@pytest.mark.parametrize("s_name, aa_region, aa_nation, aa_ipc", [
    ("Western Germany",CType.R_EUROPE, caan_germany, 3)
    ])
def test_land(s_name, aa_region, aa_nation, aa_ipc):
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

##############################################################################
@pytest.mark.parametrize("s_name, aa_region", [
    ("78",CType.R_PACIFIC)
    ])
def test_sea_init(s_name:str, aa_region:int):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caan_test = CAAI_Nation("Germany", CType.A_AXIS)
    caa = CAAT_Sea(s_name,aa_region, CAAR_Sea, [])
    
    assert caa.get_name() == s_name
    assert caa.get_region() == aa_region
    assert caa.get_type() == CType.T_SEA
    


    b_assert = False
    try:
        caa = CAAT_Sea(s_name, aa_region, CAAR_Sea(), 
                     [CAAF_AirBase(), CAAF_Major(), CAAF_Minor(), CAAF_NavalBase()])
        b_assert = True
    except:
        pass
    
    if b_assert == True:
        assert (False), "Initialisation with not allowed unit succeed (see last CAAT_Land init)"    
    assert caa.get_unit_count() == 0, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 0"
    
    caa = CAAT_Sea(s_name,aa_region, CAAR_Sea(), 
                      [CAAU_SBomb(caan_test)])
    assert caa.get_unit_count() == 1, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 1"

    caa = CAAT_Sea(s_name,aa_region, CAAR_Sea(), 
                     [CAAU_SBomb(caan_test),CAAU_Cruiser(caan_test,10)])
    assert caa.get_unit_count() == 11, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 11"

    # try to bind not allowed rules in the territory
    b_assert = False
    try:
        caa = CAAT_Sea(s_name, aa_region, CAAR_Land(), 
                         [CAAU_SBomb(caan_test),CAAU_Cruiser(caan_test,10)])
        b_assert = True
    except:
        pass

    if b_assert == True:
        assert (False), "Initialisation with not allowed rule succeed (see last CAAT_Land init)"

    #test the neigbores

    s_neighbore = 'nord'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'nord_east'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'east'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'south_east'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'south'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'south_west'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'west'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    s_neighbore = 'nord_west'
    caa_test = CAAT_Sea(f"{s_name}_{s_neighbore}",aa_region, CAAR_Sea(), [])
    assert caa.set_neighbore(s_neighbore, caa_test) == True
    assert caa.get_neighbore(s_neighbore) == caa_test
    assert caa.set_neighbore(s_neighbore, caa_test) == False

    #print item info
    print(caa.info())

##############################################################################
@pytest.mark.parametrize("s_name, aa_region", [
    ("80",CType.R_PACIFIC)
    ])
def test_sea(s_name:str, aa_region:int):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caan_test = CAAI_Nation("Germany", CType.A_AXIS)
    caa = CAAT_Sea(s_name,aa_region, CAAR_Sea, [])
    assert caa.get_name() == s_name
    assert caa.get_region() == aa_region
    assert caa.get_type() == CType.T_SEA
    
    caa = CAAT_Sea(s_name,aa_region, CAAR_Sea(), [])
    assert caa.get_unit_count() == 0, f"caa.get_unit_count() returns {caa.get_unit_count()} NOT 0"
    
    assert caa.add_unit(CAAU_AAA(caan_germany)) == False
    assert caa.get_unit_count() == 0
    assert caa.add_unit(CAAU_Figther(caan_germany)) == True
    #F_ge
    assert caa.get_unit_count() == 1
    assert caa.add_unit(CAAU_Figther(caan_germany)) == True
    #F_ge(2)
    assert caa.get_unit_count() == 2
    assert caa.add_unit(CAAU_Figther(caan_germany)) == True
    #F_ge(3)
    assert caa.get_unit_count() == 3
    assert caa.sub_unit(CAAU_Figther(caan_germany)) == True
    #F_ge(2)
    assert caa.get_unit_count() == 2, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.add_unit(CAAU_TBomb(caan_germany)) == True
    #F_ge(2),TB_ge(1)
    assert caa.get_unit_count() == 3
    assert caa.sub_unit(CAAU_Figther(caan_japan)) == False
    #F_ge(2),TB_ge(1)
    assert caa.get_unit_count() == 3, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.sub_unit(CAAU_TBomb(caan_germany)) == True
    #F_ge(2)
    assert caa.get_unit_count() == 2, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.add_unit(CAAU_TBomb(caan_japan)) == True
    #F_ge(2),TB_jp(1)
    assert caa.get_unit_count() == 3
    assert caa.sub_unit(CAAU_Figther(caan_germany)) == True
    #F_ge(1),TB_jp(1)
    assert caa.get_unit_count() == 2, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.sub_unit(CAAU_Figther(caan_germany)) == True
    #TB_jp(1)
    assert caa.get_unit_count() == 1, f"caa.get_unit_count() == {caa.get_unit_count()}"
    assert caa.add_unit(CAAU_SBomb(caan_japan)) == True
    #TB_jp(1),SB_jp(1)
    assert caa.get_unit_count() == 2
    assert caa.sub_unit(CAAU_TBomb(caan_japan)) == True
    #SB_jp(1)
    assert caa.get_unit_count() == 1  
    assert caa.add_unit(CAAU_Battleship(caan_japan)) == True
    #SB_jp(1), BS_ip(1)
    assert caa.get_unit_count() == 2
    assert caa.add_unit(CAAU_Carrier(caan_japan, CAAR_Carrier())) == True
    #SB_jp(1), BS_ip(1), Car_jp(1)
    assert caa.get_unit_count() == 3
    assert caa.add_unit(CAAU_Cargo(caan_japan, CAAR_Cargo())) == True
    #SB_jp(1), BS_ip(1), Car_jp(1), Cag_jp(1)
    assert caa.get_unit_count() == 4
    assert caa.add_unit(CAAU_Cruiser(caan_japan)) == True
    #SB_jp(1), BS_ip(1), Car_jp(1), Cag_jp(1), Cru_jp(1)
    assert caa.get_unit_count() == 5
    assert caa.add_unit(CAAU_Tank(caan_japan)) == False
    assert caa.get_unit_count() == 5
    
    caau_cargo = CAAU_Cargo(caan_test)
    assert caau_cargo.add_unit(CAAU_Inf(caan_japan)) == True
    assert caa.add_unit(caau_cargo) == True
    #SB_jp(1), BS_ip(1), Car_jp(1), Cag_jp(2), Cru_jp(1)
    assert caa.get_unit_count() == 6
    
    caar_carrier = CAAU_Carrier(caan_test)
    assert caar_carrier.add_unit(CAAU_Figther(caan_japan)) == True
    assert caa.add_unit(caar_carrier) == True
    #SB_jp(1), BS_ip(1), Car_jp(1), Car_de(1), Cag_jp(2), Cru_jp(1)
    assert caa.get_unit_count() == 7
    
    print(caa.info())    