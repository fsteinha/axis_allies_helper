##
# @mainpage Axis and allies helper
#
# @section description_main Description
# This i an application for support an ais and allies board game
# All data can be added durring the game and save for the next game

# @section notes_main Notes
# - current state is development stat
#
# Copyright (c) 2022 Fred Steinhaeuser.  All rights reserved.

# imports
import argparse
from pyfiglet import Figlet
from tabulate import tabulate

import aa_session_def_global_1940
from aa_session import *

# constanst
OPT_GLOBAL_1940 = 1


def main():
    """! The main function.
    TODO
    """

    # read in the arguments
    args = option_parser()

    if (args.global_1940 == False) and (args.file != None):
        load_session(args.file)
        pass
    else:
        aa_session = CAAI_Session(s_name              = "Global game 1940",
                                    aa_map            = C_MAP_GLOBAL_1940,
                                    i_round           = 1,
                                    l_aa_nations      = L_NATION_SETUP_GLOBAL_1940,
                                    aa_current_nation = CAAN_GERMANY,
                                    aa_current_phase  = CType.S_PH1_PURCHASE_REPAIR)

    if args.status == True:
        print_session_status(aa_session)

    if args.out != None:
        save_session(args.out, aa_session)



##############################################################################
def print_session_status(aa_session:CAAI_Session):
    # banner
    f = Figlet(font='slant')
    print (f.renderText("A & A helper"))
    table = [['Session name',   aa_session.get_name()],
             ['Map',            aa_session.aa_map.get_name()],
             ['Round',          aa_session.get_round()],
             ['Nations',        aa_session.get_nations_as_str()],
             ['Current nation', aa_session.get_current_nation().get_name()],
             ['Current phase',  aa_session.get_current_phase()]
             ]
    print(tabulate(table))


def save_session(s_file_out:str, aa_session:CAAI_Session) -> bool:
    file = open(s_file_out, 'w')
    s_json_out = aa_session.get_json()

    if s_json_out != None:
        file.write(s_json_out)
        return False

    file.close()
    return True

def load_session(s_file_in:str) -> bool:
    file = open (s_file_in, "r")
    s_json = file.read()
    print (s_json)
    CAAI_Session.set_json(s_json)



##############################################################################
def option_parser():
    """!Parse program options
        @return args object
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', '--file', action='store', type=str,
                    help='File for read in store session')

    parser.add_argument('-s', '--status', action='store_true', default=False,
                    help='Show status of the session')

    parser.add_argument('-o', '--out', action='store', type=str,
                    help='File for write session in given file')

    parser.add_argument('-d1', '--global_1940', action='store_true',
                    help='Use the initial global configuraion for the 1940 global game (default)')

    args = parser.parse_args()
    return args
    pass



if __name__ == "__main__":
    main()