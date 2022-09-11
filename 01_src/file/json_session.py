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
from aa_session import *
from aa_nation import *
from aa_map import *
from aa_container import *
from aa_rules import *
class CJSON_Session():
    """! The Json converter.
    This class provides methods to build up a session from a given csv and to store a session to a csv file.
    """
    KEY_GLOBAL_NATION_LIST = "global_nations"
    VALULE_NOT_SUPPORTED = "NOT_SUPPORTED"

    TYPE_LIST = 'list'
    TYPE_DICT = 'dict'

    TYPE_OTHER = 'other'

    def __init__(self) -> None:
        self.d_json = {}
        self.l_global_nation = []

        pass

    def get_json(self, c_object):
        # put in the class items
        self.add_object(c_object, self.d_json)

        # put in the global nation references
        self.d_json[self.KEY_GLOBAL_NATION_LIST] = {}
        for c_nation in self.l_global_nation:
            d_nation = {}
            self.add_object(c_nation, d_nation)
            self.d_json[self.KEY_GLOBAL_NATION_LIST][str(c_nation)] = d_nation
        # #return d_json
        return json.dumps(self.d_json, indent=4)


        pass

    def add_object(self, c_object, d_element:dict):
        for class_item in vars(c_object).items():
            if (type(class_item[1]) == list):
                d_element[class_item[0]] = []
                for list_item in class_item[1]:
                    self.add_element(list_item, class_item[0], d_element, self.TYPE_LIST)
            if (type(class_item[1]) == dict):
                d_dict = {}
                for dict_key in class_item[1]:
                    self.add_element(class_item[1][dict_key], dict_key, d_dict, self.TYPE_DICT)
                d_element[class_item[0]] = d_dict
            else:
                self.add_element(class_item[1], class_item[0], d_element, self.TYPE_OTHER)

        pass

    def add_element(self, value, s_list_key:str, d_element:dict, s_value_type:str):
        if (type(value) == CAAI_Nation) and (value not in self.l_global_nation):
            self.l_global_nation.append(value)


        if ((type(value) == str) or\
            (type(value) == int) or\
            (type(value) == None)):
            json_value = value
        elif (type(value) == CAAI_Nation):
            json_value = str(value)
        elif (type(value) == CAAI_Map):
            json_value = {}
            self.add_object(value, json_value)
        elif (type(value) == CAAT_Sea):
            json_value = {}
            self.add_object(value, json_value)
        elif (type(value) == CAAT_Land):
            json_value = {}
            self.add_object(value, json_value)
        elif (type(value) == CAAR_Land):
            json_value = {}
            self.add_object(value, json_value)
        elif (isinstance(value, CAAR_Sea)):
            json_value = {}
            self.add_object(value, json_value)
        elif (type(value) == CAAR_Carrier):
            json_value = {}
            self.add_object(value, json_value)
        elif (type(value) == CAAR_Cargo):
            json_value = {}
            self.add_object(value, json_value)
        elif (type(value) == CAAU_Container):
            json_value = {}
            self.add_object(value, json_value)
        else:
            json_value = self.VALULE_NOT_SUPPORTED
            print (f"Not supporded item {s_list_key} with type {type(value)}")
            #raise Exception (f"Not supporded item {s_list_key} with type {type(value)}")



        if s_value_type == self.TYPE_LIST:
            d_element[s_list_key].append(json_value)
        else:
            d_element[s_list_key] = json_value
        pass

