from pydantic import BaseModel



class Nested(BaseModel):
    a: int = 0


class TestIn(BaseModel):
    a: int
    a_o: int = 0
    
    b: str
    b_o: str = ""
    
    c: bool
    c_o: bool = True
    
    d: float
    d_o: float = 0.1
    
    e: dict
    e_o: dict = {"a": 1}
    
    f: list
    f_o: list = [0]

    g: Nested
    g_o: Nested = Nested(a=0)
