import json
import random
import os

def generate_type75_questions(num_questions=6000):
    questions = []
    seen_combinations = set()

    # We want 6000 unique questions
    while len(questions) < num_questions:
        # Percentages 1 to 9
        percentages = list(range(1, 10))
        random.shuffle(percentages)
        
        # Bases 100 to 2000, step 100 (20 values)
        # Using 100 to 3000 to give a good variety
        possible_bases = [i * 100 for i in range(1, 31)]
        bases = random.sample(possible_bases, 9)
        
        # Create a unique signature for this question to prevent exact duplicates
        # Signature can be a tuple of (percentage, base) pairs
        signature = tuple(zip(percentages, bases))
        
        if signature in seen_combinations:
            continue
            
        seen_combinations.add(signature)
        
        data_items = []
        for i, (perc, base) in enumerate(signature):
            answer = str(int((perc * base) / 100))
            data_items.append({
                "id": i + 1,
                "text": f"{perc}% van {base} =",
                "answer": answer,
                "percentage": perc,
                "base": base
            })
            
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type75",
            "subject": "Rekenen",
            "metadata": {
                "question": "Reken uit. Hoeveel is het percentage?",
                "hint": "Reken eerst 1% uit door het getal door 100 te delen. Vermenigvuldig dat daarna met het percentage.",
                "data": data_items
            }
        }
        
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type75_questions(6000)
    
    # Write to file
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type75.json"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
