import json
import random

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    # Pre-generate all 48 possible analog clock faces 
    # (12 hours * 4 quarter-intervals)
    possible_items = []
    for h in range(1, 13):
        for m in [0, 15, 30, 45]:
            possible_items.append((h, m))
            
    while len(questions) < num_questions:
        # Pick 4 distinct times for the screen
        selected = random.sample(possible_items, 4)
        
        # Sort to create a unique combination key for the entire screen
        combination = tuple(sorted(selected))
        
        if combination not in seen:
            seen.add(combination)
            
            data_list = []
            for i, (h, m) in enumerate(selected):
                data_list.append({
                    "id": i + 1,
                    "hour": h,
                    "minute": m
                })
                
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type26",  # Corrected from 'type5' in the demo
                "subject": "Rekenen",
                "metadata": {
                    "question": "Hoe laat is het op de klok?",
                    "hint": "Kijk goed naar de grote en kleine wijzer.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type26.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
