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
    "tway", "shuk", "nax", "sub", "misk", "chap", "land", "ton", "waya", "asel", "fuer", "gaen", "fasha", "bubby", "besma", "golti", "bornsnap", "pumper", "xanathu", "gukky",
    "forma", "gugmunger", "westler", "pango", "beesnog", "hollas", "ackaboob", "tit", "boob", "weewee", "snorp", "flexor", "ublubber", "kacky", "elemen", "yuckma", "kalora", 
    "fabby", "underous"]

    while i < numGoes:
        word += getRand(wordParts)
        i += 1

    if c:
        return word.title()
    else:
        return word

def capitalize(fact, ind):
    split_s = fact.split()
    returnString = ""

    for i in ind:
        try:
            split_s[i] = split_s[i].title()
        except IndexError:
            print(f"Sorry, index is not in range! ({i})")

    for word in split_s:
        returnString += word + " "
        
    return returnString

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
"was cast as @ in a TV show about", "started a Kickstarter campaign to fund the creation of", "gave an unexpected proposal to", "became", "was transformed by a magic = into",
"traveled to + with", "saw a !! game with", "created a ^ sport where you try to recreate", "wore a ^ dress made of", "made * out of", "contracted a ^ case of ~ from",
"was served fine *, which they paid for by pawning", "commit an armed robbery using", "began a criminal enterprise focused upon", "was marooned in + with only", 
"prepared @'s favorite * using", "made a pilot for a show about", "climbed to the top of + using just", "climbed _'s corporate ladder by negotiating using ",
"did groundbreaking research which discovered", "discovered that the secret to time travel is", "stole the secret recipe for * from", "built a factory to produce",
"began a club that focuses on", "conquered QQ intense fear of", "felt a pang of | while mourning the loss of", "peeled the plastic off of a fresh container of",
"threw a hissy fit over", "completely ran out of", "mulled over the idea of", "considered the consequences of endorsing", "gambled away QQ entire supply of",
"publically denounced", "called out @ over QQ prejudice towards", 'debuted QQ new movie called "%%", starring', "did voice acting for a game where you play as",
'starred in the new sitcom "%%" alongside', "donated QQ $ to", ""]

parties = ["a = wearing false teeth", "the President of +", "the most ^ haircut of all time", "your $ (but & inches in length)", "a =", "Flat Earth Theory",
"nuclear war", "white people", "^ people", "^ stool", "a = that " + getRand(verbs) + " @", "the CFO of _", 'a new street gang called "the ^CC VVCCs"', '"the ^CC VVCCs"',
"& push-ups", "a ^, ^ bodybuilder", "a = disguised as @", "a ^ly ^ Halloween costume", "the bathroom", "^ soup", "@'s new $s", "^ *", "a highly ^ strain of ~",
 "a ^CC =CC Champion", "the annual _ dance-off", "Dracula (but if he was from +)", "a ^ly ^ handshake", "an extra set of $s", "the coach of the !!", "a * dish with = meat",
"^ly ^ *", "your ^ dentist", "@'s accountant", "a mirror that makes you look ^ly ^", "gorgonzola cheese", "the CEO of _", "liquid *", "Obama's last name",
"the entire South Pole", "a stairway to +", "the reason you were born", "a ^ resignation letter", "a ^ly ^ almond", "a tree", "The World's Largest *CC", "money",
"barf", "^, ^ *", "a war between =s and =s", "a ^ly ^ corn dog", "a = with a $ that's just too ^", "a = with a =", "a = with too much |", "a = with a ^ $",
"the element of surprise", "a slip of the $", "hard, ^ drugs", "a banana that needs to be peeled & times", "* and *", "a perfect doppelganger for @", "=s' rights",
"the =CC President", "= enthusiasts", "attendees of a $ convention", "the stink eye", "the surface of the sun", "your VV's *", "@'s *", "a ='s $", "a ='s *",
"_-branded swag", "_'s holiday bash", "@", "@'s secret $", "@'s $", "#", "a program that teaches =s to speak +-ese", "@'s raison d'etre", "the !!", "an outbreak of ~",
"one of those small cheeses in wax", "toast", "two =s square-knotted together", "= cruelty", "&th degree murder", "organized crime", "the NYPD", "waaay too much *",
"someone who looks vaguely like @", "*", "^ *", "a mountain of *", "^ gossip", "memes from #", "a ^ baby", "+", "animals", "plants", "dirt", "an active volcano",
"butt", "immortality", "|", "=s", "= enthusiasts", "your $", "the $ of a =", " a = with & extra $s", "^ pants", "QQ VV wearing a @ costume", "QQ VV", "a ^ case of ~",
"@'s VV's favorite VV", "your VV riding a =", "^ chicken nuggets", madeUpWord(False), "a ^ PR campaign", "~", "the asteroid belt", "@'s pet =", "the sun", "the moon",
'a bar trivia team called "the ^CC $CC"', "'the facilities'"]

begs = ["In other news,", "In light of today's events,", "Despite what you may have heard,", "QQCC VV looked me right in the $ and said:", 
"Having been born in the year #,", "Despite a lifelong battle with ~,", "Picture this in your mind for a moment:", "Fun fact:", "Did you know?",
"Have you considered the fact that", "My favorite childhood memory is when", "What's ^ is that mainstream media would have you believe", 
"Once upon a time,", "When you really think about it,", "Yesterday,", "Whenever @ looks ^, it's because", "In the year of Our Lord #,", "My pitch for a hit new TV show:",
"In case you haven't heard yet,", "Through sheer | and |,", "If you ever have a ^ day, just remember", "In an act of |,", "^CCly, due to " + getRand(parties) + ", ",
"If you squint and turn your head ^ly to the side, you'll see that", "Despite having ^ |,", "If a = or @ is attacking you, remember that", 
"Wanna really get somebody's attention? Lay one of these on 'em:", "The German word " + madeUpWord(False) + " describes the situation where", 
"The hidden country of " + madeUpWord(True) + " is where", "To strike a balance between | and |,", "To fill your life with |,", "To fill your $ with |,",
"To impart | into @'s $, declare that", "To make @ feel |,", "Were you aware that", "If you ever visit +, ask the locals about how", "It fills me with | to know that",
"What if", "What they teach in schools now is that", "An unprecendented turn of events:", "When the !! game was canceled,", "This is the reason the !! lost to the !!:",
"If the !! beat the !! today, then", "Due to an outbreak of ~,", "History would never be the same after the day that"]

adjectives = ["dumb", "ugly", "brown", "campy", "proverbial", "obtuse", "arrogant", "swollen", "frightening", "hungry", "diseased", "naked", "squirming", "^-$'d", "surprising",
"short", "rank", "malodorous", "cold", "long", "wide", "clammy", "strong", "stirring", "classy", "high-brow", "fat", "overweight", "wooden", "verdant", "al dente", "chewy", "fudgy",
"pink", "local", "sweaty", "dry", "freeze-dried", "heroic", "suspicious", "explosive", "chunky", "*-flavored", "finely-aged", "expired", "evil", "chaotic", "black", "white", 
"chocolatey", "fast", "intimidating", "drowning", "+-ese", "bland", "problematic", "rootin' tootin'", "blessed", "savage", "room-temperature", "underwhelming", "incompetent",
"overzealoused", "slow", "burnt", "venomous", "uplifting", "beautiful", "juicy", "wet", "damp", "moist", "uncomfortable", "unhealthy", "long-winded", "unfair", "racist", 
"annoying", "pugnacious", "stabbing", "voluptuous", "candid", "quiet", "thin", "skinny", "thick", "dull", "insipid", "twisted", "knarled", "stinky", "sweet", "accidental",
"pompous", "fancy", "well-dressed", "sharp", "red", "bent", "pointed", "heavy", "tense", "intense", "lurid", "mild", "mild-mannered", "terrible", "horrible", "heinous", "passionate",
"cruel", "bumpy", "lumpy", "angry", "livid", "unnerving", "disgusting", "creamy", "woody", "peppery", "piquant", "fashionable", "prudent", "unflattering", "tricky",
"efficient", "complementary", "fortitudinous", "hard", "stiff", "tart", "sour", "acidic", "viscous", "^ly ^",  "demanding", "draining", "clever", "peanut-buttery", "verbose",
"exhausting", "well-behaved", "cute", "stunted", "bad", "good", "great", "boring", "less-than-^", "cringeworthy", "nerdy", "racy", "new", "interesting", "useful", "good",
"elaborate", "live", "cultured", "slightly ^", "overly ^", "not-so-^", "crispy", "crunchy", "pure", "medium-sized", "furtive", "poor", "milquetoast", "pensive", "suave",
"overwhelming", "wrong", "well-written", "happy-go-lucky", "old", "medium-sized", "extra large", "loose", "political", "particular", "thoughtful", "confusing", "mean", "useless",
"final", "innappropriate", "quick", "fluent", "odd", "weird", "unusual", "stupid", "suspicious", "slight", "confident", "exaggerated", "unwavering", "true", "real", "emotional",
"physical", "spiritual", "virtual", "textural", "perfect", "hot", "male", "female", "broken", "stern", "whiny", "indignant", "bright", "massive", "bare", "deft", "swift",
"convenient", "functional", "chic", "united", "greedy", "brash", "proud", "unstoppable", "floppy", "flailing", "full", "positive", "negative", "dirty", "fishy", "filthy",
"candy", "iron", "bronzen", "flaxen", "golden", "rock-hard", "titanium", madeUpWord(False), "moderate", "impressive", "successful", "unsuccessful", "hypothetical", "insufficient",
"frozen", "melted", "acute", "instant", "amateur", "flat", "unprecedented", "uncouth", "unbecoming", "subpar", "violent", "unattractive", "edible", "sociable", "dangerous", 
"fiscal", "invisible", "unexpected", "secret", "cool", "erect", "sexy", "appalling", "horrifying", "contagious", "profound", "colorful", "universal", "unidentifiable", "blue",
"green", "yellow", "purple", "painful", "unpleasant", "unsightly", "foul", "permanent"]

concepts = ["gusto", "fervor", "panache", "restraint", "sense of style", "wherewithall", "curiosity", "warrior's heart", "pride", "luck", "chastity", "charity", "joy", "wonder", 
"passion", "delicacy", "peace", "understanding", "va-va-voom", "swagger", "ingenuity", "self-control", "spirit", "innovation", "clarity", "je ne sais quoi", "gumption", "||",
"love", "nerve", "hutzpah", "cacahuetes", "resolve", "verve", "boldness", "genius", "grit", "determination", "hunger", "rage", "nostalgia", "melancholy", "wistfulness",
"longing", "resilience", "wit", "faith", "honor", "candor", "serenity", "hope", "patience", "kindness", "cheer", "goodwill", "can-do attitude", "spirit", "moxie", "soul",
"joie de vivre", "virtue", "courage", "fire", "selflessness", "pride", "glamour", "$", madeUpWord(False), "culture", "disdain", "apprehension", "hesitancy", "cowardice", 
"evil", "coldness", "underhandedness", "subtlety", "visibility", "sausage", "pancakes", "stupor", "~", "*", "ambition", "fear", "shame", "desperation", "security", "dignity",
"fidelity", "humility", "honesty", "humor", "horror", "ego", "guilt", "kindness", "gentleness"]

ends = [" while @ was still president.", ", using QQ $ to chug a two-liter of liquid *.", " with the | of a ^ =.", " - how ^ is that?", 
", which, ^ly, broke the world record.", ", because that's what ^ | looks like.", ", cause money don't grow on " + getRand(parties) + ".", 
" - however, this angered the envoy from +, starting World War &.", ", and that's a fact.", " with a | far beyond the norm.", " whilst fending off ^ ladies with a ^ spatula.",
" as part of a ^ comedy routine.", ", starting a new dance craze on _'s video-sharing hub.", ", inspiring @ to paint a ^ picture of @.", ", inspiring @ to found _.",
", landing them in ^ water with +.", ", which @ then made a ^ joke about on _'s new social media platform.", ", which jumpstarted @'s | for +'s |.", 
", which makes @ feel like a ^ =.", ", which gave @ ~.", ", which has to be the most ^ way to lose weight.", ", so, ha.", " - thanks a lot, VV!", ". ;)", 
", which took a lot of |.", " to prove to QQ VV that they have ^ |.", ", in hopes that it would make @ notice QQ |.", ", which prompted @ to cancel them on Twitter.", 
" - thank goodness!", " - the three words I'd use to describe this would be ^, ^, and ^!", " - what a ^ time to be ^!", " - what a ^ way to have " + getRand(verbs) + "!",
" by sitting and thinking very hard about %%.", " by the $ of @.", " - now that shows some ^ |!", " - now that takes some |!", " - seems a bit ^ to me...", ", which is SO not ^.", 
", giving everyone ~.", ", utilizing only %% and %%.", ", causing @ to break QQ $.", ", causing @ to instantly grow new $s.", ", after which @ got QQ $ pierced.", 
" - in other words, " + madeUpWord(False) + ".", ", permanently eradicating ~.", ", which gave @ ~.", ", curing @'s severe case of ~.", ", which is how @ and @ met.", 
", which marked @'s entry into politics.", ", earning QQ spot on the !!.", ", which should fill you with |.", ". --@"]

companies = ["Coca-Cola", "Monster Energy", "Frito-Lay", "Nestle", "Google", "Microsoft", "Minecraft", "JP Morgan", "Taco Bell", "Verizon", "US Cellular", "Cingular", 
"VVCC Jeans, Inc", "IBM", "Fatheads", "Fiji Water", "Vance Refrigeration", "Disney", "Fox News", "MSNBC", "Walmart", "IKEA", "Snuggie", "FlexTape", 
"Piggly Wiggly", "Purple Flurp", "Facebook", "Twitter", "Doofenshmirtz Evil, Inc", "Netflix", "Dunder Mifflin", "Apple", "WUPHF", "the Krusty Krab", "the Chum Bucket",
"Doritoes", "Target", "PETA", "Gamestop", "Dogecoin", "Youtube", "Naughty Dog", "CoolMath Games", "McDonald's", "Burger King", "Long John Silver's", 
"Nintendo", "Sony", "Gfuel", "Gamer Goo", "Dunkin Donuts", "Raid: Shadow Legends", "Pixar", "Popeye's", "Papa John's", "Tik Tok", "Buy N' Large", "Activision", "DreamWorks",
"Starbucks", "Raid: Shadow Legends", "Blizzard", "FizzBuzz, Inc", "Los Pollos Hermanos", "Amazon", "SpaceX", "Tesla", "Tumblr", "MySpace", "Reddit", "BitConnect", "The Dentist",
"Cost Cutters", "Dr. Pepper", "Pepsi", "GameStop"]

celebs = ["Dolly Parton", "Robert Pattinson", "the Geico =CC", "the mascot for the !!", "the = from Air Bud", "Keanu Reeves", "the Car =CC", "Chris Pratt AKA Crisp Rat",
"Ben Shapiro", "PewDiePie", "Elvis", "Nickelback", "Guy Fieri", "Gordon Ramsay", "a =", "a ^ =", "a ^ =", "The ^CC Man", "a ^ piece of fruit", "Jennifer Lawrence",
"Michael Scott", "Ghandi", "the Pope", "Jimmy Neutron", "Carl Wheezer", "the Pillsbury Dough Boy", "Jake Paul", "Logan Paul", "you", "your VVCC", "Jeff Dunham", "Olivia Cockburn",
"Dane Cook", "George Washington", "Thomas Jefferson", "Abraham Lincoln", "Plato", "Aristotle", "Leonardo Da Vinci", "John Kennedy", "Isaac Newton", "Albert Einstein", 
"Will Ferrel", "Ariana Grande", "Paul Revere", "Queen Elizabeth", "Christopher Columbus", "JK Rowling", "Pablo Picasso", "Cuddles", "Walt Disney", "Winston Churchill", 
"Elon Musk", "Bill Gates", "Jeff Bezos", "Steve Irwin", "Billy Mays", "the ^ guy from Friends", "the ^ girl from The Office", "Chester Cheeto", "Reggie Fils-Aime",
"Tony the =CC", "=CC Sam", "the Trix =CC", "John Mayer", "Elvis", "the Prince of |CC", "the Prince of *CC", "Mario", "Luigi", "Waluigi", "your favorite =", "Benedict Cumberbatch",
"the Duke of *CC", "Jake the =CC", "the Ice King", "Spongebob Squarepants", "QQ ^ VV", "Will Smith", "Miranda Cosgrove", "Drake and Josh", "the Burger King", 
"CatDog", "= =", "Arnold (from Hey Arnold)", "=CCMan", "The all-new Hyundai Sonata", "The ^CC $CC", "Joker (from Joker)", "Squidward", "Patrick", "Hoobastank",
"Brendan Frasier", "Tommy Wiseau", "Kirby", "Bubsy", "Bigfoot", "Sonic the =CC", "Gurbanguly Berdimuhamedow", "Kim Jong Un", "Xi Jinping", "Moon Jae-in", "Death",
"Reggie Fils-Aime", "Yoshihide Suga", "Grandma", "Grandpa", "^CCMan", "Finn the =CC", "a _ employee", "Warren Buffet", "Billie Eilish", "Videogamedunkey", "Grover Cleveland", 
"Thomas Edison", "Winnie the Pooh", "QuailMan", "Jeffery Bezos", "Vermin Supreme", "Chris Hemsworth", "Chevy Chase", "Dick Van Dyke", "Andy Griffith", "Bob Hope", 
"Regis Philbin", "Dr. Phil", "Hulk Hogan", "Honey Boo-Boo", "Gordon Ramsay", "Bo Burnham", "Obamna", "Conan O'Brian", "Steve Carrell", "James Brown", "Michael Jackson",
"Steve Harvey", "Tim Apple", "The One True =CC", "Peewee Herman", '@ AKA "the ^CC =CC"', "me", "VVCC", "Rongle McDongle", "*CCMan", "George RR Martin", "George Bush",
"Charles Entertainment Cheese", "Larry the *CC", "Bob the *CC", "Gex", "Glover", "Donkey Kong", "Bowser", "Dark Souls"]

places = ["^CC Jersey", "the ^CC States", "Europe", "Russia", "Asia", "Japan", "yo VV's house", "the sock drawer", "Madagascar", "Californ-I-A", "your soul", 
"the corporate offices of _", "the ^CC House", "Yellowstone Park", "Italy", "the Pentagon", "Mount Everest", "an underground city", "the dungeon", "a ^ city",
"China", "Fiji", "India", "Pyongyang", "Seoul", "one of the Koreas", "the states of ^CC and ^CC Dakota", "Hell", "^CC Virginia", "^CC Carolina", "Hell", "the year #",
"^CC York", "^CC Delhi", "Stonehenge", "VV's basement", "the Pacific Ocean", "the Statue of Liberty", madeUpWord(True), "the mouth of a =", "Delfino Plaza", "the 90s",
"a ^ hill of termites", "the realm of the =CC Queen", "$CCs-R-Us", "#", "Disneyland", "Mount Rushmore", "the =CC Kingdom", "^CC Mexico", "the @ estate", "@'s house",
"Tokyo", "Beijing", "Athens", "Ancient Rome", "London", "Austrialia", "^CC Zealand", "Azerbaijan", "Heaven", "the University of +", "^CCLand", "^CC-^CCLand", "Flat Earth",
"*CCLand", "=CCLand", "_'s headquarters"]

animals = ["lion", "cat", "dog", "squid", "mollusk", "clam", "zebra", "axolotl", "rhino", "tiger", "lamb", "octopus", "antelope", "fawn", "llama", "parrot", "whale", 
"geoduck", "barnacle", "snail", "slug", "squirrel", "giraffe", "dingo", "wolf", "coyote", "hyena", "ocelot", "puma", "mountain lion", "fox", "polar bear", "grizzly bear", 
"goldfish", "monkey", "spider monkey", "chimpanzee", "brown bear", "black bear", "lemur", "chihuahua", "flounder", "clownfish", "dolphin", "scallop", "sphinx", "griffin", 
"dragon", "donkey", "unicorn", "yokai", "mouse", "rat", "pig", "cow", "bull", "dove", "shrew", "armadillo", "pangolin", "anteater", "snake", "viper", "cobra", "orangutan", 
"rabbit", "bunny", "jackalope", "chimera", "cerberus", "manticore", "scorpion", "mosquito", "horsefly", "ladybug", "black widow", "brown recluse", "wolf spider", "human",
"dung beetle", "salamander", "firedrake", "wendigo", "wyvern", "sea lion", "pokemon", "goat", "cheetah", "animal", "worm", "lizard", "fish", "person", "hamster", "chick", "mushroom",
"labrador", "pit bull", "schnauzer", "beetle", "rodent", "feline", "canine", "bovine", "grandaddy long legs", "weevil", "earwig", "silverfish", "android", "cyborg", "wizard", 
"leopard", "elephant", "newt", "jellyfish", "mandrake", "sentient plant", "talking =", "panda", "lizard", "doberman", "beagle", "yorkie", "jackrabbit", "VV", "beetle", "tarantula", 
"porpoise", "frog", "pit bull", "eldritch horror", "dingo", "indeterminate bug", "hedgehog", "toucan", "turtle", "lizard", "toad", "tiger", "roach", "insect", "arachnid", 
"cockroach", "butterfly", "caterpillar", "dragonfly", "behemoth", "mole", "mantis", "monster", "moth", "reptile", "amphibian", "mammal", "bird", "flamingo", "penguin",
"centipede", "devil", "demon", "angel", "eagle", "hawk", "falcon", "owl", "parrot", "peacock", "pigeon", "man", "woman"]

parts = ["ear", "eyes", "nose", "earlobe", "right pinky toe", "patella", "&th eyelash from the right", "entire body", "&th nipple", "foot", "third foot", "top right incisor", 
"tooth", "teeth", "elbow", "bellybutton", "fingernail", "brain", "xiphoid process", "tooth enamel", "skin", "armpit", "foot", "bottom leg", 
"spare rib", "cheek", "butt", "no-no square", "fingie", "upper lip", "glabella", "pituitary gland", "thyroid gland", "tear ducts", "epidermis", "nerve ending", "bunion", 
"amygdala", "toe", "finger", "eye", "chest", "knee", "lower back", "upper back", "ab", "diaphragm", "tongue", "epiglottis", "vocal folds", "uvula", "stomach", "peep",
"gut", "larynx", "esophagus", "pelvis", "tibia", "phalange", "skull", "head", "scapula", "spleen", "sacrum", "coccyx", "spine", "funny bone", "cerebral cortex", "brain stem", "neck",
"mouth", "inner thigh", "urethra", "pancreas", "lung", "gallbladder", "appendix", "rectum", "hand", "chest hand", "limb", "beard", "sternum", "callous", "scalp", 
"frenulum", "pie hole", "tush", "teat", "sausage", "ovaries", "nostril", "eardrum", "tummy", "mind", "&th $"]

disease = ["$ cancer", "diabetes", "$ swelling", "$ destruction", "$ blockage", "$ parasites", "$ failure", "$ erosion", "$ disease", "$ infection", "AIDS", "claustrophobia", 
"HIV", "MRSA", "food poisoning", "depression", "asthma", "anxiety", "alcoholism", "impulsive shopping", "darwinism", "halitosis", "gynecomastia", "gastroenteritis", 
"anal fissures", "^ $ pain", "ugliness", "a really weird $", "= $", "pregnancy", "obesity", "sociopathy", "antidisestablishmentarianism", "pneumonoultramicroscopicsilicovolcanoconiosis",
"gastroenteritis", "PMS", "athlete's foot", "complementarianism", "extra limbs", "kidney stones", "broken $", "^-$", "hotdog finger", "count-choculitis", 
"spontaneous dental hydroplosion", "chronic ~", "swine flu", "literally every STI", "loss of $", "diminished |", "vitamin deficiency", "egalitarianism"]

theirReplacements = ["their", "its", "his/her", "the", "a", "her", "his", "de", "@'s", "your", "my", "thine", "y'all's", "VV's"]

family = ["mom", "gramma", "grampa", "gramps", "grampie", "momma", "daddio", "g-dizzle", "brother", "sister", "mother", "dad", "stepdad", "step-sister", "step-brother", "stepmom", 
"cousin", "great-great-great VV", "uncle", "aunt", "daddy", "mommy", "gruncle", "daughter", "son", "niece", "nephew", "&th cousin, & times removed", "father", "b-pizzle",
"VV's VV's VV's great VV's great step-VV", "husband", "wife", "&th husband", "&th wife", "family", "sis", "honey", "sweetie", "baby", "teenage child", "sugar", "cousin",
"disgruntled employee", "great VV", "step-VV", "friend", "homie", "pal"]

foods = ["broccoli", "carrots", "cabbages", "cauliflower", "celery", "creamed corn", "cucumbers", "eggplants", "garlic", "ginger", "green beans", "kale", "lettuce", "mushrooms", "water",
"burritos", "brownies", "cake", "vegetables", "fruit", "apples", "pears", "peaches", "peppers", "pineapples", "pizza", "potatoes", "radishes", "rice", "salad", "soup", "tomatoes",
"lima beans", "spinach", "radicchio", "eggs", "yogurt", "cheese", "sour cream", "flour", "sugar", "salt", "peanuts", "butter", "honey", "bagels", "doughnuts", "cookies", "pie",
"cranberries", "strawberries", "blueberries", "raspberries", "blackberries", "grapes", "grapefruits", "kiwis", "lemons", "limes", "oranges", "plums", "pomegranates", "pumpkins", "hamburgers", 
"hot dogs", "sandwiches", "sausages", "pepperonis", "salamis", "fried chicken", "collard greens", "lettuce", "pasta", "sushi", "fish", "gravy", "pork", "beef", "bacon", "steak",
"alcohol", "lemonade", "cola", "soda", "coffee", "tea", "salsa", "refried beans", "curry", "chili", "chowder", "stew", "mashed potatoes", "tacos", "lo mein", "matcha", "almonds",
"brussels sprouts", "milk", "anchovies", "avocados", "coconuts", "coconut milk", "coconut oil", "coconut water", "custard", "dressing", "egg whites", "nuts", "pudding", "pepper",
"mustard", "ketchup", "mayonnaise", "olive oil", "pickles", "* juice", "fried =", "= oil", "= juice", "= sauce", "boiled =", "baked =", "cooked =", "pancakes", "filet mignon",
"eggs benedict", "beef wellington", "quail", "= grease", "= milk", "syrup", "= concentrate", "cream of *", "cream of =", "= eggs", "pringles", "oreos", "doritos", "mountain dew",
"chocolate", "endives", "parsley", "marjoram", "basil", "cinnamon", "coriander", "dill", "fennel", "pickled *", "pickled =", "* vinegar", "= vinegar", "* syrup", "= syrup", 
"= meat", "dr. pepper"]

teams = ["Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills", "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns", 
"Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
"Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins", "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
"New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Football Team"
]

# ideas: quantities, occasions, colors
# less necessary but still options: sports

def returnFact():
    fact = getRand(begs) + " " + getRand(parties) + " " + getRand(verbs) + " " + getRand(parties) + getRand(ends)
    #fact = '"the ^CC VVCCs"' # test fact
    
    while (fact.find("_") != -1 or fact.find("#") != -1 or fact.find("@") != -1 or fact.find("&") != -1 or fact.find("+") != -1 or fact.find("^") != -1 or fact.find("|") != -1 
    or fact.find("=") != -1 or fact.find("%%") != -1 or fact.find("$") != -1 or fact.find("QQ") != -1 or fact.find("VV") != -1 or fact.find("~") != -1 or fact.find("*") != -1
    or fact.find("!!") != -1):
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
            elif fact.find("^CC-^CCLand") != -1:
                replacement = getRand(adjectives)
                if replacement.find("^") != -1:
                    replacement = replacement.replace(" ", "-")
                    replacement = replacement.title().replace("'", "")
                    replacement = replacement.replace("^", "^CC")
                    replacement = replacement.replace("$", "$CC")
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CC-^CCLand", replacement.title().replace(" ", "-").replace("'", "") + " ^CCLand", 1)
            elif fact.find("^CC") != -1:
                replacement = getRand(adjectives)
                changed = False
                if (len(replacement.split(" ")) > 1 or len(replacement.split("-")) > 1) and fact[0] != "^":
                    replacement = replacement.title()
                    changed = True
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", "VVCC", 1)
                    changed = True
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*CC", 1)
                    changed = True
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC", 1) 
                    changed = True
                if replacement.find("$") != -1:
                    replacement = replacement.replace("$", "$CC", 1)
                    changed = True
                if replacement.find("^CCLy ^") != -1:
                    replacement = replacement.replace("^CCLy ^", "^CCly ^CC")
                    changed = True

                if changed:
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CC", replacement.capitalize(), 1)
            else:
                fact = fact.replace("^", getRand(adjectives), 1)

        if fact.find("|") != -1:
            if fact.find("|CC") != -1:
                fact = fact.replace("|CC", getRand(concepts).capitalize(), 1)
            else:
                fact = fact.replace("|", getRand(concepts), 1)

        if fact.find("QQ") != -1:
            if fact.find("QQCC") != -1:
                replacement = getRand(theirReplacements)
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", "VVCC", 1)
                    fact = fact.replace("QQCC", replacement, 1)
                else:
                    fact = fact.replace("QQCC", replacement.capitalize(), 1)
            else:
                fact = fact.replace("QQ", getRand(theirReplacements), 1)

        if fact.find("VV") != -1:
            if fact.find("VVCC") != -1:
                replacement = getRand(family)
                if len(replacement.split(" ")) > 1:
                    if replacement.split(" ")[0].find("QQ") != -1:
                        replacement = replacement.replace("QQ", "QQCC", 1)
                        fact = fact.replace("VVCC", replacement, 1)
                    elif replacement.split(" ")[0].find("VV") != -1:
                        if fact.find('"the ') != -1:
                            replacement = replacement.title().replace("Vv", "VVCC")
                            fact = fact.replace("VVCC", replacement, 1)
                        else:
                            replacement = replacement.replace("VV", "VVCC")
                            fact = fact.replace("VVCC", replacement, 1)
                    else:
                        if fact.find('"the ') != -1:
                            fact = fact.replace("VVCC", replacement.title(), 1)
                        else:
                            fact = fact.replace("VVCC", replacement.capitalize(), 1)
                else:
                    if fact.find('"the ') != -1:
                        fact = fact.replace("VVCC", replacement.title(), 1)
                    else:
                        fact = fact.replace("VVCC", replacement.capitalize(), 1)
            else:
                fact = fact.replace("VV", getRand(family), 1)

        if fact.find("=") != -1:
            if fact.find("= =") != -1:
                fact = fact.replace("= =", getRand(animals).title().replace(" ", "") + getRand(animals).title().replace(" ", ""))
            if fact.find("=CCMan") != -1:
                replacement = getRand(animals)
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", "VVCC", 1)
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC", 1).replace(" ", "")
                fact = fact.replace("=CCMan", replacement.title().replace(" ", "") + "Man")
            if fact.find("=CCLand") != -1:
                replacement = getRand(animals)
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", "VVCC", 1)
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC", 1).replace(" ", "")
                fact = fact.replace("=CCLand", replacement.title().replace(" ", "").replace("'", "").replace("-", "") + "Land", 1)
            if fact.find("=CC") != -1:
                replacement = getRand(animals).title()
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC")
                if (fact.find("Land") != -1 or fact.find("Man") != -1) and replacement.find(" ") != -1:
                    replacement = replacement.replace(" ", "")
                fact = fact.replace("=CC", replacement, 1)
            else:
                fact = fact.replace("=", getRand(animals), 1)

        if fact.find("%%") != -1:
            fact = fact.replace("%%", getRand(parties), 1)

        if fact.find("$") != -1:
            replacement = getRand(parts)
            if (fact.find("-$'d") != -1 or fact.find("-$CC'd")) and replacement.find(" ") != -1:
                replacement = replacement.replace(" ", "-", 1)
            if fact.find("$CC") != -1:
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC").title()  
                    fact = fact.replace("$CC", replacement, 1)
                if replacement.find("R-Us") != -1:
                    fact = fact.replace("$CC", replacement.title().replace(" ", "-"), 1)
                else:
                    fact = fact.replace("$CC", replacement.title(), 1)
            else:
                fact = fact.replace("$", getRand(parts), 1)

        if fact.find("~") != -1:
            fact = fact.replace("~", getRand(disease), 1)

        if fact.find("*") != -1:
            if fact.find("*Cc") != -1:
                fact = fact.replace("*Cc", "*CC")
            if fact.find("*CCMan") != -1:
                replacement = getRand(foods)
                replacement = replacement[:-1].title() if replacement[-1] == "s" else replacement.title()
                if replacement.find("*") != -1:
                    replacement = replacement.title().replace(" ", "").replace("'", "").replace("-", "")
                    replacement = replacement.replace("*", "*CC")
                    fact = fact.replace("*CC", replacement, 1)
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC").replace(" ", "").replace("'", "").replace("-", "")
                    fact = fact.replace("*CC", replacement, 1)
                else:
                    fact = fact.replace("*CCMan", replacement.title().replace(" ", "").replace("'", "").replace("-", "") + "Man", 1)
            elif fact.find("*CCLand") != -1:
                replacement = getRand(foods)
                replacement = replacement[:-1] if replacement[-1] == "s" else replacement
                if replacement.find("*") != -1:
                    replacement = replacement.title()
                    replacement = replacement.replace(" ", "").replace("'", "").replace("-", "")
                    replacement = replacement.replace("*", "*CC")
                    fact = fact.replace("*CC", replacement, 1)
                if replacement.find("=") != -1:
                    replacement = replacement.title()
                    replacement = replacement.replace(" ", "").replace("'", "").replace("-", "")
                    replacement = replacement.replace("=", "=CC")  
                    fact = fact.replace("*CC", replacement, 1)
                else:
                    fact = fact.replace("*CCLand", replacement.title().replace(" ", "").replace("'", "").replace("-", "") + "Land", 1)
            elif fact.find("*CC") != -1:
                replacement = getRand(foods)
                replacement = replacement[:-1] if replacement[-1] == "s" and fact.find("Prince of *CC") == -1 and fact.find("Duke of *CC") == -1 else replacement
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*CC").title()  
                    fact = fact.replace("*CC", replacement, 1)
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC").title()  
                    fact = fact.replace("*CC", replacement, 1)
                else:
                    fact = fact.replace("*CC", replacement.title(), 1)
            else:
                fact = fact.replace("*", getRand(foods), 1)

        if fact.find("!!") != -1:
            fact = fact.replace("!!", getRand(teams), 1)

        if fact.find("Vv") != -1:
            fact = fact.replace("Vv", "VVCC")

        if fact.find("Vvcc") != -1:
            fact = fact.replace("Vvcc", "VVCC")

        if fact.find("VVcc") != -1:
            fact = fact.replace("VVcc", "VVCC")

        if fact.find("vv") != -1:
            fact = fact.replace("vv", "VV")

        if fact.find("Qq") != -1:
            fact = fact.replace("Qq", "QQCC")

        if fact.find("Qqcc") != -1:
            fact = fact.replace("Qqcc", "QQCC")

        if fact.find("QQcc") != -1:
            fact = fact.replace("QQcc", "QQCC")

        if fact.find("qq") != -1:
            fact = fact.replace("qq", "QQ")

        if fact.find("Cc") != -1:
            fact = fact.replace("Cc", "CC")

        if fact.find("^cc") != -1:
            fact = fact.replace("^cc", "^CC")

        if fact.find("$cc") != -1:
            fact = fact.replace("$cc", "$CC")

        if fact.find("|cc") != -1:
            fact = fact.replace("|cc", "|CC")

        if fact.find("~cc") != -1:
            fact = fact.replace("~cc", "~CC")

        if fact.find("*cc") != -1:
            fact = fact.replace("*cc", "*CC")

        if fact.find("=cc") != -1:
            fact = fact.replace("=cc", "=CC")

    if fact.find(" a ") != -1:
        aCount = fact.count(" a ")
        searchFrom = 0
        while aCount > -1:
            if (fact[fact.find(" a ", searchFrom) + 3] == "a" or fact[fact.find(" a ", searchFrom) + 3] == "e" or fact[fact.find(" a ", searchFrom) + 3] == "i" 
            or fact[fact.find(" a ", searchFrom) + 3] == "o" or fact[fact.find(" a ", searchFrom) + 3] == "u" or fact[fact.find(" a ", searchFrom) + 3] == "A" 
            or fact[fact.find(" a ", searchFrom) + 3] == "E" or fact[fact.find(" a ", searchFrom) + 3] == "I" or fact[fact.find(" a ", searchFrom) + 3] == "O" 
            or fact[fact.find(" a ", searchFrom) + 3] == "U") and not ((fact[fact.find(" a ", searchFrom) + 4] == "s" and fact[fact.find(" a ", searchFrom) + 5] == "e")
            or (fact[fact.find(" a ", searchFrom) + 4] == "n" and fact[fact.find(" a ", searchFrom) + 5] == "i")):
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

    if fact.find(" ?") != -1:
        fact = fact.replace(" ?", "?")

    if fact.find("  ") != -1:
        fact = fact.replace("  ", " ")

    if fact.find("yl") != -1 and fact.find("style") == -1 and fact.find("Disneyland") == -1 and fact.find("style") == -1:
        fact = fact.replace("yl", "il")

    if fact.find("yly") != -1:
        fact = fact.replace("yly", "ily")

    if fact.find("ys") != -1 and fact.find("Mays") == -1 and fact.find("hysical") == -1 and fact.find("MySpace") == -1 and fact.find("onkeys") == -1 and fact.find("Cowboys") == -1 and fact.find("oneys") == -1:
        fact = fact.replace("ys", "ies")

    if fact.find("a the") != -1 and fact.find("Grandpa") == -1:
        fact = fact.replace("a the", "a")

    if fact.find("ss ") != -1 and fact.find("glass ") == -1 and fact.find("ess ") == -1 and fact.find("loss ") == -1:
        fact = fact.replace("ss ", "ses ")

    if fact.find("ss.") != -1 and fact.find("ess.") == -1 and fact.find("eyess.") == -1:
        fact = fact.replace("ss.", "ses.")

    if fact.find("ss,") != -1 and fact.find("ess,") == -1:
        fact = fact.replace("ss,", "ses,")

    if fact.find('ss"') != -1 and fact.find('ess,"') == -1:
        fact = fact.replace('ss"', 'ses"')

    if fact.find("hs") != -1 and fact.find("thighs") == -1 and fact.find("Thighs") == -1 and fact.find("mouths") == -1 and fact.find("Mouths") == -1 and fact.find("moths") == -1 and fact.find("Moths") == -1:
        fact = fact.replace("hs", "hes")

    if fact.find("lll") != -1:
        fact = fact.replace("lll", "ll")

    if fact.find("xs") != -1:
        fact = fact.replace("xs", "xes")

    if fact.find("'S") != -1:
        fact = fact.replace("'S", "'s")

    if fact.find("lely") != -1 and fact.find("malely") == -1:
        fact = fact.replace("lely", "ly")

    if fact.find("yed") != -1 and fact.find("played") == -1 and fact.find("destroyed") == -1:
        fact = fact.replace("yed", "ied")

    if fact.find("s-y") != -1 or fact.find("s-flavored") != -1:
        fact = fact.replace("s-", "-")

    if fact.find("s juice") != -1:
        fact = fact.replace("s juice", " juice")

    if fact.find("s dish") != -1:
        fact = fact.replace("s dish", " dish")
    
    if fact.find("les-than") != -1:
        fact = fact.replace("les-than", "less-than")

    if fact.find("Have you considered the fact that") != -1 or fact.find("What if") != -1 or fact.find("Were you aware that") != -1:
        fact = fact.replace(".", "?")

    if fact.find("have gave") != -1:
        fact = fact.replace("have gave", "have given")

    if fact.find("have wrote") != -1:
        fact = fact.replace("have wrote", "have written")

    if fact.find("have broke") != -1:
        fact = fact.replace("have broke", "have broken")

    if fact.find("have saw") != -1:
        fact = fact.replace("have saw", "have seen")

    if fact.find("have did") != -1:
        fact = fact.replace("have did", "have done")

    if fact.find("have punched") != -1:
        fact = fact.replace("have punched", "have been punched")

    if fact.find("have squirted") != -1:
        fact = fact.replace("have squirted", "have been squirted")

    if fact.find("been was") != -1:
        fact = fact.replace("been was", "been ")

    if fact.find("have ate") != -1:
        fact = fact.replace("have ate", "have eaten")

    if fact.find("have hired") != -1:
        fact = fact.replace("have hired", "have been hired")

    if fact.find("siss") != -1:
        fact = fact.replace("siss", "sisters")

    if fact.find("truely") != -1:
        fact = fact.replace("truely", "truly")

    if fact.find("wolfs") != -1:
        fact = fact.replace("wolfs", "wolves")

    if fact.find("liquid liquid") != -1:
        fact = fact.replace("liquid liquid", "liquid")

    if fact.find("Did you know?") != -1:
        fact = capitalize(fact, [3])
    
    if fact.find("'S") != -1:
        fact = fact.replace("'S", "'s", 1)

    if fact.find("me's") != -1 and fact.find("Aime's") == -1 and fact.find("Rome's") == -1 and fact.find("Supreme's") == -1:
        fact = fact.replace("me's", "my")

    if fact.find("you's") != -1:
        fact = fact.replace("you's", "your")

    if fact.find("icly ") != -1 and fact.find("chicly") == -1:
        fact = fact.replace("icly ", "ically ")

    if fact.find("berrie ") != -1 and fact.find("berrie, ") != -1:
        fact = fact.replace("berrie", "berry")

    if fact.find("berrieM") != -1:
        fact = fact.replace("berrieM", "berryM")

    if fact.find("berrieL") != -1:
        fact = fact.replace("berrieL", "berryL")

    if fact.find("'s's") != -1:
        fact = fact.replace("'s's", "s'")

    if fact.find("s was ") != -1:
        fact = fact.replace("s was ", "s were ")

    if fact.find("s was ") != -1:
        fact = fact.replace("s was ", "s were ")

    if fact.find("wifes") != -1 or fact.find("Wifes") != -1:
        fact = fact.replace("ifes", "ives")

    if fact.find("? ") != -1 and fact.find("attention?") == -1 and fact.find(";)") == -1 and fact.find("know?") == -1 and fact.find(" --") == -1:
        fact = fact.replace("? ", ". ")

    if fact.find("???") != -1:
        fact = fact.replace("???", "?")

    if fact.find("atoe") != -1 and fact.find("atoes") == -1:
        fact = fact.replace("atoe", "ato")

    if fact.find("eache") != -1 and fact.find("eaches") == -1:
        fact = fact.replace("eache", "each")

    if fact.find("dishe") != -1 and fact.find("dishes") == -1:
        fact = fact.replace("dishe", "dish")

    if fact.find("stomaches") != -1:
        fact = fact.replace("stomaches", "stomachs")

    if fact.find("childs") != -1 or fact.find("Childs") != -1:
        fact = fact.replace("hilds", "hildren")

    if fact.find("wiche") != -1 and fact.find("wiches") == -1:
        fact = fact.replace("wiche", "wich")

    if fact.find("womans") != -1:
        fact = fact.replace("womans", "women")

    if fact.find("Creamof") != -1:
        fact = fact.replace("Creamof", "")

    if fact.find("AlcoholLand") != -1:
        fact = fact.replace("AlcoholLand", "AlcoHolland")

    if fact.find("1th") != -1 and fact.find("11th") == -1:
        fact = fact.replace("1th", "1st")

    if fact.find("2th") != -1 and fact.find("12th") == -1:
        fact = fact.replace("2th", "2nd")

    if fact.find("3th") != -1 and fact.find("13th") == -1:
        fact = fact.replace("3th", "3rd")

    if fact.find("1Th") != -1:
        fact = fact.replace("1Th", "1st")

    if fact.find("2Th") != -1:
        fact = fact.replace("2Th", "2nd")

    if fact.find("3Th") != -1:
        fact = fact.replace("3Th", "3rd")

    if fact.find("4Th") != -1:
        fact = fact.replace("4Th", "4th")

    if fact.find("5Th") != -1:
        fact = fact.replace("5Th", "5th")

    if fact.find("6Th") != -1:
        fact = fact.replace("6Th", "6th")

    if fact.find("7Th") != -1:
        fact = fact.replace("7Th", "7th")

    if fact.find("8Th") != -1:
        fact = fact.replace("8Th", "8th")

    if fact.find("9Th") != -1:
        fact = fact.replace("9Th", "9th")

    if fact.find("0Th") != -1:
        fact = fact.replace("0Th", "0th")

    if fact.find("11Th") != -1:
        fact = fact.replace("11Th", "11th")

    if fact.find("12Th") != -1:
        fact = fact.replace("12Th", "12th")

    if fact.find("13Th") != -1:
        fact = fact.replace("13Th", "13th")

    if fact.find("-Ese") != -1:
        fact = fact.replace("-Ese", "-ese")

    if fact.find("Removeds") != -1:
        fact = fact.replace("Removeds", "Removed")
        fact = fact.replace("Cousin", "Cousins")

    if fact.find("'D") != -1:
        fact = fact.replace("'D", "'d")

    if not fact[0].isupper():
        newFact = fact.split(" ")
        newFact[0] = newFact[0].capitalize()
        fact = " ".join(newFact)

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
