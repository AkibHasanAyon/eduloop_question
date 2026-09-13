import json
import random
import os
from datetime import datetime, timedelta

def generate_type77_questions(num_questions=6000):
    questions = []
    seen_combinations = set()
    
    # Base date to start randomizing from (e.g., Jan 1, 2024)
    start_date = datetime(2024, 1, 1)
    
    while len(questions) < num_questions:
        data_items = []
        signature_items = []
        
        # Pick a base date for the question to make the 3 items look related
        base_days_offset = random.randint(0, 365)
        base_date = start_date + timedelta(days=base_days_offset)
        
        input_fields = ["travelTime", "departureTime", "arrivalTime"]
        random.shuffle(input_fields)
        
        for i, input_field in enumerate(input_fields):
            # Travel time between 0 and 23 hours, and 0 to 55 minutes
            travel_h = random.randint(0, 23)
            travel_m = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
            
            # Avoid 0 hours 0 minutes
            if travel_h == 0 and travel_m == 0:
                travel_h = 1
                
            dep_hour = random.randint(0, 23)
            dep_minute = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
            
            departure_dt = base_date + timedelta(hours=dep_hour, minutes=dep_minute)
            arrival_dt = departure_dt + timedelta(hours=travel_h, minutes=travel_m)
            
            dep_date_str = departure_dt.strftime("%d-%m-%Y")
            dep_time_str = departure_dt.strftime("%H:%M")
            arr_date_str = arrival_dt.strftime("%d-%m-%Y")
            arr_time_str = arrival_dt.strftime("%H:%M")
            
            data_items.append({
                "id": i + 1,
                "departureDate": dep_date_str,
                "departureTime": dep_time_str,
                "arrivalDate": arr_date_str,
                "arrivalTime": arr_time_str,
                "travelTime": {
                    "hours": str(travel_h),
                    "minutes": str(travel_m)
                },
                "inputField": input_field
            })
            
            # Use hour/minute combinations as a signature for uniqueness
            signature_items.append((dep_hour, dep_minute, travel_h, travel_m, input_field))
            
        signature = tuple(signature_items)
        if signature in seen_combinations:
            continue
            
        seen_combinations.add(signature)
        
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type77",
            "subject": "Rekenen",
            "metadata": {
                "question": "Bereken de ontbrekende vertrektijd, aankomsttijd of reistijd.",
                "hint": "Reken het tijdsverschil uit. Tel eerst de minuten bij tot het volgende hele uur, en tel daarna de resterende uren op.",
                "data": data_items
            }
        }
        
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type77_questions(6000)
    
    # Output path
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type77.json"
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
