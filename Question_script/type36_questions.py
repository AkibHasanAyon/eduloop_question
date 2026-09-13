import json
import random
import os

def generate_questions():
    questions = []
    
    question_texts = [
        "Bereken de korting en de nieuwe prijs.",
        "Wat is de korting en wat wordt de nieuwe prijs?",
        "Reken de korting uit en bepaal de nieuwe prijs.",
        "Hoeveel bedraagt de korting en de nieuwe prijs?",
        "Geef de korting en de nieuwe prijs.",
        "Vind de korting en de nieuwe prijs."
    ]
    
    # Prices that generally result in clean integers when multiplied by common percentages
    prices = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1200, 1500, 2000, 2500, 3000, 5000]
    
    # Common discounts
    discounts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 75, 80]
    
    # We want unique combinations of 3 (price, discount) items.
    all_pairs = [(p, d) for p in prices for d in discounts]
    
    seen_combinations = set()
    
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type36.json")
    
    while len(questions) < 6000:
        # sample 3 unique pairs
        selected_pairs = tuple(sorted(random.sample(all_pairs, 3)))
        
        # ensure uniqueness
        if selected_pairs in seen_combinations:
            continue
            
        seen_combinations.add(selected_pairs)
        
        q_text = random.choice(question_texts)
        
        # generate a random hint example from one of the selected pairs
        ex_price, ex_disc = random.choice(selected_pairs)
        ex_korting = ex_price * ex_disc / 100
        # format without decimal if it's an integer
        ex_korting_str = f"{int(ex_korting)}" if ex_korting.is_integer() else f"{ex_korting:.2f}".replace('.', ',')
        
        ex_new = ex_price - ex_korting
        ex_new_str = f"{int(ex_new)}" if ex_new.is_integer() else f"{ex_new:.2f}".replace('.', ',')
        
        hint = f"Korting = prijs × (kortingspercentage ÷ 100). Nieuwe prijs = prijs − korting. Voorbeeld: prijs €{ex_price} met {ex_disc}% → korting €{ex_korting_str}, nieuwe prijs €{ex_new_str}."
        
        # Convert selected_pairs to data list and shuffle to avoid ordering biases
        data_pairs = list(selected_pairs)
        random.shuffle(data_pairs)
        
        q_data = {
            "id": str(len(questions) + 1),
            "type": "type36",
            "subject": "Rekenen",
            "metadata": {
                "question": q_text,
                "hint": hint,
                "data": [
                    {
                        "id": "a",
                        "price": data_pairs[0][0],
                        "discountPct": data_pairs[0][1]
                    },
                    {
                        "id": "b",
                        "price": data_pairs[1][0],
                        "discountPct": data_pairs[1][1]
                    },
                    {
                        "id": "c",
                        "price": data_pairs[2][0],
                        "discountPct": data_pairs[2][1]
                    }
                ]
            }
        }
        
        questions.append(q_data)
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
