from aa.aa_nation import *
from aa.aa_units import *
from aa.aa_type import *
from test_common import *
import inspect

##############################################################################
# Globals
##############################################################################

CAAN_GEMRANY = CAAI_Nation("Germany", CType.A_AXIS)
CAAN_JAPAN = CAAI_Nation("Japan", CType.A_AXIS)
CANN_GB_EUROPE = CAAI_Nation("Great Britain Europe", CType.A_ALLIES)

##############################################################################
# Tests
##############################################################################

##############################################################################


def sub_test_unit(caau: CAAUnit, aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    assert(type(caau.get_nation()) == CAAI_Nation)
    caan = caau.get_nation()
    sub_test_nation(caan, aa_nation.get_name(), aa_nation.get_alliance())

    if i_count != None:
        if (i_count > 0):
            assert caau.get_count(
            ) == i_count, f"{caau.get_count()} != {i_count}"
        else:
            assert caau.get_count() == 1, f"i_count should be 1"

        if (i_count > 0):
            caau.sub(i_count)
            assert caau.get_count() == 0, f"{caau.get_count()} != 0"
            caau.add(i_count)
            assert caau.get_count() == i_count
            caau.add(i_count)
            assert caau.get_count() == 2 * i_count
            caau.sub(3*i_count)
            assert caau.get_count() == 0
        elif (i_count <= 0):
            i_temp_count = caau.get_count()
            caau.sub(i_count)
            assert caau.get_count() == i_temp_count
            caau.add(i_count)
            assert caau.get_count() == i_temp_count
            caau.add(i_count)
            assert caau.get_count() == i_temp_count
            caau.sub(3*i_count)
            assert caau.get_count() == i_temp_count

        caau.reset_count(i_count)
        if (i_count >= 0):
            assert caau.get_count() == i_count
        else:
            assert caau.get_count() == 0
    else:
        assert caau.get_count(
        ) == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.sub(-1)
        assert caau.get_count(
        ) == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.sub(-10)
        assert caau.get_count(
        ) == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.add(1)
        assert caau.get_count(
        ) == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.add(10)
        assert caau.get_count(
        ) == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"
        caau.sub(1)
        assert caau.get_count(
        ) == 1, f"{caau.get_count()} should be 1 (None returns 1 always)"

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_inf(aa_nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Inf(aa_nation, i_count)
    assert(caa.get_type() == CType.U_INFANTARY)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_mech_inf(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_MechInf(aa_nation, i_count)
    assert(caa.get_type() == CType.U_MECH_INFANTARY)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_tank(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Tank(aa_nation, i_count)
    assert(caa.get_type() == CType.U_TANK)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_ari(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Ari(aa_nation, i_count)
    assert(caa.get_type() == CType.U_ARTILLERY)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_aaa(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_AAA(aa_nation, i_count)
    assert(caa.get_type() == CType.U_AAA)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_fighter(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Figther(aa_nation, i_count)
    assert(caa.get_type() == CType.U_FIGHTER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_tbomb(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_TBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.U_T_BOMBER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_sbomb(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_SBomb(aa_nation, i_count)
    assert(caa.get_type() == CType.U_S_BOMBER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_submarine(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Submarine(aa_nation, i_count)
    assert(caa.get_type() == CType.U_SUBMARINE)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_destroyer(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Destroyer(aa_nation, i_count)
    assert(caa.get_type() == CType.U_DESTROYER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_cruiser(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Cruiser(aa_nation, i_count)
    assert(caa.get_type() == CType.U_CRUISER)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


@pytest.mark.parametrize("aa_nation, i_count", [
    (CAAN_GEMRANY,   1),
    (CAAN_JAPAN,   0),
    (CANN_GB_EUROPE,  10),
    (CANN_GB_EUROPE, -10),
])
def test_battleship(aa_nation: CAAI_Nation, i_count):
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caa = CAAU_Battleship(aa_nation, i_count)
    assert(caa.get_type() == CType.U_BATTLESHIP)
    sub_test_unit(caa, aa_nation, i_count)
    print(caa.info())

##############################################################################


def test_carrier():
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
    caar = CAAR_Carrier()
    caac = CAAU_Carrier(caan_germany, caar, None)
    assert(caac.get_type() == CType.U_CARRIER)
    # Carrier must be test with i_count == None
    sub_test_unit(caac, caan_germany, None)
    assert caac.add_unit(CAAU_AAA(caan_germany)) == False
    assert caac.get_unit_count() == 0
    assert caac.add_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.add_unit(CAAU_Figther(caan_germany)) == False
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count(
    ) == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.add_unit(CAAU_TBomb(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Figther(caan_japan)) == False
    assert caac.get_unit_count(
    ) == 2, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.sub_unit(CAAU_TBomb(caan_germany)) == True
    assert caac.get_unit_count(
    ) == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.add_unit(CAAU_TBomb(caan_japan)) == True
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Figther(caan_germany)) == True
    assert caac.get_unit_count(
    ) == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.sub_unit(CAAU_Figther(caan_germany)) == False
    assert caac.get_unit_count(
    ) == 1, f"caac.get_unit_count() == {caac.get_unit_count()}"
    assert caac.add_unit(CAAU_SBomb(caan_japan)) == False
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_TBomb(caan_japan)) == True
    assert caac.get_unit_count() == 0

    print(caac.info())

##############################################################################


def test_carrier_init():
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
    caar = CAAR_Carrier()
    caac = CAAU_Carrier(caan_germany, caar, [CAAU_Figther(
        caan_germany), CAAU_Figther(caan_germany)])
    assert(caac.get_type() == CType.U_CARRIER)
    # Carrier must be test with i_count == None
    sub_test_unit(caac, caan_germany, None)
    assert caac.get_unit_count() == 2
    print(caac.info())

    try:
        caac = CAAU_Carrier(caan_germany, caar, [CAAU_SBomb(
            caan_germany), CAAU_Figther(caan_germany)])
        assert(False), "Expection requested"
    except:
        pass


##############################################################################
def test_cargo():
    sub_test_header(inspect.currentframe().f_code.co_name,
                    inspect.getargvalues(inspect.currentframe()))
    caan_germany = CAAI_Nation("Germany", CType.A_AXIS)
    caan_japan = CAAI_Nation("Japan", CType.A_AXIS)
    caar = CAAR_Cargo()
    caac = CAAU_Cargo(caan_germany, caar, None)
    assert caac.get_type() == CType.U_CARGO
    assert caac.get_name() == CType.str(CType.U_CARGO)
    # Carrier must be test with i_count == None
    sub_test_unit(caac, caan_germany, None)
    assert caac.add_unit(CAAU_AAA(caan_germany)) == False
    assert caac.get_unit_count() == 0
    assert caac.add_unit(CAAU_Inf(caan_germany)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Tank(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.add_unit(CAAU_Tank(caan_germany)) == False
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_Tank(caan_germany)) == True
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_Tank(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_Inf(caan_japan)) == False
    assert caac.get_unit_count() == 1
    assert caac.sub_unit(CAAU_Inf(caan_germany)) == True
    assert caac.get_unit_count() == 0
    assert caac.add_unit(CAAU_MechInf(caan_japan)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Figther(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_TBomb(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_SBomb(caan_germany)) == False
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Ari(caan_germany)) == True
    assert caac.get_unit_count() == 2
    assert caac.sub_unit(CAAU_MechInf(caan_japan)) == True
    assert caac.get_unit_count() == 1
    assert caac.add_unit(CAAU_Ari(caan_germany)) == False
    assert caac.get_unit_count() == 1

    print(caac.info())
