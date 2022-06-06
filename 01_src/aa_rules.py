from aa_type import CType


def class CAARCarrier:
    def __init__(self, aa_allowed_units = [CType.C_UNIT_AIR], i_units_max = 2) -> None:
        self.aa_allowed_units = aa_allowed_units
        self.i_unit_max = i_units_max
        pass