

xmltxt="""<?xml version="1.0" encoding="UTF-8"?>
<quiz>
 <question>
  <text>Kann ein String in Python verändert werden?</text>
  <solution>Nein, für Änderungen muss er neu zusammengesetzt werden.</solution>
 </question>
</quiz>
"""

pos = 0
while True:
    idx = xmltxt.find("<", pos)
    if idx < 0: break
    end = xmltxt.find(">", idx)
    print(xmltxt[idx:end+1])
    pos = end +1
 
