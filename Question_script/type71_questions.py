import json
import random
import os

def generate_part(part_id):
    op = random.choice(["+", "-"])
    start = random.randint(11, 99)
    
    if op == "+":
        change = random.randint(1, 10) * 5  # Produces 5, 10, 15... 50
        total = start + change
        templates = [
            "Ik spaar er {X} euro bij.",
            "Ik krijg {X} euro van oma.",
            "Ik verdien {X} euro met klusjes.",
            "Voor mijn verjaardag krijg ik {X} euro.",
            "Ik vind {X} euro op straat."
        ]
        text = random.choice(templates).replace("{X}", str(change))
        return {
            "id": part_id,
            "start": start,
            "saved": change,
            "op": "+",
            "total": total,
            "text": text
        }
    else:
        # For subtraction, make sure we only spend what we have
        # and prefer nice round numbers for the change, like in the demo
        valid_changes = [x for x in range(5, start) if x % 5 == 0]
        if not valid_changes:
            change = random.randint(1, start - 1)
        else:
            change = random.choice(valid_changes)
            
        total = start - change
        templates = [
            "Ik koop een boek voor {X} euro.",
            "Ik geef {X} euro uit aan een spel.",
            "Ik koop snoep voor {X} euro.",
            "Een bioscoopkaartje kost {X} euro.",
            "Ik betaal {X} euro voor een cadeautje.",
            "Ik koop een cadeau voor {X} euro."
        ]
        text = random.choice(templates).replace("{X}", str(change))
        return {
            "id": part_id,
            "start": start,
            "spent": change,
            "op": "-",
            "total": total,
            "text": text
        }

def generate_questions():
    questions = []
    seen_signatures = set()
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type71.json")
    
    while len(questions) < 6000:
        p1 = generate_part("r1")
        p2 = generate_part("r2")
        p3 = generate_part("r3")
        p4 = generate_part("r4")
        
        # We define a signature based on the math operations to guarantee unique scenarios
        sig = (
            p1["start"], p1.get("saved", p1.get("spent")), p1["op"],
            p2["start"], p2.get("saved", p2.get("spent")), p2["op"],
            p3["start"], p3.get("saved", p3.get("spent")), p3["op"],
            p4["start"], p4.get("saved", p4.get("spent")), p4["op"]
        )
        
        if sig in seen_signatures:
            continue
            
        seen_signatures.add(sig)
        
        questions.append({
            "id": str(len(questions) + 1),
            "type": "type71",
            "subject": "Rekenen",
            "metadata": {
                "question": "Hoeveel heb ik nu? Reken uit.",
                "hint": "Kijk goed of er geld bijkomt (sparen/krijgen) of afgaat (kopen/uitgeven). Reken daarna het nieuwe totaalbedrag uit.",
                "data": [p1, p2, p3, p4]
            }
        })
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} type71 questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
