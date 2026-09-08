import json
import random

def generate_dataset():
    num_questions = 6000
    questions = []
    seen = set()
    
    while len(questions) < num_questions:
        # We need 5 distinct analog clock faces to avoid ambiguity.
        # If we just picked 5 random digital times, we might pick 08:30 and 20:30,
        # which look identical on an analog clock!
        faces = set()
        while len(faces) < 5:
            h_12 = random.randint(0, 11)
            m = random.randint(0, 59)
            faces.add((h_12, m))
            
        # Convert the 5 unique analog faces into 5 digital times (randomly AM/PM)
        times = []
        for h_12, m in faces:
            is_pm = random.choice([True, False])
            h_24 = h_12 + (12 if is_pm else 0)
            times.append(f"{h_24:02d}:{m:02d}")
            
        # Ensure this exact combination of 5 digital times hasn't been used before
        combination = tuple(sorted(times))
        if combination not in seen:
            seen.add(combination)
            
            # Assign these times to the analog clocks.
            # We enforce a derangement (no clockTime matches its time directly above it)
            # to make the matching exercise more engaging.
            clock_times = list(times)
            while any(times[i] == clock_times[i] for i in range(5)):
                random.shuffle(clock_times)
                
            data_list = []
            for i in range(5):
                data_list.append({
                    "id": i + 1,
                    "time": times[i],
                    "clockTime": clock_times[i],
                    "correct": times.index(clock_times[i]) + 1
                })
                
            question_obj = {
                "id": str(len(questions) + 1),
                "type": "type27",
                "subject": "Rekenen",
                "metadata": {
                    "question": "Welke digitale tijd hoort bij welke klok? Vul het juiste nummer in.",
                    "hint": "Kijk naar de wijzers van de klok en zoek het overeenkomstige nummer van de digitale tijd.",
                    "data": data_list
                }
            }
            questions.append(question_obj)
            
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type27.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
