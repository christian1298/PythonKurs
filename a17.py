def write_xml(dict):
    msg = """<?xml version="1.0" encoding="UTF-8"?>
<dict>"""
    for i in dict:
        msg += f"""
    <entry>
        <key>{i}</key>
        <value>{dict[i]}</value>
    </entry>"""
    msg += "</dict>"
    #print(msg)
    with open("a17.txt", "w") as f:
        f.write(msg)

d = {
    "a" : 3,
    "b" : 5,
    "c" : "hallo"
}

write_xml(d)
