
class CType():
    
    C_TERRITORY         = 0
    C_UNIT              = 1
    C_UNIT_LAND         = 2
    C_UNIT_SEA          = 3
    C_UNIT_AIR          = 4
    C_IPC               = 5
    C_NATION            = 6
    C_ALLIANCE          = 7
    C_FACILITY          = 8
    C_REGION            = 9
    

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

    d_Class = {
        C_TERRITORY        : C_TERRITORY,
        C_UNIT             : C_UNIT     ,
        C_IPC              : C_IPC      ,
        C_NATION           : C_NATION   ,
        C_ALLIANCE         : C_ALLIANCE ,
        C_FACILITY         : C_FACILITY ,
        C_REGION           : C_REGION   ,


        T_LAND             : C_TERRITORY,
        T_SEA              : C_TERRITORY,
           
        U_INFANTARY        : C_UNIT,
        U_MECH_INFANTARY   : C_UNIT,
        U_TANK             : C_UNIT,
        U_ARTILLERY        : C_UNIT,
        U_AAA              : C_UNIT,
        U_FIGHTER          : C_UNIT,
        U_T_BOMBER         : C_UNIT,
        U_S_BOMBER         : C_UNIT,
        U_CARGO            : C_UNIT,
        U_SUBMARINE        : C_UNIT,
        U_DESTROYER        : C_UNIT,
        U_CRUISER          : C_UNIT,
        U_BATTLESHIP       : C_UNIT,
        U_CARRIER          : C_UNIT,

        A_AXIS             : C_ALLIANCE,
        A_ALLIES           : C_ALLIANCE,
   
        F_MAJOR_FACTORY    : C_FACILITY,
        F_MINOR_FACTORY    : C_FACILITY,
        F_AIR_BASE         : C_FACILITY,
        F_NAVAL_BASE       : C_FACILITY,
   
        R_EUROPE           : C_REGION,
        R_ASIA_FAR_EAST    : C_REGION,
        R_NORDAMERICA      : C_REGION,
        R_SOUTHAMERICA     : C_REGION,
        R_AFRICA           : C_REGION,
        R_PACIFIC          : C_REGION,
        R_ASIA_MIDDLE_EAST : C_REGION,
        
        NA                 : NA
    }

    d_Sub_Class = {
        U_INFANTARY        : C_UNIT_LAND,
        U_MECH_INFANTARY   : C_UNIT_LAND,
        U_TANK             : C_UNIT_LAND,
        U_ARTILLERY        : C_UNIT_LAND,
        U_AAA              : C_UNIT_LAND,
        U_FIGHTER          : C_UNIT_AIR,
        U_T_BOMBER         : C_UNIT_AIR,
        U_S_BOMBER         : C_UNIT_AIR,
        U_CARGO            : C_UNIT_SEA,
        U_SUBMARINE        : C_UNIT_SEA,
        U_DESTROYER        : C_UNIT_SEA,
        U_CRUISER          : C_UNIT_SEA,
        U_BATTLESHIP       : C_UNIT_SEA,
        U_CARRIER          : C_UNIT_SEA,
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

    @staticmethod
    def get_class(t_type:int) -> int:
        try:
            return CType.d_Class[t_type]
        except:
            return None   

    @staticmethod
    def get_sub_class(t_type:int) -> int:
        try:
            return CType.d_Sub_Class[t_type]
        except:
            return None   

# test 
if __name__ == "__main__":
    assert CType.str(CType.C_TERRITORY       ) == "Territory"
    assert CType.str(CType.C_UNIT            ) == "Unit"
    assert CType.str(CType.C_IPC             ) == "IPC"
    assert CType.str(CType.C_NATION          ) == "Nation"

    assert CType.str(CType.T_LAND            ) == "Land"
    assert CType.str(CType.T_SEA             ) == "Sea"
    
    assert CType.str(CType.U_INFANTARY       ) == "Infantary"
    assert CType.str(CType.U_MECH_INFANTARY  ) == "Mech-Infantary"
    assert CType.str(CType.U_TANK            ) == "Tank"
    assert CType.str(CType.U_ARTILLERY       ) == "Artillery"
    assert CType.str(CType.U_AAA             ) == "AAA"
    assert CType.str(CType.U_FIGHTER         ) == "Fighter"
    assert CType.str(CType.U_T_BOMBER        ) == "Tactical-Bomber"
    assert CType.str(CType.U_S_BOMBER        ) == "Stratic-Bomber"
    assert CType.str(CType.U_CARGO           ) == "Cargo"
    assert CType.str(CType.U_SUBMARINE       ) == "Submarine"
    assert CType.str(CType.U_DESTROYER       ) == "Destroyer"
    assert CType.str(CType.U_CRUISER         ) == "Cruiser"
    assert CType.str(CType.U_BATTLESHIP      ) == "Battelship"
    assert CType.str(CType.U_CARRIER         ) == "Carrier"
    assert CType.str(CType.A_AXIS            ) == "Axis"
    assert CType.str(CType.A_ALLIES          ) == "Allies"
   
    assert CType.str(CType.F_MAJOR_FACTORY   ) == "Major factory"
    assert CType.str(CType.F_MINOR_FACTORY   ) == "Minor factory"
    assert CType.str(CType.F_AIR_BASE        ) == "Air base"
    assert CType.str(CType.F_NAVAL_BASE      ) == "Naval base"
   
    assert CType.str(CType.R_EUROPE          ) == "Europe"
    assert CType.str(CType.R_ASIA_FAR_EAST   ) == "Asia far east"
    assert CType.str(CType.R_NORDAMERICA     ) == "North america"
    assert CType.str(CType.R_SOUTHAMERICA    ) == "South america"
    assert CType.str(CType.R_AFRICA          ) == "Africa"
    assert CType.str(CType.R_PACIFIC         ) == "Pacific"
    assert CType.str(CType.R_ASIA_MIDDLE_EAST) == "Asia middle east"
    
    assert CType.str(CType.NA                ) == "N/A"

    assert CType.get_class(CType.C_TERRITORY        )  == CType.C_TERRITORY
    assert CType.get_class(CType.C_UNIT             )  == CType.C_UNIT     
    assert CType.get_class(CType.C_IPC              )  == CType.C_IPC      
    assert CType.get_class(CType.C_NATION           )  == CType.C_NATION   
    assert CType.get_class(CType.C_ALLIANCE         )  == CType.C_ALLIANCE 
    assert CType.get_class(CType.C_FACILITY         )  == CType.C_FACILITY 
    assert CType.get_class(CType.C_REGION           )  == CType.C_REGION   


    assert CType.get_class(CType.T_LAND             )  == CType.C_TERRITORY
    assert CType.get_class(CType.T_SEA              )  == CType.C_TERRITORY
       
    assert CType.get_class(CType.U_INFANTARY        )  == CType.C_UNIT
    assert CType.get_class(CType.U_MECH_INFANTARY   )  == CType.C_UNIT
    assert CType.get_class(CType.U_TANK             )  == CType.C_UNIT
    assert CType.get_class(CType.U_ARTILLERY        )  == CType.C_UNIT
    assert CType.get_class(CType.U_AAA              )  == CType.C_UNIT
    assert CType.get_class(CType.U_FIGHTER          )  == CType.C_UNIT
    assert CType.get_class(CType.U_T_BOMBER         )  == CType.C_UNIT
    assert CType.get_class(CType.U_S_BOMBER         )  == CType.C_UNIT
    assert CType.get_class(CType.U_CARGO            )  == CType.C_UNIT
    assert CType.get_class(CType.U_SUBMARINE        )  == CType.C_UNIT
    assert CType.get_class(CType.U_DESTROYER        )  == CType.C_UNIT
    assert CType.get_class(CType.U_CRUISER          )  == CType.C_UNIT
    assert CType.get_class(CType.U_BATTLESHIP       )  == CType.C_UNIT
    assert CType.get_class(CType.U_CARRIER          )  == CType.C_UNIT

    assert CType.get_class(CType.A_AXIS             )  == CType.C_ALLIANCE
    assert CType.get_class(CType.A_ALLIES           )  == CType.C_ALLIANCE
   
    assert CType.get_class(CType.F_MAJOR_FACTORY    )  == CType.C_FACILITY
    assert CType.get_class(CType.F_MINOR_FACTORY    )  == CType.C_FACILITY
    assert CType.get_class(CType.F_AIR_BASE         )  == CType.C_FACILITY
    assert CType.get_class(CType.F_NAVAL_BASE       )  == CType.C_FACILITY
   
    assert CType.get_class(CType.R_EUROPE           )  == CType.C_REGION
    assert CType.get_class(CType.R_ASIA_FAR_EAST    )  == CType.C_REGION
    assert CType.get_class(CType.R_NORDAMERICA      )  == CType.C_REGION
    assert CType.get_class(CType.R_SOUTHAMERICA     )  == CType.C_REGION
    assert CType.get_class(CType.R_AFRICA           )  == CType.C_REGION
    assert CType.get_class(CType.R_PACIFIC          )  == CType.C_REGION
    assert CType.get_class(CType.R_ASIA_MIDDLE_EAST )  == CType.C_REGION
    
    assert CType.get_class(CType.NA                 )  == CType.NA

    assert CType.get_sub_class(CType.C_TERRITORY        )  == None
    assert CType.get_sub_class(CType.C_UNIT             )  == None
    assert CType.get_sub_class(CType.C_IPC              )  == None
    assert CType.get_sub_class(CType.C_NATION           )  == None
    assert CType.get_sub_class(CType.C_ALLIANCE         )  == None
    assert CType.get_sub_class(CType.C_FACILITY         )  == None
    assert CType.get_sub_class(CType.C_REGION           )  == None


    assert CType.get_sub_class(CType.T_LAND             )  == None
    assert CType.get_sub_class(CType.T_SEA              )  == None
       
    assert CType.get_sub_class(CType.U_INFANTARY        )  == CType.C_UNIT_LAND
    assert CType.get_sub_class(CType.U_MECH_INFANTARY   )  == CType.C_UNIT_LAND
    assert CType.get_sub_class(CType.U_TANK             )  == CType.C_UNIT_LAND
    assert CType.get_sub_class(CType.U_ARTILLERY        )  == CType.C_UNIT_LAND
    assert CType.get_sub_class(CType.U_AAA              )  == CType.C_UNIT_LAND
    assert CType.get_sub_class(CType.U_FIGHTER          )  == CType.C_UNIT_AIR
    assert CType.get_sub_class(CType.U_T_BOMBER         )  == CType.C_UNIT_AIR
    assert CType.get_sub_class(CType.U_S_BOMBER         )  == CType.C_UNIT_AIR
    assert CType.get_sub_class(CType.U_CARGO            )  == CType.C_UNIT_SEA
    assert CType.get_sub_class(CType.U_SUBMARINE        )  == CType.C_UNIT_SEA
    assert CType.get_sub_class(CType.U_DESTROYER        )  == CType.C_UNIT_SEA
    assert CType.get_sub_class(CType.U_CRUISER          )  == CType.C_UNIT_SEA
    assert CType.get_sub_class(CType.U_BATTLESHIP       )  == CType.C_UNIT_SEA
    assert CType.get_sub_class(CType.U_CARRIER          )  == CType.C_UNIT_SEA

    assert CType.get_sub_class(CType.A_AXIS             )  == None
    assert CType.get_sub_class(CType.A_ALLIES           )  == None
   
    assert CType.get_sub_class(CType.F_MAJOR_FACTORY    )  == None
    assert CType.get_sub_class(CType.F_MINOR_FACTORY    )  == None
    assert CType.get_sub_class(CType.F_AIR_BASE         )  == None
    assert CType.get_sub_class(CType.F_NAVAL_BASE       )  == None
   
    assert CType.get_sub_class(CType.R_EUROPE           )  == None
    assert CType.get_sub_class(CType.R_ASIA_FAR_EAST    )  == None
    assert CType.get_sub_class(CType.R_NORDAMERICA      )  == None
    assert CType.get_sub_class(CType.R_SOUTHAMERICA     )  == None
    assert CType.get_sub_class(CType.R_AFRICA           )  == None
    assert CType.get_sub_class(CType.R_PACIFIC          )  == None
    assert CType.get_sub_class(CType.R_ASIA_MIDDLE_EAST )  == None
    
    assert CType.get_sub_class(CType.NA                 )  == None


    