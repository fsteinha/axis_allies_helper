class CType:
    type_TERRITORY = 0
    type_UNIT      = 1
    type_IPC       = 2
    type_END       = 3

    def get_type(self, t_type:int) -> str:
        
        if t_type >= self.type_TERRITORY:
            return "Territory"

        if t_type >= self.type_UNIT:
            return "Unit"

        if t_type >= self.type_IPC:
            return "IPC"
        
        return None
        
class CType_Territory:
    type_TERRITORY_LAND = 0
    type_TERRITORY_SEA  = 1
    type_TERRITORY_END  = 2
    
    def get_type(self, t_type:int) -> str:
        
        if t_type >= self.type_TERRITORY_LAND:
            return "Land"

        if t_type >= self.type_TERRITORY_SEA:
            return "Sea"
        
        return None
    

class CItem:
    def __init__(self, s_name:str, t_type:CType) -> None:
        self.s_name = s_name

        if CType.get_type(t_type) != None:
            self.t_type = t_type
        else:
            self.t_type = None

        pass

class CTerritory