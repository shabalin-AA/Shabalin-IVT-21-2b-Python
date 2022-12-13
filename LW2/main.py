from classes import *


p = Printing()
p.json_load("ex.json")
p.json_save("p.json")

m = Magazine()
m.json_load("ex2.json")
m.json_save("m.json")
