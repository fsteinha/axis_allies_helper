
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

    STR_C_TERRITORY = "Territory"
    STR_C_UNIT      = "Unit"
    STR_C_IPC      = "IPC"

    STR_T_LAND = "Land"
    STR_T_SEA  = "Sea"

    STR_U_INFANTARY          = "Infantary"
    STR_U_MECH_INFANTARY     = "Mech-Infantary"
    STR_U_TANK               = "U_TANK"
    STR_U_ARTILLERY          = "U_ARTILLERY"
    STR_U_AAA                = "U_AAA"
    STR_U_FIGHTER            = "U_FIGHTER"
    STR_U_T_BOMBER           = "Tactical-Bomber"
    STR_U_S_BOMBER           = "Stratical-Bomber"
    STR_U_CARGO              = "U_CARGO"
    STR_U_SUBMARINE          = "U_SUBMARINE"
    STR_U_DESTROYER          = "U_DESTROYER"
    STR_U_CRUISER            = "U_CRUISER"
    STR_U_BATTLESHIP         = "Battelship"
    STR_U_CARRIER            = "U_CARRIER"
    
    d_Str = {
        C_TERRITORY          : STR_C_TERRITORY,
        C_UNIT               : STR_C_UNIT,
        C_IPC                : STR_C_IPC,        

        T_LAND               : STR_T_LAND,
        T_SEA                : STR_T_SEA,
        
        U_INFANTARY          : STR_U_INFANTARY,
        U_MECH_INFANTARY     : STR_U_MECH_INFANTARY,
        U_TANK               : STR_U_TANK,
        U_ARTILLERY          : STR_U_ARTILLERY,
        U_AAA                : STR_U_AAA,
        U_FIGHTER            : STR_U_FIGHTER,
        U_T_BOMBER           : STR_U_T_BOMBER,
        U_S_BOMBER           : STR_U_S_BOMBER,
        U_CARGO              : STR_U_CARGO,
        U_SUBMARINE          : STR_U_SUBMARINE,
        U_DESTROYER          : STR_U_DESTROYER,
        U_CRUISER            : STR_U_CRUISER,
        U_BATTLESHIP         : STR_U_BATTLESHIP,
        U_CARRIER            : STR_U_CARRIER
    }
    
    @staticmethod
    def get_str(t_type:int) -> str:
        try:
            return CType.d_Str[t_type]
        except:
            return None
    
class CTClass():
    
    
    d_Str = {
    }

    @staticmethod
    def get_str(t_type:int) -> str:
        try:
            return CTClass.d_Str[t_type]
        except:
            return None
        

# test 
if __name__ == "__main__":
    print (f"{CTClass.TERRITORY}")
    print (f"{CTClass.get_str(CTClass.TERRITORY)}")
    print (f"{CTTerritory.get_str(CTTerritory.TERRITORY_LAND)}")
    