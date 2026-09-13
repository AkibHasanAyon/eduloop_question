import json
import random
import os

def fmt(num):
    if float(num).is_integer():
        return str(int(num))
    return str(num).replace('.', ',')

def generate_questions():
    # 1. Rectangle
    rect_items = ["De kamer", "De tuin", "Het kantoor", "De hal", "De woonkamer", "De schuur", "Het terras"]
    rect_lengths = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 20]
    rect_widths = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 8, 9, 10, 12]
    
    rect_pool = []
    for item in rect_items:
        for l in rect_lengths:
            for w in rect_widths:
                if l > w:
                    ans = l * w
                    # Only accept items where the final square meter answer is an integer
                    if float(ans).is_integer():
                        rect_pool.append({
                            "type": "rectangle",
                            "text": f"{item} is {fmt(l)} m lang en {fmt(w)} m breed.",
                            "answer_m2": str(int(ans))
                        })

    # 2. Hectare
    ha_items = ["Het park", "Het bos", "Het natuurgebied", "Het landgoed", "De polder", "Het weiland", "Het maisveld"]
    ha_lengths = [100, 200, 250, 300, 400, 500, 600, 800, 1000, 1200, 1500, 2000]
    ha_widths = [50, 100, 150, 200, 250, 300, 400, 500, 600, 800, 1000]
    
    ha_pool = []
    for item in ha_items:
        for l in ha_lengths:
            for w in ha_widths:
                if l >= w:
                    area = l * w
                    # ensure the area divides perfectly into 10,000 for integer hectares
                    if area >= 10000 and area % 10000 == 0:
                        ha = area // 10000
                        ha_pool.append({
                            "type": "rectangle_hectare",
                            "text": f"{item} is {l} m lang en {w} m breed.",
                            "answer_m2": str(area),
                            "answer_ha": str(ha)
                        })

    # 3. Are
    are_items = ["Het schoolplein", "Het sportveld", "Het parkeerterrein", "Het gazon", "De akker", "De moestuin"]
    are_lengths = [20, 25, 30, 40, 50, 60, 70, 80, 100, 120, 150, 200, 250, 300, 400, 500]
    are_widths = [10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 100, 150, 200]
    
    are_pool = []
    for item in are_items:
        for l in are_lengths:
            for w in are_widths:
                if l >= w:
                    area = l * w
                    # ensure the area divides perfectly into 100 for integer ares
                    if area >= 100 and area % 100 == 0:
                        are = area // 100
                        are_pool.append({
                            "type": "rectangle_are",
                            "text": f"{item} is {l} m lang en {w} m breed.",
                            "answer_m2": str(area),
                            "answer_are": str(are)
                        })

    # 4. Triangle
    tri_bases = list(range(4, 25))
    tri_heights = list(range(4, 25))
    tri_pool = []
    for b in tri_bases:
        for h in tri_heights:
            # base * height must be even to yield integer area
            if (b * h) % 2 == 0:
                tri_pool.append({
                    "type": "triangle",
                    "text": "De oppervlakte is",
                    "base": b,
                    "height": h,
                    "answer_cm2": str((b * h) // 2)
                })

    # 5. Trapezoid
    trap_pool = []
    for b1 in range(4, 25):
        for b2 in range(2, b1):
            for h in range(2, 20):
                # (base1 + base2) * height must be even to yield integer area
                if ((b1 + b2) * h) % 2 == 0:
                    trap_pool.append({
                        "type": "trapezoid",
                        "text": "De oppervlakte is",
                        "base1": b1,
                        "base2": b2,
                        "height": h,
                        "answer_cm2": str(((b1 + b2) * h) // 2)
                    })

    questions = []
    seen_combinations = set()
    
    q_texts = [
        "Bereken de oppervlakte.",
        "Wat is de oppervlakte?",
        "Reken de oppervlakte uit.",
        "Bepaal de oppervlakte van de figuren."
    ]
    
    hints = [
        "Oppervlakte rechthoek = lengte × breedte. 1 ha = 10.000 m², 1 are = 100 m². Oppervlakte driehoek = (basis × hoogte) ÷ 2.",
        "Onthoud: oppervlakte rechthoek = lengte × breedte, 1 ha = 10.000 m², 1 are = 100 m², oppervlakte driehoek = basis × hoogte ÷ 2.",
        "Tip: Oppervlakte rechthoek is lengte keer breedte. Oppervlakte driehoek is basis keer hoogte gedeeld door 2. (1 ha = 10.000 m², 1 are = 100 m²)"
    ]

    output_dir = "/home/akib/Desktop/IIT/eduloop/Question_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "type57.json")

    while len(questions) < 6000:
        r1 = random.choice(rect_pool)
        r2 = random.choice(ha_pool)
        r3 = random.choice(are_pool)
        r4 = random.choice(tri_pool)
        r5 = random.choice(trap_pool)
        
        # signature to ensure absolute uniqueness of the composite 5 items
        sig = (r1["text"], r2["text"], r3["text"], r4["base"], r4["height"], r5["base1"], r5["base2"], r5["height"])
        if sig in seen_combinations:
            continue
            
        seen_combinations.add(sig)
        
        # copy dicts and inject unique structural ID per item
        data = [
            {**r1, "id": 1},
            {**r2, "id": 2},
            {**r3, "id": 3},
            {**r4, "id": 4},
            {**r5, "id": 5}
        ]
        
        questions.append({
            "id": str(len(questions) + 1),
            "type": "type57",
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
