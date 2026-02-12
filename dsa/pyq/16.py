# x,y=map(int,input().split())
# rem=x%y
# if rem<y-rem:
#   print(x-rem)
# else:
#   print(x+(y-rem))
def roundingof(number):
  int_part=int(number)
  dec_part=number-int_part
  if dec_part>=0.5:
    return int_part+1
  else:
    return int_part
x,y=map(int,input().split())
nearest=x/y
rounded=roundingof(nearest)
print(rounded*y)