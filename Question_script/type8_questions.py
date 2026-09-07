import json
import random

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        data_list = []
        item_tuples = set()
        
        # We need 2 distinct items per question (like the demo)
        while len(data_list) < 2:
            # Pick a whole number (z) between 1 and 100
            z = random.randint(1, 100)
            
            # Pick a part (x) between 0 and z
            x = random.randint(0, z)
            
            # Avoid parts being equal so we get 4 distinct equations
            if x * 2 == z:
                continue
                
            y = z - x
            
            # Track uniqueness of the family by storing (whole, smaller part)
            family_tuple = (z, min(x, y))
            
            if family_tuple not in item_tuples:
                item_tuples.add(family_tuple)
                
                answers = [
                    {"a": x, "op": "+", "b": y, "result": z},
                    {"a": y, "op": "+", "b": x, "result": z},
                    {"a": z, "op": "-", "b": x, "result": y},
                    {"a": z, "op": "-", "b": y, "result": x}
                ]
                
                data_list.append({
                    "id": len(data_list) + 1,
                    "numbers": [z, x, y],
                    "answers": answers
                })
        
        # Create combination tuple to ensure question uniqueness
        combination = tuple(sorted(list(item_tuples)))
        
        if combination not in seen:
            seen.add(combination)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type8",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Maak de sommen met deze drie getallen.",
                    "hint": "Gebruik de getallenfamilie om optellen en aftrekken te maken.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type8.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
