import inspect
import pytest
from aa_type import CType

##############################################################################
# debug out
##############################################################################
def sub_test_header(s_func_name:str, info):
    print ( "############################################################")
    print (f"   Test {s_func_name}")
    for arg in info[0]:
        print (f"    {arg} = {info[3][arg]}")
    print ()    
    pass

def sub_test_header(s_func_name: str, info):
    print (f"       Sub Test {s_func_name}")
    for arg in info[0]:
        print (f"       {arg} = {info[3][arg]}")
    print ()    
    pass

def sub_test_nation(caan, s_name:str, aa_alliance:int):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    assert(caan.get_name() == s_name)
    assert(caan.get_type() == CType.C_NATION)
    assert(caan.get_alliance() == aa_alliance)
    