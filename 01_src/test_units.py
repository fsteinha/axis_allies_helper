from aa_units import *
from aa_type import *
from test_common import *
import inspect

##############################################################################
# Tests
##############################################################################

##############################################################################
def sub_test_unit(caau:CAAUnit, aa_nation:CAANation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    assert(type(caau.get_nation()) == CAANation)
    caan = caau.get_nation()
    sub_test_nation(caan, aa_nation.get_name(), aa_nation.get_alliance())
    
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
def test_inf(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Inf(aa_nation, i_count)
    assert(caa.get_type() == CType.U_INFANTARY)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_mech_inf(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_MechInf(aa_nation, i_count)
    assert(caa.get_type() == CType.U_MECH_INFANTARY)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_tank(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Tank(aa_nation, i_count)
    assert(caa.get_type() == CType.U_TANK)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_ari(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Ari(aa_nation, i_count)
    assert(caa.get_type() == CType.U_ARTILLERY)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_aaa(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_AAA(aa_nation, i_count)
    assert(caa.get_type() == CType.U_AAA)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_fighter(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Figther(aa_nation, i_count)
    assert(caa.get_type() == CType.U_FIGHTER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_tbomb(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_TBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.U_T_BOMBER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_sbomb(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_SBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.U_S_BOMBER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_submarine(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Submarine(aa_nation, i_count)
    assert(caa.get_type() == CType.U_SUBMARINE)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_destroyer(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Destroyer(aa_nation, i_count)
    assert(caa.get_type() == CType.U_DESTROYER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_cruiser(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Cruiser(aa_nation, i_count)
    assert(caa.get_type() == CType.U_CRUISER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_battleship(aa_nation, i_count):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Battleship(aa_nation, i_count)
    assert(caa.get_type() == CType.U_BATTLESHIP)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_carrier():
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAANation("Germany", CType.A_AXIS)
    caan_japan = CAANation("Japan", CType.A_AXIS)
    caar = CAAR_Carrier()
    caac = CAAU_Carrier(caan_germany,caar,None)
    assert(caac.get_type() == CType.U_CARRIER)
    #Carrier must be test with i_count == None
    sub_test_unit(caac, caan_germany, None)
    assert caac.add_unit(CAAU_AAA(caan_germany)) == False
    assert caac.get_unit_count() == 0
    assert caac.add_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.add_unit(CAAU_Figther(caan_germany)) == False
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count() == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.add_unit(CAAU_TBomb(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Figther(caan_japan)) == False
    assert caac.get_unit_count() == 2, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.sub_unit(CAAU_TBomb(caan_germany)) == True
    assert caac.get_unit_count() == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.add_unit(CAAU_TBomb(caan_japan)) == True
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count() == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.sub_unit(CAAU_Figther(caan_germany)) == False
    assert caac.get_unit_count() == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.add_unit(CAAU_SBomb(caan_japan)) == False
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_TBomb(caan_japan)) == True
    assert caac.get_unit_count() == 0  
    
    print(caac.info())    

##############################################################################
def test_carrier_init():
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAANation("Germany", CType.A_AXIS)
    caan_japan = CAANation("Japan", CType.A_AXIS)
    caar = CAAR_Carrier()
    caac = CAAU_Carrier(caan_germany,caar,[CAAU_Figther(caan_germany),CAAU_Figther(caan_germany)])
    assert(caac.get_type() == CType.U_CARRIER)
    #Carrier must be test with i_count == None
    sub_test_unit(caac, caan_germany, None)
    assert caac.get_unit_count() == 2
    print(caac.info())    

    try:
        caac = CAAU_Carrier(caan_germany,caar,[CAAU_SBomb(caan_germany),CAAU_Figther(caan_germany)])
        assert(False), "Expection requested"
    except:
        pass
        

##############################################################################
def test_cargo():
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAANation("Germany", CType.A_AXIS)
    caan_japan = CAANation("Japan", CType.A_AXIS)
    caar = CAAR_Cargo()
    caac = CAAU_Cargo(caan_germany,caar,None)
    assert caac.get_type() == CType.U_CARGO
    assert caac.get_name() == CType.str(CType.U_CARGO)
    #Carrier must be test with i_count == None
    sub_test_unit(caac, caan_germany, None)
    assert caac.add_unit(CAAU_AAA(caan_germany)) == False
    assert caac.get_unit_count() == 0
    assert caac.add_unit(CAAU_Inf(caan_germany)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Tank(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.add_unit(CAAU_Tank(caan_germany)) == False
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Tank(caan_germany)) == True
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_Tank(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_Inf(caan_japan)) == False
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_Inf(caan_germany)) == True
    assert caac.get_unit_count() == 0
    assert caac.add_unit(CAAU_MechInf(caan_japan)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Figther(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_TBomb(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_SBomb(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Ari(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_MechInf(caan_japan)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Ari(caan_germany)) == False
    assert caac.get_unit_count() == 1
    
    print(caac.info())    

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
    
##############################################################################
if __name__ == "__main__":   
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

    test_carrier()
    test_carrier_init()

    test_cargo()    