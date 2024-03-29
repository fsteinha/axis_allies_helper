##
# @file aa_map.py
#
# @brief class for map of territories.
#
# @section description_aa_territory Description
# This modul includes the classes:
# - CAAI_Map
# 
# The CAAI_Map contains all territoires of axis and allies session
#
# @section libraries_main Libraries/Modules
# - aa_type (local)
# - aa_item (local)
# - aa_territory(local)
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_map TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 08/07/2022.
# - Modified by Fred Steinhäuser on 08/08/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.

from ast import Or
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
        @param s_name           Name of the map
        @param l_aa_territories list with all inclusing territoriespreset units.
        @return  An instance of map class.
        """
        super().__init__(s_name, CType.S_MAP)
         
        self.d_territories = {}
        if l_aa_territories != None:
            for territory in l_aa_territories:
                if self.add_territory(territory) == False:
                    raise Exception (f"Add territory fail {territory.get_name()}")
        pass

    def add_territory(self, aa_territory:CAAI_Territory) -> bool:
        """! Add a territory to global dictionary
        @param aa_unit Unit which should ad
        @return  
         - True 
            - territory was added sucessfull.
         - False 
            - territory could not add.
        """
        if (aa_territory.get_name() not in self.d_territories) and \
            ((aa_territory.get_type() == CType.T_LAND) or \
             (aa_territory.get_type() == CType.T_SEA)):
            self.d_territories[aa_territory.get_name()] = aa_territory
        else:
            return False
        
        return True
        
    def get_territory(self, s_territory: str) -> CAAI_Territory:
        """! Returns the territory object by given name
        @param s_territory name of territory
        @return 
        - Success territory object
        - Fail    None
        """
        if s_territory in self.d_territories:
            return self.d_territories[s_territory]
        
        return None
    
    def get_lands_as_list(self, l_filter_nation = None) -> list:
        """! Returns all territorys as list 
        @param l_filter_nation list with nations with should be exclusive in the list
        @return 
        - list with territories (lands)
        """
        l_ret = []
        for s_land_name in self.d_territories:
            if (self.d_territories[s_land_name].get_type() == CType.T_LAND) and \
                ((l_filter_nation == None) or (self.d_territories[s_land_name].get_nation() in l_filter_nation)):
                l_ret.append(self.d_territories[s_land_name])
        return l_ret
                
    def get_nations(self) -> list:
        """! Returns all nations which place in the map 
        @param 
        @return list with all nations 
        """
        
        l_ret = []
        for s_land_name in self.d_territories:
            l_nations = self.d_territories[s_land_name].get_nations()
            for aa_nation in l_nations:
                if aa_nation not in l_ret:
                    l_ret.append(aa_nation)

        return l_ret
        
        return super().get_nation()    
    
##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")