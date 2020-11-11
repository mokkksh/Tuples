# creating an empty tuple
tuple1=()
print(tuple1)

#creating tuples with integer element
tuple2=(1,2,3)
print(tuple2)

#tuple with mixed datatypes
tuple3=(101,"Moksh",20000.00,"HR Dept")
print(tuple3)

#creation of nested tuple
tuple4=("points",[1,4,3],(7,8,6))
print(tuple4)

#tuple can be created without any parentness
#also called tuple packing
tuple5=101,"Moksh",20000.00,"HR Dept"
print(tuple5)

#tuple unpacking is also possible
empid,empname,empsal,empdept = tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)
print(type(tuple5))

