import paralleldots
paralleldots.set_api_key('NX4kgHEw0ORE5sz78OIR7V0AZ5ju36IJPKimE2vvLD0')

def ner(text):
    ner = paralleldots.ner(text)
    return ner