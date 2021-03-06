from aa_type import CType
from aa_item import CAAItem
from aa_nation import *
from aa_rules import *

##############################################################################
class CAAI_Territory(CAAItem):
    def __init__(self, s_name:str,aa_region:CType, c_rules:CAAR, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_LAND)
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
        
        return self.c_container.add(aa_unit)
        
    def sub_unit(self, aa_unit) -> bool:
        if self.c_rules.check_sub(self.c_container) == False:
            return False
        
        return self.c_container.sub(aa_unit)
        
    def get_unit_count(self):
        return self.c_container.get_unit_count()


##############################################################################
class CAAT_Land(CAAI_Territory):
    def __init__(self, s_name: str, aa_region: CType, aa_nation: CAAI_Nation, aa_ipc: int, c_rules: CAAR, l_aa_units: list = []) -> None:
        
        if (str(c_rules).find("CAAR_Land") == -1):
            raise Exception (f"isinstance(c_rules, CAAR_Land) results False")
        
        super().__init__(s_name, aa_region, c_rules, l_aa_units)
        self.aa_ipc=aa_ipc
        self.aa_nation = aa_nation
        
        pass
        
##############################################################################
class CAAT_Sea(CAAI_Territory):
    def __init__(self, s_name: str, aa_region: CType, c_rules: CAAR, l_aa_units: list = []) -> None:
        super().__init__(s_name, aa_region, c_rules, l_aa_units)
        pass

    
##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")