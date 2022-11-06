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

import json
import collections

from aa_type import CType
from aa_item import CAAItem
from aa_nation import *
from aa_map import *
from aa_relnation import *

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
    """! The session class.
    The session class contains all objects of an axis and allies session
    """

    JSON_SESSION_META   = "session_meta"

    JSON_SESSION_NAME   = "session_name"
    JSON_MAP            = "map"
    JSON_ROUND          = "round"
    JSON_NATIONS        = "nations"
    JSON_CURRENT_NATION = "current_nation"
    JSON_CURRENT_PHASE  = "current_phase"

    def __init__(self, s_name:str,
                       aa_map:CAAI_Map = C_MAP_GLOBAL_1940,
                       i_round:int = 1,
                       l_aa_nations = L_NATION_SETUP_GLOBAL_1940,
                       aa_current_nation:CAAI_Nation = CAAN_GERMANY,
                       aa_current_phase:int = CType.S_PH1_PURCHASE_REPAIR,
                       l_aa_relnations:list = [C_REL_NATION]) -> None:
        """! The session class initializer.
        @param s_name               Name of the session
        @param aa_map               aa_map object (default = None).
        @param i_round              Number for round (default = 1)
        @param l_aa_nations         List with playing nations ((default = [])).
        @param aa_current_nation    Nation which is active (default = None)
        @param aa_current_phase     Active phase (default = None)
        @param l_aa_relations       list with active relations

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

        #check is current nation in l_aa_nations
        if (aa_current_nation not in l_aa_nations):
            raise Exception (f"Given aa_current_nation object is not in l_aa_nations")
        
        self.aa_current_nation = aa_current_nation

        #check is are nations l_aa_nations all in map
        l_map_nations = aa_map.get_nations()
        for aa_nation in l_aa_nations:
            if aa_nation not in l_map_nations:
                raise Exception (f"given nation {aa_nation.get_name()} in play list is not placed in map")
        
        # check current phase
        if (aa_current_phase < CType.S_PH1_PURCHASE_REPAIR) or (aa_current_phase > CType.S_PH6_COLLECT_INCOME):
            raise Exception (f"aa_current_phase not valid {aa_current_phase}")

        # check nation relations
        self.l_aa_relnations = l_aa_relnations
        if (len(self.l_aa_relnations) > 0):
            for aa_relnation in self.l_aa_relnations:
                if self.check_relnations(aa_relnation) == False:
                    raise Exception (f"check_relnations failes with {aa_relnation}")
            pass
            
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

    def get_nation_names_as_str(self, s_seperator = '\n'):
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

    def get_nation_names_as_list(self):
        """! Getter for nations as list
           @return nations in a list
        """
        l_ret = []
        # check nation list type
        for aa_nation in self.l_aa_nations:
            l_ret.append(aa_nation.get_name())
        return l_ret

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

    def get_nation_ipc(self, nation) -> int:
        """! Collect the ipc 
           @return current nation as object or string
        """
        aa_nation = None
        if (type(nation) == str):
            aa_nation = self.get_nation_obj(nation)
        elif (type(nation) == CAAI_Nation):
            aa_nation = nation
        
        if aa_nation == None:
            i_IPC =-1
        else:
            i_IPC = 0
            l_lands = self.aa_map.get_lands_as_list([aa_nation])
            for land in l_lands:
                i_IPC = i_IPC + land.get_ipc()
        
        return i_IPC
    
    def get_nation_obj(self, s_nation):
        """! Return the nation object from self.l_aa_nations as aa_object
            @param nation as string
            @return nation as object
        """ 
        for aa_nation in self.l_aa_nations:
            if s_nation == aa_nation.get_name():
                return aa_nation
        return None

    def get_relnation(self, s_relnation_name):
        
        for relnation in self.l_aa_relnations:
            if relnation.get_name() == s_relnation_name:
                return relnation
        return None


    def get_json(self) -> str:
        """! Returns a json text with the status
           @return json with status
        """
        
        s_json = json.dumps({self.JSON_SESSION_META :
                                {
                                    self.JSON_SESSION_NAME  : self.get_name(),
                                    self.JSON_MAP           : self.aa_map.get_name(),
                                    self.JSON_ROUND         : self.get_round(),
                                    self.JSON_NATIONS       : self.get_nations_as_list(),
                                    self.JSON_CURRENT_NATION: self.get_current_nation().get_name(),
                                    self.JSON_CURRENT_PHASE : self.get_current_phase()
                                }
                            }, indent=4)
        return s_json

    @staticmethod
    def set_json(s_json:str):
        d_json = json.loads(s_json)
        pass

    def check_relnations(self, aa_relnation:CAAI_RelNation) -> bool:
        """! Checker for plausiblity for nations in relnation list"""
        if collections.Counter(self.l_aa_nations) != collections.Counter(aa_relnation.get_nations()):
            return False
        return True

##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")