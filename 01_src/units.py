from  aa_type import CType

class CAAItem():
    def __init__(self,s_name) -> None:
        self.s_name = s_name

    def set_type(self,aa_type) -> bool:    
        if type(aa_type) == str:
            self.aa_type = CType.get_type(aa_type)
        elif  CType.get_str(aa_type) != None:
            self.aa_type = aa_type
        
        return self.aa_type != None

    def print(self):
        s_out = f'''
Name: {self.s_name}
Type: {CType.get_str(self.aa_type)}
                 '''
        print (s_out)
        
if __name__ == "__main__":
    item = CAAItem("test")
    item.set_type(CType.T_LAND)
    item.print()