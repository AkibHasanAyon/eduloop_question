import json
import random

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        items_data = []
        item_strs = []
        
        # Each question needs 6 distinct items (equations)
        while len(items_data) < 6:
            # Pick a pair that sums to exactly 10 (vriendjes van 10)
            p1 = random.randint(1, 9)
            p2 = 10 - p1
            
            # Pick a third number. To keep sums between 0 and 100, we pick up to 90.
            x = random.randint(0, 90)
            
            # Shuffle so the "friends of 10" appear in random positions
            nums = [p1, p2, x]
            random.shuffle(nums)
            
            q_str = f"{nums[0]} + {nums[1]} + {nums[2]} ="
            
            # Ensure no duplicate equations within the same screen
            if q_str not in item_strs:
                item_strs.append(q_str)
                items_data.append({
                    "id": len(items_data) + 1,
                    "question": q_str,
                    "answer": sum(nums),
                    "type": "addition"
                })
                
        # Use a sorted tuple of the 6 question strings to guarantee uniqueness of the whole screen
        combination = tuple(sorted(item_strs))
        
        if combination not in seen:
            seen.add(combination)
            
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type16",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Reken handig uit. Zoek eerst de getallen die samen 10 zijn.",
                    "hint": "Zoek eerst de vriendjes van 10.",
                    "data": items_data
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type16.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
