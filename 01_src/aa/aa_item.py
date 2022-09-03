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

        self.s_error_message = None

    def set_error_message(self, s_error_msg: str) -> None:
        #print(f"Error: {s_error_msg}")
        self.s_error_message = s_error_msg

    def get_error_message(self) -> None:
        return self.s_error_message

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

    def get_origin_nation(self):
        if ('aa_origin_nation' in dir(self)):
            return self.aa_origin_nation
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
        s_ret = ""
        s_nation = None
        s_origin_nation = None
        if (self.get_nation()) != None:
            s_nation = self.get_nation().s_name

        if (self.get_origin_nation()) != None:
            s_origin_nation = self.get_origin_nation().s_name

        s_container = self.get_units()
        if s_container != None:
            s_container = "\n    " + s_container.replace("\n", "\n    ") + "\n"
        else:
            s_container = "N/A"

        if ('d_neighbore' in dir(self)):
            b_neighbore = True

            def intern_get_neighbore(s_key):
                if self.get_neighbore(s_key) != None:
                    return self.get_neighbore(s_key).get_name()
                return None

            s_neighbore_nord       = intern_get_neighbore('n')
            s_neighbore_nord_east  = intern_get_neighbore('ne')
            s_neighbore_east       = intern_get_neighbore('e')
            s_neighbore_south_east = intern_get_neighbore('se')
            s_neighbore_south      = intern_get_neighbore('s')
            s_neighbore_south_west = intern_get_neighbore('sw')
            s_neighbore_west       = intern_get_neighbore('w')
            s_neighbore_nord_west  = intern_get_neighbore('nw')
        else:
            b_neighbore = False


        s_ret = s_ret + f"{__name__}.{inspect.currentframe().f_code.co_name}:"
        s_ret = s_ret + f"  Name          : {self.get_name()}" + "\n"
        s_ret = s_ret + f"  Region        : {CType.str(self.get_region())}" + "\n"
        s_ret = s_ret + f"  Type          : {CType.str(self.get_type())}" + "\n"
        s_ret = s_ret + f"  Nation        : {s_nation}" + "\n"
        s_ret = s_ret + f"  Origin Nation : {s_origin_nation}" + "\n"
        s_ret = s_ret + f"  Alliance      : {CType.str(self.get_alliance())}" + "\n"
        s_ret = s_ret + f"  IPC           : {self.get_ipc()}" + "\n"
        s_ret = s_ret + f"  Count         : {self.get_count()}" + "\n"
        s_ret = s_ret + f"  Units         : {s_container}" + "\n"
        if b_neighbore == True:
            s_ret = s_ret + f"  Neighbore nord       : {s_neighbore_nord}"       + "\n"
            s_ret = s_ret + f"  Neighbore nord_east  : {s_neighbore_nord_east}"  + "\n"
            s_ret = s_ret + f"  Neighbore east       : {s_neighbore_east}"       + "\n"
            s_ret = s_ret + f"  Neighbore south_east : {s_neighbore_south_east}" + "\n"
            s_ret = s_ret + f"  Neighbore south      : {s_neighbore_south}"      + "\n"
            s_ret = s_ret + f"  Neighbore south_west : {s_neighbore_south_west}" + "\n"
            s_ret = s_ret + f"  Neighbore west       : {s_neighbore_west}"       + "\n"
            s_ret = s_ret + f"  Neighbore nord_west  : {s_neighbore_nord_west}"  + "\n"
        else:
            s_ret = s_ret + f"  Neighbore  : N/A" + "\n"
        s_ret = s_ret + f"Error           :{self.get_error_message()}"


        return s_ret

##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")