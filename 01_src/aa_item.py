from aa_type import CType
import inspect

##############################################################################
class CAAItem():
    def __init__(self,s_name, aa_type) -> None:
        self.s_name = s_name

        if type(aa_type) == str:
            self.aa_type = CType.type(aa_type)
        elif  CType.str(aa_type) != None:
            self.aa_type = aa_type

    def get_name(self) -> str:
        if ('s_name' in dir(self)):
            return self.s_name
        return None

    def get_region(self) -> str:
        if ('aa_region' in dir(self)):
            return self.aa_region
        return CType.na()

    def get_type(self) -> str:
        return self.aa_type

    def get_nation(self):
        if ('aa_nation' in dir(self)):
            return self.aa_nation
        return None
        
    def get_alliance(self) -> str:
        if ('aa_alliance' in dir(self)):
            return self.aa_alliance
        elif ('aa_nation' in dir(self)):
            return self.aa_nation.get_alliance()
        return None

    def get_ipc(self) -> int:
        if ('aa_ipc' in dir(self)):
            return self.aa_ipc
        return CType.na()

    def get_units(self) -> int:
        if ('c_container' in dir(self)):
            if self.c_container != None:
                #return [item for item in self.l_aa_units]
                return self.c_container.info()
            return None
        return CType.na()

    def get_count(self) -> int:
        if ('i_count' in dir(self)):
            if self.i_count != None:
                return self.i_count
            return 1
        return CType.na()


    def info(self):
        s_nation = None
        if (self.get_nation()) != None:
            s_nation = self.get_nation().s_name
        
        s_container = self.get_units()
        if s_container != None:
            s_container = "\n    " + s_container.replace("\n", "\n    ") + "\n"
        else:
            s_container = "N/A"
        return f'''
{__name__}.{inspect.currentframe().f_code.co_name}:
  Name    : {self.get_name()}
  Region  : {CType.str(self.get_region())}
  Type    : {CType.str(self.get_type())}
  Nation  : {s_nation}
  Alliance: {CType.str(self.get_alliance())}
  IPC     : {self.get_ipc()}
  Count   : {self.get_count()}
  Units   : {s_container}
'''
      
##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")