from copy import deepcopy
from aa_type import CType
from aa_rules import *
from aa_container import *
from aa_items import *
from tabulate import tabulate

##############################################################################
class CAAU_Inf(CAAUnit):
    def __init__(self, aa_nation:CAANation, i_count = 1) -> None:
        super().__init__(CType.U_INFANTARY, aa_nation, i_count)
        pass

##############################################################################
class CAAU_MechInf(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_MECH_INFANTARY, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Tank(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_TANK, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Ari(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_ARTILLERY, aa_nation, i_count)
        pass

##############################################################################
class CAAU_AAA(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_AAA, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Figther(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_FIGHTER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_TBomb(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_T_BOMBER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_SBomb(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_S_BOMBER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Submarine(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_SUBMARINE, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Destroyer(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_DESTROYER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Cruiser(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_CRUISER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Battleship(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_BATTLESHIP, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Container(CAAUnit):
    def __init__(self, aa_nation, c_rules:CAAR, l_aa_units:list = None) -> None:
        super().__init__(CType.U_CARRIER, aa_nation, i_count = None)
        self.c_rules = c_rules
        self.c_container = CAAUnitContainer()

        if l_aa_units != None:
            for unit in l_aa_units:
                if self.add_unit(unit) == False:
                    raise Exception (f"Add unit fail {unit}")
        pass

    def add_unit(self, aa_unit:CAAUnit) -> bool:
        if self.c_rules.check_add(self.c_container, aa_unit.get_type()) == False:
            return False
        
        self.c_container.add(aa_unit)
        return True
    
    def sub_unit(self, aa_unit) -> bool:
        if self.c_rules.check_sub(self.c_container) == False:
            return False
        
        return self.c_container.sub(aa_unit)
        
    def get_unit_count(self):
        return self.c_container.get_unit_count()

##############################################################################
class CAAU_Carrier(CAAU_Container):
    def __init__(self, aa_nation, c_rules: CAAR_Carrier, l_aa_units: list = None) -> None:
        super().__init__(aa_nation, c_rules, l_aa_units)
        pass
 
##############################################################################
class CAAU_Cargo(CAAU_Container):
    def __init__(self, aa_nation, c_rules: CAAR_Cargo, l_aa_units: list = None) -> None:
        super().__init__(aa_nation, c_rules, l_aa_units)
        pass


##############################################################################
class CAAF_Major(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_MAJOR_FACTORY)
        pass

##############################################################################
class CAAF_Minor(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_MINOR_FACTORY)
        pass

##############################################################################
class CAAF_AirBase(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_AIR_BASE)
        pass

##############################################################################
class CAAF_NavalBase(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_NAVAL_BASE)
        pass


##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")