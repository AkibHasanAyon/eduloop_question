import json
import random
import itertools

def generate_dataset():
    num_questions = 6000
    items_per_question = 6
    total_items_needed = num_questions * items_per_question

    # Generate all proper fractions with denominator 2 to 12
    fractions = []
    for d in range(2, 13):
        for n in range(1, d):
            fractions.append({
                "str": f"{n}/{d}",
                "val": n / d
            })

    # Generate all valid combinations of 3 fractions
    valid_combos = []
    for combo in itertools.combinations(fractions, 3):
        # Ensure they all have distinct values to allow strict sorting
        if combo[0]["val"] != combo[1]["val"] and \
           combo[1]["val"] != combo[2]["val"] and \
           combo[0]["val"] != combo[2]["val"]:
            valid_combos.append(combo)
            
    # Check if we have enough combinations
    if len(valid_combos) < total_items_needed:
        raise ValueError(f"Not enough unique combinations! Needed {total_items_needed}, found {len(valid_combos)}")

    # Shuffle and select the required number of combinations
    random.shuffle(valid_combos)
    selected_combos = valid_combos[:total_items_needed]

    questions = []
    combo_idx = 0
    
    for q_idx in range(num_questions):
        data_list = []
        for i in range(items_per_question):
            combo = selected_combos[combo_idx]
            combo_idx += 1
            
            # Extract strings and sort by value
            sorted_combo = sorted(combo, key=lambda x: x["val"])
            
            # We shuffle the fractions for the initial display so they aren't pre-sorted
            display_fractions = [f["str"] for f in combo]
            random.shuffle(display_fractions)
            
            data_list.append({
                "id": i + 1,
                "fractions": display_fractions,
                "sorted": [f["str"] for f in sorted_combo]
            })
            
        question_obj = {
            "id": str(q_idx + 1),
            "type": "type29",
            "subject": "Rekenen",
            "metadata": {
                "question": "Zet de breuken in volgorde van klein naar groot.",
                "hint": "Kijk goed naar de grootte van de breuken.",
                "data": data_list
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type29.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
