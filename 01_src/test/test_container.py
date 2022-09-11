from aa_units import *
from aa_type import *
from aa_container import *
from test_common import *

import inspect


##############################################################################
def test_container_init(*args):
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    try:
        caacon = CAAUnitContainer(*args)
        print(caacon.info())    

    except:
        print ("ERROR")
        pass  
    
##############################################################################
def test_container_add_sub():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_nordpol = CAAI_Nation("Nordpol", CType.A_ALLIES)
    
    #print ("... init")
    caacon = CAAUnitContainer(CAAU_Inf(caan_germany, 1))
    d_cont = caacon.get_container()
    #print(caacon.info())  
    assert d_cont[CType.U_INFANTARY][caan_germany.get_name()].get_count() == 1
    assert caacon.get_unit_count() == 1, f"caacon.get_unit_count() returns {caacon.get_unit_count()}"
    assert caacon.get_unit_count(CType.U_INFANTARY) == 1
    assert caacon.get_unit_count(CType.U_AAA) == 0
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 1
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 1
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 0

    
    #print ("... add Inf Germany 1")
    caacon.add(CAAU_Inf(caan_germany, 1)) 
    d_cont = caacon.get_container()
    #print(caacon.info())  
    assert d_cont[CType.U_INFANTARY][caan_germany.get_name()].get_count()  == 2
    assert caacon.get_unit_count() == 2
    assert caacon.get_unit_count(CType.U_INFANTARY) == 2
    assert caacon.get_unit_count(CType.U_AAA) == 0
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 0

    #print ("... add AAA Germany 1")
    caacon.add(CAAU_AAA(caan_germany, 1)) 
    d_cont = caacon.get_container()
    #print(caacon.info())  
    assert d_cont[CType.U_AAA][caan_germany.get_name()].get_count()  == 1
    assert caacon.get_unit_count() == 3
    assert caacon.get_unit_count(CType.U_INFANTARY) == 2
    assert caacon.get_unit_count(CType.U_AAA) == 1
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 3
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 0
    
    #print ("... add AAA Nordpol 1")
    caacon.add(CAAU_AAA(caan_nordpol, 1)) 
    d_cont = caacon.get_container()
    #print(caacon.info())  
    assert d_cont[CType.U_AAA][caan_nordpol.get_name()].get_count()  == 1
    assert caacon.get_unit_count() == 4
    assert caacon.get_unit_count(CType.U_INFANTARY) == 2
    assert caacon.get_unit_count(CType.U_AAA) == 2
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 3
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 1
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 1
        
    #print ("... add AAA Nordpol 10")
    caacon.add(CAAU_AAA(caan_nordpol, 10)) 
    d_cont = caacon.get_container()
    #print (d_cont)
    #print(caacon.info())  
    assert d_cont[CType.U_AAA][caan_nordpol.get_name()].get_count()  == 11
    assert caacon.get_unit_count() == 14
    assert caacon.get_unit_count(CType.U_INFANTARY) == 2
    assert caacon.get_unit_count(CType.U_AAA) == 12
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 3
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 11
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 11
    
    
    #print ("... sub AAA Nordpol 1")
    caacon.sub(CAAU_AAA(caan_nordpol, 1)) 
    d_cont = caacon.get_container()
    #print (d_cont)
    #print(caacon.info())  
    assert d_cont[CType.U_AAA][caan_nordpol.get_name()].get_count()  == 10
    assert caacon.get_unit_count() == 13
    assert caacon.get_unit_count(CType.U_INFANTARY) == 2
    assert caacon.get_unit_count(CType.U_AAA) == 11
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 3
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 10
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 10
    
    #print ("... sub AAA Nordpol 20 - no unit in ")
    caacon.sub(CAAU_AAA(caan_nordpol, 20)) 
    d_cont = caacon.get_container()
    #print (d_cont)
    #print(caacon.info())  
    assert caan_nordpol.get_name() not in d_cont[CType.U_AAA], print (d_cont[CType.U_AAA])
    assert caacon.get_unit_count() == 3, f"caacon.get_unit_count() returns {caacon.get_unit_count()}"
    assert caacon.get_unit_count(CType.U_INFANTARY) == 2
    assert caacon.get_unit_count(CType.U_AAA) == 1
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 3
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 0
    
    #print ("... sub AAA Nordpol 20 again - no unit in ")
    caacon.sub(CAAU_AAA(caan_nordpol, 20)) 
    d_cont = caacon.get_container()
    #print (d_cont)
    #print(caacon.info())  
    assert caan_nordpol.get_name() not in d_cont[CType.U_AAA], print (d_cont[CType.U_AAA])
    assert caacon.get_unit_count() == 3
    assert caacon.get_unit_count(CType.U_INFANTARY) == 2
    assert caacon.get_unit_count(CType.U_AAA) == 1
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_germany.get_name()) == 2
    assert caacon.get_unit_count(None, caan_germany.get_name()) == 3
    assert caacon.get_unit_count(CType.U_INFANTARY, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(CType.U_AAA, caan_nordpol.get_name()) == 0
    assert caacon.get_unit_count(None, caan_nordpol.get_name()) == 0
    
##############################################################################
def test_container_get_nations():
    sub_test_header(inspect.currentframe().f_code.co_name, inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_nordpol = CAAI_Nation("Nordpol", CType.A_ALLIES)
    caan_australia = CAAI_Nation("australia", CType.A_ALLIES)
    
    caacon = CAAUnitContainer(CAAU_Inf(caan_germany, 1))
    caacon.add(CAAU_Inf(caan_nordpol, 1)) 
    caacon.add(CAAU_Inf(caan_australia, 1)) 
    
    l_nations = caacon.get_nations()
    assert (caan_germany in l_nations)
    assert (caan_nordpol in l_nations)
    assert (caan_australia in l_nations)

    caacon.sub(CAAU_Inf(caan_australia, 1)) 
    l_nations = caacon.get_nations()
    assert (caan_australia not in l_nations)
    
##############################################################################
if __name__ == "__main__":
    
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
    caan_gb_europe = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)
    
    test_container_init(CAAU_Inf(caan_germany, 1))
    test_container_init(CAAU_Inf(caan_germany, 10), CAAU_Inf(caan_japan, 1),CAAU_TBomb(caan_japan, 3))
    test_container_add_sub()
    