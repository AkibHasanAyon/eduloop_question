import json
import random

def get_time_text_and_expected(h, m):
    # Determine the part of the day based on the hour (24-hour format)
    if 0 <= h < 6:
        part = "nacht"
    elif 6 <= h < 12:
        part = "ochtend"
    elif 12 <= h < 18:
        part = "middag"
    else:
        part = "avond"
        
    expected = f"{h:02d}:{m:02d}"
    
    # Calculate 12-hour format hour for text representation
    if m == 0:
        hour_text = h if h <= 12 else h - 12
        if hour_text == 0: hour_text = 12
        text = f"Het is {hour_text} uur in de {part}."
    elif m == 15:
        hour_text = h if h <= 12 else h - 12
        if hour_text == 0: hour_text = 12
        text = f"Het is kwart over {hour_text} in de {part}."
    elif m == 30:
        # "half X" means X is the *next* hour
        hour_text = h + 1
        if hour_text > 12: hour_text -= 12
        if hour_text == 0: hour_text = 12
        text = f"Het is half {hour_text} in de {part}."
    elif m == 45:
        # "kwart voor X" means X is the *next* hour
        hour_text = h + 1
        if hour_text > 12: hour_text -= 12
        if hour_text == 0: hour_text = 12
        text = f"Het is kwart voor {hour_text} in de {part}."
        
    return text, expected

def generate_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    # Pre-generate all 96 valid 15-minute interval items for a 24-hour clock
    possible_items = []
    for h in range(24):
        for m in [0, 15, 30, 45]:
            possible_items.append(get_time_text_and_expected(h, m))
            
    while len(questions) < num_questions:
        # Pick 3 distinct times
        selected = random.sample(possible_items, 3)
        
        # Sort to create a unique combination key for the entire screen
        combination = tuple(sorted(selected))
        
        if combination not in seen:
            seen.add(combination)
            
            data_list = []
            for i, (text, expected) in enumerate(selected):
                data_list.append({
                    "id": i + 1,
                    "text": text,
                    "expectedTime": expected
                })
                
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type22",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Schrijf de tijd in digitale cijfers.",
                    "hint": "Let goed op ochtend, middag of avond.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type22.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
