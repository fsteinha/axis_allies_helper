from copy import deepcopy
from sqlite3 import SQLITE_TRANSACTION
from  aa_type import CType
from  aa_rules import *
from tabulate import tabulate

##############################################################################
class CAAItem():
    def __init__(self,s_name, aa_type) -> None:
        self.s_name = s_name

        if type(aa_type) == str:
            self.aa_type = CType.type(aa_type)
        elif  CType.str(aa_type) != None:
            self.aa_type = aa_type

    def get_name(self) -> str:
        if ('s_name' in dir(self)):
            return self.s_name
        return None

    def get_region(self) -> str:
        if ('aa_region' in dir(self)):
            return CType.str(self.aa_region)
        return CType.na()

    def get_type(self) -> str:
        return CType.str(self.aa_type)

    def get_nation(self):
        if (type(self) == CAANation):
            return self
        elif ('aa_nation' in dir(self)):
            return self.aa_nation
        
        return None
        
    def get_alliance(self) -> str:
        if ('aa_alliance' in dir(self)):
            return CType.str(self.aa_alliance)
        elif ('aa_nation' in dir(self)):
            return self.aa_nation.get_alliance()
        return None

    def get_ipc(self) -> int:
        if ('aa_ipc' in dir(self)):
            return self.aa_ipc
        return CType.na()

    def get_units(self) -> int:
        if ('l_aa_units' in dir(self)):
            if self.l_aa_units != None:
                #return [item for item in self.l_aa_units]
                return str(self.l_aa_units)
            return None
        return CType.na()

    def get_count(self) -> int:
        if ('i_count' in dir(self)):
            if self.i_count != None:
                return self.i_count
            return 1
        return CType.na()


    def info(self):
        s_nation = None
        if (self.get_nation()) != None:
            s_nation = self.get_nation().s_name
        
        return f'''
Name    : {self.get_name()}
Region  : {self.get_region()}
Type    : {self.get_type()}
Nation  : {s_nation}
Alliance: {self.get_alliance()}
IPC     : {self.get_ipc()}
Units   : {self.get_units()}
Count   : {self.get_count()}
'''
      

##############################################################################
class CAANation(CAAItem):
    def __init__(self, s_name:str, aa_alliance:int) -> None:
        super().__init__(s_name, CType.C_NATION)
        self.aa_alliance = aa_alliance
        pass


##############################################################################
class CAALand(CAAItem):
    def __init__(self, s_name:str,aa_region:CType, aa_nation:CAANation, aa_ipc:int, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_LAND)
        self.aa_ipc=aa_ipc
        self.l_aa_units = l_aa_units
        self.aa_nation = aa_nation
        self.aa_region = aa_region
        pass
        
##############################################################################
class CAASea(CAAItem):
    def __init__(self, s_name:str, aa_ipc:int, l_aa_units:list = []) -> None:
        super().__init__(s_name, CType.T_SEA)
        self.l_aa_units = l_aa_units
        pass


##############################################################################
class CAAUnit(CAAItem):
    def __init__(self, aa_type:int, aa_nation, i_count:int = 1) -> None:
        super().__init__(CType.str(aa_type), aa_type)
        self.aa_nation = aa_nation
        if i_count != None:
            if (i_count > 0):
                self.i_count = i_count
            else:
                self.i_count = 1 
            pass
        else:
           self.i_count = None
        

    def add(self, i_add):
        if self.i_count != None:
            if (i_add >= 0):
                self.i_count = self.i_count + i_add 

    def sub(self, i_sub):
        if self.i_count != None:
            if (i_sub >= 0):
                self.i_count = self.i_count - i_sub
                if (self.i_count < 0):
                    self.i_count = 0
            
    def reset_count(self, i_count:int) -> None:
        if self.i_count != None:
            if (i_count >= 0):
                self.i_count = i_count
            else:
                self.i_count = 0

##############################################################################
class CAAFacillity(CAAItem):
    def __init__(self, aa_type:int) -> None:
        super().__init__(CType.str(aa_type), aa_type)        
        self.i_count = 1

    def add(self, i_add):
        if (self.i_count != None) and (self.i_count < 1):
            if (i_add >= 0):
                self.i_count = self.i_count + i_add 
        
        if (self.i_count > 1):
            self.i_count = 1

    def sub(self, i_sub):
        if self.i_count != None:
            if (i_sub >= 0):
                self.i_count = self.i_count - i_sub
            
    def reset_count(self, i_count:int) -> None:
        if self.i_count != None:
            if (i_count >= 0):
                self.i_count = i_count
            else:
                self.i_count = 0

##############################################################################
class CAAUnitContainer():
    def __init__(self, *args) -> None:
        self.d_aa_units = {}
        for unit in args:
            if self.add(unit) == False:
                raise Exception (f"Wrong type {type(unit)}")
        pass

    def add(self, unit) -> bool:
        if issubclass(type(unit), CAAUnit):
            if unit.get_type() not in self.d_aa_units:
                self.d_aa_units[unit.get_type()] = {unit.get_nation().get_name():unit}
            elif unit.get_nation().get_name() not in self.d_aa_units[unit.get_type()]:
                self.d_aa_units[unit.get_type()][unit.get_nation().get_name()] = unit
            else:
                self.d_aa_units[unit.get_type()][unit.get_nation().get_name()].add(unit.get_count())
            return True
        return False

    def sub(self, unit) -> bool:
        if issubclass(type(unit), CAAUnit):
            key_unit = None
            key_nation = None 
            if (unit.get_type() in self.d_aa_units):
                key_unit = unit.get_type()
            if (key_unit != None) and \
               (unit.get_nation().get_name() in self.d_aa_units[key_unit]):
                    key_nation = unit.get_nation().get_name()
            if (key_unit != None) and (key_nation != None):
                self.d_aa_units[key_unit][key_nation].sub(unit.get_count())
                if self.d_aa_units[key_unit][key_nation].get_count() == 0:
                    del(self.d_aa_units[key_unit][key_nation])
                    #print (self.d_aa_units[key_unit][key_nation])
                    if self.d_aa_units[key_unit] == None:
                        del(self.d_aa_units[key_unit])

            return True
        return False

    def get_container(self) -> list:
        return self.d_aa_units
    
    def info(self):
        l_tab = [['Unit', 'Nation' 'Count']]
        for s_unit in self.d_aa_units:
            for  s_nation in self.d_aa_units[s_unit]:
                l_tab.append([s_unit, s_nation, self.d_aa_units[s_unit][s_nation].get_count()])
        return tabulate(l_tab, headers="firstrow", tablefmt="grid")
        pass

        

##############################################################################
class CAAU_Inf(CAAUnit):
    def __init__(self, aa_nation:CAANation, i_count = 1) -> None:
        super().__init__(CType.U_INFANTARY, aa_nation, i_count)
        pass

##############################################################################
class CAAU_MechInf(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_MECH_INFANTARY, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Tank(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_TANK, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Ari(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_ARTILLERY, aa_nation, i_count)
        pass

##############################################################################
class CAAU_AAA(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_AAA, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Figther(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_FIGHTER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_TBomb(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_T_BOMBER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_SBomb(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_S_BOMBER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Submarine(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_SUBMARINE, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Destroyer(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_DESTROYER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Cruiser(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_CRUISER, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Battleship(CAAUnit):
    def __init__(self,  aa_nation, i_count = 1) -> None:
        super().__init__(CType.U_BATTLESHIP, aa_nation, i_count)
        pass

##############################################################################
class CAAU_Carrier(CAAUnit):
    def __init__(self,  aa_nation, c_rules:CAAR_Carrier, l_aa_units:list = None) -> None:
        super().__init__(CType.U_CARRIER, aa_nation, i_count = None)
        self.c_rules = c_rules
        self.l_aa_units = l_aa_units
        pass

    def add_unit(self, aa_unit:CType) -> bool:
        if self.c_rules.check_add(self.l_aa_units, aa_unit) == False:
            return False
        
        self.l_aa_units.append(aa_unit)
        return True
    
    def sub_unit(self, aa_unit:CType) -> bool:
        if self.c_rules.check_sub(self.l_aa_units, aa_unit) == False:
            return False
        
        self.l_aa_units.remove(aa_unit)
        return True

##############################################################################
class CAAU_Cargo(CAAUnit):
    def __init__(self,  aa_nation, i_count:int = 1, l_aa_units:list = None) -> None:
        super().__init__(CType.U_CARGO, aa_nation, i_count)
        self.l_aa_units = l_aa_units
        pass

if __name__ == "__main__":
    raise Exception ("Not executable")


##############################################################################
class CAAF_Major(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_MAJOR_FACTORY)
        pass

##############################################################################
class CAAF_Minor(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_MINOR_FACTORY)
        pass

##############################################################################
class CAAF_AirBase(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_AIR_BASE)
        pass

##############################################################################
class CAAF_NavalBase(CAAFacillity):
    def __init__(self) -> None:
        super().__init__(CType.F_NAVAL_BASE)
        pass
