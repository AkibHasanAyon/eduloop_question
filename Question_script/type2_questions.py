import json
import random

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    pool = list(range(1, 101))
    # Give a higher weight to multiples of 5 to prioritize them
    # Multiples of 5 will have a weight of 15, others will have 1.
    weights = [15 if x % 5 == 0 else 1 for x in pool]

    while len(questions) < num_questions:
        num_options = random.randint(5, 8)
        
        selected = set()
        # Weighted random sampling without replacement
        while len(selected) < num_options:
            choice = random.choices(pool, weights=weights, k=1)[0]
            selected.add(choice)
            
        # Sort the options in ascending order
        selected_sorted = tuple(sorted(list(selected)))
        
        # Ensure no repeated combinations
        if selected_sorted not in seen:
            seen.add(selected_sorted)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type2",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Vul de getallen in op de getallenlijn.",
                    "hint": "Kijk naar de schaalverdeling.",
                    "options": list(selected_sorted)
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/questions.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
