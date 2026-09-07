import json
import random

def get_range(number):
    if 0 <= number <= 20:
        return 0, 20
    elif 21 <= number <= 40:
        return 21, 40
    elif 41 <= number <= 60:
        return 41, 60
    elif 61 <= number <= 80:
        return 61, 80
    else:
        return 81, 100

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    ranges = [
        (0, 20),
        (21, 40),
        (41, 60),
        (61, 80),
        (81, 100)
    ]

    while len(questions) < num_questions:
        # Pick one random number from each range
        numbers = [random.randint(r[0], r[1]) for r in ranges]
        
        # Shuffle the numbers to randomize their order
        random.shuffle(numbers)
        
        combination = tuple(numbers)
        if combination not in seen:
            seen.add(combination)
            
            data_list = []
            for i, num in enumerate(numbers):
                frm, to = get_range(num)
                data_list.append({
                    "id": i + 1,
                    "number": num,
                    "from": frm,
                    "to": to
                })
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type3",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Tussen welke getallen?",
                    "hint": "Kijk tussen welke getallen het getal valt.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type3_questions.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
