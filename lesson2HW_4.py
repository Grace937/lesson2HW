m=int(input('數學成績?'))
e=int(input('英文成績?'))
if m>90 and e>90:
    print('有獎品')
elif m<60 and e<60:
    print('要處罰')
elif m<60 or e<60:
    print('再加油')