import json
import random

def generate_addition():
    left = random.randint(0, 100)
    # Ensure the sum does not exceed 100
    right = random.randint(0, 100 - left)
    return {"left": left, "operator": "+", "right": right, "answer": left + right}

def generate_subtraction():
    left = random.randint(0, 100)
    # Ensure the result is not negative
    right = random.randint(0, left)
    return {"left": left, "operator": "-", "right": right, "answer": left - right}

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        data = []
        eq_tuples = []
        
        # 4 columns (sub-arrays) as in the demo
        for _ in range(4):
            column = []
            
            # First 2 equations are addition
            for _ in range(2):
                eq = generate_addition()
                column.append(eq)
                eq_tuples.append((eq["left"], eq["operator"], eq["right"]))
                
            # Next 2 equations are subtraction
            for _ in range(2):
                eq = generate_subtraction()
                column.append(eq)
                eq_tuples.append((eq["left"], eq["operator"], eq["right"]))
                
            data.append(column)
            
        # Use the ordered tuple of all 16 equations to guarantee the whole screen combination is unique
        combination = tuple(eq_tuples)
        
        if combination not in seen:
            seen.add(combination)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type14",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Reken de sommen uit.",
                    "hint": "Probeer de getallen stap voor stap op te tellen of af te trekken.",
                    "method": 1,
                    "data": data
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type14.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
