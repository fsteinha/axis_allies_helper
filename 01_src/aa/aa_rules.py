from aa_type import CType
from aa_container import *

class CAAR:
    def __init__(self, aa_allowed_units = [], aa_conditinal_units = [], i_units_max = None, d_exlusive_limits = {}) -> None:
        self.aa_allowed_units = aa_allowed_units
        self.aa_conditinal_units = aa_conditinal_units
        self.i_unit_max = i_units_max
        self.d_exlusive_limits = d_exlusive_limits
        self.s_error_message = ""
        pass

    def check_add(self, t_container:CAAUnitContainer, aa_unit:CType) -> bool:    
        b_ret = True
        
        # check the overall limit
        if (self.i_unit_max != None) and t_container.get_unit_count() >= self.i_unit_max:
            self.s_error_message = "CAAR_ERROR,check_add: check the overall limit failed"
            b_ret = False
            pass

        # check for allowness 
        if (b_ret == True) and \
             ((aa_unit not in self.aa_allowed_units) and 
                (CType.get_sub_class(aa_unit) not in self.aa_allowed_units)):
            self.s_error_message = "CAAR_ERROR,check_add: check for allowness failed"
            b_ret = False
            pass

        # check is there an contional unit 
        if (b_ret == True) and \
            (len(self.aa_conditinal_units) > 0) and \
                (aa_unit not in self.aa_conditinal_units):
            i_cond_unit = 0
            for aa_cond_unit in self.aa_conditinal_units:
                if (t_container.get_unit_count(aa_cond_unit) > 0):
                    i_cond_unit = i_cond_unit + 1
                pass
            if (i_cond_unit == 0):
                self.s_error_message = "CAAR_ERROR,check_add: check is there an contional unit failed"
                b_ret = False     
                pass
            pass

        # check for limitations
            if (b_ret == True) and \
                (aa_unit in self.d_exlusive_limits) and \
                    (t_container.get_unit_count(aa_unit) >= self.d_exlusive_limits[aa_unit]):
                self.s_error_message = "CAAR_ERROR,check_add: check for limitations failed"
                b_ret = False     
            pass

        return b_ret
    
    def check_sub(self, t_container:CAAUnitContainer):
        if t_container.get_unit_count() <= 0:
            return False
        return True

class CAAR_Carrier(CAAR):
    def __init__(self, 
                 aa_allowed_units=[CType.U_FIGHTER, CType.U_T_BOMBER], 
                 aa_conditinal_units = [],
                 i_units_max=2) -> None:
        super().__init__(aa_allowed_units, aa_conditinal_units, i_units_max)
        pass

class CAAR_Cargo(CAAR):
    def __init__(self, 
                 aa_allowed_units=[CType.U_INFANTARY, CType.U_AAA, CType.U_ARTILLERY, CType.U_MECH_INFANTARY, CType.U_TANK], 
                 aa_conditinal_units = [CType.U_INFANTARY, CType.U_MECH_INFANTARY],
                 i_units_max=2) -> None:
        super().__init__(aa_allowed_units, aa_conditinal_units, i_units_max)
        pass

class CAAR_Land(CAAR):
    def __init__(self,  aa_allowed_units=[CType.F_MINOR_FACTORY, 
                                            CType.F_MAJOR_FACTORY, 
                                            CType.F_NAVAL_BASE, 
                                            CType.F_AIR_BASE,
                                            CType.C_UNIT_AIR,
                                            CType.C_UNIT_LAND], 
                        aa_conditinal_units=[], i_units_max=None, 
                    d_exlusive_limits={CType.F_MINOR_FACTORY:1, CType.F_MAJOR_FACTORY:1, CType.F_NAVAL_BASE:1, CType.F_AIR_BASE:1}) -> None:
        super().__init__(aa_allowed_units, aa_conditinal_units, i_units_max, d_exlusive_limits)
        pass

class CAAR_Sea(CAAR):
    def __init__(self, aa_allowed_units=[CType.C_UNIT_AIR, CType.C_UNIT_SEA], aa_conditinal_units=[], i_units_max=None, 
                    d_exlusive_limits={}) -> None:
        super().__init__(aa_allowed_units, aa_conditinal_units, i_units_max, d_exlusive_limits)
        pass
