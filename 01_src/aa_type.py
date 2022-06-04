
class CType():
    
    C_TERRITORY         = 0
    C_UNIT              = 1
    C_IPC               = 2

    T_LAND              = 10
    T_SEA               = 11
    
    U_INFANTARY          = 100
    U_MECH_INFANTARY     = 101
    U_TANK               = 102
    U_ARTILLERY          = 103
    U_AAA                = 104
    U_FIGHTER            = 105
    U_T_BOMBER           = 106
    U_S_BOMBER           = 107
    U_CARGO              = 108
    U_SUBMARINE          = 109
    U_DESTROYER          = 110
    U_CRUISER            = 111
    U_BATTLESHIP         = 112
    U_CARRIER            = 113

    STR_C_TERRITORY       = "Territory"
    STR_C_UNIT            = "Unit"
    STR_C_IPC             = "IPC"

    STR_T_LAND            = "Land"
    STR_T_SEA             = "Sea"

    STR_U_INFANTARY       = "Infantary"
    STR_U_MECH_INFANTARY  = "Mech-Infantary"
    STR_U_TANK            = "Tank"
    STR_U_ARTILLERY       = "Artillery"
    STR_U_AAA             = "AAA"
    STR_U_FIGHTER         = "Fighter"
    STR_U_T_BOMBER        = "Tactical-Bomber"
    STR_U_S_BOMBER        = "Stratical-Bomber"
    STR_U_CARGO           = "Cargo"
    STR_U_SUBMARINE       = "Submarine"
    STR_U_DESTROYER       = "Destroyer"
    STR_U_CRUISER         = "Cruier"
    STR_U_BATTLESHIP      = "Battelship"
    STR_U_CARRIER         = "Carrier"
    
    d_Str = {
        C_TERRITORY     : STR_C_TERRITORY,
        C_UNIT          : STR_C_UNIT,
        C_IPC           : STR_C_IPC,        

        T_LAND          : STR_T_LAND,
        T_SEA           : STR_T_SEA,
        
        U_INFANTARY     : STR_U_INFANTARY,
        U_MECH_INFANTARY: STR_U_MECH_INFANTARY,
        U_TANK          : STR_U_TANK,
        U_ARTILLERY     : STR_U_ARTILLERY,
        U_AAA           : STR_U_AAA,
        U_FIGHTER       : STR_U_FIGHTER,
        U_T_BOMBER      : STR_U_T_BOMBER,
        U_S_BOMBER      : STR_U_S_BOMBER,
        U_CARGO         : STR_U_CARGO,
        U_SUBMARINE     : STR_U_SUBMARINE,
        U_DESTROYER     : STR_U_DESTROYER,
        U_CRUISER       : STR_U_CRUISER,
        U_BATTLESHIP    : STR_U_BATTLESHIP,
        U_CARRIER       : STR_U_CARRIER
    }
    
    @staticmethod
    def get_str(t_type:int) -> str:
        try:
            return CType.d_Str[t_type]
        except:
            return None      

# test 
if __name__ == "__main__":
    assert (CType.get_str(CType.C_TERRITORY)      == "Territory")
    assert (CType.get_str(CType.C_UNIT)           == "Unit")
    assert (CType.get_str(CType.C_IPC)            == "IPC")

    assert (CType.get_str(CType.T_LAND)           == "Land")
    assert (CType.get_str(CType.T_SEA)            == "Sea")
    
    assert (CType.get_str(CType.U_INFANTARY)      == "Infantary")
    assert (CType.get_str(CType.U_MECH_INFANTARY) == "Mech-Infantary")
    assert (CType.get_str(CType.U_TANK)           == "Tank")
    assert (CType.get_str(CType.U_ARTILLERY)      == "Artillery")
    assert (CType.get_str(CType.U_AAA)            == "AAA")
    assert (CType.get_str(CType.U_FIGHTER)        == "Fighter")
    assert (CType.get_str(CType.U_T_BOMBER)       == "Tactical-Bomber")
    assert (CType.get_str(CType.U_S_BOMBER)       == "Stratical-Bomber")
    assert (CType.get_str(CType.U_CARGO)          == "Cargo")
    assert (CType.get_str(CType.U_SUBMARINE)      == "Submarine")
    assert (CType.get_str(CType.U_DESTROYER)      == "Destroyer")
    assert (CType.get_str(CType.U_CRUISER)        == "Cruier")
    assert (CType.get_str(CType.U_BATTLESHIP)     == "Battelship")
    assert (CType.get_str(CType.U_CARRIER)        == "Carrier")


    