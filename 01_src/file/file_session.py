##
# @file file_session.py
#
# @brief supports functions for saving and loading a session.
#
# @section description_conv_excel Description
# Classes provided by this module:
# - CFILE_Session, class for storing the session
#   - Supported file formats: python dump (MODE_BIN)
##
# @section libraries_main Libraries/Modules
# - pickle for dump
#
# @section notes_aa_territory Notes
# - Comments are Doxygen compatible.
#
# @section todo_file_session TODO
# - JSON support
#
# @section author_doxygen_aa_territory Author(s)
# - Created by Fred Steinhäuser on 2022/08/17.
#
# Copyright (c) 2022 Fred Steinhäuser.  All rights reserved.

import pickle

class CFILE_Session():
    """! Class for store and load a session to or from file"""

    MODE_BIN = "binary_dump"
    """! Class constant for binary dump"""

    def __init__(self, s_filename:str, s_mode = MODE_BIN) -> None:
        """! Constructor for the file export / import class"""
        self.s_filename = s_filename
        self.s_mode = s_mode
        pass

    def save_session(self, aa_session) -> bool:
        """! Save the session
           @param aa_session session object
           @return
            - True - Success
            - False - Failure
        """
        if self.s_mode == self.MODE_BIN:
            file_aa_session = open(self.s_filename, 'wb')
            pickle.dump(aa_session, file_aa_session)
        return True

    def load_session(self):
        """! Load the session
            @return
                - Session object - sucess
                - None - Failure
        """
        aa_session = None
        if self.s_mode == self.MODE_BIN:
            file_aa_session = open(self.s_filename, 'rb')
            aa_session = pickle.load(file_aa_session)
        return aa_session