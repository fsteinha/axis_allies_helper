from aa_type import CType
from aa_unit import CAAUnit
from aa_facillities import CAAI_Facillity
from tabulate import tabulate

##############################################################################
class CAAUnitContainer():
    def __init__(self, *args) -> None:
        self.d_aa_units = {}
        for unit in args:
            if self.add(unit) == False:
                raise Exception (f"Wrong type {type(unit)}")
        pass

    def add(self, unit) -> bool:
        if (issubclass(type(unit), CAAUnit)):
            if unit.get_type() not in self.d_aa_units:
                self.d_aa_units[unit.get_type()] = {unit.get_nation().get_name():unit}
            elif unit.get_nation().get_name() not in self.d_aa_units[unit.get_type()]:
                self.d_aa_units[unit.get_type()][unit.get_nation().get_name()] = unit
            else:
                self.d_aa_units[unit.get_type()][unit.get_nation().get_name()].add(unit.get_count())
            return True
        elif issubclass(type(unit), CAAI_Facillity):
            if unit.get_type() not in self.d_aa_units:
                self.d_aa_units[unit.get_type()] = {CType.str(CType.C_FACILITY):unit}
            else:
                self.d_aa_units[unit.get_type()][CType.str(CType.C_FACILITY)].add(unit.get_count())
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
                print (key_nation)
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

    def get_unit_count(self, t_type:int = None, s_nation:str = None) -> int:
        i_count = 0
        for unit in self.d_aa_units:
            if t_type == None or t_type == unit:
                for aa_nation in self.d_aa_units[unit]:
                    if s_nation == None or s_nation == aa_nation:
                        i_count = i_count + self.d_aa_units[unit][aa_nation].get_count()
                 
        return i_count
    
    def info(self):
        l_tab = [['Unit', 'Nation' 'Count']]
        for t_unit in self.d_aa_units:
            for  s_nation in self.d_aa_units[t_unit]:
                l_tab.append([CType.str(t_unit), s_nation, self.d_aa_units[t_unit][s_nation].get_count()])
        return tabulate(l_tab, headers="firstrow", tablefmt="grid")
        pass

##############################################################################
# Not executable
##############################################################################
if __name__ == "__main__":
    raise Exception ("Not executable")