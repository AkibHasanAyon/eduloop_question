import json
import random
import os

def format_number(val):
    # Matches demo format: uses comma only for 10,000 and above.
    if val >= 10000:
        return f"{val:,}"
    return str(val)

def generate_mul():
    expected_A = random.randint(2, 9)
    expected_B = random.randint(2, 9) * 100
    
    # We apply a slight offset so there is something to round
    offset = random.choice([x for x in range(-15, 16) if x != 0])
    actual_B = expected_B + offset
    actual_A = expected_A
    
    ans_value = expected_A * expected_B
    correct_str = f"€{ans_value}"
    
    distractors = [
        f"€{expected_A * (expected_B - 100)}",
        f"€{expected_A * (expected_B + 100)}",
        f"€{(expected_A - 1) * expected_B}",
        f"€{(expected_A + 1) * expected_B}"
    ]
    # Remove negative or zero, and duplicates
    distractors = list(set([d for d in distractors if d != correct_str and "-" not in d and d != "€0"]))
    
    # Need exactly 3 options total
    options = [correct_str] + random.sample(distractors, 2)
    random.shuffle(options)
    
    return {
        "id": f"mul-{actual_A}x{actual_B}",
        "kind": "mul",
        "equation": f"{actual_A} × €{actual_B} = ?",
        "options": options,
        "correct": correct_str,
        "answerValue": ans_value,
        "expectedWork": f"{expected_A} × {expected_B}"
    }

def generate_ratio():
    divisor = random.randint(3, 9)
    expected_q = random.randint(2, 9)
    expected_div = divisor * expected_q
    
    # Apply offset to create a decimal that needs rounding to expected_div
    offset_int = random.choice([x for x in range(-1900, 1900) if abs(x) > 150])
    offset = offset_int / 1000
    actual_div = round(expected_div + offset, 3)
    
    unit = random.choice(["kg", "km", "l", "m", "g"])
    correct_str = f"{expected_q} {unit}"
    
    # Create distractors by shifting the decimal place, matching demo pattern
    possible_distractors = [
        f"{expected_q / 10:g} {unit}",
        f"{expected_q / 100:g} {unit}",
        f"{expected_q / 1000:g} {unit}",
        f"{expected_q * 10:g} {unit}"
    ]
    possible_distractors = list(set([d for d in possible_distractors if d != correct_str]))
    
    options = [correct_str] + random.sample(possible_distractors, 2)
    random.shuffle(options)
    
    actual_div_str = f"{actual_div:g}"
    
    return {
        "id": f"ratio-{actual_div_str.replace('.', '_')}-{divisor}",
        "kind": "ratio",
        "equation": f"{actual_div_str} {unit} : {divisor} = ?",
        "options": options,
        "correct": correct_str,
        "answerValue": expected_q,
        "expectedWork": f"{expected_div} : {divisor}",
        "unitSuffix": unit
    }

def generate_mixed():
    n1_exp = random.randint(4, 9) * 1000
    n2_exp = random.randint(1, n1_exp // 1000 - 1) * 1000
    n3_exp = random.randint(1, 5) * 1000
    
    # Add offsets to create numbers that should be rounded to nearest 1000
    n1_act = n1_exp + random.choice([x for x in range(-150, 150) if abs(x) > 10])
    n2_act = n2_exp + random.choice([x for x in range(-150, 150) if abs(x) > 10])
    n3_act = n3_exp + random.choice([x for x in range(-150, 150) if abs(x) > 10])
    
    ans_value = n1_exp - n2_exp + n3_exp
    correct_str = format_number(ans_value)
    
    possible_distractors = [
        format_number(ans_value - 1000),
        format_number(ans_value + 1000),
        format_number(ans_value - 2000),
        format_number(ans_value + 2000)
    ]
    possible_distractors = list(set([d for d in possible_distractors if d != correct_str and not d.startswith("-") and d != "0"]))
    
    options = [correct_str] + random.sample(possible_distractors, 2)
    random.shuffle(options)
    
    return {
        "id": f"mixed-{n1_act}-{n2_act}+{n3_act}",
        "kind": "mixed",
        # Note the specific unicode minus sign used in the demo equation
        "equation": f"{n1_act} − {n2_act} + {n3_act} = ?",
        "options": options,
        "correct": correct_str,
        "answerValue": ans_value,
        "expectedWork": f"{n1_exp} - {n2_exp} + {n3_exp}"
    }

def generate_questions():
    questions = []
    seen_combinations = set()
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type69.json")
    
    while len(questions) < 6000:
        p1 = generate_mul()
        p2 = generate_ratio()
        p3 = generate_mixed()
        
        sig = (p1["id"], p2["id"], p3["id"])
        if sig in seen_combinations:
            continue
            
        seen_combinations.add(sig)
        
        questions.append({
            "id": str(len(questions) + 1),
            "type": "type69",
            "subject": "Rekenen",
            "metadata": {
                "question": "Hoeveel is het ongeveer?\nSchrijf de som op die je berekent. Kruis daarna het juiste antwoord aan.",
                "hint": "Rond af op handige ronde getallen en noteer je tussenstap. Kruis vervolgens het antwoord aan dat het dichtst in de buurt komt.",
                "data": [p1, p2, p3]
            }
        })
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} type69 questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
