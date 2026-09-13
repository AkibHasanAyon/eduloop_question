import json
import random
import os

def generate_type82_questions(num_questions=6000):
    questions = []
    seen_combinations = set()
    
    # Pool of all possible fractions (n, d) with d in 2..12 and n in 1..d
    # 2 to 12 are very common denominators for visual circle fraction problems
    fraction_pool = []
    for d in range(2, 13):
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
                "id": f"c{i + 1}",
                "numerator": n,
                "denominator": d,
                "label": "deel"
            })
            
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type82",
            "subject": "Rekenen",
            "metadata": {
                "question": "Welk deel is gekleurd?",
                "hint": "Tel hoeveel gelijke stukken de cirkel heeft (dat is de noemer) en hoeveel stukken er gekleurd zijn (dat is de teller).",
                "data": data_items
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type82_questions(6000)
    
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type82.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
