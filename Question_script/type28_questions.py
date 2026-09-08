import json
import random

def generate_dataset():
    num_questions = 6000
    questions = []
    seen = set()
    
    # Generate all valid improper fractions
    # Denominator (D) between 2 and 12 (standard for primary school)
    # Whole number part (W) between 1 and 5
    # Remainder (R) between 1 and D-1 to ensure a fractional part exists
    possible_items = []
    for d in range(2, 13):
        for w in range(1, 6):
            for r in range(1, d):
                n = w * d + r
                expected = f"{w} {r}/{d}"
                possible_items.append({
                    "numerator": n,
                    "denominator": d,
                    "expected": expected
                })
                
    while len(questions) < num_questions:
        # Pick 12 distinct fractions for the screen (3x4 grid)
        selected = random.sample(possible_items, 12)
        
        # Create a unique key for the combination of 12 fractions
        combination = tuple(sorted([(item["numerator"], item["denominator"]) for item in selected]))
        
        if combination not in seen:
            seen.add(combination)
            
            data_list = []
            for i, item in enumerate(selected):
                item_copy = {"id": i + 1}
                item_copy.update(item)
                data_list.append(item_copy)
                
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type28",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Haal de helen eruit.",
                    "hint": "Zet de onechte breuk om naar een gemengde breuk.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type28.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
