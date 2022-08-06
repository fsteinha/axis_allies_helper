##
# @file aa_territory.py
#
# @brief class for territories (land and sea).
#
# @section description_aa_territory Description
# This modul includes the classes:
# - CAAI_Territory
# - TBD
#
# @section libraries_main Libraries/Modules
# - time standard library (https://docs.python.org/3/library/time.html)
#   - Access to sleep function.
# - sensors module (local)
#   - Access to Sensor and TempSensor classes.
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_territory TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 07/09/2022.
# - Modified by Fred Steinhäuser on 08/05/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.


from aa_type import CType
from aa_item import CAAItem
from aa_nation import *
from aa_rules import *

'''! Keys for the neighbore dictionary in CAAI_Territory'''
L_NEIGHBORE_KEY = ['nord', 'nord_east', 'east', 'south_east', 'south', 'south_west', 'west', 'nord_west']

##############################################################################
class CAAI_Territory(CAAItem):
    """! The territory class.
    This calls is the parrent class for CAAT_Land and CAAT_Sea.
    The class provides adding and removing units according to the given rules.
    """
    def __init__(self, s_name:str,aa_region:CType, c_rules:CAAR, l_aa_units:list = []) -> None:
        """! The Teritory class initializer.
        @param s_name     The name of the territory.
        @param aa_region  Region from static class CType.
        @param c_rules    Rules for the territory (land or sea), class CAAR.
        @param l_aa_units list with preset units.
        
        @return  An instance of territory class.
        """
        super().__init__(s_name, CType.T_LAND)
        self.aa_region = aa_region
        self.c_rules = c_rules
        self.c_container = CAAUnitContainer()
        self.d_neighbore = {'nord': None,
                            'nord_east': None,
                            'east': None,
                            'south_east': None,
                            'south': None,
                            'south_west': None,
                            'west': None,
                            'nord_west': None}
        
        if l_aa_units != None:
            for unit in l_aa_units:
                if self.add_unit(unit) == False:
                    raise Exception (f"Add unit fail {unit}")
        pass

    def add_unit(self, aa_unit:CAAUnit) -> bool:
        """! Add a unit to conatainer
        @param aa_unit Unit which should ad
        @return  
         - True 
            - Unit was added sucessfull.
         - False 
            - Unit could not add.
        """
        if self.c_rules.check_add(self.c_container, aa_unit.get_type()) == False:
            return False
        
        return self.c_container.add(aa_unit)
        
    def sub_unit(self, aa_unit) -> bool:
        """! Remove a containing unit
        @param aa_unit Unit which should remove
        @return  
         - True 
            - Unit was remove sucessfull.
         - False 
            - Unit could not remove.
        """

        if self.c_rules.check_sub(self.c_container) == False:
            return False
        
        return self.c_container.sub(aa_unit)
        
    def set_neighbore(self, s_neighbore: str, aa_territory) -> bool:
        """! Set a neighbore of territory
        @param s_neighbore  key value from L_NEIGHBORE_KEY.
        @param aa_territory class from type (inheritor) CAAI_Territory.
        @return  
         - True 
            - setting was successfull.
         - False 
            - preset of the value in s_neighbore is not None
            - s_neighbore is unknown
        """

        if (s_neighbore in L_NEIGHBORE_KEY) and (self.d_neighbore[s_neighbore] == None):
            self.d_neighbore[s_neighbore] = aa_territory
            return True
        return False

    def get_unit_count(self) -> int:
        """! Returns the coaunt of containing units
        @return  Containing units
        """

        return self.c_container.get_unit_count()


    def get_neighbore(self, s_neighbore: str) -> bool:
        """! Get a neighbore of territory
        @param s_neighbore  key value from L_NEIGHBORE_KEY.
        @return 
            - stored value for neigbore
            - Exception in case the s_neigbore ky is wrong
        """

        if (s_neighbore in L_NEIGHBORE_KEY):
            return self.d_neighbore[s_neighbore]
        else:
            raise Exception (f"wrong neibore key {s_neighbore}")
        
        # Never reached
        return None

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