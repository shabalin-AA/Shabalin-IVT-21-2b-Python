from classes import *


p = Printing("Winnie Pooh")
p.json_load("ex.json")
p.json_save("p.json")

m = Magazine("Forbes")
m.json_load("ex2.json")
m.json_save("m.json")
