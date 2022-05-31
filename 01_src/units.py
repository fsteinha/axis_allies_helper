class CType_Territory:
    type_TERRITORY_LAND = 0
    type_TERRITORY_SEA  = 1
    type_TERRITORY_END  = 2
    
    d_Str = {
        type_TERRITORY_LAND : "Land",
        type_TERRITORY_SEA  : "Sea",
        type_TERRITORY_END  :  None
    }

    def get_type(self, t_type:int) -> str:
        try:
            return self.d_Str[t_type]
        except:
            return None
    
class CType_Unit:
    type_Unit_Infantary          = 0
    type_Unit_MechInfantary      = 1
    type_Unit_Tank               = 2
    type_Unit_Artillery          = 3
    type_Unit_AAA                = 4
    type_Unit_Fighter            = 5
    type_Unit_TacticalBomber     = 6
    type_Unit_StraticalBomer     = 7
    type_Unit_Cargo              = 8
    type_Unit_Submarine          = 9
    type_Unit_Destroyer          = 10
    type_Unit_Cruiser            = 11
    type_Unit_BattleShip         = 12
    type_Unit_Carrier            = 13
    
    
    
    
    def get_type(self, t_type:int) -> str:
        
        if t_type >= self.type_TERRITORY_LAND:
            return "Land"

        if t_type >= self.type_TERRITORY_SEA:
            return "Sea"
        
        return None
    


class CType:
    type_TERRITORY = 0
    type_UNIT      = 1
    type_IPC       = 2
    type_END       = 3
    
    @staticmethod
    def get_type(t_type:int) -> str:
        
        if t_type >= CType.type_TERRITORY:
            return "Territory"

        if t_type >= CType.type_UNIT:
            return "Unit"

        if t_type >= CType.type_IPC:
            return "IPC"
        
        return None
    
    @staticmethod
    def get_sub_type(t_type:int, t_subtype:int) -> str:
        if t_type >= CType.type_TERRITORY:
            return CType_Territory.get_type(t_subtype)

        if t_type >= CType.type_UNIT:
            return "Unit"

        if t_type >= CType.type_IPC:
            return "IPC"
        
        return None
        

class CItem:
    def __init__(self, s_name:str, t_type:CType, t_subtype) -> None:
        self.s_name = s_name

        if CType.get_type(t_type) != None:
            self.t_type = t_type
        else:
            self.t_type = None

        pass


# test 
if __name__ == "__main__":
    print (f"{CType.type_TERRITORY}")
    print (f"{CType.get_type(CType.type_TERRITORY)}")
    