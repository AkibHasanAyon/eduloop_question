import json
import random

def generate_dataset():
    num_questions = 6000
    items_per_question = 2
    total_items_needed = num_questions * items_per_question

    templates = [
        {
            "statement": "{percentage}% van het tuinoppervlak is {part} m²",
            "question": "Wat is de oppervlakte van de hele tuin?",
            "answer": "{total} m²",
            "hint_part": "{part} m²"
        },
        {
            "statement": "{percentage}% van de prijs is €{part}",
            "question": "Wat is de totale prijs?",
            "answer": "€{total}",
            "hint_part": "€{part}"
        },
        {
            "statement": "{percentage}% van het gewicht is {part} kg",
            "question": "Wat is het totale gewicht?",
            "answer": "{total} kg",
            "hint_part": "{part} kg"
        },
        {
            "statement": "{percentage}% van de inhoud is {part} liter",
            "question": "Wat is de totale inhoud?",
            "answer": "{total} liter",
            "hint_part": "{part} liter"
        },
        {
            "statement": "{percentage}% van de afstand is {part} km",
            "question": "Wat is de totale afstand?",
            "answer": "{total} km",
            "hint_part": "{part} km"
        },
        {
            "statement": "{percentage}% van de groep is {part} personen",
            "question": "Hoeveel personen zijn er in totaal?",
            "answer": "{total} personen",
            "hint_part": "{part} personen"
        },
        {
            "statement": "{percentage}% van de tijd is {part} minuten",
            "question": "Wat is de totale tijd?",
            "answer": "{total} minuten",
            "hint_part": "{part} minuten"
        },
        {
            "statement": "{percentage}% van de boeken is {part} stuks",
            "question": "Hoeveel boeken zijn er in totaal?",
            "answer": "{total} stuks",
            "hint_part": "{part} stuks"
        },
        {
            "statement": "{percentage}% van het spaargeld is €{part}",
            "question": "Wat is het totale spaargeld?",
            "answer": "€{total}",
            "hint_part": "€{part}"
        },
        {
            "statement": "{percentage}% van de muur is {part} m²",
            "question": "Wat is de oppervlakte van de hele muur?",
            "answer": "{total} m²",
            "hint_part": "{part} m²"
        },
        {
            "statement": "{percentage}% van de leerlingen is {part} kinderen",
            "question": "Hoeveel leerlingen zijn er in totaal?",
            "answer": "{total} kinderen",
            "hint_part": "{part} kinderen"
        },
        {
            "statement": "{percentage}% van de route is {part} km",
            "question": "Hoe lang is de hele route?",
            "answer": "{total} km",
            "hint_part": "{part} km"
        },
        {
            "statement": "{percentage}% van de oogst is {part} kg",
            "question": "Wat is de totale oogst?",
            "answer": "{total} kg",
            "hint_part": "{part} kg"
        },
        {
            "statement": "{percentage}% van de verf is {part} ml",
            "question": "Hoeveel verf is er in totaal?",
            "answer": "{total} ml",
            "hint_part": "{part} ml"
        },
        {
            "statement": "{percentage}% van het maandsalaris is €{part}",
            "question": "Wat is het totale maandsalaris?",
            "answer": "€{total}",
            "hint_part": "€{part}"
        },
        {
            "statement": "{percentage}% van de sportclub is {part} leden",
            "question": "Hoeveel leden heeft de club in totaal?",
            "answer": "{total} leden",
            "hint_part": "{part} leden"
        },
        {
            "statement": "{percentage}% van de kosten is €{part}",
            "question": "Wat zijn de totale kosten?",
            "answer": "€{total}",
            "hint_part": "€{part}"
        },
        {
            "statement": "{percentage}% van de rekening is €{part}",
            "question": "Wat is het bedrag van de hele rekening?",
            "answer": "€{total}",
            "hint_part": "€{part}"
        },
        {
            "statement": "{percentage}% van het zwembad is {part} liter",
            "question": "Wat is de totale inhoud van het zwembad?",
            "answer": "{total} liter",
            "hint_part": "{part} liter"
        },
        {
            "statement": "{percentage}% van de plank is {part} cm",
            "question": "Wat is de totale lengte van de plank?",
            "answer": "{total} cm",
            "hint_part": "{part} cm"
        }
    ]

    totals = list(range(10, 1001, 10)) + list(range(1100, 10001, 100))
    percentages = list(range(1, 100))
    
    number_pairs = []
    for t in totals:
        for p in percentages:
            part = (p * t) / 100
            if part.is_integer() and part > 0:
                number_pairs.append({
                    "percentage": p,
                    "total": t,
                    "part": int(part)
                })
                
    all_items = []
    for pair in number_pairs:
        for tmpl in templates:
            statement = tmpl["statement"].format(percentage=pair["percentage"], part=pair["part"], total=pair["total"])
            question_text = tmpl["question"].format(percentage=pair["percentage"], part=pair["part"], total=pair["total"])
            answer = tmpl["answer"].format(percentage=pair["percentage"], part=pair["part"], total=pair["total"])
            hint_part = tmpl["hint_part"].format(percentage=pair["percentage"], part=pair["part"], total=pair["total"])
            
            all_items.append({
                "statement": statement,
                "question": question_text,
                "answer": answer,
                "hint_part": hint_part,
                "percentage": pair["percentage"],
                "template_idx": templates.index(tmpl)
            })

    if len(all_items) < total_items_needed:
        raise ValueError(f"Not enough unique items generated! Needed {total_items_needed}, got {len(all_items)}")

    random.shuffle(all_items)
    
    questions = []
    used_sentences = set()
    item_idx = 0
    
    for q_idx in range(num_questions):
        data_list = []
        
        picked_for_q = []
        tmpl_in_q = set()
        
        while len(picked_for_q) < items_per_question:
            candidate = all_items[item_idx]
            item_idx += 1
            
            if candidate["template_idx"] not in tmpl_in_q and candidate["statement"] not in used_sentences:
                picked_for_q.append(candidate)
                tmpl_in_q.add(candidate["template_idx"])
                used_sentences.add(candidate["statement"])
        
        for i, picked in enumerate(picked_for_q):
            data_list.append({
                "id": i + 1,
                "statement": picked["statement"],
                "question": picked["question"],
                "answer": picked["answer"]
            })
            
        # The hint should use the values from the first item
        first_item = picked_for_q[0]
        hint = f"Als {first_item['percentage']}% gelijk is aan {first_item['hint_part']}, wat is dan 100%?"
        
        question_obj = {
            "id": str(q_idx + 1),
            "type": "type31",
            "subject": "Rekenen",
            "metadata": {
                "question": "Bereken het geheel vanuit het percentage.",
                "hint": hint,
                "data": data_list
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    dataset = generate_dataset()
    output_path = '/home/akib/Desktop/IIT/eduloop/Question_output/type31.json'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {len(dataset)} questions to {output_path}")
