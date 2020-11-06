import re
finder=re.finditer("ad","adadadbdadbd")
for item in finder:
    print(item.start())