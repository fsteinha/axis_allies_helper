##
# @file conv_csv.py
#
# @brief converter a session for import export from csv.
#
# @section description_conv_excel Description
# Classes provided by this module:
# - CCONV_Csv
#
# The territories in axis an allies are the areas for the conficting nations.
# Units (Troups, Facillities) are place on territories. 
#
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

class CCONV_Csv():
    """! The Csv converter.
    This class provides methods to build up a session from a given csv and to store a session to a csv file.
    """ 
    def __init__(self, s_file_name = None, s_csv_seperator = ';', s_list_seperator = ',', s_version = "0.1") -> None:
        """! The csv class initializer.
        @param s_file_name      The name of file (default: None)
        @param s_csv_seperator  Separator char for Csv.
        @param s_list_seperator Sepparator for lists in the Csv fields
        @param s_version        Format Version (Major.Minor). TODO(define Readin, writeout format)
        
        @return  An instance of csv converter class.
        """
 
        pass




