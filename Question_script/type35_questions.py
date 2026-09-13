import json
import random

def generate_dataset():
    num_questions = 6000
    items_per_question = 3
    total_items_needed = num_questions * items_per_question

    valid_items = []
    # Generate clean combinations where percentages and prices are integers
    for p in range(1, 100):
        # We use totals in steps of 5 or 10 to keep the prices looking like typical shop prices
        for t in range(10, 20001, 10):
            d = (p * t) / 100
            if d.is_integer() and d > 0:
                b = int(t - d)
                valid_items.append({
                    "oldPrice": t,
                    "newPrice": b,
                    "discount": p
                })

    if len(valid_items) < total_items_needed:
        raise ValueError(f"Not enough unique items generated! Needed {total_items_needed}, got {len(valid_items)}")

    # Shuffle to ensure randomness
    random.shuffle(valid_items)
    
    questions = []
    item_idx = 0
    
    for q_idx in range(num_questions):
        values_list = []
        
        # Pick 3 items for the question
        while len(values_list) < items_per_question:
            candidate = valid_items[item_idx]
            item_idx += 1
            
            # Ensure the items in the same question are somewhat distinct (e.g. different discount percentage)
            if not any(item['discount'] == candidate['discount'] for item in values_list):
                values_list.append(candidate)
            else:
                # If duplicate discount, we can just grab it later or discard it. The pool is huge.
                pass
            
        data_list = [
            {
                "id": "left",
                "values": values_list
            }
        ]
        
        question_obj = {
            "id": str(q_idx + 1),
            "type": "type35",
            "subject": "Rekenen",
            "metadata": {
                "question": "Bereken de nieuwe prijs na korting.",
                "hint": "Nieuwe prijs = oude prijs × (1 − korting/100).",
                "data": data_list
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type35.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
