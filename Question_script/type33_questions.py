import json
import random

def generate_dataset():
    num_questions = 6000
    items_per_question = 4
    total_items_needed = num_questions * items_per_question

    # Generate valid (percentage, total, part) pairs
    # Using total up to 20000 with step 5 to get a massive pool of pairs
    valid_pairs = []
    for p in range(1, 100):
        for t in range(10, 20001, 5):
            part = (p * t) / 100
            if part.is_integer() and part > 0:
                valid_pairs.append({
                    "percentage": p,
                    "total": t,
                    "part": int(part)
                })

    if len(valid_pairs) < total_items_needed:
        raise ValueError(f"Not enough unique items generated! Needed {total_items_needed}, got {len(valid_pairs)}")

    # Shuffle pairs to ensure randomness
    random.shuffle(valid_pairs)
    
    questions = []
    
    for q_idx in range(num_questions):
        data_list = []
        
        # Pick 4 pairs with distinct totals
        selected_pairs = []
        while len(selected_pairs) < items_per_question:
            candidate = valid_pairs.pop()
            # Ensure the total is distinct from already selected ones for this question
            if candidate["total"] not in [p["total"] for p in selected_pairs]:
                selected_pairs.append(candidate)
            else:
                # If it's a duplicate total, we can just discard it or put it at the beginning.
                # Since the pool is huge, discarding is perfectly fine.
                pass
                
        # Extract the totals
        totals = [p["total"] for p in selected_pairs]
        
        # Shuffle the totals for the right side
        shuffled_totals = totals.copy()
        random.shuffle(shuffled_totals)
        
        for i, p in enumerate(selected_pairs):
            correct_idx = shuffled_totals.index(p["total"])
            data_list.append({
                "id": i + 1,
                "leftText": f"{p['percentage']}% is €{p['part']}.",
                "correctMatch": correct_idx
            })
            
        right_side_values = [f"€{t}." for t in shuffled_totals]
        
        question_obj = {
            "id": str(q_idx + 1),
            "type": "type33",
            "subject": "Rekenen",
            "metadata": {
                "question": "Verbind het percentage met het juiste bedrag.",
                "hint": "Reken uit wat 100% is.",
                "data": data_list,
                "rightSideValues": right_side_values
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type33.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
