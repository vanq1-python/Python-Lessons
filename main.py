a = 'Doroty'
b = 'dorotY'
if a.casefold() == b.casefold():
    print(True)
else:
    print(False)