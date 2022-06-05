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

    def get_type(self) -> str:
        return CType.str(self.aa_type)

    def get_nation(self) -> str:
        if ('aa_nation' in dir(self)):
            return self.aa_nation.s_name
        return CType.na()

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


    def info(self):
        return f'''
Name    : {self.get_name()}
Type    : {self.get_type()}
Nation  : {self.get_nation()}
Alliance: {self.get_alliance()}
IPC     : {self.get_ipc()}
Units   : {self.get_units()}
'''

##############################################################################
class CAANation(CAAItem):
    def __init__(self, s_name:str, alliance:int) -> None:
        super().__init__(s_name, CType.C_NATION)
        self.aa_alliance = alliance
        pass


##############################################################################
class CAALand(CAAItem):
    def __init__(self, s_name:str, aa_nation:CAANation, aa_ipc:int, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_LAND)
        self.aa_ipc=aa_ipc
        self.l_aa_units = l_aa_units
        self.aa_nation = aa_nation
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
        self.set_nation(aa_nation)
        self.i_count = i_count
        pass

##############################################################################
class CAAInf(CAAUnit):
    def __init__(self, aa_nation, i_count = 1) -> None:
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
def test_nation(s_name:string, aa_alliance:int):
    caa = CAANation(s_name, aa_alliance)
    assert(caa.get_name() == s_name)
    assert(caa.get_type() == CType.str(CType.C_NATION))
    assert(caa.get_alliance() == CType.str(aa_alliance))
    print(caa.info())    

def test_land(s_name:string, aa_nation:CAANation, aa_ipc:int, l_aa_units:list):
    caa = CAALand(s_name, aa_nation, aa_ipc, l_aa_units)
    assert(caa.get_name() == s_name)
    assert(caa.get_type() == CType.str(CType.T_LAND))
    assert caa.get_alliance() == aa_nation.get_alliance(), f"{caa.get_alliance()} != {aa_nation.get_alliance()}"
    assert(caa.get_ipc()  == aa_ipc)
    assert(caa.get_units()  == str(l_aa_units))
    
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
    test_land("Western Germany",CAANation("Germany",CType.A_AXIS),10,[])
    
    