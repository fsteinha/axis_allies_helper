from aa_units import *


##############################################################################
# Tests
##############################################################################

def sub_test_nation(caan, s_name:str, aa_alliance:int):
    assert(caan.get_name() == s_name)
    assert(caan.get_type() == CType.str(CType.C_NATION))
    assert(caan.get_alliance() == CType.str(aa_alliance))
    
##############################################################################
def test_nation(s_name:str, aa_alliance:int):
    caa = CAANation(s_name, aa_alliance)
    sub_test_nation(caa, s_name, aa_alliance)
    print(caa.info())    

##############################################################################
def sub_test_unit(caau:CAAUnit, aa_nation:CAANation, i_count):
    assert(type(caau.get_nation()) == CAANation)
    caan = caau.get_nation()
    sub_test_nation(caan, aa_nation.get_name(), CType.type(aa_nation.get_alliance()))
    
    if i_count != None:
        if (i_count > 0):
            assert caau.get_count() == i_count, f"{caau.get_count()} != {i_count}"
        else:
            assert caau.get_count() == 1, f"i_count should be 1"

        if (i_count > 0):
            caau.sub(i_count)
            assert caau.get_count() == 0, f"{caau.get_count()} != 0"
            caau.add(i_count)
            assert caau.get_count() == i_count
            caau.add(i_count)
            assert caau.get_count() == 2 * i_count
            caau.sub(3*i_count)
            assert caau.get_count() == 0
        elif (i_count <= 0):
            i_temp_count =  caau.get_count()
            caau.sub(i_count)
            assert caau.get_count() == i_temp_count
            caau.add(i_count)
            assert caau.get_count() == i_temp_count
            caau.add(i_count)
            assert caau.get_count() == i_temp_count
            caau.sub(3*i_count)
            assert caau.get_count() == i_temp_count

        caau.reset_count(i_count)       
        if (i_count >= 0):
            assert caau.get_count() == i_count
        else:
            assert caau.get_count() == 0
    else:
        assert caau.get_count() == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.sub(-1)
        assert caau.get_count() == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.sub(-10)
        assert caau.get_count() == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.add(1)
        assert caau.get_count() == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.add(10)
        assert caau.get_count() == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.sub(1)
        assert caau.get_count() == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"


##############################################################################
def test_container(*args):
    #try:
        caacon = CAAUnitContainer(*args)
        print(caacon.info())    

    #except:
    #    print ("ERROR")
    #    pass
    


        
        
    
    
    

##############################################################################
def test_inf(aa_nation, i_count):
    caa = CAAU_Inf(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_INFANTARY))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_mech_inf(aa_nation, i_count):
    caa = CAAU_MechInf(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_MECH_INFANTARY))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_tank(aa_nation, i_count):
    caa = CAAU_Tank(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_TANK))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_ari(aa_nation, i_count):
    caa = CAAU_Ari(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_ARTILLERY))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_aaa(aa_nation, i_count):
    caa = CAAU_AAA(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_AAA))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_fighter(aa_nation, i_count):
    caa = CAAU_Figther(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_FIGHTER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_tbomb(aa_nation, i_count):
    caa = CAAU_TBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_T_BOMBER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_sbomb(aa_nation, i_count):
    caa = CAAU_SBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_S_BOMBER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_submarine(aa_nation, i_count):
    caa = CAAU_Submarine(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_SUBMARINE))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_destroyer(aa_nation, i_count):
    caa = CAAU_Destroyer(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_DESTROYER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_cruiser(aa_nation, i_count):
    caa = CAAU_Cruiser(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_CRUISER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_battleship(aa_nation, i_count):
    caa = CAAU_Battleship(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_BATTLESHIP))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_carrier(aa_nation, aa_rules_carrier:CAAR_Carrier, l_aa_units = None):
    caa = CAAU_Carrier(aa_nation,aa_rules_carrier,l_aa_units)
    assert(caa.get_type() == CType.str(CType.U_CARRIER))
    #Carrier must be test with i_count == None
    sub_test_unit(caa, aa_nation, None)

    print(caa.info())    

'''
##############################################################################
class CAACarrier(CAAUnit):
    def __init__(self,  aa_nation, i_count:int = 1, l_aa_units:list = None) -> None:
        super().__init__(CType.U_CARRIER, aa_nation, i_count)
        self.l_aa_units = l_aa_units
        pass

##############################################################################
class CAACargo(CAAUnit):
    def __init__(self,  aa_nation, i_count:int = 1, l_aa_units:list = None) -> None:
        super().__init__(CType.U_CARGO, aa_nation, i_count)
        self.l_aa_units = l_aa_units
        pass
'''


def test_land(s_name:str, aa_region:int, aa_nation:CAANation, aa_ipc:int, l_aa_units:list):
    caa = CAALand(s_name,aa_region, aa_nation, aa_ipc, l_aa_units)
    assert caa.get_name() == s_name
    assert caa.get_region() == CType.str(aa_region)  
    assert caa.get_type() == CType.str(CType.T_LAND)
    assert caa.get_alliance() == aa_nation.get_alliance(), f"{caa.get_alliance()} != {aa_nation.get_alliance()}"
    assert caa.get_ipc()  == aa_ipc
    assert caa.get_units()  == str(l_aa_units)
    
    #TBD list
    print(caa.info())


    
    
##############################################################################
if __name__ == "__main__":
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


    
    caan_germany = CAANation("Germany", CType.A_AXIS)
    caan_japan = CAANation("Japan", CType.A_AXIS)
    caan_gb_europe = CAANation("Great Britain Europe", CType.A_ALLIES)
    
    test_inf(caan_germany, 1)
    test_inf(caan_japan, 0)
    test_inf(caan_gb_europe, 10)
    test_inf(caan_gb_europe, -10)
    

    test_mech_inf(caan_germany, 1)
    test_mech_inf(caan_japan, 0)
    test_mech_inf(caan_gb_europe, 10)
    test_mech_inf(caan_gb_europe, -10)
    
    
    test_tank(caan_germany, 1)
    test_tank(caan_japan, 0)
    test_tank(caan_gb_europe, 10)
    test_tank(caan_gb_europe, -10)
 
    test_ari(caan_germany, 1)
    test_ari(caan_japan, 0)
    test_ari(caan_gb_europe, 10)
    test_ari(caan_gb_europe, -10)

    test_aaa(caan_germany, 1)
    test_aaa(caan_japan, 0)
    test_aaa(caan_gb_europe, 10)
    test_aaa(caan_gb_europe, -10)

    test_fighter(caan_germany, 1)
    test_fighter(caan_japan, 0)
    test_fighter(caan_gb_europe, 10)
    test_fighter(caan_gb_europe, -10)

    test_tbomb(caan_germany, 1)
    test_tbomb(caan_japan, 0)
    test_tbomb(caan_gb_europe, 10)
    test_tbomb(caan_gb_europe, -10)
 
    test_sbomb(caan_germany, 1)
    test_sbomb(caan_japan, 0)
    test_sbomb(caan_gb_europe, 10)
    test_sbomb(caan_gb_europe, -10)

    test_submarine(caan_germany, 1)
    test_submarine(caan_japan, 0)
    test_submarine(caan_gb_europe, 10)
    test_submarine(caan_gb_europe, -10)

    test_destroyer(caan_germany, 1)
    test_destroyer(caan_japan, 0)
    test_destroyer(caan_gb_europe, 10)
    test_destroyer(caan_gb_europe, -10)

    test_cruiser(caan_germany, 1)
    test_cruiser(caan_japan, 0)
    test_cruiser(caan_gb_europe, 10)
    test_cruiser(caan_gb_europe, -10)

    test_battleship(caan_germany, 1)
    test_battleship(caan_japan, 0)
    test_battleship(caan_gb_europe, 10)
    test_battleship(caan_gb_europe, -10)


    test_container(CAAU_Inf(caan_germany, 1))
    test_container(CAAU_Inf(caan_germany, 10), CAAU_Inf(caan_japan, 1))
'''    
    caar = CAAR_Carrier()
    test_carrier(caan_germany, caar)
    test_carrier(caan_japan, caar)
    test_carrier(caan_gb_europe, caar)
    test_carrier(caan_gb_europe, caar)
    
    test_carrier(caan_germany, caar, [CType.U_FIGHTER])
    
    #TBD CARRIER
    #tbd CARGO


    test_land("Western Germany",CType.R_EUROPE, caan_germany,10,[])
    test_land("Japan",CType.R_ASIA_FAR_EAST, caan_japan,10,[])
    test_land("Egypt",CType.R_AFRICA, caan_gb_europe,10,[])
'''