import json
import random
import os

def get_phrase_and_minutes(h, m):
    # Convert to 12-hour format
    hour_12 = h % 12
    if hour_12 == 0:
        hour_12 = 12
        
    next_hour = hour_12 + 1
    if next_hour == 13:
        next_hour = 1
        
    # Determine correct Dutch phrasing for the minutes
    if 1 <= m <= 14:
        return m, f"over {hour_12}"
    elif 16 <= m <= 29:
        return 30 - m, f"voor half {next_hour}"
    elif 31 <= m <= 44:
        return m - 30, f"over half {next_hour}"
    elif 46 <= m <= 59:
        return 60 - m, f"voor {next_hour}"
    
    return None, None

def get_period(h):
    if 0 <= h < 6:
        return "nacht"
    elif 6 <= h < 12:
        return "ochtend"
    elif 12 <= h < 18:
        return "middag"
    else:
        return "avond"

def generate_new_dataset():
    num_questions = 3000
    questions = []
    seen = set()
    
    # Pre-generate all valid times EXCLUDING the 'voor half' range (16-29)
    possible_items = []
    for h in range(24):
        for m in range(0, 60):
            # Use the "other" ranges
            if (1 <= m <= 14) or (31 <= m <= 44) or (46 <= m <= 59):
                time_str = f"{h:02d}:{m:02d}"
                minutes_val, phrase = get_phrase_and_minutes(h, m)
                period = get_period(h)
                
                possible_items.append({
                    "time": time_str,
                    "answer": {
                        "minutes": minutes_val,
                        "phrase": phrase,
                        "period": period
                    }
                })
                
    while len(questions) < num_questions:
        selected = random.sample(possible_items, 2)
        
        combination = tuple(sorted([item["time"] for item in selected]))
        
        if combination not in seen:
            seen.add(combination)
            
            data_list = []
            for i, item in enumerate(selected):
                item_copy = {"id": i + 1}
                item_copy.update(item)
                data_list.append(item_copy)
                
            question_obj = {
                "id": 0, # Will be set dynamically later
                "type": "type25",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Hoeveel minuten tot het volgende half uur?",
                    "hint": "Kijk naar de minutenwijzer van de klok.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type25.json'
    
    # Read existing 3000 questions to append to
    existing_questions = []
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding='utf-8') as f:
            existing_questions = json.load(f)
            
    new_questions = generate_new_dataset()
    
    # Assign sequential IDs to the new questions continuing from the existing ones
    start_id = len(existing_questions) + 1
    for i, q in enumerate(new_questions):
        q["id"] = str(start_id + i)
        
    # Combine old and new
    combined_questions = existing_questions + new_questions
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(combined_questions, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully appended {len(new_questions)} new questions. Total in file is now {len(combined_questions)}.")
