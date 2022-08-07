##
# @file aa_map.py
#
# @brief class for map of territories.
#
# @section description_aa_territory Description
# This modul includes the classes:
# - TBD
#
# @section libraries_main Libraries/Modules
# - aa_type (local)
# - aa_item (local)
# - aa_territory(local)
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_territory TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 08/07/2022.
# - Modified by Fred Steinhäuser on 08/07/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.


from locale import D_FMT
from aa_type import CType
from aa_item import CAAItem
from aa_territory import *


##############################################################################
class CAAI_Map(CAAItem):
    """! The map class.
    The map class contains all territories and return this by name
    TODO
    """
    def __init__(self, s_name: str, l_aa_territories:list = []) -> None:
        """! The map class initializer.
        @param l_aa_territories list with all inclusing territoriespreset units.
        @return  An instance of map class.
        """
        super().__init__(s_name, CType.S_MAP)
         
        self.d_territories = {}
        if l_aa_territories != None:
            for territory in l_aa_territories:
                if self.add_territorie(territory) == False:
                    raise Exception (f"Add territorie fail {territory}")
        pass

    def add_unit(self, aa_territory:CAAI_Territory) -> bool:
        """! Add a territory to global dictionary
        @param aa_unit Unit which should ad
        @return  
         - True 
            - territory was added sucessfull.
         - False 
            - territory could not add.
        """
        if aa_territory not in self.d_territories:
            self.d_territories[aa_territory.get_name()] = aa_territory
        else:
            return False
        
        return True
        
    def get_territory(self, s_territory: str) -> CAAI_Territory:
        """! Returns the territory object by given name
        @return 
        - Success territory object
        - Fail    None
        """
        if s_territory not in self.d_territories:
            return self.d_territories[s_territory]
        
        return None
    
##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")