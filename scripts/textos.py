# textos.py
import random

frases = [
    "¿Todo bien, pibe?", 
    "¡Aguante el fernet!", 
    "Nos tomamos unos mates, ¿o qué?", 
    "¿Listo para el asado?", 
    "Che, no te olvides del dulce de leche."
]

insultos = [
    "che boludo", 
    "che pelotudo"
]

refranes = [
    "No hay mal que por bien no venga.",
    "Al que madruga, Dios lo ayuda.",
    "Más vale pájaro en mano que cien volando.",
    "El que se quema con leche, ve una vaca y llora.",
    "Camarón que se duerme, se lo lleva la corriente."
]

respuestas_insultos = [
    "Eh, tranqui, no te calientes que estamos en paz.",
    "Jajaja, no me ofendo, somos argentos.",
    "Ahí nomás, no la bardees."
]

def Obtener_Frase():
    frase=random.choice(frases)