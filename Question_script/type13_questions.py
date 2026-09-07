import json
import random

def generate_dataset():
    num_questions = 6000
    questions = []
    seen = set()
    
    # Generate all possible valid items.
    # We use hours 1 to 12 and add a difference of 1 to 11 hours.
    # This ensures 132 distinct items, resulting in 8646 possible pairs of 2 items,
    # which is well over the 3000 distinct questions needed.
    possible_items = []
    for h1 in range(1, 13):
        for diff in range(1, 12):
            h2 = h1 + diff
            if h2 > 12:
                h2 -= 12
            possible_items.append((h1, h2, diff))
            
    while len(questions) < num_questions:
        # We need 2 distinct items per question, like in the demo
        items = random.sample(possible_items, 2)
        
        # Sort items to ensure order doesn't matter for the unique combination
        combination = tuple(sorted(items))
        
        if combination not in seen:
            seen.add(combination)
            
            data_list = []
            for i, (h1, h2, diff) in enumerate(items):
                data_list.append({
                    "id": i + 1,
                    "clock": {
                        "hour": h1,
                        "minute": 0
                    },
                    "boxTime": {
                        "hour": h2,
                        "minute": 0
                    },
                    "answer": diff
                })
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type13",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Hoeveel uur later is het?",
                    "hint": "Tel de uren vooruit vanaf de kloktijd tot de doeltijd.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type13.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
