from test_common import *
from aa_facillities import *
import inspect

##############################################################################
# Tests
##############################################################################

##############################################################################
def sub_test_facillity(caaf:CAAI_Facillity):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    assert caaf.get_count() == 1, f"Precondition error count is {caaf.get_count()}"
    caaf.add(1)
    assert caaf.get_count() == 1
    caaf.sub(10)
    assert caaf.get_count() == -9
    caaf.add(20)
    assert caaf.get_count() == 1
    print(caaf.info())
    
def test_major():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_Major()
    assert (caaf.get_type() == CType.F_MAJOR_FACTORY)
    sub_test_facillity(caaf)
    
def test_minor():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_Minor()
    assert (caaf.get_type() == CType.F_MINOR_FACTORY)
    sub_test_facillity(caaf)
    
def test_airbase():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_AirBase()
    assert (caaf.get_type() == CType.F_AIR_BASE)
    sub_test_facillity(caaf)

def test_navalbase():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caaf = CAAF_NavalBase()
    assert (caaf.get_type() == CType.F_NAVAL_BASE)
    sub_test_facillity(caaf)

if __name__ == "__main__":
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
    caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)
    
    test_major()
    test_minor()
    test_airbase()
    test_navalbase()
