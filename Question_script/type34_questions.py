import json
import random

def generate_dataset():
    num_questions = 6000
    items_per_question = 2
    total_items_needed = num_questions * items_per_question

    valid_items = []
    # Generate clean combinations where percentages and prices are integers
    for p in range(1, 100):
        # We use totals in steps of 10 to keep the prices looking like typical shop prices
        for t in range(10, 20001, 10):
            d = (p * t) / 100
            if d.is_integer() and d > 0:
                d = int(d)
                b = t - d
                valid_items.append({
                    "totalPrice": t,
                    "buyingPrice": b,
                    "discountPrice": d,
                    "discountpercentage": p
                })

    if len(valid_items) < total_items_needed:
        raise ValueError(f"Not enough unique items generated! Needed {total_items_needed}, got {len(valid_items)}")

    # Shuffle to ensure randomness
    random.shuffle(valid_items)
    
    questions = []
    item_idx = 0
    
    for q_idx in range(num_questions):
        data_list = []
        
        # Pick items for the question
        while len(data_list) < items_per_question:
            candidate = valid_items[item_idx]
            item_idx += 1
            
            # Ensure the items in the same question are not identical
            if not any(item['totalPrice'] == candidate['totalPrice'] and item['discountpercentage'] == candidate['discountpercentage'] for item in data_list):
                data_list.append(candidate)
            
        question_obj = {
            "id": str(q_idx + 1),
            "type": "type34",
            "subject": "Rekenen",
            "metadata": {
                "question": "Bereken de korting en het kortingspercentage.",
                "hint": "Korting = oude prijs − nieuwe prijs. Percentage = (korting ÷ oude prijs) × 100.",
                "data": data_list
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type34.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
