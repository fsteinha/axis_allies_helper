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

from multiprocessing import reduction
from re import I
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
                       aa_map:CAAI_Map = C_MAP_GLOBAL_1940,
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

        # check map type
        if (type(aa_map) != CAAI_Map):
            raise Exception (f"Given map is unvalid {type(aa_map)}")

        self.aa_map = aa_map

        # check the round
        if (self.set_round(i_round) == False):
            raise Exception (f"i_round not valid: {i_round}")

        # check nations list
        if (type(l_aa_nations) != list):
            raise Exception (f"Given nation list is unvalid {type(l_aa_nations)}")

        # check nation list type
        for aa_nation in l_aa_nations:
            if (type(aa_nation) != CAAI_Nation):
                raise Exception (f"Given object in l_aa_nations is not an nation object {type(aa_nation)}")

        self.l_aa_nations = l_aa_nations

        # check current nation type
        if (type(aa_current_nation) != CAAI_Nation):
            raise Exception (f"Given aa_current_nation object is not an nation object {type(aa_current_nation)}")

        if (aa_current_nation not in l_aa_nations):
            raise Exception (f"Given aa_current_nation object is not in l_aa_nations")

        self.aa_current_nation = aa_current_nation

        # check current phase
        if (aa_current_phase < CType.S_PH1_PURCHASE_REPAIR) or (aa_current_phase > CType.S_PH6_COLLECT_INCOME):
            raise Exception (f"aa_current_phase not valid {aa_current_phase}")

        self.aa_current_phase = aa_current_phase
        pass

    def set_round(self, i_round:int) -> bool:
        """! set the round for session
            @param i_round integer for round counter
            @return
                - True: Setting is successfull
                - False: setting is not successful
        """
        # check the round
        if (i_round < 1):
            return False
        self.i_round = i_round
        return True

    def set_next_round(self) -> bool:
        """! Set the next round
             Checks the phase status,
             incremets the counter
             sets the new phase
             @return
                - True: Setting is successfull
                - False: setting is not successful
        """
        if (self.aa_current_phase == CType.S_PH6_COLLECT_INCOME):
            self.i_round = self.i_round + 1
            self.aa_current_phase = CType.S_PH1_PURCHASE_REPAIR
            return True
        return False

    def get_round(self):
        """! Getter for the session round
            @return the current round counter
        """
        return self.i_round

    def get_nations_as_str(self, s_seperator = '\n'):
        """! Getter for nations as string
           @param  s_seperator speartor for nations in string
           @return nations as string
        """
        s_ret = ""
        # check nation list type
        for aa_nation in self.l_aa_nations:
            s_ret = s_ret + aa_nation.get_name()
            s_ret = s_ret + s_seperator
        s_ret = s_ret[:-1]
        return s_ret

    def get_current_nation(self):
        """! Returns the current nation which should to the turn
           @return current nation
        """
        return self.aa_current_nation

    def get_current_phase(self):
        """! Returns the current nation which should to the turn
           @return current nation
        """
        return CType.str(self.aa_current_phase)

##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")