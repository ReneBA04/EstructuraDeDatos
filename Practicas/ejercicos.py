vocales = "a, e, i, o, u"

for letra in "murcielago":
    if letra in vocales:
        print(letra)

preguntas = ['nombre', 'objetivo','sistema operativo']
respuestas= ['Rene', 'aprender pyhton', 'Linux']

for pregunta, respuestas in zip(preguntas, respuestas):
    print('¿Cúal es tu {0}?, la respuesta es: {1}.'.format(pregunta, respuestas))

