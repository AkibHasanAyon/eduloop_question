import json
import random
import os

def make_tokens(prefix, show_word, suffix):
    accepts = [show_word]
    if show_word == "duizend":
        accepts.append("duizenden")
    elif show_word == "miljoen":
        accepts.append("miljoenen")
    elif show_word == "miljard":
        accepts.append("miljarden")
    elif show_word == "miljoenen":
        accepts = ["miljoen", "miljoenen"]
    elif show_word == "duizenden":
        accepts = ["duizend", "duizenden"]
    elif show_word == "miljarden":
        accepts = ["miljard", "miljarden"]
        
    return [
        {"type": "text", "text": prefix},
        {"type": "blank", "accepts": accepts, "show": show_word},
        {"type": "text", "text": suffix}
    ]

def gen_duizend_1():
    N = random.randint(20, 60)
    return make_tokens(f"Een nieuwe gezinsauto kost al snel {N} ", "duizend", " euro.")

def gen_duizend_2():
    N = random.randint(2, 15)
    return make_tokens(f"In ons dorp wonen ongeveer {N} ", "duizend", " mensen.")

def gen_duizend_3():
    N = random.randint(3, 8)
    return make_tokens(f"De hoogste berg is bijna {N} ", "duizend", " meter hoog.")

def gen_duizend_4():
    N = random.randint(40, 80)
    return make_tokens(f"In het voetbalstadion zitten wel {N} ", "duizend", " juichende fans.")

def gen_duizend_5():
    N = random.randint(4, 10)
    return make_tokens(f"De wolharige mammoet stierf {N} ", "duizend", " jaar geleden uit.")

def gen_duizend_6():
    N = random.randint(12, 20)
    return make_tokens(f"De afstand van de Noordpool naar de Zuidpool is ongeveer {N} ", "duizend", " km.")

def gen_duizend_7():
    N = random.randint(100, 300)
    return make_tokens(f"Een hele snelle sportauto kan wel {N} ", "duizend", " euro kosten.")

def gen_duizend_8():
    N = random.randint(300, 800)
    return make_tokens(f"Ongeveer {N} ", "duizend", " Nederlanders gaan op vakantie naar dit land.")

def gen_duizend_9():
    stad = random.choice(["Groningen", "Eindhoven", "Tilburg", "Almere", "Breda", "Nijmegen", "Haarlem"])
    N = random.randint(150, 250)
    return make_tokens(f"In de stad {stad} wonen meer dan {N} ", "duizend", " mensen.")

def gen_duizend_10():
    N = random.randint(40, 45)
    return make_tokens(f"Een marathon is een hardloopwedstrijd van ruim {N} ", "duizend", " meter.")

def gen_duizend_11():
    N = random.choice(["Honderden", "Tientallen"])
    return make_tokens(f"{N} ", "duizenden", " vogels vliegen in de winter naar het zuiden.")

def gen_duizend_12():
    N = random.randint(3, 7)
    return make_tokens(f"Een volwassen olifant weegt ongeveer {N} ", "duizend", " kilo.")

def gen_duizend_13():
    N = random.randint(1, 3)
    return make_tokens(f"Een ticket voor een verre vliegreis kost soms meer dan {N} ", "duizend", " euro.")

def gen_duizend_14():
    return make_tokens("Er zwemmen ", "duizenden", " vissen in dit grote koraalrif.")

def gen_duizend_15():
    N = random.randint(15, 30)
    return make_tokens(f"Een populair concert was binnen {N} ", "duizend", " seconden uitverkocht.")

def gen_duizend_16():
    N = random.randint(2, 6)
    return make_tokens(f"Mijn opa heeft vroeger meer dan {N} ", "duizend", " gulden gespaard.")

def gen_duizend_17():
    N = random.randint(10, 20)
    return make_tokens(f"Er passen wel {N} ", "duizend", " boeken in deze grote bibliotheek.")

def gen_miljoen_1():
    N = random.randint(17, 19)
    return make_tokens(f"Nederland heeft ongeveer {N} ", "miljoen", " inwoners.")

def gen_miljoen_2():
    N = random.randint(10, 15)
    return make_tokens(f"Elk jaar gaan ongeveer {N} ", "miljoen", " Nederlanders op vakantie.")

def gen_miljoen_3():
    return make_tokens("Een gloednieuw vliegtuig kost al snel tientallen ", "miljoenen", " euro's.")

def gen_miljoen_4():
    N = random.randint(2, 5)
    return make_tokens(f"Naar deze spannende wedstrijd keken wel {N} ", "miljoen", " mensen.")

def gen_miljoen_5():
    N = random.randint(140, 160)
    return make_tokens(f"De afstand van de aarde tot de zon is ongeveer {N} ", "miljoen", " kilometer.")

def gen_miljoen_6():
    N = random.randint(10, 30)
    return make_tokens(f"De hoofdprijs in de loterij was maar liefst {N} ", "miljoen", " euro.")

def gen_miljoen_7():
    N = random.randint(20, 100)
    return make_tokens(f"Die bekende YouTuber heeft al meer dan {N} ", "miljoen", " abonnees.")

def gen_miljoen_8():
    N = random.randint(50, 200)
    return make_tokens(f"Dit populaire computerspel is al {N} ", "miljoen", " keer verkocht wereldwijd.")

def gen_miljoen_9():
    N = random.randint(700, 750)
    return make_tokens(f"In het hele werelddeel Europa wonen ongeveer {N} ", "miljoen", " mensen.")

def gen_miljoen_10():
    N = random.randint(60, 70)
    return make_tokens(f"De T-Rex liep ongeveer {N} ", "miljoen", " jaar geleden op aarde rond.")

def gen_miljoen_11():
    N = random.randint(2, 3)
    return make_tokens(f"Je lichaam maakt elke seconde wel {N} ", "miljoen", " nieuwe bloedcellen aan.")

def gen_miljoen_12():
    N = random.randint(14, 16)
    return make_tokens(f"De kern van de zon heeft een temperatuur van zo'n {N} ", "miljoen", " graden.")

def gen_miljoen_13():
    N = random.randint(30, 40)
    return make_tokens(f"In de grote stad Tokyo wonen ruim {N} ", "miljoen", " mensen.")

def gen_miljoen_14():
    return make_tokens("De overheid investeert ", "miljoenen", " in het bouwen van nieuwe fietspaden.")

def gen_miljard_1():
    N = random.randint(7, 9)
    return make_tokens(f"Er leven momenteel ruim {N} ", "miljard", " mensen op aarde.")

def gen_miljard_2():
    N = random.choice(["13", "14"])
    return make_tokens(f"Het universum is naar schatting {N} ", "miljard", " jaar oud.")

def gen_miljard_3():
    return make_tokens(f"De rijkste ondernemers bezitten samen honderden ", "miljarden", " dollars.")

def gen_miljard_4():
    N = random.randint(100, 400)
    return make_tokens(f"Onze melkweg bevat waarschijnlijk meer dan {N} ", "miljard", " sterren.")

def gen_miljard_5():
    N = random.randint(300, 400)
    return make_tokens(f"De regering van Nederland geeft elk jaar ongeveer {N} ", "miljard", " euro uit.")

def gen_miljard_6():
    N = random.randint(80, 90)
    return make_tokens(f"De menselijke hersenen bevatten ongeveer {N} ", "miljard", " zenuwcellen.")

def gen_miljard_7():
    N = random.randint(10, 50)
    return make_tokens(f"Zo'n groot technologiebedrijf maakt soms wel {N} ", "miljard", " euro winst per jaar.")

def gen_miljard_8():
    return make_tokens("De aarde is ongeveer 4,5 ", "miljard", " jaar oud.")

def gen_miljard_9():
    N = random.randint(4, 5)
    return make_tokens(f"In het werelddeel Azië wonen meer dan {N} ", "miljard", " mensen.")

def gen_miljard_10():
    N = random.randint(1, 2)
    return make_tokens(f"Elk jaar worden er wereldwijd ruim {N} ", "miljard", " smartphones verkocht.")

def gen_miljard_11():
    return make_tokens("In een theelepel water zitten meer dan honderd ", "miljard", " watermoleculen.")

def gen_miljard_12():
    N = random.randint(2, 4)
    return make_tokens(f"Het internet wordt dagelijks door meer dan {N} ", "miljard", " mensen gebruikt.")

def gen_miljard_13():
    return make_tokens("Het uitgestrekte heelal is gevuld met vele ", "miljarden", " verre sterrenstelsels.")

generators = [
    gen_duizend_1, gen_duizend_2, gen_duizend_3, gen_duizend_4, gen_duizend_5,
    gen_duizend_6, gen_duizend_7, gen_duizend_8, gen_duizend_9, gen_duizend_10,
    gen_duizend_11, gen_duizend_12, gen_duizend_13, gen_duizend_14, gen_duizend_15,
    gen_duizend_16, gen_duizend_17,
    
    gen_miljoen_1, gen_miljoen_2, gen_miljoen_3, gen_miljoen_4, gen_miljoen_5,
    gen_miljoen_6, gen_miljoen_7, gen_miljoen_8, gen_miljoen_9, gen_miljoen_10,
    gen_miljoen_11, gen_miljoen_12, gen_miljoen_13, gen_miljoen_14,
    
    gen_miljard_1, gen_miljard_2, gen_miljard_3, gen_miljard_4, gen_miljard_5,
    gen_miljard_6, gen_miljard_7, gen_miljard_8, gen_miljard_9, gen_miljard_10,
    gen_miljard_11, gen_miljard_12, gen_miljard_13
]

def generate_questions():
    questions = []
    seen_signatures = set()
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type73.json")
    
    while len(questions) < 6000:
        chosen_gens = random.sample(generators, 8)
        
        left = []
        right = []
        
        for i in range(4):
            left.append({
                "id": f"l{i+1}",
                "tokens": chosen_gens[i]()
            })
            right.append({
                "id": f"r{i+1}",
                "tokens": chosen_gens[i+4]()
            })
            
        # Signature is the exact text of the 8 sentences
        sig_parts = []
        for side in [left, right]:
            for row in side:
                t = row["tokens"]
                sig_parts.append(t[0]["text"] + t[1]["show"] + t[2]["text"])
        sig = tuple(sig_parts)
        
        if sig in seen_signatures:
            continue
        seen_signatures.add(sig)
        
        questions.append({
            "id": str(len(questions) + 1),
            "type": "type73",
            "subject": "Rekenen",
            "metadata": {
                "question": "Welk woord ontbreekt? Kies uit: duizend – miljoen – miljard.",
                "hint": "Let op de grootte van het getal: duizend (1.000), miljoen (1.000.000), miljard (1.000.000.000).",
                "wordBank": [
                    "duizend",
                    "miljoen",
                    "miljard"
                ],
                "data": {
                    "left": left,
                    "right": right
                }
            }
        })
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} type73 questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
