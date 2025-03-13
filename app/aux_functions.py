# -*- coding: utf-8 -*-
import random

def generate_custom_run_name():
    
    nouns = [
        "Quetzalcóatl", "Tezcatlipoca", "Huitzilopochtli", "Tlaloc", "Xochiquetzal",
        "Coyolxauhqui", "Tonatiuh", "Metztli", "Cihuacóatl", "Mictlantecuhtli",
        "Tlazoltéotl", "Chalchiuhtlicue", "Xipe Tótec", "Mayahuel", "Itzpapálotl",
        "Mixcóatl", "Xiuhtecuhtli", "Ixtlilton", "Ehecatl", "Ometeotl"
            ]
    
    adjectives = [
        "wise", "mysterious", "fierce", "stormy", "graceful",
        "rebellious", "brilliant", "mystical", "protective", "grim",
        "sensual", "flowing", "sacrificial", "nurturing", "fearsome",
        "hunting", "eternal", "joyful", "windy", "dualistic"
    ]
    
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(100, 999)  # Three-digit random number
    return f"{adj}-{noun}-{number}"