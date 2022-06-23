from aa_type import CType
from aa_container import *


class CAAR_Carrier:
    def __init__(self, aa_allowed_units = [CType.U_FIGHTER, CType.U_T_BOMBER], i_units_max = 2) -> None:
        self.aa_allowed_units = aa_allowed_units
        self.i_unit_max = i_units_max
        pass

    def check_add(self, t_container:CAAUnitContainer, aa_unit:CType) -> bool:
        if t_container.get_unit_count() >= self.i_unit_max:
            return False
        if aa_unit not in self.aa_allowed_units:
            return False
        return True
    
    def check_sub(self, t_container:CAAUnitContainer):
        if t_container.get_unit_count() <= 0:
            return False
        return True
