class CT:
    s_Str = {}

    @staticmethod
    def get_str(t_type:int) -> str:
        try:
            return CT.d_Str[t_type]
        except:
            return None
    

class CTTerritory(CT):
    TERRITORY_LAND = 0
    TERRITORY_SEA  = 1
    TERRITORY_END  = 2

    STR_TERRITORY_LAND = "Land"
    STR_TERRITORY_SEA  = "Sea"
    
    d_Str = {
        TERRITORY_LAND : STR_TERRITORY_LAND,
        TERRITORY_SEA  : STR_TERRITORY_SEA,
        TERRITORY_END  :  None
    }

    
class CTUnit(CT):
    INFANTARY          = 0
    MECH_INFANTARY     = 1
    TANK               = 2
    ARTILLERY          = 3
    AAA                = 4
    FIGHTER            = 5
    TACTICAL_BOMBER    = 6
    STRATICAL_BOMBER   = 7
    CARGO              = 8
    SUBMARINE          = 9
    DESTROYER          = 10
    CRUISER            = 11
    BATTLESHIP         = 12
    CARRIER            = 13
    
    STR_INFANTARY          = "Infantary"
    STR_MECH_INFANTARY     = "Mech-Infantary"
    STR_TANK               = "Tank"
    STR_ARTILLERY          = "Artillery"
    STR_AAA                = "AAA"
    STR_FIGHTER            = "Fighter"
    STR_TACTICAL_BOMBER    = "Tactical-Bomber"
    STR_STRATICAL_BOMBER   = "Stratical-Bomber"
    STR_CARGO              = "Cargo"
    STR_SUBMARINE          = "Submarine"
    STR_DESTROYER          = "Destroyer"
    STR_CRUISER            = "Cruiser"
    STR_BATTLESHIP         = "Battelship"
    STR_CARRIER            = "Carrier"
    
    d_Str = {
        INFANTARY          : STR_INFANTARY,
        MECH_INFANTARY     : STR_MECH_INFANTARY,
        TANK               : STR_TANK,
        ARTILLERY          : STR_ARTILLERY,
        AAA                : STR_AAA,
        FIGHTER            : STR_FIGHTER,
        TACTICAL_BOMBER    : STR_TACTICAL_BOMBER,
        STRATICAL_BOMBER   : STR_STRATICAL_BOMBER,
        CARGO              : STR_CARGO,
        SUBMARINE          : STR_SUBMARINE,
        DESTROYER          : STR_DESTROYER,
        CRUISER            : STR_CRUISER,
        BATTLESHIP         : STR_BATTLESHIP,
        CARRIER            : STR_CARRIER
    }

    
class CTClass(CT):
    TERRITORY = 0
    UNIT      = 1
    IPC       = 2
    
    STR_TERRITORY = "Territory"
    STR_UNIT      = "Unit"
    STR_IPC       = "IPC"
    
    d_Str = {
        TERRITORY : STR_TERRITORY,
        UNIT      : STR_UNIT,
        IPC       : STR_IPC        
    }

    @staticmethod
    def get_sub_str(t_type:int, t_subtype:int) -> str:
        if t_type >= CT.TERRITORY:
            return CTTerritory.get_str(t_subtype)

        if t_type >= CT.UNIT:
            return CTUnit.get_str(t_subtype)

        return None
        

class CItem:
    def __init__(self, s_name:str, t_type:CT, t_subtype) -> None:
        self.s_name = s_name

        if CT.get_str(t_type) != None:
            self.t_type = t_type
        else:
            self.t_type = None

        pass


# test 
if __name__ == "__main__":
    print (f"{CTClass.TERRITORY}")
    print (f"{CTClass.get_str(CTClass.TERRITORY)}")
    