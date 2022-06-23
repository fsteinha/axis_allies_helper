from aa_type import CType
from aa_item import CAAItem

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
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")