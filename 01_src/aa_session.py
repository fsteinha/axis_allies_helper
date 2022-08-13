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
from aa_nation import *
from aa_map import *

from aa_session_def_global_1940 import *

L_SESSION_PHASES = [
    CType.S_PH1_PURCHASE_REPAIR,
    CType.S_PH2_COMBAT_MOVE,
    CType.S_PH3_CONDUCT_COMBAT,
    CType.S_PH4_NONCOMBAT_MOVE,
    CType.S_PH5_MOBILIZE_NEW_UNITS,
    CType.S_PH6_COLLECT_INCOME,
]

##############################################################################
class CAAI_Session(CAAItem):
    """! The map class.
    The session class contains all objects of an axis and allies session
    """
    def __init__(self, s_name:str,
                       aa_map:CAAI_Map = None,
                       i_round:int = 1,
                       l_aa_nations = L_NATION_SETUP_GLOBAL_1940,
                       aa_current_nation:CAAI_Nation = CAAN_GERMANY,
                       aa_current_phase:int = CType.S_PH1_PURCHASE_REPAIR) -> None:
        """! The session class initializer.
        @param s_name               Name of the session
        @param aa_map               aa_map object (default = None).
        @param i_round              Number for round (default = 1)
        @param l_aa_nations         List with playing nations ((default = [])).
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