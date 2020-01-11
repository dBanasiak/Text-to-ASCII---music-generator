from CONVERTER.convertTextToAscii import CONVERT_TEXT_TO_ASCII
from SYMPHONY.createSymphony import CREATE_SYMPHONY
import re

# text = "Szła dzieweczka do laseczka Do zielonego, do zielonego, do zielonego. Napotkała myśliweczka Bardzo szwarnego, bardzo szwarnego, bardzo szwarnego"

text = str(input("Wklej teskt ulubionej piosenki (UWAGA - tekst musi być w jednej linii tak ja w powyższym przykładzie): ")).strip()
text = " ".join(re.findall("[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", text)).lower()
print("TEKST: ", text)

convText = CONVERT_TEXT_TO_ASCII(text)
print("ASCII: ", convText)
trio = CREATE_SYMPHONY(convText)[:-4]
print("NUTY: ", trio)


file = open('music.hs', 'w')
file.write('play $ (' + trio + ')')