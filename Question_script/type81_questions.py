import json
import random
import os

def generate_type81_questions(num_questions=6000):
    questions = []
    seen_combinations = set()
    
    # Pool of all possible fractions (n, d) with d in 2..10 and n in 1..d
    # Keeping denominator up to 10 to ensure visual strips fit well on screen
    fraction_pool = []
    for d in range(2, 11):
        for n in range(1, d + 1):
            fraction_pool.append((n, d))
            
    while len(questions) < num_questions:
        selected = random.sample(fraction_pool, 4)
        
        signature = tuple(sorted(selected))
        if signature in seen_combinations:
            continue
            
        seen_combinations.add(signature)
        
        data_items = []
        for i, (n, d) in enumerate(selected):
            data_items.append({
                "id": str(i + 1),
                "numerator": n,
                "denominator": d,
                "label": "deel"
            })
            
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type81",
            "subject": "Rekenen",
            "metadata": {
                "question": "Kleur het juiste deel van de strook.",
                "hint": "Klik op de vakjes van de strook om het aangegeven deel te kleuren. Bij 2/4 kleur je 2 van de 4 vakjes.",
                "data": data_items
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type81_questions(6000)
    
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type81.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
