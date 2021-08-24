from random import choice

def get_head():
    return choice([
        "Customizable Fashion Imagery",
        "Brand New Style",
        "Must Have Item",
        "Season Hot Item",
        "Top Selling Item",
        "Unique Style",
    ])

def get_content():
    return choice([
        "The solution allows you to showcase products on your existing, previously photographed real model images with Genfit",
        "Use your own real model images or pick from our catalog of 3D model with Genfits",
        "Put together products and showcase outfits on models with Genfit",
        "Retailers can save 75% of photoshoot costs with Genfit"
    ])
