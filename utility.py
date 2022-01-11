from random import randint

def randYear():
    year = randint(-5000, 3000)
    if year < 0:
        return str(year * -1) + " BC"
    elif year > 0 and year < 1400:
        return str(year) + " AD"
    else:
        return str(year)

def randNum():
    num = randint(0, 100)
    return str(num)

def getRand(group):
    index = randint(0, len(group) - 1)
    return group[index]

def madeUpWord(c):
    i = 0
    word = ""
    numGoes = randint(3, 6)
    
    wordParts = ["tel", "mon", "sup", "ner", "welt", "so", "sc", "wer", "ont", "onc", "chen", "ber", "ni", "clo", "shlo", "din", "ger", "que", "nte", "zel", "phi", "chur", "pret", 
    "ker", "ble", "ret", "but", "orn", "pel", "ton", "ex", "neef", "glut", "vri", "sta", "neb", "mud", "sted", "preen", "op", "pusk", "mit", "rosc", "ey", "flong", "delp", "per",
    "tod", "deg", "nan", "bre", "pley", "stel", "chag", "zeet", "bot", "norb", "blet", "ling", "tion", "twog", "wit", "milg", "gleem", "ster", "vred", "wask", "ley", "dang", 
    "dled", "yep", "yod", "flit", "cow", "slam", "stle", "sten", "onc", "ology", "bia", "fred", "nkey", "ma", "no", "yes", "ey", "chew", "low", "fled", "donk", "ot", "man", "wo", 
    "lal", "len", "lod", "meed", "naf", "zax", "fort", "unt", "al", "eth", "eld", "mu\'n", "smor", "smel", "sming", "er", "acker", "wed", "wink", "two", "one", "mask", "b\'us", "rod", 
    "fled", "night", "day", "ben", "tom", "snod", "went", "stad", "bug", "tord", "bink", "lont", "swed", "cheed", "huld", "wher", "snal", "vud", "nast", "gel", "boot", "nan", "mex", 
    "pli", "swog", "gik", "vair", "whe", "sal", "suk", "ket", "kuv", "nub", "neen", "pel", "pud", "wunk", "chob", "flan", "crent", "mug", "dere", "fwee", "ople", "alt", "art", 
    "awe", "uk", "bare", "n\'t", "queg", "pot", "plud", "fare", "far", "mok", "mek", "mink", "bost", "mort", "hech", "y\'oy", "yun", "yer", "yix", "bof", "zif", "nort", "bauf", "sran", 
    "bume", "bay", "vust", "venk", "fav", "naf", "chie", "int", "ial", "irt", "ikle", "bres", "weet", "orp", "blem", "theel", "thusn", "thip", "thay", "klow", "murn", "shae", "fler",
    "bya", "slo", "chee", "nel", "oxna", "berni", "blau", "fie", "clae", "bakle", "voni", "swo", "bee", "mada", "mo\'do", "meeker", "baert", "ski", "cue", "kae", "zena", "moomo", "momo",
    "chacha", "bingo", "tata", "fera", "voomoo", "slappy", "chundy", "boost", "naka", "badi", "voz", "minko", "bada", "nikler", "fedma", "seldu", "wudma", "dindy", "mek", "soo", "freg",
    "vee", "kla", "bu", "zoo", "fla", "show", "bunkna", "wi\'p", "pelni", "zunksha", "chwee", "snad", "glin", "bup", "cod", "snif", "de", "chi", "gun", "po", "whop", "snooby", "borch", "fosk",
    "\'tway", "shuk", "nax", "sub", "misk", "chap", "land", "ton", "wa\'ya", "asel", "fuer", "gaen", "fasha", "bubby", "besma", "golti", "bornsnap", "pumper", "xanathu", "gukky",
    "forma", "gugmunger", "w\'estler", "pango", "beesnog", "hollas", "ackaboob", "tit", "boob", "weewee", "snorp", "flexor", "ublubber", "kacky", "elemen", "yuckma", "kalora", 
    "fabby", "underous", "nopal", "aliah", "morway", "sosig", "meme", "westerly", "abeeg", "haster", "bonapple", "googin", "mangerly", "bopis", "wawa", "dogin", "hooba", "cooki",
    "zass", "gunga", "apapa", "bonob", "shmo", "gawk", "taxes", "stanky", "euouae", "aeiou", "glunger", "swammy", "chungy", "a\'na", "gref\'chi", "b\'opway", "phobia", "astia", 
    "blub", "philia", "\'ton", "sneek", "chotchni", "ccio", "piis", "teef"]

    while i < numGoes:
        word += getRand(wordParts)
        i += 1

    if c:
        return word.capitalize()
    else:
        return word