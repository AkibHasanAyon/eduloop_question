import json
import random
import os

def format_place_value(digit, position_from_right, decimals):
    power = position_from_right - decimals
    if power >= 0:
        return str(digit) + "0" * power
    else:
        zeros = abs(power) - 1
        return "0," + "0" * zeros + str(digit)

def format_number(digits, decimals):
    s = "".join(map(str, digits))
    insert_pos = 4 - decimals
    return s[:insert_pos] + "," + s[insert_pos:]

def generate_part(part_id, config, digits):
    from_unit = config["from"]
    to_unit = config["to"]
    decimals = config["decimals"]
    
    number_str = format_number(digits, decimals)
    
    rows = []
    # Process from right to left (as in the demo)
    for i, d in enumerate(reversed(digits)):
        place_value = format_place_value(d, i, decimals)
        # The mathematical beauty of this conversion is that the answers 
        # from right to left always follow the pattern: d, d0, d00, d000
        answer = str(d) + "0" * i
        rows.append({
            "digit": str(d),
            "placeValue": place_value,
            "fromUnit": from_unit,
            "answer": answer,
            "toUnit": to_unit
        })
        
    return {
        "id": part_id,
        "number": number_str,
        "fromUnit": from_unit,
        "toUnit": to_unit,
        "rows": rows
    }

def get_factor(decimals):
    return 10 ** decimals

def generate_questions():
    configs = [
        {"from": "l", "to": "cl", "decimals": 2},
        {"from": "l", "to": "ml", "decimals": 3},
        {"from": "m", "to": "cm", "decimals": 2},
        {"from": "kg", "to": "g", "decimals": 3},
        {"from": "km", "to": "m", "decimals": 3},
        {"from": "g", "to": "mg", "decimals": 3},
        {"from": "m", "to": "mm", "decimals": 3},
        {"from": "cl", "to": "ml", "decimals": 1},
        {"from": "cm", "to": "mm", "decimals": 1},
        {"from": "dl", "to": "ml", "decimals": 2},
        {"from": "dm", "to": "mm", "decimals": 2},
        {"from": "l", "to": "dl", "decimals": 1},
        {"from": "m", "to": "dm", "decimals": 1}
    ]
    
    q_texts = [
        "Wat is elk cijfer waard? Vul in.",
        "Vul de waarde van elk cijfer in.",
        "Bereken de positiewaarde en vul in.",
        "Wat is de waarde van de cijfers in de andere eenheid?"
    ]
    
    questions = []
    seen_combinations = set()
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type67.json")
    
    while len(questions) < 6000:
        c1 = random.choice(configs)
        c2 = random.choice(configs)
        
        # Ensure digits are unique within the same number so the exercise logic works well
        # (if all digits were the same, it would be confusing for the student to match rows to digits)
        digits1 = random.sample(range(1, 10), 4)
        digits2 = random.sample(range(1, 10), 4)
        
        sig = (c1["from"], c1["to"], tuple(digits1), c2["from"], c2["to"], tuple(digits2))
        if sig in seen_combinations:
            continue
            
        seen_combinations.add(sig)
        
        p1 = generate_part("p1", c1, digits1)
        p2 = generate_part("p2", c2, digits2)
        
        # Dynamic hint tailored to the specific units chosen for this question
        hint = f"Tip: Bepaal de positiewaarde van elk cijfer en reken deze om naar de gevraagde eenheid (bijv. 1 {c1['from']} = {get_factor(c1['decimals'])} {c1['to']}"
        if c1["from"] != c2["from"] or c1["to"] != c2["to"]:
            hint += f" of 1 {c2['from']} = {get_factor(c2['decimals'])} {c2['to']})."
        else:
            hint += ")."
            
        questions.append({
            "id": str(len(questions) + 1),
            "type": "type67",
            "subject": "Rekenen",
            "metadata": {
                "question": random.choice(q_texts),
                "hint": hint,
                "data": [p1, p2]
            }
        })
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
