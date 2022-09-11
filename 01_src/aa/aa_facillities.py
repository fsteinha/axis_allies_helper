from aa_type import CType
from aa_item import CAAItem
from aa_rules import *

##############################################################################
class CAAI_Facillity(CAAItem):
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
class CAAF_Major(CAAI_Facillity):
    def __init__(self) -> None:
        super().__init__(CType.F_MAJOR_FACTORY)
        pass

##############################################################################
class CAAF_Minor(CAAI_Facillity):
    def __init__(self) -> None:
        super().__init__(CType.F_MINOR_FACTORY)
        pass

##############################################################################
class CAAF_AirBase(CAAI_Facillity):
    def __init__(self) -> None:
        super().__init__(CType.F_AIR_BASE)
        pass

##############################################################################
class CAAF_NavalBase(CAAI_Facillity):
    def __init__(self) -> None:
        super().__init__(CType.F_NAVAL_BASE)
        pass


##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")