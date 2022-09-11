import inspect
import pytest
from aa_type import CType
from aa_nation import CAAI_Nation

##############################################################################
# debug out
##############################################################################
def sub_test_header(s_func_name:str, info):
    print ("******************************")    
    print (f"Test: {s_func_name}")
    for arg in info[0]:
        arg_obj = info[3][arg]
        if type (arg_obj) != CAAI_Nation:
            print (f" {arg} = {arg_obj}")
        else:
            print (f" {arg} = {arg_obj.s_name}")
    print ("------------------------------")    
    pass

def sub_test_nation(caan, s_name:str, aa_alliance:int):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    assert(caan.get_name() == s_name)
    assert(caan.get_type() == CType.C_NATION)
    assert(caan.get_alliance() == aa_alliance)
    