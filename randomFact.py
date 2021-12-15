from random import randint

def randYear():
    year = randint(-5000, 3000)
    if year < 0:
        return str(year * -1) + " BC"
    else:
        return str(year)

def randNum():
    num = randint(-100, 100)
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
    "lal", "len", "lod", "meed", "naf", "zax", "fort", "unt", "al", "eth", "eld", "mun", "smor", "smel", "sming", "er", "acker", "wed", "wink", "two", "one", "mask", "bus", "rod", 
    "fled", "night", "day", "ben", "tom", "snod", "went", "stad", "bug", "tord", "bink", "lont", "swed", "cheed", "huld", "wher", "snal", "vud", "nast", "gel", "boot", "nan", "mex", 
    "pli", "swog", "gik", "vair", "whe", "sal", "suk", "ket", "kuv", "nub", "neen", "pel", "pud", "wunk", "chob", "flan", "crent", "mug", "dere", "fwee", "ople", "alt", "art", 
    "awe", "uk", "bare", "n't", "queg", "pot", "plud", "fare", "far", "mok", "mek", "mink", "bost", "mort", "hech", "yoy", "yun", "yer", "yix", "bof", "zif", "nort", "bauf", "sran", 
    "bume", "bay", "vust", "venk", "fav", "naf", "chie", "int", "ial", "irt", "ikle", "bres", "weet", "orp", "blem", "theel", "thusn", "thip", "thay", "klow", "murn", "shae", "fler",
    "bya", "slo", "chee", "nel", "oxna", "berni", "blau", "fie", "clae", "bakle", "voni", "swo", "bee", "mada", "modo", "meeker", "baert", "ski", "cue", "kae", "zena", "moomo", "momo",
    "chacha", "bingo", "tata", "fera", "voomoo", "slappy", "chundy", "boost", "naka", "badi", "voz", "minko", "bada", "nikler", "fedma", "seldu", "wudma", "dindy", "mek", "soo", "freg",
    "vee", "kla", "bu", "zoo", "fla", "show", "bunkna", "wip", "pelni", "zunksha", "chwee", "snad", "glin", "bup", "cod", "snif", "de", "chi", "gun", "po", "whop", "snooby", "borch", "fosk",
    "tway", "shuk", "nax", "sub", "misk", "chap", "land", "ton"]

    while i < numGoes:
        word += getRand(wordParts)
        i += 1

    if c:
        return word.title()
    else:
        return word

verbs = ["got", "chuggled", "fell in love with the idea of", "slurped", "locked eyes with", "consumed", "concieved", "started a ^ revolution around the idea of", "^ly chewed on",
"won", "hired", "claimed", "started a standing ovation for", "delivered the keynote speech at a conference devoted to", "started a religion that worships", "punched the | out of",
"made a GoFundMe for", "starred in a commercial advertising", "applied ^ pressure to", "ate a ^ meal consisting exclusively of", "held ^ eye contact with", "acquired",
"created an algorithm that calculates", "fought", "sued", "smelled the ^ odor of", "rued the day that they met", "considered purchasing", "tasted, and loved", 
"met, and was bored by", "lost & pounds by only eating", "fist-bumped", "gave a ^ talking to", "delivered a stirring speech to a crowd of people dressed like", "discovered",
"happened upon", "embraced", "lost", "entered the ring with", "spent & dollars on", "shanked", "imprisoned", "played doubles tennis with", "won a @ lookalike contest against", 
"shot a ^ look at", "took a swing at", "won an all-expenses-paid trip to", "^ly defeated", "whooshed past", "took a ^ picture of", "held a ^ conversation with",
"painted a ^ picture of", "tweeted about", "created a social media platform for", "organized a campaign for", "managed a corporate merger with the help of", "squirted out",
"founded a ^ kingdom with the help of", "^ly destroyed + while researching", "started _ in a garage owned by", "shot", "killed", "murdered", "^ly kissed", "sucked",
"wrote a ^ novel about", "learned about", "squeezed out", "gave birth to", "bought %% for", "drank an entire glass of", "wanted to slap", "^ly swallowed", "loved to hate",
"held a charity yard sale for", "^ly slit the $ of", "^ly saved", "showed real | to", "broke QQ $ because of", "punctured QQ $ with", "chewed up and spit out", "doggedly pursued",
"raised a ^ $ toward", "created the first prototype for", "envisioned a ^ future for", "proposed a toast to", "threw a ^ party to celebrate", "flew too close to", 
"engaged in $-to-$ combat with", "started a restaurant that only serves", "joked about the size of @'s $ by referencing", "started a petition to outlaw", "held",
"was cast as @ in a TV show about", "started a kickstarter campaign to fund the creation of"]

parties = ["a = wearing false teeth", "the President of +", "the most ^ haircut of all time", "your $, but & inches in length", "a =",
"nuclear war", "white people", "^ people", "^ stool", "a = that " + getRand(verbs) + " @", "the CFO of _", "a new street gang called 'the ^ babies'", 
"& push-ups", "a ^, ^ bodybuilder", "a = disguised as @", "a ^ly ^ Halloween costume", "the bathroom", "^ soup",
 "a ^CC =CC Champion", "the annual _ dance-off", "Dracula (but if he was from +)", "a ^ly ^ handshake", "an extra set of $s",
"^ly ^ pasta", "your ^ dentist", "@'s accountant", "a mirror that makes you look ^ly ^", "gorgonzola cheese", "the CEO of _",
"the entire South Pole", "a stairway to +", "the reason you were born", "a ^ resignation letter", "a ^ly ^ almond",
"barf", "^, ^ burritos", "a war between =s and =s", "a ^ly ^ corn dog", "a = with a tail that's just too ^", "a = with a =", "a = with too much |",
"the element of surprise", "a slip of the $", "hard, ^ drugs", "a banana that needs to be peeled & times", "apples and grapes", "anal fissures", 
"the =CC President", "train enthusiasts", "attendees of a $ convention", "the stink eye", "the surface of the sun", "^, ^ brownies",
"_-branded swag", "_'s holiday bash", "@", "@'s secret $", "@'s $", "#", "a program that teaches =s to speak +-ese",
"one of those small cheeses in wax", "toast", "two =s square-knotted together", "= cruelty", "2nd degree murder", "organized crime", "the NYPD", 
"someone who looks vaguely like @", "milk", "^ milk", "a mountain of broccoli", "^ gossip", "memes from 2010", "a ^ baby", "+", "animals", "plants", "dirt", 
"butt", "immortality", "|", "=s", "= enthusiasts", "your $", "the $ of a =", " a = with & extra $s", "^ pants", "QQ VV wearing a @ costume", "QQ VV",
"@'s VV's favorite VV", "your VV riding a =", "^ chicken nugget", madeUpWord(False), "a ^ PR campaign"]

begs = ["In other news,", "In light of today's events,", "Despite what you may have heard,", "He looked me right in the eye and said these exact words:", 
"Having been born in the year #,", "Despite a lifelong battle with ~,", "Picture this in your mind for a moment:", "Fun fact:", "Did you know?",
"Have you considered the fact that", "My favorite childhood memory is when", "What's ^ is that mainstream media would have you believe", 
"Once upon a time,", "When you really think about it,", "Yesterday,", "Whenever @ looks ^, it's because", "In the year of Our Lord #,", 
"In case you haven't heard yet,", "Through sheer | and |,", "If you ever have a ^ day, just remember", "In an act of desperation,", "^CCly, due to " + getRand(parties) + ", ",
"If you squint and turn your head ^ly to the side, you'll see that", "Despite having ^ |,", "If a = or @ is attacking you, remember that", 
"Wanna really get somebody's attention? Try screaming this:", "The German word " + madeUpWord(False) + " describes the situation where", 
"The hidden country of " + madeUpWord(True) + " is where"]

adjectives = ["dumb", "ugly", "brown", "fuchsia", "campy", "proverbial", "obtuse", "arrogant", "swollen", "frightening", "hungry", "diseased", "naked", "squirming", "^-$'ed", "surprising",
"short", "rank", "malodorous", "cold", "long", "wide", "clammy", "strong", "stirring", "classy", "high-brow", "fat", "overweight", "wooden", "verdant", "al dente", "chewy", "fudgy",
"pink", "local", "sweaty", "dry", "freeze-dried", "heroic", "suspicious", "explosive", "chunky", "matcha-flavored", "finely-aged", "expired", "evil", "chaotic", "black", "white", 
"chocolatey", "fast", "intimidating", "drowning", "+-ese", "bland", "gosh darn", "problematic", "rootin' tootin'", "blessed", "savage", "room-temperature", "underwhelming", 
"overzealoused", "slow", "burnt", "venomous", "uplifting", "beautiful", "", "juicy", "wet", "damp", "moist", "uncomfortable", "unhealthy", "long-winded", "unfair", "racist", 
"annoying", "pugnacious", "stabbing", "voluptuous", "candid", "quiet", "thin", "skinny", "thick", "dull", "insipid", "twisted", "knarled", "stinky", "sweet", "accidental",
"pompous", "fancy", "well-dressed", "sharp", "red", "bent", "pointed", "heavy", "tense", "intense", "lurid", "mild", "mild-mannered", "terrible", "horrible", "heinous", "passionate",
"cruel", "bumpy", "lumpy", "angry", "livid", "unnerving", "disgusting", "lemon-flavored", "creamy", "woody", "peppery", "piquant", "fashionable", "prudent", "unflattering", 
"efficient", "complementary", "fortitudinous", "hard", "stiff", "tart", "sour", "acidic", "viscous", "^ly ^",  "demanding", "draining", "clever", "eldritch", "peanut-buttery",
"exhausting", "well-behaved", "cute", "stunted", "bad", "good", "great", "boring", "less-than-^", "cringeworthy", "nerdy", "racy", "new", "interesting",
"elaborate", "live", "cultured", "slightly ^", "overly ^", "not-so-^", "crispy", "crunchy", "pure", "medium-sized", "anime", "furtive", "poor", "milquetoast", "pensive", "suave",
"overwhelming", "wrong", "well-written", "happy-go-lucky", "old", "medium-sized", "extra large", "loose", "political", "particular", "thoughtful", "confusing", "mean", "useless",
"final", "innappropriate", "quick", "fluent", "odd", "weird", "unusual", "stupid", "suspicious", "slight", "confident", "exaggerated", "unwavering", "true", "real", "emotional",
"physical", "spiritual", "virtual", "textural", "perfect", "hot", "male", "female", "broken", "stern", "whiny", "indignant", "bright", "massive", "bare", "deft", "agile", "swift",
"convenient", "mushroom", "functional", "chic", "united", "greedy", "brash", "proud", "unstoppable", "floppy", "flailing", "full", "positive", "negative", "dirty", "fishy", "filthy",
"candy", "iron", "bronzen", "flaxen", "golden", "rock-hard", "titanium", "VV's", madeUpWord(False), "moderate", "impressive", "successful", "unsuccessful", "hypothetical", "sly",
"frozen", "melted", "acute", "instant", "amateur", "flat", "unprecedented", "uncouth", "unbecoming", "subpar", "chronic"]

concepts = ["gusto", "fervor", "panache", "restraint", "sense of style", "wherewithall", "curiosity", "warrior's heart", "pride", "luck", "chastity", "charity", "joy", "wonder", 
"passion", "delicacy", "peace", "understanding", "va-va-voom", "^ strut", "^ swagger", "ingenuity", "self-control", "spirit", "innovation", "clarity", "je ne sais quoi",
"love", "nerve", "hutzpah", "cacahuetes", "resolve", "verve", "boldness", "^ genius", "grit", "determination", "hunger", "rage", "nostalgia", "melancholy", "wistfulness",
"longing", "resilience", "wit", "faith", "honor", "candor", "serenity", "hope", "patience", "kindness", "cheer", "goodwill", "can-do attitude", "spirit", "moxie", "soul",
"joie de vivre", "virtue", "courage", "fire", "selflessness", "pride", "glamour", "$", madeUpWord(False), "culture", "disdain", "apprehension", "hesitancy", "cowardice", 
"evil", "coldness", "underhandedness", "subtlety", "visibility", "sausage", "pancakes", "eggs", "stupor", "stones"]

ends = [" while @ was still president.", ", using QQ $ to chug a two-liter of mountain dew.", " with the | of a ^ =.", " - how cool is that?", 
", which, ^ly, broke the world record.", ", because that's what ^ | looks like.", ", cause money don't grow on " + getRand(parties) + ".", 
" - however, this angered the envoy from +, starting World War &.", ", and that's a fact.", " with a | far beyond the norm.", " whilst fending off ^ ladies with a ^ spatula.",
" as part of a ^ comedy routine.", ", starting a new dance craze on Tik Tok.", ", inspiring @ to paint a ^ picture of @.", ", inspiring @ to found _.",
", landing them in ^ water with +.", ", which @ then made a ^ joke about on social media.", ", which jumpstarted @'s | for +'s |.", ", which makes me feel like a ^ =.",
", which gave @ ~.", ", which has to be the most ^ way to lose weight.", ", so, ha.", " - thanks a lot, VV!", ". ;)", " using | to save the multiverse.",
" to prove to QQ VV that they have ^ |.", ", in hopes that it would make @ notice QQ |.", ", which prompted @ to cancel them on Twitter.", 
" - thank goodness!", " - the three words I'd use to describe this would be ^, ^, and ^!", " - what a ^ time to be ^!", " - what a ^ way to have been " + getRand(verbs) + "!", 
" - what a ^ way to have been " + getRand(verbs) + "!", " - what a ^ way to have been " + getRand(verbs) + "!", " by sitting and thinking very hard about %%.",
" by the $ of @.", ' while juggling & "%%"-s.', " - now that shows ^ |!", " - now that takes |!", " - seems a bit ^ to me...", ", which is SO not ^.", ", giving everyone ~.",
", utilizing only %% and %%.", ", causing @ to break QQ $.", ", causing @ to instantly grow new $s.", ", after which @ got QQ $ pierced.", " - in other words, " + madeUpWord(False) + "."]

companies = ["Coca-Cola", "Monster Energy", "Frito-Lay", "Nestle", "Google", "Microsoft", "Minecraft", "JP Morgan", "Taco Bell", "Verizon", "US Cellular", "Cingular", 
"VVCC Jeans, Inc.", "IBM", "Fatheads", "Fiji Water", "Vance Refrigeration", "Disney", "Fox News", "MSNBC", "Walmart", "IKEA", "Snuggie", "FlexTape", 
"Piggly Wiggly", "Purple Flurp", "Facebook", "Twitter", "Doofenshmirtz Evil, Inc.", "Netflix", "Dunder Mifflin", "Apple", "WUPHF", "the Krusty Krab", "the Chum Bucket",
"Doritoes", "Target", "PETA", "Gamestop", "Dogecoin", "Youtube", "Naughty Dog", "CoolMath Games", "McDonald's", "Burger King", "Long John Silver's", 
"Nintendo", "Sony", "Gfuel", "Gamer Goo", "Dunkin Donuts", "Raid: Shadow Legends", "Pixar", "Popeye's", "Papa John's", "Tik Tok", "Buy N' Large", "Activision", "DreamWorks",
"Starbucks", "Raid: Shadow Legends", "Blizzard", "FizzBuzz, Inc.", "Los Pollos Hermanos", "Amazon", "SpaceX", "Tesla", "Tumblr", "MySpace", "Reddit", "BitConnect", "The Dentist",
"Cost Cutters"]

celebs = ["Dolly Parton", "Robert Pattinson", "the Geico =CC", "the mascot for the Pittsburg Steelers", "the = from Air Bud", "Keanu Reeves", "the Car =CC", 
"Ben Shapiro", "PewDiePie", "Elvis", "Nickelback", "Guy Fieri", "Gordon Ramsay", "a =", "a ^ =", "a ^ =", "The ^CC Man", "a ^ piece of fruit", 
"Michael Scott", "Ghandi", "the Pope", "Jimmy Neutron", "Carl Wheezer", "the Pillsbury Dough Boy", "Jake Paul", "Logan Paul", "you", "your VVCC", "Jeff Dunham", 
"Dane Cook", "George Washington", "Thomas Jefferson", "Abraham Lincoln", "Plato", "Aristotle", "Leonardo Da Vinci", "John Kennedy", "Isaac Newton", "Albert Einstein", 
"Will Ferrel", "Ariana Grande", "Paul Revere", "Queen Elizabeth", "Christopher Columbus", "JK Rowling", "Pablo Picasso", "Cuddles", "Walt Disney", "Winston Churchill", 
"Elon Musk", "Bill Gates", "Jeff Bezos", "Steve Irwin", "Billy Mays", "the ^ guy from Friends", "the ^ girl from The Office", "Chester Cheeto", 
"Tony the =CC", "=CC Sam", "the Trix =CC", "John Mayer", "Elvis", "the Prince of |CC", "Mario", "Luigi", "Waluigi", "your favorite =", 
"the Duke of Nuts", "Jake the =CC", "the Ice King", "Spongebob Squarepants", "QQ ^ VV", "Will Smith", "Miranda Cosgrove", "Drake and Josh", "the Burger King",
"CatDog", "= =", "Arnold (from Hey Arnold)", "=CCMan", "The all-new Hyundai Sonata", "The ^CC $CC", "Joker (from Joker)", "Squidward", "Patrick",
"Brendan Frasier", "Tommy Wiseau", "Kirby", "Bubsy", "Bigfoot", "Sonic the =CC", "Gurbanguly Berdimuhamedow", "Kim Jong Un", "Xi Jinping", "Moon Jae-in", 
"Reggie Fils-Aime", "Yoshihide Suga", "Grandma", "Grandpa", "^CCMan", "Finn the =CC", "a _ employee", "Warren Buffet", "Billie Eilish", "Videogamedunkey", "Grover Cleveland", 
"Thomas Edison", "Winnie the Pooh", "QuailMan", "Jeffery Bezos", "Vermin Supreme", "Chris Hemsworth", "Chevy Chase", "Dick Van Dyke", "Andy Griffith", "Bob Hope", 
"Regis Philbin", "Dr. Phil", "Hulk Hogan", "Honey Boo-Boo", "Gordon Ramsay", "Bo Burnham", "Obamna", "a perfect doppelganger for @", "Conan O'Brian", "Steve Carrell", 
"Steve Harvey", "Tim Apple", "The One True =CC"]

places = ["^CC Jersey", "the ^CC States", "Europe", "Russia", "Asia", "Japan", "yo VV's house", "the sock drawer", "Madagascar", "Californ-I-A", "your soul", 
"the corporate offices of _", "the ^CC House", "Yellowstone Park", "Italy", "the Pentagon", "Mt. Everest", "an underground city", "the dungeon", "a ^ city",
"China", "Fiji", "India", "Pyongyang", "Seoul", "one of the Koreas", "the states of ^CC and ^CC Dakota", "Hell", "^CC Virginia", "^CC Carolina", "Hell",
"^CC York", "^CC Delhi", "Stonehenge", "Gramps' basement", "any given island in the Pacific Ocean", "the tip of the Statue of Liberty's torch", madeUpWord(True),
"a ^ hill of termites", "the realm of the =CC Queen", "a store that only sells ^ pictures of @'s $", "#", "Disneyland", "Mt. Rushmore", "the Animal Kingdom",
"Tokyo", "Beijing", "Athens", "Ancient Rome", "London", "Austrialia", "^CC Zealand", "Azerbaijan", "Heaven", "the University of +", "^CCLand", "^CC ^CCLand" "the Flat Earth"]

animals = ["lion", "cat", "dog", "squid", "mollusk", "clam", "zebra", "axolotl", "rhino", "tiger", "lamb", "octopus", "antelope", "fawn", "llama", "parrot", "whale", 
"geoduck", "barnacle", "snail", "slug", "squirrel", "giraffe", "dingo", "wolf", "coyote", "hyena", "ocelot", "puma", "mountain lion", "fox", "polar bear", "grizzly bear", 
"goldfish", "monkey", "spider monkey", "chimpanzee", "brown bear", "black bear", "lemur", "chihuahua", "flounder", "clownfish", "dolphin", "scallop", "sphinx", "griffin", 
"dragon", "donkey", "unicorn", "yokai", "mouse", "rat", "pig", "cow", "bull", "dove", "shrew", "armadillo", "pangolin", "anteater", "snake", "viper", "cobra", "orangutan", 
"rabbit", "bunny", "jackalope", "chimera", "cerberus", "manticore", "scorpion", "mosquito", "horse fly", "ladybug", "black widow", "brown recluse", "wolf spider", "human",
"dung beetle", "salamander", "firedrake", "wendigo", "wyvern", "sea lion", "pokemon", "goat", "cheetah", "animal", "worm", "lizard", "fish", "person", "hamster", "chick", "mushroom",
"labrador", "pit bull", "schnauzer", "beetle", "rodent", "feline", "canine", "bovine", "grandaddy long legs", "weevil", "earwig", "silverfish", "android", "cyborg", "wizard", 
"leopard", "elephant", "newt", "jellyfish", "mandrake", "sentient plant", "talking =", "panda", "lizard", "doberman", "beagle", "yorkie", "hare"]

parts = ["ear", "eyes", "nose", "earlobe", "right pinky toe", "patella", "&th eyelash from the right", "entire body", "&th nipple", "foot", "third foot", "top right incisor", 
"tooth", "teeth", "elbow", "trick knee", "bellybutton", "fingernails", "beating heart", "brain", "xiphoid process", "tooth enamel", "skin", "armpits", "foot", "bottom leg", 
"extra rib", "cheek", "butt", "no-no square", "fingies", "upper lip", "glabella", "pituitary gland", "thyroid gland", "tear ducts", "epidermis", "nerve ending", "bunion", 
"amygdala", "hand", "toe", "finger", "eye", "chest", "knee", "lower back", "upper back", "abs", "diaphragm", "tongue", "epiglottis", "vocal folds", "uvula", "stomach", "peep",
"gut", "larynx", "esophagus", "pelvis", "tibia", "phalanges", "skull", "head", "scapula", "spleen", "sacrum", "coccyx", "spine", "funny bone", "cerebral cortex", "brain stem", "neck",
"mouth", "inner thighs", "urethra", "pancreas", "lungs", "gallbladder", "appendix", "rectum", "hand", "chest hands", "limbs", "beard", "foots", "sternum", "callous", "scalp", 
"frenulum", "pie hole", "tush"]

disease = ["$ cancer", "diabetes", "$ swelling", "$ destruction", "$ blockage", "$ parasites", "$ failure", "$ erosion", "$ disease", "$ infection", "AIDS", "claustrophobia", 
"HIV", "MRSA", "food poisoning", "$ depression", "asthma", "anxiety", "alcoholism", "impulsive shopping", "darwinism", "halitosis", "gynecomastia", "gastroenteritis", 
"anal fissures", "^ $ pain"]

theirReplacements = ["their", "its", "his/her", "the", "a", "her", "his", "de", "@'s", "your", "my"]

family = ["mom", "gramma", "grampa", "gramps", "grampie", "g-dizzle", "brother", "sister", "mother", "dad", "stepdad", "step-sister", "step-brother", "stepmom", "cousin",
"great-great-great VV", "uncle", "aunt", "daddy", "mommy", "gruncle", "daughter", "son", "niece", "nephew", "&th cousin, & times removed", "father",
"VV's VV's VV's great VV's great step-VV", "husband", "wife", "&th husband", "&th wife", "family", "sis", "bruv", "honey", "sweetie", "baby", "teenage child", 
"disgruntled employee"]

# ideas: food, quantities

def returnFact():
    fact = getRand(begs) + " " + getRand(parties) + " " + getRand(verbs) + " " + getRand(parties) + getRand(ends)
    #fact = "= = =CCMan ^CC ^CCLand"
    while (fact.find("_") != -1 or fact.find("#") != -1 or fact.find("@") != -1 or fact.find("&") != -1 or fact.find("+") != -1 or fact.find("^") != -1 or fact.find("~") != -1
    or fact.find("|") != -1 or fact.find("=") != -1 or fact.find("%%") != -1 or fact.find("$") != -1 or fact.find("QQ") != -1 or fact.find("VV") != -1):
        if fact.find("_") != -1:
            fact = fact.replace("_", getRand(companies), 1)

        if fact.find("#") != -1:
            fact = fact.replace("#", randYear(), 1)

        if fact.find("@") != -1:
            fact = fact.replace("@", getRand(celebs), 1)

        if fact.find("&") != -1:
            fact = fact.replace("&", randNum(), 1)

        if fact.find("+") != -1:
            fact = fact.replace("+", getRand(places), 1)

        if fact.find("^") != -1:
            if fact.find("^Cc") != -1:
                fact = fact.replace("^Cc", "^CC")
            if fact.find("^CCMan") != -1:
                replacement = getRand(adjectives)
                if replacement.find("^") != -1:
                    replacement = replacement.title().replace(" ", "").replace("'", "").replace("-", "")
                    replacement = replacement.replace("^", "^CC")
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CCMan", replacement.title().replace(" ", "").replace("'", "").replace("-", "") + "Man", 1)
            elif fact.find("^CCLand") != -1:
                replacement = getRand(adjectives)
                if replacement.find("^") != -1:
                    replacement = replacement.title().replace(" ", "").replace("'", "").replace("-", "")
                    replacement = replacement.replace("^", "^CC")
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CCLand", replacement.title().replace(" ", "").replace("'", "").replace("-", "") + "Land", 1)
            elif fact.find("^CC ^CCLand") != -1:
                replacement = getRand(adjectives)
                if replacement.find("^") != -1:
                    replacement = replacement.replace(" ", "-")
                    replacement = replacement.title().replace("'", "")
                    replacement = replacement.replace("^", "^CC")
                    replacement = replacement.replace("$", getRand(parts).title())
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CC ^CCLand", replacement.title().replace(" ", "-").replace("'", "") + " ^CCLand", 1)
            elif fact.find("^CC") != -1:
                replacement = getRand(adjectives)
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", getRand(family), 1).title()
                    fact = fact.replace("^CC", replacement, 1)
                elif replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC").title()  
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CC", replacement.title(), 1)
            else:
                fact = fact.replace("^", getRand(adjectives), 1)

        if fact.find("|") != -1:
            if fact.find("|CC") != -1:
                fact = fact.replace("|CC", getRand(concepts).title(), 1)
            else:
                fact = fact.replace("|", getRand(concepts), 1)

        if fact.find("QQ") != -1:
            fact = fact.replace("QQ", getRand(theirReplacements), 1)

        if fact.find("VV") != -1:
            if fact.find("VVCC") != -1:
                fact = fact.replace("VVCC", getRand(family).title(), 1)
            else:
                fact = fact.replace("VV", getRand(family), 1)

        if fact.find("=") != -1:
            if fact.find("= =") != -1:
                fact = fact.replace("= =", getRand(animals).title().replace(" ", "") + getRand(animals).title().replace(" ", ""))
            if fact.find("=CCMan") != -1:
                fact = fact.replace("=CCMan", getRand(animals).title().replace(" ", "") + "Man")
            if fact.find("=CC") != -1:
                replacement = getRand(animals).title()
                if replacement.find("=") != -1:
                    replacement.replace("=", "=CC")
                fact = fact.replace("=CC", replacement, 1)
            else: 
                fact = fact.replace("=", getRand(animals), 1)

        if fact.find("%%") != -1:
            fact = fact.replace("%%", getRand(parties), 1)

        if fact.find("$") != -1:
            if fact.find("$CC") != -1:
                replacement = getRand(parts)
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC").title()  
                    fact = fact.replace("$CC", replacement, 1)
                else:
                    fact = fact.replace("$CC", replacement.title(), 1)
            else:
                fact = fact.replace("$", getRand(parts), 1)

        if fact.find("~") != -1:
            fact = fact.replace("~", getRand(disease), 1)

    if fact.find(" a ") != -1:
        aCount = fact.count(" a ")
        searchFrom = 0
        while aCount > -1:
            if (fact[fact.find(" a ", searchFrom) + 3] == "a" or fact[fact.find(" a ", searchFrom) + 3] == "e" or fact[fact.find(" a ", searchFrom) + 3] == "i" 
            or fact[fact.find(" a ", searchFrom) + 3] == "o" or fact[fact.find(" a ", searchFrom) + 3] == "u" or fact[fact.find(" a ", searchFrom) + 3] == "A" 
            or fact[fact.find(" a ", searchFrom) + 3] == "E" or fact[fact.find(" a ", searchFrom) + 3] == "I" or fact[fact.find(" a ", searchFrom) + 3] == "O" 
            or fact[fact.find(" a ", searchFrom) + 3] == "U") and not (fact[fact.find(" a ", searchFrom) + 4] == "n" and fact[fact.find(" a ", searchFrom) + 5] == "i" and
            (fact[fact.find(" a ", searchFrom) + 3] == "U" or fact[fact.find(" a ", searchFrom) + 3] == "u")):
                fact = fact[0:searchFrom] + fact[searchFrom:].replace(" a ", " an ", 1)
                aCount -= 1
                searchFrom = fact.find(" an ", searchFrom) + 3
            else:
                aCount -= 1
                searchFrom = fact.find(" a ", searchFrom) + 3

    if fact.find(" ,") != -1:
        fact = fact.replace(" ,", ",")

    if fact.find(" .") != -1:
        fact = fact.replace(" .", ".")

    if fact.find(" !") != -1:
        fact = fact.replace(" !", "!")

    if fact.find("  ") != -1:
        fact = fact.replace("  ", " ")

    if fact.find("yl") != -1 and fact.find("style") == -1 and fact.find("Disneyland") == -1:
        fact = fact.replace("yl", "il")

    if fact.find("a the") != -1 and fact.find("Grandpa") == -1:
        fact = fact.replace("a the", "a")

    if fact.find("ss ") != -1 and fact.find("glass") == -1 and fact.find("ess ") == -1:
        fact = fact.replace("ss ", "ses ")

    if fact.find("ss.") != -1 and fact.find("ess.") == -1:
        fact = fact.replace("ss.", "ses.")

    if fact.find("ss,") != -1 and fact.find("ess,") == -1:
        fact = fact.replace("ss,", "ses,")

    if fact.find("hs") != -1 and fact.find("fuchsia") == -1 and fact.find("Fuchsia") == -1 and fact.find("thighs") == -1 and fact.find("Thighs") == -1:
        fact = fact.replace("hs", "hes")

    if fact.find("lll") != -1:
        fact = fact.replace("lll", "ll")

    if fact.find("xs") != -1:
        fact = fact.replace("xs", "xes")

    if fact.find("lely") != -1:
        fact = fact.replace("lely", "ly")

    return fact

print()
print()
print()
print()
print()
print()
print()
print()

print(returnFact())
