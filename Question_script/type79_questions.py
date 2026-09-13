import json
import random
import os

def generate_amount(min_cents, max_cents):
    # Generate a random amount in cents
    val = random.randint(min_cents, max_cents)
    # Randomly decide if it should have 1 or 2 decimal places visually 
    # (by making it a multiple of 10 cents half the time)
    if random.choice([True, False]):
        val = (val // 10) * 10
    return round(val / 100.0, 2)

def generate_type79_questions(num_questions=6000):
    questions = []
    seen_combinations = set()
    
    while len(questions) < num_questions:
        data_items = []
        signature_items = []
        
        for i in range(3):
            amounts = [
                generate_amount(10000, 19999), # 100.00 to 199.99
                generate_amount(2000, 9999),   # 20.00 to 99.99
                generate_amount(10, 999),      # 0.10 to 9.99
                generate_amount(100, 2099)     # 1.00 to 20.99
            ]
            
            # Shuffle the order slightly for variety?
            # The demo shows descending order of magnitude roughly. 
            # Let's keep it strictly like the demo: large, medium, tiny, small.
            
            total = round(sum(amounts), 2)
            
            data_items.append({
                "id": f"c{i+1}",
                "amounts": amounts,
                "total": total
            })
            signature_items.append(tuple(amounts))
            
        signature = tuple(sorted(signature_items))
        if signature in seen_combinations:
            continue
            
        seen_combinations.add(signature)
        
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type79",
            "subject": "Rekenen",
            "metadata": {
                "question": "Eerst schatten, dan met de rekenmachine precies uitrekenen.",
                "hint": "Tel de vier bedragen onder elkaar bij elkaar op. Gebruik eventueel een schatting vooraf en reken het precieze bedrag uit.",
                "data": data_items
            }
        }
        
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type79_questions(6000)
    
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type79.json"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
