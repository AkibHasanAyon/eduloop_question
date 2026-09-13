import json
import random
import os

def generate_questions():
    questions = []
    
    question_texts = [
        "Reken uit.",
        "Bereken de antwoorden.",
        "Los de vermenigvuldigingen op.",
        "Wat is de uitkomst?",
        "Reken de bedragen en gewichten uit."
    ]
    
    mults = list(range(2, 10))
    int_parts = list(range(0, 15))
    # Wide variety of common decimal fractions used in currency and weight
    frac_parts = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.99]
    
    pool = []
    for m in mults:
        for i in int_parts:
            for f in frac_parts:
                v = i + f
                if v <= 0: continue
                exp = round(m * v, 2)
                
                # Make integer if it's a whole number
                val_clean = int(v) if float(v).is_integer() else round(v, 2)
                exp_clean = int(exp) if float(exp).is_integer() else round(exp, 2)
                
                pool.append({
                    "mult": m,
                    "val": val_clean,
                    "expected": exp_clean
                })
                
    seen_combinations = set()
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type50.json")
    
    def fmt(num):
        if isinstance(num, (int, float)) and float(num).is_integer():
            return f"{int(num)}"
        return f"{num:.2f}"
    
    while len(questions) < 6000:
        selected = random.sample(pool, 12)
        
        # Sort to create a unique signature for this set of 12 questions
        sig = tuple(sorted((item["mult"], item["val"]) for item in selected))
        if sig in seen_combinations:
            continue
            
        seen_combinations.add(sig)
        
        left_items = selected[:6]
        right_items = selected[6:]
        
        # Pick a hint item that has both a non-zero integer part and a non-zero decimal part 
        # so the hint example makes sense.
        suitable = [item for item in left_items if int(item["val"]) > 0 and round(item["val"] - int(item["val"]), 2) > 0]
        hint_item = random.choice(suitable) if suitable else left_items[0]
        
        m = hint_item["mult"]
        v = hint_item["val"]
        exp = hint_item["expected"]
        
        int_p = int(v)
        frac_p = round(v - int_p, 2)
        step1_1 = m * int_p
        step1_2 = round(m * frac_p, 2)
        
        # Generates: "Splits het getal in gehelen en decimalen als dat helpt. Bijvoorbeeld: 4 × € 4.60 = 4 × € 4 + 4 × € 0.60 = € 16 + € 2.40 = € 18.40."
        hint = f"Splits het getal in gehelen en decimalen als dat helpt. Bijvoorbeeld: {m} × € {fmt(v)} = {m} × € {fmt(int_p)} + {m} × € {fmt(frac_p)} = € {fmt(step1_1)} + € {fmt(step1_2)} = € {fmt(exp)}."
        
        q_data = {
            "id": str(len(questions) + 1),
            "type": "type50",
            "subject": "Rekenen",
            "metadata": {
                "question": random.choice(question_texts),
                "hint": hint,
                "data": {
                    "left": [{"mult": r["mult"], "price": r["val"], "expected": r["expected"]} for r in left_items],
                    "right": [{"mult": r["mult"], "kg": r["val"], "expected": r["expected"]} for r in right_items]
                }
            }
        }
        
        questions.append(q_data)
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
