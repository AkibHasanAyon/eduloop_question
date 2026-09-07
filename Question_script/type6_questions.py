import json
import random

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        data_list = []
        item_tuples = []
        
        # Generate 2 items per question (as in the demo)
        for i in range(1, 3):
            # result between 5 and 100 to ensure we can pick up to 5 distinct pairs
            result = random.randint(5, 100)
            
            # number of pairs between 3 and 5
            num_pairs = random.randint(3, 5)
            
            # pick distinct fixed values
            fixed_values = random.sample(range(result + 1), num_pairs)
            
            pairs = []
            pair_tuples = []
            
            for fixed in fixed_values:
                expected = result - fixed
                inputSide = random.choice(["left", "right"])
                
                pairs.append({
                    "fixed": fixed,
                    "expected": expected,
                    "inputSide": inputSide
                })
                pair_tuples.append((fixed, expected, inputSide))
            
            data_list.append({
                "id": i,
                "result": result,
                "pairs": pairs
            })
            
            # Create a tuple for the item to check uniqueness later
            item_tuples.append((result, tuple(sorted(pair_tuples))))
            
        # The combination for the whole question is the sorted items
        combination = tuple(sorted(item_tuples))
        
        if combination not in seen:
            seen.add(combination)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type6",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Splits het getal op verschillende manieren.",
                    "hint": "Bedenk welke twee getallen samen het bovenste getal vormen.",
                    "method": "addition",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type6.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
