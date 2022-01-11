import re
import lists
import utility

def returnFact():
    fact = utility.getRand(lists.begs) + " " + utility.getRand(lists.parties) + " " + utility.getRand(lists.verbs) + " " + utility.getRand(lists.parties) + utility.getRand(lists.ends)
    #fact = "* gravy, * sauce, * syrup, * concentrate, *CCMan, *CCLand, the World's Smallest *CC." # juicy test fact
    #fact = "*---free *, *CC---Free *CC, less-than-*---flavored, More-Than-*CC---Free" # I like this test too
    fact = "the Duke of *CC." # real test
    while (fact.find("_") != -1 or fact.find("#") != -1 or fact.find("@") != -1 or fact.find("&") != -1 or fact.find("+") != -1 or fact.find("^") != -1 or fact.find("|") != -1 
    or fact.find("=") != -1 or fact.find("%%") != -1 or fact.find("$") != -1 or fact.find("QQ") != -1 or fact.find("VV") != -1 or fact.find("~") != -1 or fact.find("*") != -1
    or fact.find("??") != -1 or fact.find("!!") != -1 or fact.find("!!!") != -1):
        if fact.find("CCCC") != -1:
            fact = fact.replace("CCCC", "CC")
        if fact.find("_") != -1:
            fact = fact.replace("_", utility.getRand(lists.companies), 1)

        if fact.find("#") != -1:
            fact = fact.replace("#", utility.randYear(), 1)

        if fact.find("@") != -1:
            fact = fact.replace("@", utility.getRand(lists.celebs), 1)

        if fact.find("&") != -1:
            fact = fact.replace("&", utility.randNum(), 1)

        if fact.find("+") != -1:
            fact = fact.replace("+", utility.getRand(lists.places), 1)

        if fact.find("^") != -1:
            if fact.find("^Cheese") != -1:
                fact = fact.replace("^", utility.getRand(lists.adjectives).title().replace(" ", "").replace("\'", "").replace("-", ""), 1)
            elif fact.find("^CCMan") != -1:
                replacement = utility.getRand(lists.adjectives)
                if replacement.find("^") != -1:
                    replacement = replacement.title().replace(" ", "").replace("\'", "").replace("-", "")
                    replacement = replacement.replace("^", "^CC")
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CCMan", replacement.title().replace(" ", "").replace("\'", "").replace("-", "") + "Man", 1)
            elif fact.find("^CCLand") != -1:
                replacement = utility.getRand(lists.adjectives)
                if replacement.find("^") != -1:
                    replacement = replacement.title().replace(" ", "").replace("\'", "").replace("-", "")
                    replacement = replacement.replace("^", "^CC")
                    fact = fact.replace("^CC", replacement, 1)
                if replacement.find("*") != -1:
                    replacement = replacement.title().replace(" ", "").replace("\'", "").replace("-", "")
                    replacement = replacement.replace("*", "*CC")
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CCLand", replacement.title().replace(" ", "").replace("\'", "").replace("-", "") + "Land", 1)
            elif fact.find("^CC-^CCLand") != -1:
                replacement = utility.getRand(lists.adjectives)
                if replacement.find("^") != -1:
                    replacement = replacement.replace(" ", "-")
                    replacement = replacement.title().replace("\'", "")
                    replacement = replacement.replace("^", "^CC")
                    replacement = replacement.replace("$", "$CC")
                    replacement = replacement.replace("*", "*CC")
                    fact = fact.replace("^CC", replacement, 1)
                else:
                    fact = fact.replace("^CC-^CCLand", replacement.title().replace(" ", "-").replace("\'", "") + " ^CCLand", 1)
            elif fact.find("^--") != -1:
                replacement = utility.getRand(lists.adjectives)
                if replacement.find(" ") != -1: 
                    replacement = replacement.replace(" ", "-")
                fact = fact.replace("^--", replacement, 1)
            elif fact.find("^CC--") != -1:
                replacement = utility.getRand(lists.adjectives).title()
                if replacement.find(" ") != -1: 
                    replacement = replacement.replace(" ", "-")
                fact = fact.replace("^--", replacement, 1)
            elif fact.find("^CC") != -1:
                replacement = utility.getRand(lists.adjectives)
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
                fact = fact.replace("^", utility.getRand(lists.adjectives), 1)

        if fact.find("|") != -1:
            replacement = utility.getRand(lists.concepts)
            if fact.find("|CC") != -1:
                replacement = replacement.title()
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC")
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*CC")
                if replacement.find("$") != -1:
                    replacement = replacement.replace("$", "$CC")
                if replacement.find("|") != -1:
                    replacement = replacement.replace("|", "|CC")
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC")
                if replacement.find("Vv") != -1:
                    replacement = replacement.replace("Vv", "VVCC")
                if replacement.find("Qq") != -1:
                    replacement = replacement.replace("Qq", "QQCC")
                if replacement.find("%%") != -1:
                    replacement = replacement.replace("%%", "%%CC")
                fact = fact.replace("|CC", replacement, 1)
            else:
                fact = fact.replace("|", utility.getRand(lists.concepts), 1)

        if fact.find("QQ") != -1:
            if fact.find("QQCC") != -1:
                replacement = utility.getRand(lists.possessives)
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", "VVCC", 1)
                    fact = fact.replace("QQCC", replacement, 1)
                else:
                    fact = fact.replace("QQCC", replacement.capitalize(), 1)
            else:
                fact = fact.replace("QQ", utility.getRand(lists.possessives), 1)

        if fact.find("VV") != -1:
            if fact.find("VVCC") != -1:
                replacement = utility.getRand(lists.family)
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
                    elif fact.find("Planet of the ") != -1:
                        replacement = replacement.title()
                        fact = fact.replace("VVCC", replacement, 1)
                    else:
                        if fact.find('\"the ') != -1:
                            fact = fact.replace("VVCC", replacement.title(), 1)
                        else:
                            fact = fact.replace("VVCC", replacement.capitalize(), 1)
                else:
                    if fact.find('\"the ') != -1:
                        fact = fact.replace("VVCC", replacement.title(), 1)
                    else:
                        fact = fact.replace("VVCC", replacement.capitalize(), 1)
            else:
                fact = fact.replace("VV", utility.getRand(lists.family), 1)

        if fact.find("=") != -1:
            if fact.find("= =") != -1:
                fact = fact.replace("= =", utility.getRand(lists.animals).title().replace(" ", "") + utility.getRand(lists.animals).title().replace(" ", ""))
            elif fact.find("=CCMan") != -1:
                replacement = utility.getRand(lists.animals)
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", "VVCC", 1)
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC", 1).replace(" ", "")
                fact = fact.replace("=CCMan", replacement.title().replace(" ", "") + "Man")
            elif fact.find("=CCLand") != -1:
                replacement = utility.getRand(lists.animals)
                if replacement.find("VV") != -1:
                    replacement = replacement.replace("VV", "VVCC", 1)
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC", 1).replace(" ", "")
                fact = fact.replace("=CCLand", replacement.title().replace(" ", "").replace("\'", "").replace("-", "") + "Land", 1)
            elif fact.find("=CC--") != -1:
                replacement = utility.getRand(lists.animals).title()
                if replacement.find(" ") != -1:
                    replacement = replacement.replace(" ", "-")
                fact = fact.replace("=CC--", replacement, 1)
            elif fact.find("=CC") != -1:
                replacement = utility.getRand(lists.animals).title()
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC")
                if ((fact.find("Land") != -1 or fact.find("Man") != -1) and (fact[fact.find("Land") - 1] == "C" or fact[fact.find("Man") - 1] == "C")) and replacement.find(" ") != -1:
                    replacement = replacement.replace(" ", "")
                elif fact.find("---") != -1:
                    replacement = replacement.replace(" ", "-")
                elif replacement.find(" ") != -1:
                    if fact[fact.find("=CC") + 3].isupper():
                        replacement = replacement.replace(" ", "")
                if fact.find("R-Us") != -1:
                    replacement = replacement.title().replace(" ", "-")
                fact = fact.replace("=CC", replacement, 1)
            elif fact.find("=--") != -1:
                replacement = utility.getRand(lists.animals)
                if replacement.find(" ") != -1:
                    replacement = replacement.replace(" ", "-", 1)
                fact = fact.replace("=--", replacement, 1)
            else:
                fact = fact.replace("=", utility.getRand(lists.animals), 1)

        if fact.find("%%") != -1:
            replacement = utility.getRand(lists.parties)
            if fact.find("%%CC") != -1:
                replacement = replacement.title()
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC")
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*CC")
                if replacement.find("$") != -1:
                    replacement = replacement.replace("$", "$CC")
                if replacement.find("|") != -1:
                    replacement = replacement.replace("|", "|CC")
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC")
                if replacement.find("Vv") != -1:
                    replacement = replacement.replace("Vv", "VVCC")
                if replacement.find("Qq") != -1:
                    replacement = replacement.replace("Qq", "QQCC")
                if replacement.find("%%") != -1:
                    replacement = replacement.replace("%%", "%%CC")
                fact = fact.replace("%%CC", replacement, 1)
            else:
                fact = fact.replace("%%", replacement, 1)

        if fact.find("$") != -1:
            replacement = utility.getRand(lists.parts)
            if fact.find("$--") != -1:
                replacement = replacement.replace(" ", "-")
            elif fact.find("$CC--") != -1:
                replacement = replacement.replace(" ", "-").title()
            if fact.find("$CC") != -1:
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC").title()  
                    fact = fact.replace("$CC", replacement, 1)
                elif fact.find("R-Us") != -1:
                    fact = fact.replace("$CC", replacement.title().replace(" ", "-"), 1)
                else:
                    fact = fact.replace("$CC", replacement.title(), 1)
            else:
                fact = fact.replace("$", replacement, 1)

        if fact.find("~") != -1:
            replacement = utility.getRand(lists.disease)
            if fact.find("~CC") != -1:
                replacement = replacement.title()
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC")
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*CC")
                if replacement.find("$") != -1:
                    replacement = replacement.replace("$", "$CC")
                if replacement.find("|") != -1:
                    replacement = replacement.replace("|", "|CC")
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC")
                if replacement.find("Qq") != -1:
                    replacement = replacement.replace("Qq", "QQCC")
                fact.replace("~CC", replacement, 1)
            else:
                fact = fact.replace("~", utility.getRand(lists.disease), 1)

        if fact.find("*") != -1:
            replacement = utility.getRand(lists.foods)
            if fact.find("Man") != -1 and fact[fact.find("Man") - 1] == "C":
                replacement = replacement[:-1].title() if replacement[-1] == "s" else replacement.title()
                if replacement.find("*") != -1:
                    replacement = replacement.replace(" ", "").replace("\'", "").replace("-", "").replace(".", "")
                    replacement = replacement.replace("*", "*CC")
                    fact = fact.replace("*CC", replacement, 1)
                elif replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC").replace(" ", "").replace("\'", "").replace("-", "").replace(".", "")
                    fact = fact.replace("*CC", replacement, 1)
                elif replacement.find("^ ") != -1:
                    replacement = replacement.replace(" ", "").replace("\'", "").replace("-", "").replace(".", "")
                    replacement = replacement.replace("^", "^CC")
                    fact = fact.replace("*CC", replacement, 1)
                else:
                    fact = fact.replace("*CCMan", replacement.replace(" ", "").replace("\'", "").replace("-", "").replace(".", "") + "Man", 1)
            elif fact.find("Land") != -1 and fact[fact.find("Land") - 1] == "C":
                replacement = replacement[:-1].title() if replacement[-1] == "s" else replacement.title()
                if replacement.find("*") != -1:
                    replacement = replacement.replace(" ", "").replace("\'", "").replace("-", "").replace(".", "")
                    replacement = replacement.replace("*Cc", "*CC")
                    replacement = replacement.replace("*", "*CC")
                    fact = fact.replace("*CC", replacement, 1)
                elif replacement.find("=") != -1:
                    replacement = replacement.replace(" ", "").replace("\'", "").replace("-", "").replace(".", "")
                    replacement = replacement.replace("=Cc", "=CC")
                    replacement = replacement.replace("=", "=CC")  
                    fact = fact.replace("*CC", replacement, 1)
                elif replacement.find("^ ") != -1:
                    replacement = replacement.replace(" ", "").replace("\'", "").replace("-", "").replace(".", "")
                    replacement = replacement.replace("^Cc ", "^CC")
                    replacement = replacement.replace("^", "^CC")  
                    fact = fact.replace("*CC", replacement, 1)
                else:
                    fact = fact.replace("*CCLand", replacement.replace(" ", "").replace("\'", "").replace("-", "").replace(".", "") + "Land", 1)
            elif fact.find("*--") != -1:
                replacement = replacement[:-1].replace(".", "") if replacement[-1] == "s" else replacement.replace(".", "")
                replacement = replacement.replace(" ", "-")
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*--")
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=--")
                fact = fact.replace("*--", replacement, 1)

            elif fact.find("*CC--") != -1:
                replacement = replacement[:-1].title().replace(".", "") if replacement[-1] == "s" else replacement.title().replace(".", "")
                replacement = replacement.replace(" ", "-")
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC")
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*CC")
                if replacement.find("$") != -1:
                    replacement = replacement.replace("$", "$CC")
                if replacement.find("|") != -1:
                    replacement = replacement.replace("|", "|CC")
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC--")
                if replacement.find("Qq") != -1:
                    replacement = replacement.replace("Qq", "QQCC")
                fact = fact.replace("*CC--", replacement, 1)
            elif fact.find("*CC") != -1:
                if fact.find("* juice") == -1:
                    replacement = "* juice"
                replacement = replacement[:-1].title() if replacement[-1] == "s" and (fact.find("Prince of *CC") == -1 and fact.find("Duke of *CC") == -1) else replacement.title()
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC")
                    fact = fact.replace("*CC", replacement, 1)
                if fact.find(" *CC ") != -1:
                    fact = fact.replace(" *CC ", " " + replacement.replace("*", "*CC").replace("=", "=CC") + " ", 1)
                elif fact.find(" *CC.") != -1:
                    fact = fact.replace(" *CC.", " " + replacement.replace("*", "*CC").replace("=", "=CC") + ".", 1)
                elif fact.find(" *CC,") != -1:
                    fact = fact.replace(" *CC,", " " + replacement.replace("*", "*CC").replace("=", "=CC") + ",", 1)
                elif fact.find(' *CC\"') != -1:
                    fact = fact.replace(' *CC\"', " " + replacement.replace("*", "*CC").replace("=", "=CC") + '\"', 1)
                elif fact.find(' *CC\'') != -1:
                    fact = fact.replace(' *CC\'', " " + replacement.replace("*", "*CC").replace("=", "=CC") + '\'', 1)
                else:
                    if ((fact.find("Land") != -1 or fact.find("Man") != -1) and (fact[fact.find("Land") - 1] == "C" or fact[fact.find("Man") - 1] == "C")) and replacement.find(" ") != -1:
                        replacement = replacement.replace(" ", "")
                    elif replacement.find(" ") != -1:
                        if fact[fact.find("*CC") + 3] == "-" or fact[fact.find("*CC") -1] == "-":
                            replacement = replacement.replace(" ", "-")
                        elif fact[fact.find("*CC") + 3].isupper():
                            replacement = replacement.replace(" ", "")
                    if replacement.find("*") != -1:
                        replacement = replacement.replace("*", "*CC").replace(" ", "").replace("\'", "").replace(".", "")
                    if replacement.find("=") != -1:
                        replacement = replacement.replace("=", "=CC").replace(" ", "").replace("\'", "").replace(".", "")
                    if replacement.find("^") != -1:
                        replacement = replacement.replace("^", "^CC").replace(" ", "").replace("\'", "").replace(".", "")

                    fact = fact.replace("*CC", replacement, 1)

            elif (fact.find("a hypothetical *") != -1 or fact.find("a *") != -1 or fact.find("* soup") != -1 or fact.find("* grease") != -1 or fact.find("* eggs") != -1 
            or fact.find("* milk") != -1 or fact.find("* syrup") != -1 or fact.find("* oil") != -1 or fact.find("* vinegar") != -1 or fact.find("* meat") != -1 
            or fact.find("* sauce") != -1 or fact.find("* concentrate") != -1 or fact.find("* tea") != -1 or fact.find("* tea") != -1 or fact.find("* pie") != -1
            or fact.find("* cheese") != -1 or fact.find("* butter") != -1 or fact.find("* paste") != -1 or fact.find("* gravy") != -1):
                replacement = replacement[:-1] if replacement[-1] == "s" else replacement
                fact = fact.replace("*", replacement, 1)

            else:
                fact = fact.replace("*", utility.getRand(lists.foods), 1)

        if fact.find("??") != -1:
            if fact.find("??CC") != -1:
                replacement = replacement.title()
                if replacement.find("^") != -1:
                    replacement = replacement.replace("^", "^CC")
                if replacement.find("*") != -1:
                    replacement = replacement.replace("*", "*CC")
                if replacement.find("$") != -1:
                    replacement = replacement.replace("$", "$CC")
                if replacement.find("|") != -1:
                    replacement = replacement.replace("|", "|CC")
                if replacement.find("=") != -1:
                    replacement = replacement.replace("=", "=CC")
                if replacement.find("Qq") != -1:
                    replacement = replacement.replace("Qq", "QQCC")
                fact = fact.replace("??CC", replacement, 1)
            else:
                fact = fact.replace("??", utility.getRand(lists.interjection), 1)

        if fact.find("!!") != -1:
            if fact.find("!!!") != -1:
                fact = fact.replace("!!!", utility.getRand(lists.pronounsObject))
            else:
                fact = fact.replace("!!", utility.getRand(lists.pronounsSubject))

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
            or fact[fact.find(" a ", searchFrom) + 3] == "U"):
                fact = fact[0:searchFrom] + fact[searchFrom:].replace(" a ", " an ", 1)
                aCount -= 1
                searchFrom = fact.find(" an ", searchFrom) + 3
            elif ((fact[fact.find(" a ", searchFrom) + 3] == '"') and (fact[fact.find(" a ", searchFrom) + 4] == "a" 
            or fact[fact.find(" a ", searchFrom) + 4] == "e" or fact[fact.find(" a ", searchFrom) + 4] == "i" or fact[fact.find(" a ", searchFrom) + 4] == "o" 
            or fact[fact.find(" a ", searchFrom) + 4] == "u" or fact[fact.find(" a ", searchFrom) + 4] == "A" or fact[fact.find(" a ", searchFrom) + 4] == "E" 
            or fact[fact.find(" a ", searchFrom) + 4] == "I" or fact[fact.find(" a ", searchFrom) + 4] == "O" or fact[fact.find(" a ", searchFrom) + 4] == "U")):
                fact = fact[0:searchFrom] + fact[searchFrom:].replace(" a ", " an ", 1)
                aCount -= 1
                searchFrom = fact.find(" an ", searchFrom) + 5
            else:
                aCount -= 1
                searchFrom = fact.find(" a ", searchFrom) + 3

    if (fact.find(" an uni") != -1 and fact.find(" an unidentifiable") == -1):
        fact = fact.replace(" an uni", " a uni")

    if fact.find(" an use") != -1:
        fact = fact.replace(" an use", " a use")

    if fact.find(" an uvu") != -1:
        fact = fact.replace(" an uvu", " a uvu")

    if (fact.find(" an Uni") != -1 and fact.find(" an Unidentifiable") == -1):
        fact = fact.replace(" an Uni", " a Uni")

    if fact.find(" an Use") != -1:
        fact = fact.replace(" an Use", " a Use")

    if fact.find(" an Uvu") != -1:
        fact = fact.replace(" an Uvu", " a Uvu")

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

    if fact.find("yl") != -1 and fact.find("style") == -1 and fact.find("Disneyland") == -1 and fact.find("style") == -1 and fact.find("argoyle") == -1:
        fact = fact.replace("yl", "il")

    if fact.find("yly") != -1:
        fact = fact.replace("yly", "ily")

    if fact.find("ys") != -1 and fact.find("hysic") == -1 and fact.find("MySpace") == -1 and fact.find("onkeys") == -1 and fact.find("Cowboys") == -1 and fact.find("oneys") == -1 and fact.find("Abyss") == -1 and fact.find("ays") == -1:
        fact = fact.replace("ys", "ies")

    if fact.find("a the") != -1 and fact.find("Grandpa") == -1:
        fact = fact.replace("a the", "a")

    if fact.find("sss") != -1:
        fact = fact.replace("sss", "sses")

    if fact.find("ippopotamuss") != -1:
        fact = fact.replace("ippopotamuss", "ippopotamuses")

    if fact.find("esophaguss") != -1:
        fact = fact.replace("esophaguss", "esophaguses")

    if fact.find('yess') != -1:
        fact = fact.replace('yess', 'yes')

    if fact[fact.find("iss") + 3] == " " or fact[fact.find("iss") + 3] == "-":
        fact = fact.replace("iss", "ises")

    if fact.find("hs") != -1 and fact.find("highs") == -1 and fact.find("ouths") == -1  and fact.find("oths") == -1 and fact.find("heetahs") == -1 and fact.find("ariahs") == -1:
        fact = fact.replace("hs", "hes")

    if fact.find("lll") != -1:
        fact = fact.replace("lll", "ll")

    if fact.find("xs") != -1:
        fact = fact.replace("xs", "xes")

    if fact.find("'S") != -1:
        fact = fact.replace("'S", "'s")

    if fact.find("lely") != -1 and fact.find("malely") == -1:
        fact = fact.replace("lely", "ly")

    if fact.find("Ly") != -1:
        fact = fact.replace("Ly", "ly")

    if fact.find('S"') != -1:
        fact = fact.replace('S"', 's"')

    if fact.find("yed") != -1 and fact.find("played") == -1 and fact.find("destroyed") == -1:
        fact = fact.replace("yed", "ied")

    if fact.find("s-y") != -1 or fact.find("s-flavored") != -1:
        fact = fact.replace("s-", "-")

    if fact.find("ragu ") != -1 or fact.find("ragu-") != -1 or fact.find("ragu,") != -1 or fact.find("ragu.") != -1:
        fact = fact.replace("ragu", "ragus")

    if fact.find("Abys") != -1 and fact.find("Abyss") == -1:
        fact = fact.replace("Abys", "Abyss")

    if fact.find("s juice") != -1:
        fact = fact.replace("s juice", " juice")

    if fact.find("s dish") != -1:
        fact = fact.replace("s dish", " dish")
    
    if fact.find("les-than") != -1:
        fact = fact.replace("les-than", "less-than")

    if (fact.find("Have you considered the fact that") != -1 or fact.find("What if") != -1 or fact.find("Were you aware that") != -1) and fact.find("...") == -1:
        fact = fact.replace(".", "?")

    if fact.find("it have") != -1 or fact.find("he have") != -1 or fact.find("she have") != -1 or fact.find("somebody have ") != -1:
        fact = fact.replace(" have ", " has ")

    if fact.find("it want ") != -1 or fact.find("he want ") != -1 or fact.find("she want ") != -1 or fact.find("somebody want ") != -1:
        fact = fact.replace(" want ", " wants ")

    if fact.find("it teach ") != -1 or fact.find("he teach ") != -1 or fact.find("she teach ") != -1 or fact.find("somebody teach ") != -1:
        fact = fact.replace(" teach ", " teaches ")

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
    
    if fact.find("have wore") != -1:
        fact = fact.replace("have wore", "have worn")

    if fact.find("been was") != -1:
        fact = fact.replace("been was", "been ")

    if fact.find("people was") != -1:
        fact = fact.replace("people was", "people were")

    if fact.find("have ate") != -1:
        fact = fact.replace("have ate", "have eaten")

    if fact.find("have hired") != -1:
        fact = fact.replace("have hired", "have been hired")

    if fact.find("have took") != -1:
        fact = fact.replace("have took", "have taken")

    if fact.find("have threw") != -1:
        fact = fact.replace("have threw", "have thrown")

    if fact.find("roletariats") != -1:
        fact = fact.replace("roletariats", "roletariat")

    if fact.find("siss") != -1:
        fact = fact.replace("siss", "sisters")

    if fact.find("S ") != -1:
        fact = fact.replace("S ", "s ")

    if fact.find("pss") != -1:
        fact = fact.replace("pss", "pses")

    if fact.find("puss") != -1:
        fact = fact.replace("puss", "puses")

    if fact.find("ruely") != -1:
        fact = fact.replace("ruely", "ruly")

    if fact.find("hocolateily") != -1:
        fact = fact.replace("hocolateily", "hocolately")

    if fact.find("olfs") != -1:
        fact = fact.replace("olfs", "olves")

    if fact.find("liquid liquid") != -1:
        fact = fact.replace("liquid liquid", "liquid")

    if fact.find("water water") != -1:
        fact = fact.replace("water water", "water")

    if fact.find("Water Water") != -1:
        fact = fact.replace("Water Water", "Water")
    
    if fact.find("'S") != -1:
        fact = fact.replace("'S", "'s", 1)

    if fact.find("me's") != -1 and fact.find("Aime's") == -1 and fact.find("Rome's") == -1 and fact.find("Supreme's") == -1:
        fact = fact.replace("me's", "my")

    if fact.find("you's") != -1:
        fact = fact.replace("you's", "your")

    if fact.find("icly ") != -1 and fact.find("chicly") == -1 and fact.find("publicly") == -1:
        fact = fact.replace("icly ", "ically ")

    if fact.find("a proletariat") != -1:
        fact = fact.replace("a proletariat", "the proletariat")

    if fact.find("a Proletariat") != -1:
        fact = fact.replace("a Proletariat", "the Proletariat")

    if fact.find("a proletariat") != -1:
        fact = fact.replace("a bourgeoisie", "the bourgeoisie")

    if fact.find("a Bourgeoisie") != -1:
        fact = fact.replace("a Bourgeoisie", "the Bourgeoisie")

    if fact.find("Creamof") != -1:
        fact = fact.replace("Creamof", "CreamOf")

    if fact.find("ConcentrateConcentrate") != -1:
        fact = fact.replace("ConcentrateConcentrate", "Concentrate")

    if fact.find("PastePaste") != -1:
        fact = fact.replace("PastePaste", "Paste")

    if fact.find("FriedFried") != -1:
        fact = fact.replace("FriedFried", "Fried")

    if fact.find("Deepfried") != -1:
        fact = fact.replace("Deepfried", "DeepFried")

    if fact.find("DeepFriedDeepFried") != -1:
        fact = fact.replace("DeepFriedDeepFried", "DeepFried")

    if fact.find("VinegarVinegar") != -1:
        fact = fact.replace("VinegarVinegar", "Vinegar")

    if fact.find("JuiceJuice") != -1:
        fact = fact.replace("JuiceJuice", "Juice")

    if fact.find("SauceSauce") != -1:
        fact = fact.replace("SauceSauce", "Sauce")

    if fact.find("SyrupSyrup") != -1:
        fact = fact.replace("SyrupSyrup", "syrup")

    if fact.find("GreaseGrease") != -1:
        fact = fact.replace("GreaseGrease", "Grease")

    if fact.find("MeatMeat") != -1:
        fact = fact.replace("MeatMeat", "Meat")

    if fact.find("GravyGravy") != -1:
        fact = fact.replace("GravyGravy", "Gravy")

    if fact.find("SoupSoup") != -1:
        fact = fact.replace("SoupSoup", "Soup")

    if fact.find("MilkMilk") != -1:
        fact = fact.replace("MilkMilk", "Milk")

    if fact.find("EggsEggs") != -1:
        fact = fact.replace("EggsEggs", "Eggs")

    if fact.find("OilOil") != -1:
        fact = fact.replace("OilOil", "Oil")

    if fact.find("TeaTea") != -1:
        fact = fact.replace("TeaTea", "Tea")

    if fact.find("PiePie") != -1:
        fact = fact.replace("PiePie", "Pie")

    if fact.find("VeganVegan") != -1:
        fact = fact.replace("VeganVegan", "Vegan")

    if fact.find("CheeseCheese") != -1:
        fact = fact.replace("CheeseCheese", "Cheese")

    if fact.find("ButterButter") != -1:
        fact = fact.replace("ButterButter", "Butter")

    if fact.find("PickledPickled") != -1:
        fact = fact.replace("PickledPickled", "Pickled")

    if fact.find("BoiledBoiled") != -1:
        fact = fact.replace("BoiledBoiled", "Boiled")

    if fact.find("CreamOfCreamOf") != -1:
        fact = fact.replace("CreamOfCreamOf", "CreamOf")

    if fact.find("Concentrate Concentrate") != -1:
        fact = fact.replace("Concentrate Concentrate", "Concentrate")

    if fact.find("Butter Butter") != -1:
        fact = fact.replace("Butter Butter", "Butter")

    if fact.find("Cheese Cheese") != -1:
        fact = fact.replace("Cheese Cheese", "Cheese")

    if fact.find("Vinegar Vinegar") != -1:
        fact = fact.replace("Vinegar Vinegar", "Vinegar")

    if fact.find("Juice Juice") != -1:
        fact = fact.replace("Juice Juice", "Juice")

    if fact.find("Sauce Sauce") != -1:
        fact = fact.replace("Sauce Sauce", "Sauce")

    if fact.find("Syrup Syrup") != -1:
        fact = fact.replace("Syrup Syrup", "Syrup")

    if fact.find("Grease Grease") != -1:
        fact = fact.replace("Grease Grease", "Grease")

    if fact.find("Meat Meat") != -1:
        fact = fact.replace("Meat Meat", "Meat")

    if fact.find("Paste Paste") != -1:
        fact = fact.replace("Paste Paste", "Paste")

    if fact.find("Gravy Gravy") != -1:
        fact = fact.replace("Gravy Gravy", "Gravy")

    if fact.find("Soup Soup") != -1:
        fact = fact.replace("Soup Soup", "Soup")

    if fact.find("Milk Milk") != -1:
        fact = fact.replace("Milk Milk", "Milk")

    if fact.find("Eggs Eggs") != -1:
        fact = fact.replace("Eggs Eggs", "Eggs")

    if fact.find("Fried Fried") != -1:
        fact = fact.replace("Fried Fried", "Fried")

    if fact.find("Vegan Vegan") != -1:
        fact = fact.replace("Vegan Vegan", "Vegan")

    if fact.find("Pickled Pickled") != -1:
        fact = fact.replace("Pickled Pickled", "Pickled")

    if fact.find("Boiled Boiled") != -1:
        fact = fact.replace("Boiled Boiled", "Boiled")

    if fact.find("Oil Oil") != -1:
        fact = fact.replace("Oil Oil", "Oil")

    if fact.find("Tea Tea") != -1:
        fact = fact.replace("Tea Tea", "Tea")

    if fact.find("Pie Pie") != -1:
        fact = fact.replace("Pie Pie", "Pie")

    if fact.find("Deep-Fried Deep-Fried") != -1:
        fact = fact.replace("Deep-Fried Deep-Fried", "Deep-Fried")

    if fact.find("concentrate concentrate") != -1:
        fact = fact.replace("concentrate concentrate", "concentrate")

    if fact.find("butter butter") != -1:
        fact = fact.replace("butter butter", "butter")

    if fact.find("cheese cheese") != -1:
        fact = fact.replace("cheese cheese", "cheese")

    if fact.find("vinegar vinegar") != -1:
        fact = fact.replace("vinegar vinegar", "vinegar")

    if fact.find("juice juice") != -1:
        fact = fact.replace("juice juice", "juice")

    if fact.find("sauce sauce") != -1:
        fact = fact.replace("sauce sauce", "sauce")

    if fact.find("syrup syrup") != -1:
        fact = fact.replace("syrup syrup", "syrup")

    if fact.find("grease grease") != -1:
        fact = fact.replace("grease grease", "grease")

    if fact.find("meat meat") != -1:
        fact = fact.replace("meat meat", "meat")

    if fact.find("paste paste") != -1:
        fact = fact.replace("paste paste", "paste")

    if fact.find("gravy gravy") != -1:
        fact = fact.replace("gravy gravy", "gravy")

    if fact.find("soup soup") != -1:
        fact = fact.replace("soup soup", "soup")

    if fact.find("milk milk") != -1:
        fact = fact.replace("milk milk", "milk")

    if fact.find("eggs eggs") != -1:
        fact = fact.replace("eggs eggs", "eggs")

    if fact.find("fried fried") != -1:
        fact = fact.replace("fried fried", "fried")

    if fact.find("vegan vegan") != -1:
        fact = fact.replace("vegan vegan", "vegan")

    if fact.find("pickled pickled") != -1:
        fact = fact.replace("pickled pickled", "pickled")

    if fact.find("boiled boiled") != -1:
        fact = fact.replace("boiled boiled", "boiled")

    if fact.find("oil oil") != -1:
        fact = fact.replace("oil oil", "oil")

    if fact.find("tea tea") != -1:
        fact = fact.replace("tea tea", "tea")

    if fact.find("pie pie") != -1:
        fact = fact.replace("pie pie", "pie")

    if fact.find("deep-fried deep-fried") != -1:
        fact = fact.replace("deep-fried deep-fried", "deep-fried")

    if fact.find("\'s\'s") != -1:
        fact = fact.replace("\'s\'s", "s\'")

    if fact.find("s was ") != -1 and fact.find("mountain of") == -1:
        fact = fact.replace("s was ", "s were ")

    if fact.find("you was ") != -1:
        fact = fact.replace("you was ", "you were ")

    if fact.find("wifes") != -1 or fact.find("Wifes") != -1:
        fact = fact.replace("ifes", "ives")

    if fact.find("? ") != -1 and fact.find("attention?") == -1 and fact.find(";)") == -1 and fact.find("know?") == -1 and fact.find(" --") == -1:
        fact = fact.replace("? ", ". ")

    if fact.find("chovie") != -1 and fact.find("chovies") == -1:
        fact = fact.replace("chovie", "chovy")

    if fact.find("berrie") != -1 and fact.find("berries") == -1:
        fact = fact.replace("berrie", "berry")

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

    if fact.find("ummu") != -1 and fact.find("ummus") == -1:
        fact = fact.replace("ummu", "ummus")

    if fact.find("womans") != -1:
        fact = fact.replace("womans", "women")

    if fact.find("AlcoholLand") != -1:
        fact = fact.replace("AlcoholLand", "AlcoHolland")

    if fact.find("s beats") != -1:
        fact = fact.replace("s beats", "s beat")

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

    if fact.find('\"a a') != -1:
        fact = fact.replace('\"a a', '\"an a')

    if fact.find('\"a A') != -1:
        fact = fact.replace('\"a A', '\"an A')

    if fact.find('\"a e') != -1:
        fact = fact.replace('\"a e', '\"an e')

    if fact.find('\"a E') != -1:
        fact = fact.replace('\"a E', '\"an E')

    if fact.find('\"a i') != -1:
        fact = fact.replace('\"a i', '\"an i')

    if fact.find('\"a I') != -1:
        fact = fact.replace('\"a I', '\"an I')

    if fact.find('\"a o') != -1:
        fact = fact.replace('\"a o', '\"an o')

    if fact.find('\"a O') != -1:
        fact = fact.replace('\"a O', '\"an O')

    if fact.find('\"a u') != -1 and fact.find('uni') == -1 and fact.find('use') == -1:
        fact = fact.replace('\"a u', '\"an u')

    if fact.find('\"a U') != -1 and fact.find('Uni') == -1 and fact.find('Use') == -1:
        fact = fact.replace('\"a U', '\"an U')

    if (not fact[0].isupper()) or fact[0] == "\'" or fact[0] == "\"":
        if fact[0] == "\'" or fact[0] == "\"":
            newFact = fact.split(" ")
            newFact[0] = newFact[0].title()
            fact = " ".join(newFact)
        else:
            newFact = fact.split(" ")
            newFact[0] = newFact[0].capitalize()
            fact = " ".join(newFact)

    fact = re.sub("(^|[.?!])\s*([a-zA-Z])", lambda p: p.group(0).upper(), fact)

    if fact.find('A a') != -1:
        fact = fact.replace('A a', 'An a')

    if fact.find('A e') != -1:
        fact = fact.replace('A e', 'An e')

    if fact.find('A i') != -1:
        fact = fact.replace('A i', 'An i')

    if fact.find('A o') != -1:
        fact = fact.replace('A o', 'An o')

    if fact.find('A A') != -1:
        fact = fact.replace('A A', 'An A')

    if fact.find('A E') != -1:
        fact = fact.replace('A E', 'An E')

    if fact.find('A I') != -1 and fact.find('IKEA') == -1:
        fact = fact.replace('A I', 'An I')

    if fact.find('A O') != -1:
        fact = fact.replace('A O', 'An O')

    if fact.find("Us Cellular") != -1:
        fact = fact.replace("Us Cellular", "US Cellular")

    if fact[:4].find('A u') != -1 and fact[:8].find('uni') == -1 and fact[:8].find('use') == -1:
        fact = fact.replace('A u', 'An u', 1)

    if fact[:4].find('A U') != -1 and fact[:8].find('Uni') == -1 and fact[:8].find('Use') == -1:
        fact = fact.replace('A U', 'An U', 1)
    
    if fact.find('n US') != -1:
        fact = fact.replace('n US', ' US')

    if fact.find(' Us ') != -1:
        fact = fact.replace(' Us ', ' US ')

    if fact.find(' with!') != -1:
        fact = fact.replace(' with!', '!')

    return fact

# testing
print()
print()
print()
print()
print()
print()
print()
print()

print(returnFact())
