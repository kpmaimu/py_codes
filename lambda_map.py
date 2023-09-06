print("hellooooooo")
cube=lambda x:x*x*x
print(cube(3))
my_list=(1,2,3)
new_list=list(map(cube,my_list))	
print(new_list)