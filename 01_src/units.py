import string
from  aa_type import CType

##############################################################################
class CAAItem():
    def __init__(self,s_name, aa_type) -> None:
        self.s_name = s_name

        if type(aa_type) == str:
            self.aa_type = CType.type(aa_type)
        elif  CType.str(aa_type) != None:
            self.aa_type = aa_type

    def get_name(self) -> str:
        return self.s_name

    def get_region(self) -> str:
        if ('aa_region' in dir(self)):
            return CType.str(self.aa_region)
        return CType.na()

    def get_type(self) -> str:
        return CType.str(self.aa_type)

    def get_nation(self):
        if (type(self) == CAANation):
            return self
        else:
            return self.aa_nation
        
    def get_alliance(self) -> str:
        if ('aa_alliance' in dir(self)):
            return CType.str(self.aa_alliance)

        return self.aa_nation.get_alliance()

    def get_ipc(self) -> int:
        if ('aa_ipc' in dir(self)):
            return self.aa_ipc
        return CType.na()

    def get_units(self) -> int:
        if ('l_aa_units' in dir(self)):
            return str(self.l_aa_units)
        return CType.na()

    def get_count(self) -> int:
        if ('i_count' in dir(self)):
            return self.i_count
        return CType.na()


    def info(self):
        return f'''
Name    : {self.get_name()}
Region  : {self.get_region()}
Type    : {self.get_type()}
Nation  : {self.get_nation().s_name}
Alliance: {self.get_alliance()}
IPC     : {self.get_ipc()}
Units   : {self.get_units()}
Count   : {self.get_count()}
'''

##############################################################################
class CAANation(CAAItem):
    def __init__(self, s_name:str, aa_alliance:int) -> None:
        super().__init__(s_name, CType.C_NATION)
        self.aa_alliance = aa_alliance
        pass


##############################################################################
class CAALand(CAAItem):
    def __init__(self, s_name:str,aa_region:CType, aa_nation:CAANation, aa_ipc:int, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_LAND)
        self.aa_ipc=aa_ipc
        self.l_aa_units = l_aa_units
        self.aa_nation = aa_nation
        self.aa_region = aa_region
        pass
        
##############################################################################
class CAASea(CAAItem):
    def __init__(self, s_name:str, aa_ipc:int, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_SEA)
        self.l_aa_units = l_aa_units
        pass


##############################################################################
class CAAUnit(CAAItem):
    def __init__(self, aa_type:int, aa_nation, i_count = 1) -> None:
        super().__init__(CType.str(aa_type), aa_type)
        self.aa_nation = aa_nation
        if (i_count > 0):
            self.i_count = i_count
        else:
            self.i_count = 1 
        pass

    def add(self, i_add):
        if (i_add >= 0):
            self.i_count = self.i_count + i_add 

    def sub(self, i_sub):
        if (i_sub >= 0):
            self.i_count = self.i_count - i_sub
            if (self.i_count < 0):
                self.i_count = 0
            

    def reset_count(self, i_count:int) -> None:
        if (i_count >= 0):
            self.i_count = i_count
        else:
            self.i_count = 0
    
    
        

##############################################################################
class CAAInf(CAAUnit):
    def __init__(self, aa_nation:CAANation, i_count = 1) -> None:
        super().__init__(CType.U_INFANTARY, aa_nation, i_count)
        pass

##############################################################################
class CAAMechInf(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_MECH_INFANTARY, aa_nation, i_count)
        pass

##############################################################################
class CAATank(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_TANK, aa_nation, i_count)
        pass

##############################################################################
class CAAAri(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_ARTILLERY, aa_nation, i_count)
        pass

##############################################################################
class CAAAAA(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_AAA, aa_nation, i_count)
        pass

##############################################################################
class CAAFigther(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_FIGHTER, aa_nation, i_count)
        pass

##############################################################################
class CAATBomb(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_T_BOMBER, aa_nation, i_count)
        pass

##############################################################################
class CAASBomb(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_S_BOMBER, aa_nation, i_count)
        pass

##############################################################################
class CAASubmarine(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_SUBMARINE, aa_nation, i_count)
        pass

##############################################################################
class CAADestroyer(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_DESTROYER, aa_nation, i_count)
        pass

##############################################################################
class CAACruiser(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_CRUISER, aa_nation, i_count)
        pass

##############################################################################
class CAABattleship(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_BATTLESHIP, aa_nation, i_count)
        pass

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

##############################################################################
# Tests
##############################################################################

def sub_test_nation(caan, s_name:string, aa_alliance:int):
    assert(caan.get_name() == s_name)
    assert(caan.get_type() == CType.str(CType.C_NATION))
    assert(caan.get_alliance() == CType.str(aa_alliance))
    
##############################################################################
def test_nation(s_name:string, aa_alliance:int):
    caa = CAANation(s_name, aa_alliance)
    sub_test_nation(caa, s_name, aa_alliance)
    print(caa.info())    

##############################################################################
def sub_test_unit(caau:CAAUnit, aa_nation:CAANation, i_count):
    assert(type(caau.get_nation()) == CAANation)
    caan = caau.get_nation()
    sub_test_nation(caan, aa_nation.get_name(), CType.type(aa_nation.get_alliance()))
    
    if (i_count > 0):
        assert caau.get_count() == i_count, f"{caa.get_count()} != {i_count}"
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


        
        
    
    
    

##############################################################################
def test_inf(aa_nation, i_count):
    caa = CAAInf(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_INFANTARY))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_mech_inf(aa_nation, i_count):
    caa = CAAMechInf(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_MECH_INFANTARY))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_tank(aa_nation, i_count):
    caa = CAATank(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_TANK))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_ari(aa_nation, i_count):
    caa = CAAAri(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_ARTILLERY))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_aaa(aa_nation, i_count):
    caa = CAAAAA(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_AAA))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_fighter(aa_nation, i_count):
    caa = CAAFigther(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_FIGHTER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_tbomb(aa_nation, i_count):
    caa = CAATBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_T_BOMBER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_sbomb(aa_nation, i_count):
    caa = CAASBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_S_BOMBER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_submarine(aa_nation, i_count):
    caa = CAASubmarine(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_SUBMARINE))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_destroyer(aa_nation, i_count):
    caa = CAADestroyer(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_DESTROYER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_cruiser(aa_nation, i_count):
    caa = CAACruiser(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_CRUISER))
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())    

##############################################################################
def test_battleship(aa_nation, i_count):
    caa = CAABattleship(aa_nation, i_count)
    assert(caa.get_type() == CType.str(CType.U_BATTLESHIP))
    sub_test_unit(caa, aa_nation, i_count)
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


def test_land(s_name:string, aa_region:int, aa_nation:CAANation, aa_ipc:int, l_aa_units:list):
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
    
    test_tank(caan_germany, 1)
    test_tank(caan_japan, 0)
    test_tank(caan_gb_europe, 10)
 
    test_ari(caan_germany, 1)
    test_ari(caan_japan, 0)
    test_ari(caan_gb_europe, 10)

    test_aaa(caan_germany, 1)
    test_aaa(caan_japan, 0)
    test_aaa(caan_gb_europe, 10)

    test_fighter(caan_germany, 1)
    test_fighter(caan_japan, 0)
    test_fighter(caan_gb_europe, 10)

    test_tbomb(caan_germany, 1)
    test_tbomb(caan_japan, 0)
    test_tbomb(caan_gb_europe, 10)
 
    test_sbomb(caan_germany, 1)
    test_sbomb(caan_japan, 0)
    test_sbomb(caan_gb_europe, 10)

    test_submarine(caan_germany, 1)
    test_submarine(caan_japan, 0)
    test_submarine(caan_gb_europe, 10)

    test_destroyer(caan_germany, 1)
    test_destroyer(caan_japan, 0)
    test_destroyer(caan_gb_europe, 10)

    test_cruiser(caan_germany, 1)
    test_cruiser(caan_japan, 0)
    test_cruiser(caan_gb_europe, 10)

    test_battleship(caan_germany, 1)
    test_battleship(caan_japan, 0)
    test_battleship(caan_gb_europe, 10)

    test_land("Western Germany",CType.R_EUROPE, caan_germany,10,[])
    test_land("Japan",CType.R_ASIA_FAR_EAST, caan_japan,10,[])
    test_land("Egypt",CType.R_AFRICA, caan_gb_europe,10,[])
    
    