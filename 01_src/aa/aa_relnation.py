##
# @file aa_relnation.py
#
# @brief class for map of territories.
#
# @section description_aa_territory Description
# This modul includes the classes:
# TODO
#
# The CAAI_Map contains all territoires of axis and allies session
#
# @section libraries_main Libraries/Modules
# TODO
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_map TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 18/09/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.

from os import EX_CANTCREAT

from aa_type import CType
from aa_item import CAAItem
from aa_nation import CAAI_Nation

class CAAI_RelNation(CAAItem):
    """! The relation nation class.
    This class contains the nations and the state of the relation
    """
    def __init__(self, s_name, l_aa_nations, l_aa_relations) -> None:
        """! The relation nation class.
            @param s_name name of the relation
            @param l_aa_nations list of the involved nations
            @param l_aa_relations list of the tracked relation values            
        """
    
        super().__init__(s_name, CType.C_RELATION)
        
        # dictionary for the relations 
        #  key = hash
        #  value = tulpe (aa_nation1, aa_nation_2, relation_value)
        self.d_relations = {}

        # check is nation in class list and append
        self.l_aa_nations = []
        for aa_nation in l_aa_nations:
            if not isinstance(aa_nation, CAAI_Nation):
                raise Exception (f"{aa_nation} is not a CAAI_Nation type")
            if aa_nation not in self.l_aa_nations:
                self.l_aa_nations.append(aa_nation)
        
        # Check is value in list and append
        self.l_aa_rel_values = []
        for aa_rel_value in l_aa_relations:
            if CType.get_class(aa_rel_value) != CType.C_RELATION:
                raise Exception (f"{aa_rel_value} is not a C_RELATION type")
            if aa_rel_value not in self.l_aa_rel_values:
                self.l_aa_rel_values.append(aa_rel_value)
        
        # Check are names in list double
        l_nation_names = []
        for aa_nation in self.l_aa_nations:
            l_nation_names.append(aa_nation.get_name())
        
        for s_nation_name in l_nation_names:
            if l_nation_names.count(s_nation_name) > 1:
                raise Exception (f"multiple nation name {s_nation_name}")
        


    def set_relation(self, aa_nation_1:CAAI_Nation, aa_nation_2:CAAI_Nation, aa_rel_value) -> bool:
        """! Method for setting the relation for two nations.
            @param aa_nation_1 name of the one nation
            @param aa_nation_2 name of the second nation
            @param aa_rel_value  list of the involved nations
        """

        b_ret = self.check_parameter(aa_nation_1:CAAI_Nation, aa_nation_2:CAAI_Nation, aa_rel_value)        
        
        # Build the hash and set relation
        if b_ret == True:
            s_hash = self.build_hash(aa_nation_1, aa_nation_2)
            self.d_relations[s_hash] = (aa_nation_1, aa_nation_2, aa_rel_value)

        return b_ret

    def get_relation(self, aa_nation_1:CAAI_Nation, aa_nation_2:CAAI_Nation):
        """! Method for setting the relation for two nations.
            @param aa_nation_1 name of the one nation
            @param aa_nation_2 name of the second nation
        """

        b_check = self.check_parameter(aa_nation_1:CAAI_Nation, aa_nation_2:CAAI_Nation, aa_rel_value) 
        
        # Build the hash and set relation
        if b_check == True:
            s_hash = self.build_hash(aa_nation_1, aa_nation_2)
            if s_hash in self.d_relations:
                return self.d_relations[s_hash] 

        return None


    def check_parameter(self, aa_nation_1:CAAI_Nation, aa_nation_2:CAAI_Nation, aa_rel_value) -> bool:
        """! Check the parameter for methods set_relation / get_relation .
            @param aa_nation_1 name of the one nation
            @param aa_nation_2 name of the second nation
            @param aa_rel_value  list of the involved nations
        """
        
        # Check are nation listed
        if aa_nation_1 not in self.l_aa_nations:
            self.set_error_message(f"Nation {aa_nation_1} not listed")
            return False

        if aa_nation_2 not in self.l_aa_nations:
            self.set_error_message(f"Nation {aa_nation_2} not listed")
            return False
        
        # Check is value listed
        if aa_rel_value not in self.l_aa_rel_values:
            self.set_error_message(f"Value {aa_rel_value} not listed")
            return False

        
    def build_hash(self, aa_nation_1:CAAI_Nation, aa_nation_2:CAAI_Nation) -> str:
        """! Build hash from two nation .
            @param aa_nation_1 name of the one nation
            @param aa_nation_2 name of the second nation
        """
        l_temp = [aa_nation_1.get_name(), aa_nation_2.get_name()]
        l_temp = l_temp.sort()
        return (l_temp[0] + l_temp[1])
                