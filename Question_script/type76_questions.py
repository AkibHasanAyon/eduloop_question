import json
import random
import os

def format_answer(val):
    # Round to 3 decimal places
    rounded = round(val, 3)
    # Format to string, strip trailing zeros and the decimal point if it's a whole number
    ans_str = f"{rounded:.3f}".rstrip('0').rstrip('.')
    if ans_str == "":
        ans_str = "0"
    return ans_str

def generate_type76_questions(num_questions=6000):
    questions = []
    seen_combinations = set()
    
    # Common denominators for fractions
    denominators = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 24, 25, 30, 40, 50, 75, 100]
    
    # Generate a pool of simple fractions (no whole number)
    simple_fractions = []
    for b in denominators:
        for a in range(1, b):
            simple_fractions.append((0, a, b))
            
    # Generate a pool of mixed fractions (with a whole number)
    mixed_fractions = []
    # Whole numbers 1 to 5 for most denominators
    for w in range(1, 6):
        for b in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20]:
            for a in range(1, b):
                mixed_fractions.append((w, a, b))
    # Add some mixed numbers with larger denominators
    for w in range(1, 4):
        for b in [25, 30, 40, 50, 75]:
            for a in range(1, b):
                mixed_fractions.append((w, a, b))
                
    all_possible = simple_fractions + mixed_fractions
    
    while len(questions) < num_questions:
        # We need 10 items per question
        selected = random.sample(all_possible, 10)
        
        # Sort to create a unique signature (order independent)
        signature = tuple(sorted(selected))
        
        if signature in seen_combinations:
            continue
            
        seen_combinations.add(signature)
        
        data_items = []
        for i, (w, a, b) in enumerate(selected):
            if w == 0:
                frac_str = f"{a}/{b}"
                val = a / b
            else:
                frac_str = f"{w} {a}/{b}"
                val = w + (a / b)
                
            ans_str = format_answer(val)
            
            data_items.append({
                "id": i + 1,
                "fraction": frac_str,
                "answer": ans_str
            })
            
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type76",
            "subject": "Rekenen",
            "metadata": {
                "question": "Schrijf als kommagetal. Gebruik eventueel een rekenmachine.",
                "hint": "Deel de teller door de noemer (bijvoorbeeld 6 : 9 ≈ 0,667). Rond zo nodig af op 3 decimalen.",
                "data": data_items
            }
        }
        
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type76_questions(6000)
    
    # Output path
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type76.json"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
