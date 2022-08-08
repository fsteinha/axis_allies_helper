##
# @file aa_session.py
#
# @brief class for map of territories.
#
# @section description_aa_territory Description
# This modul includes the classes:
# - CAAI_Session
# 
# The CAAI_Map contains all territoires of axis and allies session
#
# @section libraries_main Libraries/Modules
# - aa_type (local)
# - aa_item (local)
# - aa_map(local)
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_map TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 08/08/2022.
# - Modified by Fred Steinhäuser on 08/08/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.

from aa_type import CType
from aa_item import CAAItem
from aa_map import *


##############################################################################
class CAAI_Session(CAAItem):
    """! The map class.
    The session class contains all objects of an axis and allies session
    """
    def __init__(self, s_name:str, 
                       aa_map:CAAI_Map = None, 
                       l_aa_alliances:list = [], 
                       d_aa_nations:dict = {}, 
                       l_aa_session_phases:list = [], 
                       i_round:int = 1, 
                       aa_current_nation:CAAI_Nation = None,
                       aa_current_phase:int = 0) -> None:
        """! The session class initializer.
        @param s_name               Name of the session
        @param aa_map               aa_map object (default = None).
        @param l_aa_alliances       List with playing alliances ((default = [])).
        @param d_aa_nations         Dictionary with playing nations (key=nation, value=alliance).
        @param l_aa_session_phases  List of the phases in the round. (default = [])
        @param i_round              Number for round (default = 1)
        @param aa_current_nation    Nation which is active (default = None)
        @param aa_current_phase     Active phase (default = None)

        @return  An instance of session class.
        """
        super().__init__(s_name, CType.S_SESSION)
        TODO 
        pass

    
##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")