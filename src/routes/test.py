from fastapi import APIRouter, Header, Form, Cookie, File, Path
from fastapi.responses import RedirectResponse

from core.schemas.test import TestIn, Nested


test_router = APIRouter(prefix="/test", tags=["test"])


# Methods test
@test_router.get("/get_test")
def get_test():
    return True

@test_router.post("/post_test")
def post_test():
    return True

@test_router.put("/put_test")
def put_test():
    return True

@test_router.delete("/delete_test")
def delete_test():
    return True

@test_router.options("/options_test")
def options_test():
    return True

@test_router.head("/head_test")
def head_test():
    return True


# Input test
@test_router.get("/query_test")
def query_test(a: int, b: str, c: bool, d: float):
    return True

@test_router.get("/query_optional_test")
def query_optional_test(a: int=0, b: str="", c: bool=True, d: float=0.1):
    return True

@test_router.post("/body_test")
def body_test(body: TestIn):
    return True

@test_router.post("/body_optional_test")
def body_optional_test(
        body: TestIn = TestIn(
            a=0,
            b="",
            c=True,
            d=0.1,
            e={"a": 1},
            f=[0],
            g=Nested(a=0),
        )
    ):
    return True

@test_router.get("/headers_test")
def headers_test(a: str = Header(...)):
    return True

@test_router.get("/headers_optional_test")
def headers_test(a: str = Header(default="hello")):
    return True

@test_router.post("/form_test")
def form_test(a: str = Form(...)):
    return True

@test_router.post("/form_optional_test")
def form_optional_test(a: str = Form(default="hello")):
    return True

@test_router.post("/cookies_test")
def cookies_test(a: str = Cookie(...)):
    return True

@test_router.post("/cookies_optional_test")
def cookies_optional_test(a: str = Cookie(default="hello")):
    return True

@test_router.put("/file_test")
def file_test(a: bytes = File(...)):
    return True

@test_router.put("/file_optional_test")
def file_optional_test(a: bytes = File(default=b"file_bytes")):
    return True

@test_router.put("/path_test/{a:str}/{b:int}/{c:float}")
def path_test(a: str = Path(...), b: int = Path(...), c: float = Path(...)):
    return True


# Response test
@test_router.get("/r_test_str")
def r_test_str():
    return "hello"

@test_router.get("/r_test_int")
def r_test_int():
    return 1

@test_router.get("/r_test_none")
def r_test_none():
    return None

@test_router.get("/r_test_float")
def r_test_float():
    return 0.1

@test_router.get("/r_test_array")
def r_test_array():
    return [1]

@test_router.get("/r_test_dict")
def r_test_dict():
    return {"a": 1}

@test_router.get("/r_test_no_200", status_code=201)
def r_test_no_200():
    return "hello"

@test_router.get("/r_test_3xx", status_code=300)
def r_test_3xx():
    return "hello"


@test_router.get("/r_test_redirect")
def r_test_redirect():
    return RedirectResponse(url="get_test")
