import json
import random

def generate_dataset():
    num_questions = 6000
    questions = []
    seen = set()
    
    # Pre-generate all valid (factor1, factor2) combinations
    # factor1: 1-digit number (2 to 9)
    # factor2: 2-digit number (11 to 99, excluding multiples of 10)
    possible_items = []
    for f1 in range(2, 10):
        for f2 in range(11, 100):
            if f2 % 10 == 0:
                continue # Skip numbers ending in 0 (e.g. 20) as they don't have a meaningful units split
            
            b1 = (f2 // 10) * 10
            b2 = f2 % 10
            pp1 = f1 * b1
            pp2 = f1 * b2
            prod = f1 * f2
            
            possible_items.append({
                "factor1": f1,
                "factor2": f2,
                "breakdown1": b1,
                "breakdown2": b2,
                "partialProduct1": pp1,
                "partialProduct2": pp2,
                "product": prod
            })
            
    while len(questions) < num_questions:
        # Pick 2 distinct problems for the screen
        selected = random.sample(possible_items, 2)
        
        # Sort by factor1 and factor2 to create a unique identifier for the entire screen combination
        combination = tuple(sorted([(item["factor1"], item["factor2"]) for item in selected]))
        
        if combination not in seen:
            seen.add(combination)
            
            data_list = []
            for i, item in enumerate(selected):
                # Create a copy and insert 'id' as the first key
                item_copy = {"id": i + 1}
                item_copy.update(item)
                data_list.append(item_copy)
                
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type24",  # Note: Corrected from 'type5' in the demo to 'type24'
                "subject": "Rekenen",
                "metadata": {
                    "question": "Reken de vermenigvuldiging uit met de tussenstappen.",
                    "hint": "Splits het getal in tientallen en eenheden.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type24.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
