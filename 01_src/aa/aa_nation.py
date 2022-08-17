from aa_type import CType
from aa_item import CAAItem
from aa_rules import *

##############################################################################
class CAAI_Nation(CAAItem):
    def __init__(self, s_name:str, aa_alliance:int) -> None:
        super().__init__(s_name, CType.C_NATION)
        self.aa_alliance = aa_alliance
        pass
    
    def get_nation(self):
        return self

##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")