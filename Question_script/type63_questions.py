import json
import random
import os

def generate_questions():
    questions = []
    
    q_texts = [
        "Tel verder en terug.",
        "Vul de ontbrekende getallen in.",
        "Reken vooruit en achteruit.",
        "Tel met sprongen vooruit en achteruit."
    ]
    
    hints = [
        "Tip: Tel vooruit (+) en terug (-) met de aangegeven spronggrootte.",
        "Let op de spronggrootte boven de tabel. Tel af (-) aan de linkerkant en tel op (+) aan de rechterkant.",
        "Kijk goed naar het getal bovenaan de pijlen. Dat is je sprong. Gebruik dat om te minnen en te plussen."
    ]
    
    seen_combinations = set()
    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type63.json")
    
    while len(questions) < 6000:
        # Generate 4 distinct centers for the question
        # We ensure they are large enough so subtracting 1000 doesn't result in negative numbers
        centers = tuple(sorted(random.sample(range(1200, 9900), 4)))
        
        if centers in seen_combinations:
            continue
        seen_combinations.add(centers)
        
        # shuffle centers so they don't always appear in sorted order
        row_centers = list(centers)
        random.shuffle(row_centers)
        
        steps = [1, 10, 100, 1000]
        data = []
        for step in steps:
            rows = [{"center": c} for c in row_centers]
            data.append({
                "step": step,
                "minus": -step,
                "plus": step,
                "labelMinus": f"-{step}",
                "labelPlus": f"+{step}",
                "rows": rows
            })
            
        questions.append({
            "id": str(len(questions) + 1),
            "type": "type63",
            "subject": "Rekenen",
            "metadata": {
                "question": random.choice(q_texts),
                "hint": random.choice(hints),
                "data": data
            }
        })
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(questions)} questions at {output_path}")

if __name__ == "__main__":
    generate_questions()
