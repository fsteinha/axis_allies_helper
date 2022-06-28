from aa_type import CType
from aa_item import CAAItem
from aa_rules import *

##############################################################################
class CAANation(CAAItem):
    def __init__(self, s_name:str, aa_alliance:int) -> None:
        super().__init__(s_name, CType.C_NATION)
        self.aa_alliance = aa_alliance
        pass
    
    def get_nation(self):
        return self


##############################################################################
class CAALand(CAAItem):
    def __init__(self, s_name:str,aa_region:CType, aa_nation:CAANation, aa_ipc:int, c_rules:CAAR, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_LAND)
        self.aa_ipc=aa_ipc
        self.l_aa_units = l_aa_units
        self.aa_nation = aa_nation
        self.aa_region = aa_region
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
class CAASea(CAAItem):
    def __init__(self, s_name:str, aa_ipc:int, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_SEA)
        self.l_aa_units = l_aa_units
        pass

##############################################################################
class CAAFacillity(CAAItem):
    def __init__(self, aa_type:int) -> None:
        super().__init__(CType.str(aa_type), aa_type)        
        self.i_count = 1

    def add(self, i_add):
        if (self.i_count != None) and (self.i_count < 1):
            if (i_add >= 0):
                self.i_count = self.i_count + i_add 
        
        if (self.i_count > 1):
            self.i_count = 1

    def sub(self, i_sub):
        if self.i_count != None:
            if (i_sub >= 0):
                self.i_count = self.i_count - i_sub
            
    def reset_count(self, i_count:int) -> None:
        if self.i_count != None:
            if (i_count >= 0):
                self.i_count = i_count
            else:
                self.i_count = 0        

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