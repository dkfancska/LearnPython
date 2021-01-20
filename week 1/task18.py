speed = int(input())
time = int(input())

route_of_mkad = 109

route = speed * time
print((route + route_of_mkad) % route_of_mkad)
