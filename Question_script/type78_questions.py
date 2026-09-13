import json
import random
import os

def generate_type78_questions(num_questions=6000):
    item_pool = []
    cases = [
        (0, "{H} uur", 0),
        (5, "5 over {H}", 0),
        (10, "10 over {H}", 0),
        (15, "kwart over {H}", 0),
        (30, "half {H}", -1),
        (45, "kwart voor {H}", -1),
        (50, "10 voor {H}", -1),
        (55, "5 voor {H}", -1)
    ]
    
    for h in range(1, 12):
        for m, text_template, offset in cases:
            actual_h = h + offset
            
            # Format time strings
            am_str = f"{actual_h:02d}:{m:02d}"
            pm_str = f"{actual_h + 12:02d}:{m:02d}"
            
            if h in [1, 2, 3, 4, 5]:
                period_am = "'s nachts"
                period_pm = "'s middags"
            else:
                period_am = "'s ochtends"
                period_pm = "'s avonds"
                
            prompt_am = f"{text_template.format(H=h)} {period_am}"
            item_pool.append({
                "prompt": prompt_am,
                "options": [am_str, pm_str],
                "correct": 0,
                "answer": am_str
            })
            
            prompt_pm = f"{text_template.format(H=h)} {period_pm}"
            item_pool.append({
                "prompt": prompt_pm,
                "options": [am_str, pm_str],
                "correct": 1,
                "answer": pm_str
            })
            
    questions = []
    seen_combinations = set()
    
    while len(questions) < num_questions:
        # Pick 5 unique items from the pool
        selected = random.sample(item_pool, 5)
        
        # Unique signature to avoid duplicate combinations
        signature = tuple(sorted([item["prompt"] for item in selected]))
        
        if signature in seen_combinations:
            continue
            
        seen_combinations.add(signature)
        
        data_items = []
        for i, item in enumerate(selected):
            data_items.append({
                "id": f"c{i+1}",
                "prompt": item["prompt"],
                "options": item["options"],
                "correct": item["correct"],
                "answer": item["answer"]
            })
            
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type78",
            "subject": "Rekenen",
            "metadata": {
                "question": "Welke digitale tijd hoort bij de omschrijving?",
                "hint": "Lees de omschrijving goed: 's ochtends/’s nachts is vóór 12:00 uur, 's middags/'s avonds is ná 12:00 uur (tel er 12 bij op).",
                "data": data_items
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type78_questions(6000)
    
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type78.json"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
