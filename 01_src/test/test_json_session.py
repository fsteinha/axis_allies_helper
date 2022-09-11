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

from json_session import *
from aa_session import *

def test_get_json():
    aa_session = CAAI_Session("test")
    s_json = CJSON_Session().get_json(aa_session)
   # print (s_json)

if __name__ == "__main__":
    test_get_json()
