from test_common import *
from aa_items import *
import inspect

##############################################################################
# Tests
##############################################################################

##############################################################################
def test_nation(s_name:str, aa_alliance:int):
    test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAANation(s_name, aa_alliance)
    sub_test_nation(caa, s_name, aa_alliance)
    print(caa.info())    

if __name__ == "__main__":
    test_nation("Germany"              , CType.A_AXIS)
    test_nation("Sovietunion"          , CType.A_ALLIES)
    test_nation("Japan"                , CType.A_AXIS)
    test_nation("United States"        , CType.A_ALLIES)
    test_nation("Italy"                , CType.A_AXIS)
    test_nation("Great Britain Europe" , CType.A_ALLIES)
    test_nation("Great Britain Pacific", CType.A_ALLIES)
    test_nation("France"               , CType.A_ALLIES)
    test_nation("China"                , CType.A_ALLIES)
    test_nation("ANZAC"                , CType.A_ALLIES)

    