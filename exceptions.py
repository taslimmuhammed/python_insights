try:
    a=0
    z = 1/a
except Exception as e:
    print(e)

# custom  exception class
class Accident(Exception):
    def __init__(self,msg) -> None:
        self.msg = msg
