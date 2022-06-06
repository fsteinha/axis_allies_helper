
class CType():
    
    C_TERRITORY         = 0
    C_UNIT              = 1
    C_IPC               = 2
    C_NATION            = 3
    C_ALLIANCE          = 4
    C_FACILITY          = 5
    C_REGION            = 6

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
    
    A_AXIS               = 200
    A_ALLIES             = 201

    F_MAJOR_FACTORY     = 300
    F_MINOR_FACTORY     = 301
    F_AIR_BASE          = 302
    F_NAVAL_BASE        = 303
    
    R_EUROPE            =400
    R_ASIA_FAR_EAST     =401
    R_NORDAMERICA       =402
    R_SOUTHAMERICA      =403
    R_AFRICA            =404
    R_PACIFIC           =405
    R_ASIA_MIDDLE_EAST  =406
    
    
    NA                  = 1000    
      
    d_Str = {
        C_TERRITORY        : "Territory",
        C_UNIT             : "Unit",
        C_IPC              : "IPC",
        C_NATION           : "Nation",
        C_ALLIANCE         : "Alliance",
        C_FACILITY         : "Facility",
        C_REGION           : "Region",


        T_LAND             : "Land",
        T_SEA              : "Sea",
           
        U_INFANTARY        : "Infantary",
        U_MECH_INFANTARY   : "Mech-Infantary",
        U_TANK             : "Tank",
        U_ARTILLERY        : "Artillery",
        U_AAA              : "AAA",
        U_FIGHTER          : "Fighter",
        U_T_BOMBER         : "Tactical-Bomber",
        U_S_BOMBER         : "Stratic-Bomber",
        U_CARGO            : "Cargo",
        U_SUBMARINE        : "Submarine",
        U_DESTROYER        : "Destroyer",
        U_CRUISER          : "Cruiser",
        U_BATTLESHIP       : "Battelship",
        U_CARRIER          : "Carrier",

        A_AXIS             : "Axis",
        A_ALLIES           : "Allies",
   
        F_MAJOR_FACTORY    : "Major factory",
        F_MINOR_FACTORY    : "Minor factory",
        F_AIR_BASE         : "Air base",
        F_NAVAL_BASE       : "Naval base",
   
        R_EUROPE           : "Europe",
        R_ASIA_FAR_EAST    : "Asia far east",
        R_NORDAMERICA      : "North america",
        R_SOUTHAMERICA     : "South america",
        R_AFRICA           : "Africa",
        R_PACIFIC          : "Pacific",
        R_ASIA_MIDDLE_EAST : "Asia middle east",
        
        NA                 : "N/A"
    }
    
    @staticmethod
    def str(t_type:int) -> str:
        try:
            return CType.d_Str[t_type]
        except:
            return None   

    @staticmethod
    def type(s_type:str) -> int:
        keys = [k for k, v in CType.d_Str.items() if v == s_type]
        return keys[0]

    @staticmethod
    def na()->str:
        return CType.str(CType.NA)    
# test 
if __name__ == "__main__":
    assert (CType.str(CType.C_TERRITORY)      == "Territory")
    assert (CType.str(CType.C_UNIT)           == "Unit")
    assert (CType.str(CType.C_IPC)            == "IPC")
    assert (CType.str(CType.C_NATION)         == "Nation")

    assert (CType.str(CType.T_LAND)           == "Land")
    assert (CType.str(CType.T_SEA)            == "Sea")
    
    assert (CType.str(CType.U_INFANTARY)      == "Infantary")
    assert (CType.str(CType.U_MECH_INFANTARY) == "Mech-Infantary")
    assert (CType.str(CType.U_TANK)           == "Tank")
    assert (CType.str(CType.U_ARTILLERY)      == "Artillery")
    assert (CType.str(CType.U_AAA)            == "AAA")
    assert (CType.str(CType.U_FIGHTER)        == "Fighter")
    assert (CType.str(CType.U_T_BOMBER)       == "Tactical-Bomber")
    assert (CType.str(CType.U_S_BOMBER)       == "Stratical-Bomber")
    assert (CType.str(CType.U_CARGO)          == "Cargo")
    assert (CType.str(CType.U_SUBMARINE)      == "Submarine")
    assert (CType.str(CType.U_DESTROYER)      == "Destroyer")
    assert (CType.str(CType.U_CRUISER)        == "Cruier")
    assert (CType.str(CType.U_BATTLESHIP)     == "Battelship")
    assert (CType.str(CType.U_CARRIER)        == "Carrier")


    