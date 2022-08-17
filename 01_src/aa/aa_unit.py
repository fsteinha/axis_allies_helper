from aa_type import CType
from aa_item import CAAItem

##############################################################################
class CAAUnit(CAAItem):
    def __init__(self, aa_type:int, aa_nation, i_count:int = 1) -> None:
        super().__init__(CType.str(aa_type), aa_type)
        self.aa_nation = aa_nation
        if i_count != None:
            if (i_count > 0):
                self.i_count = i_count
            else:
                self.i_count = 1 
            pass
        else:
           self.i_count = None
        

    def add(self, i_add):
        if self.i_count != None:
            if (i_add >= 0):
                self.i_count = self.i_count + i_add 

    def sub(self, i_sub):
        if self.i_count != None:
            if (i_sub >= 0):
                self.i_count = self.i_count - i_sub
                if (self.i_count < 0):
                    self.i_count = 0
            
    def reset_count(self, i_count:int) -> None:
        if self.i_count != None:
            if (i_count >= 0):
                self.i_count = i_count
            else:
                self.i_count = 0
