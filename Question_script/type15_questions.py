import json
import random

def generate_addition():
    while True:
        left = random.randint(11, 99)
        unit = left % 10
        # For addition, unit + right <= 10. We also want right to be a single digit 1-9
        max_right = min(9, 10 - unit)
        if max_right >= 1:
            right = random.randint(1, max_right)
            return {"left": left, "op": "+", "right": right}

def generate_subtraction():
    while True:
        left = random.randint(11, 99)
        unit = left % 10
        # For subtraction, unit - right >= 0, so right <= unit. right should be 1-9.
        if unit >= 1:
            right = random.randint(1, unit)
            return {"left": left, "op": "-", "right": right}

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        item_tuples = []
        
        # 3 distinct subtractions
        subs = []
        while len(subs) < 3:
            item = generate_subtraction()
            tup = (item["left"], item["op"], item["right"])
            if tup not in item_tuples:
                item_tuples.append(tup)
                subs.append(item)
                
        # 3 distinct additions
        adds = []
        while len(adds) < 3:
            item = generate_addition()
            tup = (item["left"], item["op"], item["right"])
            if tup not in item_tuples:
                item_tuples.append(tup)
                adds.append(item)
                
        data = subs + adds
        
        # Ensure the whole set of 6 questions is unique for the dataset
        combination = tuple(item_tuples)
        if combination not in seen:
            seen.add(combination)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type15",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Reken uit en vul de hulpsom in de denkbal in.",
                    "hint": "Gebruik de eenheden van het eerste getal om de hulpsom te maken.",
                    "data": data
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type15.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
