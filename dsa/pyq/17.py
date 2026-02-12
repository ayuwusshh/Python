password=input()
n=int(input())
has_alpha = False
has_upper = False
has_lower = False
has_special = False
has_digit=False
isvalid=False
ans=''
for ch in password:
  if ch.isalpha():
    has_alpha=True
  if ch.isupper():
    has_upper=True
  if ch.islower():
    has_lower=True
  if not ch.isalnum():
    has_special=True
  if ch.isdigit():
    has_digit=True
if len(password)>=8 and has_alpha and has_upper and has_lower and has_special and has_digit:
  isvalid=True
  for i in password:
    if i=='@':
      ans+='#'
    elif i=='#':
      ans+='@'
    else:
      ans+=chr(ord(i)+n)
if isvalid:
  print(ans)
else:
  print('Invalid')