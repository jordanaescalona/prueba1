import random

emojis = [":)",":(","O_0"]

print(random.choice(emojis))

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una bromita",
    "SHEESH": "Ligera desaprobación",
    "AGGRO": "Enojarse"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("Esa palabra significa: ", meme_dict[word])
else:
    print("La palabra no se encontró")
