import json
import random
import os

def int_to_dutch(n):
    ones = ["", "een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen",
            "tien", "elf", "twaalf", "dertien", "veertien", "vijftien", "zestien", "zeventien", "achttien", "negentien"]
    tens = ["", "", "twintig", "dertig", "veertig", "vijftig", "zestig", "zeventig", "tachtig", "negentig"]
    
    if n == 0: 
        return "nul"
    if n < 20: 
        return ones[n]
    if n < 100:
        t, o = divmod(n, 10)
        if o == 0: 
            return tens[t]
        # Rules for trema (diaeresis) in Dutch numbers
        connector = "ën" if o in [2, 3] else "en"
        return ones[o] + connector + tens[t]
    if n < 1000:
        h, r = divmod(n, 100)
        prefix = "honderd" if h == 1 else ones[h] + "honderd"
        if r == 0: 
            return prefix
        # Add "en" for remainders up to 12 as per common Dutch spelling
        if r <= 12:
            return prefix + "en" + int_to_dutch(r)
        return prefix + int_to_dutch(r)

def generate_type80_questions(num_questions=6000):
    questions = []
    seen_combinations = set()
    
    # We will generate thousands from 10,000 to 999,000
    pool = list(range(10, 1000))
    
    while len(questions) < num_questions:
        selected_ks = random.sample(pool, 6)
        
        signature = tuple(sorted(selected_ks))
        if signature in seen_combinations:
            continue
            
        seen_combinations.add(signature)
        
        data_items = []
        for i, k in enumerate(selected_ks):
            words = int_to_dutch(k) + "duizend"
            val = k * 1000
            data_items.append({
                "id": f"r{i+1}",
                "words": words,
                "value": val
            })
            
        question_id = str(len(questions) + 1)
        question_obj = {
            "id": question_id,
            "type": "type80",
            "subject": "Rekenen",
            "metadata": {
                "question": "Schrijf het getal in cijfers.",
                "hint": "Schrijf het getal in cijfers. Je mag eventueel punten gebruiken om de duizendtallen te scheiden (bijv. 250.000).",
                "data": data_items
            }
        }
        questions.append(question_obj)
        
    return questions

if __name__ == "__main__":
    questions = generate_type80_questions(6000)
    
    output_path = "/home/akib/Desktop/IIT/eduloop/Question_output/type80.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4, ensure_ascii=False)
        
    print(f"Generated {len(questions)} questions and saved to {output_path}")
