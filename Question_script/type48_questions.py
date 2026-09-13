import json
import random
import os

def generate_questions():
    questions = []
    
    question_texts = [
        "Bereken de oude prijs. Vul de tabel in.",
        "Wat was de oorspronkelijke prijs? Vul de tabellen aan.",
        "Bepaal de oude prijs en vul deze in.",
        "Reken de oude prijs uit en vul de tabellen in.",
        "Hoeveel kostte het artikel eerst? Reken het uit en vul de tabel in."
    ]
    
    # Generate prices between 20 and 1500 (multiples of 10)
    old_prices = list(range(20, 1510, 10))
    # Common discounts
    discounts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 75, 80, 90]
    
    valid_pairs = []
    for op in old_prices:
        for d in discounts:
            np = op * (100 - d) / 100.0
            # Ensure the new price is a clean integer
            if np.is_integer():
                valid_pairs.append({
                    "oldPrice": int(op),
                    "newPrice": int(np),
                    "discount": d
                })
                
    # Ensure combinations of 8 pairs are unique
    seen_combinations = set()
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type48.json")
    
    while len(questions) < 6000:
        # We need 8 rows per question (4 for left table, 4 for right table)
        selected = random.sample(valid_pairs, 8)
        
        # Sort based on newPrice and discount to generate a unique signature for the set of 8
        sig = tuple(sorted((p['newPrice'], p['discount']) for p in selected))
        if sig in seen_combinations:
            continue
            
        seen_combinations.add(sig)
        
        q_text = random.choice(question_texts)
        
        # Pick one pair to use in the hint example
        ex = random.choice(selected)
        hint = f"Gebruik: oude prijs = nieuwe prijs ÷ (1 − korting/100). Bijvoorbeeld: € {ex['newPrice']},- bij {ex['discount']}% korting was € {ex['oldPrice']},-."
        
        left_rows = selected[:4]
        right_rows = selected[4:]
        
        q_data = {
            "id": str(len(questions) + 1),
            "type": "type48",
            "subject": "Rekenen",
            "metadata": {
                "question": q_text,
                "hint": hint,
                "data": [
                    {
                        "id": "left",
                        "rows": [{"newPrice": r["newPrice"], "discount": r["discount"]} for r in left_rows]
                    },
                    {
                        "id": "right",
                        "rows": [{"newPrice": r["newPrice"], "discount": r["discount"]} for r in right_rows]
                    }
                ]
            }
        }
        
        questions.append(q_data)
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
