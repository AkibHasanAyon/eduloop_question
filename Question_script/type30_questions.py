import json
import random

def generate_dataset():
    num_questions = 6000
    items_per_question = 2
    total_items_needed = num_questions * items_per_question

    # Generate all valid (part, total, percentage) combinations
    totals = [
        10, 20, 25, 40, 50, 100, 200, 250, 300, 400, 500, 600, 800, 1000, 
        1200, 1500, 2000, 30, 60, 75, 80, 120, 150, 160, 180, 700, 900
    ]
    
    number_pairs = []
    for t in totals:
        for z in range(1, 100):
            part = z * t / 100
            if part.is_integer():
                number_pairs.append((int(part), t, z))
                
    # Remove duplicates if any
    number_pairs = list(set(number_pairs))

    # Format A: Van de {total} {item} zijn er {part} {property}.
    format_a = {
        "fietsen": ["verhuurd", "verkocht", "kapot", "rood", "blauw"],
        "auto's": ["elektrisch", "verkocht", "geparkeerd", "rood", "nieuw"],
        "appels": ["rot", "verkocht", "groen", "opgegeten"],
        "boeken": ["uitgeleend", "verkocht", "gelezen", "beschadigd"],
        "huizen": ["verkocht", "verhuurd", "vrijstaand"],
        "stoelen": ["bezet", "gereserveerd", "kapot"],
        "computers": ["defect", "verkocht", "geüpdatet"],
        "spelers": ["geblesseerd", "geschorst", "verkocht"],
        "dieren": ["ziek", "geadopteerd", "verkocht"],
        "taartjes": ["opgegeten", "verkocht", "versierd"],
        "bomen": ["gekapt", "ziek", "geplant"],
        "kledingstukken": ["verkocht", "in de uitverkoop", "gewassen"],
        "lampen": ["kapot", "vervangen", "aangezet"],
        "ramen": ["gebroken", "open", "gesloten"],
        "deelnemers": ["geslaagd", "gezakt", "afwezig"],
        "werknemers": ["ziek", "op vakantie", "aanwezig"]
    }

    # Format B: Van de {total} {item} hebben {part} {property}.
    format_b = {
        "leerlingen": ["een bril", "een huisdier", "een fiets", "een voldoende", "een onvoldoende", "een broer of zus", "een smartphone"],
        "mensen": ["een rijbewijs", "een auto", "een hond", "een kat", "een tuin", "een baan"],
        "huizen": ["een tuin", "een garage", "zonnepanelen", "een dakterras"],
        "auto's": ["een trekhaak", "een navigatiesysteem", "winterbanden"],
        "docenten": ["een bril", "een auto", "een laptop"],
        "kinderen": ["een fiets", "een bal", "een huisdier", "zwemles"]
    }

    all_items = []
    
    for (part, total, z) in number_pairs:
        for subject, properties in format_a.items():
            for prop in properties:
                sentence = f"Van de {total} {subject} zijn er {part} {prop}."
                all_items.append({
                    "sentence": sentence,
                    "answer": f"{z}%",
                    "subject": subject
                })
                
        for subject, properties in format_b.items():
            for prop in properties:
                sentence = f"Van de {total} {subject} hebben {part} {prop}."
                all_items.append({
                    "sentence": sentence,
                    "answer": f"{z}%",
                    "subject": subject
                })

    if len(all_items) < total_items_needed:
        raise ValueError(f"Not enough unique items generated! Needed {total_items_needed}, got {len(all_items)}")

    # Shuffle the huge pool
    random.shuffle(all_items)
    
    questions = []
    used_items = set()
    item_idx = 0
    
    for q_idx in range(num_questions):
        data_list = []
        
        # We try to pick 2 items that have different subjects and different sentences
        picked_for_q = []
        subjects_in_q = set()
        
        while len(picked_for_q) < items_per_question:
            candidate = all_items[item_idx]
            item_idx += 1
            
            # Simple check to make the 2 items slightly diverse
            if candidate["subject"] not in subjects_in_q and candidate["sentence"] not in used_items:
                picked_for_q.append(candidate)
                subjects_in_q.add(candidate["subject"])
                used_items.add(candidate["sentence"])
        
        for i, picked in enumerate(picked_for_q):
            data_list.append({
                "id": i + 1,
                "question": picked["sentence"],
                "answer": picked["answer"]
            })
            
        question_obj = {
            "id": str(q_idx + 1),
            "type": "type30",
            "subject": "Rekenen",
            "metadata": {
                "question": "Bereken het percentage.",
                "hint": "Deel het deel door het geheel en vermenigvuldig met 100%.",
                "data": data_list
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type30.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
