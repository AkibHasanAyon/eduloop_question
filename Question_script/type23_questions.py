import json
import random

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        # Select 4 distinct digits from 0 to 9.
        # random.sample also randomizes the order, yielding 10 P 4 = 5040 permutations,
        # which is plenty for 3000 uniquely ordered questions.
        digits = random.sample(range(10), 4)
        
        # Use the ordered tuple to ensure this exact sequence of digits hasn't been used
        combination = tuple(digits)
        
        if combination not in seen:
            seen.add(combination)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type23",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Maak 3-cijferige getallen onder de 1000 met de gegeven cijfers.",
                    "hint": "Combineer de cijfers om geldige getallen te maken.",
                    "data": [
                        {
                            "digits": list(combination)
                        }
                    ]
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type23.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
