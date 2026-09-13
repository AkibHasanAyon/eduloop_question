import json
import random
import os
import itertools

# We expand the contexts to reach 6000 unique questions while preserving mathematical sense
contexts = [
    {"div": 7, "unit": "dagen", "container_sg": "week", "container_pl": "weken", "desc": "Er zitten 7 dagen in 1 week. Hoeveel weken zijn dat?"},
    {"div": 12, "unit": "maanden", "container_sg": "jaar", "container_pl": "jaren", "desc": "Er zitten 12 maanden in 1 jaar. Hoeveel jaren zijn dat?"},
    {"div": 6, "unit": "flessen", "container_sg": "krat", "container_pl": "kratten", "desc": "Er zitten 6 flessen in 1 krat. Hoeveel kratten zijn dat?"},
    {"div": 8, "unit": "koekjes", "container_sg": "pak", "container_pl": "pakken", "desc": "Er zitten 8 koekjes in 1 pak. Hoeveel pakken zijn dat?"},
    {"div": 4, "unit": "ballen", "container_sg": "koker", "container_pl": "kokers", "desc": "Er zitten 4 ballen in 1 koker. Hoeveel kokers zijn dat?"},
    {"div": 5, "unit": "snoepjes", "container_sg": "zakje", "container_pl": "zakjes", "desc": "Er zitten 5 snoepjes in 1 zakje. Hoeveel zakjes zijn dat?"},
    {"div": 9, "unit": "spelers", "container_sg": "team", "container_pl": "teams", "desc": "Er passen 9 spelers in 1 team. Hoeveel teams zijn dat?"},
    {"div": 3, "unit": "tennisballen", "container_sg": "blik", "container_pl": "blikken", "desc": "Er zitten 3 tennisballen in 1 blik. Hoeveel blikken zijn dat?"},
    {"div": 10, "unit": "eieren", "container_sg": "doos", "container_pl": "dozen", "desc": "Er zitten 10 eieren in 1 doos. Hoeveel dozen zijn dat?"},
    {"div": 2, "unit": "schoenen", "container_sg": "paar", "container_pl": "paren", "desc": "Er zitten 2 schoenen in 1 paar. Hoeveel paren zijn dat?"},
    {"div": 11, "unit": "spelers", "container_sg": "elftal", "container_pl": "elftallen", "desc": "Er zitten 11 spelers in 1 elftal. Hoeveel elftallen zijn dat?"}
]

def generate_questions():
    questions = []
    seen_signatures = set()
    
    # base_tens: 10, 20, 30, 40, 50, 60, 70, 80, 90
    base_tens = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    
    # We need 4 sorted remainders out of [1..9] per question
    # This gives exactly 126 combinations per base per context
    remainder_combinations = list(itertools.combinations(range(1, 10), 4))
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type72.json")
    
    while len(questions) < 6000:
        ctx = random.choice(contexts)
        base = random.choice(base_tens)
        rems = random.choice(remainder_combinations)
        
        # signature ensures we don't repeat the same logic parameters
        sig = (ctx["div"], base, rems)
        if sig in seen_signatures:
            continue
        seen_signatures.add(sig)
        
        div = ctx["div"]
        
        data = []
        for i, r in enumerate(rems):
            total_items = (base * div) + (r * div)
            total_containers = base + r
            
            # Using 'days' and 'weeks' as keys to match the demo's exact frontend expectations,
            # but putting our dynamic context strings in the values.
            row = {
                "id": f"r{i+1}",
                "days": f"{total_items} {ctx['unit']}",
                "partialSum": f"{total_items}:{div}",
                "helpSum1": {
                    "text": f"{base * div}:{div}",
                    "answer": str(base)
                },
                "helpSum2": {
                    "text": f"{r * div}:{div}",
                    "answer": str(r)
                },
                "weeks": str(total_containers),
                "isExample": (i == 0)
            }
            data.append(row)
            
        # Format the hint using the second row's remainder to match the demo logic
        ex_r = rems[1]
        hint = f"Splits het getal in een tiental (zoals {base * div} : {div} = {base}) en een restant (zoals {ex_r * div} : {div} = {ex_r}). Tel de uitkomsten bij elkaar op."
        
        questions.append({
            "id": str(len(questions) + 1),
            "type": "type72",
            "subject": "Rekenen",
            "metadata": {
                "question": "Welke som hoort erbij? Vul de tabel in.",
                "context": ctx["desc"],
                "hint": hint,
                "headers": [
                    "",
                    "deelsom",
                    "hulpsommen",
                    f"aantal {ctx['container_pl']}"
                ],
                "data": data
            }
        })
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} type72 questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
