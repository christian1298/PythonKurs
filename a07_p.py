import re

def main():
    f = open("Dateien/Uebung/xml_vorlage.py", "r")
    text = f.read()
    f.close()
    # print(text)
    xml_tags_rx(text)
    xml_tags(text)

def xml_tags(s: str):
    pos = 0
    while True:
        idx = s.find("<", pos)
        if idx < 0: break
        end = s.find(">", idx)
        if end < 0: break
        print(s[idx:end+1])
        pos = end+1

def xml_tags_rx(s: str):
    x = re.findall("<[^>]+>",s)
    for i in x:
        print(i)

if __name__ == "__main__":
    main()