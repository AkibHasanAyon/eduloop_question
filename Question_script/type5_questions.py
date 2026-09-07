import json
import random

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        data_list = []
        item_tuples = set()
        
        # We need 4 distinct items per question
        while len(data_list) < 4:
            top = random.randint(0, 100)
            given_value = random.randint(0, top)
            is_left = random.choice([True, False])
            
            if is_left:
                left = given_value
                right = None
                answer = top - given_value
            else:
                left = None
                right = given_value
                answer = top - given_value
                
            item_tuple = (top, left, right, answer)
            if item_tuple not in item_tuples:
                item_tuples.add(item_tuple)
                data_list.append({
                    "id": len(data_list) + 1,
                    "top": top,
                    "left": left,
                    "right": right,
                    "answer": answer
                })
        
        # Create a unique representation for the combination to avoid duplicate questions
        # Sort the tuples so the combination is independent of the order, handling None correctly
        combination = tuple(sorted(list(item_tuples), key=lambda x: tuple(-1 if i is None else i for i in x)))
        
        if combination not in seen:
            seen.add(combination)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type5",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Waar hoort het vakje?",
                    "hint": "Vul het ontbrekende getal van de splitsing in.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type5.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
