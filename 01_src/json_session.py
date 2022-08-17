##
# @file json_session.py
#
# @brief converter a session for import export from json.
#
# @section description_conv_excel Description
# Classes provided by this module:
# - CJSON_Session
##
# @section libraries_main Libraries/Modules
# TODO
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_aa_territory TODO
# - None.
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 08/07/2022.
# - Modified by Fred Steinhäuser on 08/08/2022.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.

import json
from this import d
from types import NoneType
from aa_session import *
from aa_nation import *
class CJSON_Session():
    """! The Json converter.
    This class provides methods to build up a session from a given csv and to store a session to a csv file.
    """
    KEY_GLOBAL_NATION_LIST = "global_nations"

    def __init__(self) -> None:
        self.d_json = {}
        self.l_global_nation = []

        pass

    def get_json(self, aa_session:CAAI_Session):
        # put in the class items
        self.add_object(aa_session)

        # put in the global nation references
        self.d_json[self.KEY_GLOBAL_NATION_LIST] = {}
        for nation in self.l_global_nation:
            d_nation = {}
            self.d_json[self.KEY_GLOBAL_NATION_LIST][str(nation)] = d_nation
        # #return d_json
        return json.dumps(self.d_json, indent=4)


        pass

    def add_object(self, c_object):
        for class_item in vars(c_object).items():
            if (type(class_item[1]) == list):
                self.d_json[class_item[0]] = []
                for list_item in class_item[1]:
                    self.add_element(list_item, class_item[0], True)
            else:
                self.add_element(class_item[1], class_item[0])

        pass

    def add_element(self, value, s_list_key:str, b_list = False):
        if (type(value) == CAAI_Nation) and (value not in self.l_global_nation):
            self.l_global_nation.append(value)


        if ((type(value) == str) or\
            (type(value) == int) or\
            (type(value) == NoneType)):
            json_value = value
        elif (type(value) == CAAI_Nation):
            json_value = str(value)
        else:
            json_value = "NOT_SUPPORTED"
            print (f"Not supporded item {s_list_key} with type {type(value)}")


        if b_list == False:
            self.d_json[s_list_key] = json_value
        else:
            self.d_json[s_list_key].append(json_value)
        pass

