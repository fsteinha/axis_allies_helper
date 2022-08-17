import pytest
from test_common import *
from aa_nation import *
import inspect

##############################################################################
# Tests
##############################################################################

##############################################################################
@pytest.mark.parametrize("s_name, aa_alliance", [
    ("Germany"              , CType.A_AXIS),
    ("Sovietunion"          , CType.A_ALLIES),
    ("Japan"                , CType.A_AXIS),
    ("United States"        , CType.A_ALLIES),
    ("Italy"                , CType.A_AXIS),
    ("Great Britain Europe" , CType.A_ALLIES),
    ("Great Britain Pacific", CType.A_ALLIES),
    ("France"               , CType.A_ALLIES),
    ("China"                , CType.A_ALLIES),
    ("ANZAC"                , CType.A_ALLIES)
    ])
def test_nation(s_name, aa_alliance):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caa = CAAI_Nation(s_name, aa_alliance)
    sub_test_nation(caa, s_name, aa_alliance)
    print(caa.info())    
