import re, sys, random
sys.stdout.reconfigure(encoding='utf-8')

def make_vocalization_distractors(ar_word):
    """Generate 4 vocalized variants with different case endings (Dammah, Fathah, Kasrah, Tanween)"""
    base = re.sub(r'[\u064b-\u0652]$', '', ar_word.strip())
    opt_damma = base + 'ُ'
    opt_kasra = base + 'ِ'
    opt_fatha = base + 'َ'
    opt_tanween = base + 'ٌ' if not base.startswith('ال') else base + 'ُ'
    
    opts = [ar_word]
    for candidate in [opt_kasra, opt_damma, opt_fatha, opt_tanween]:
        if candidate != ar_word and candidate not in opts:
            opts.append(candidate)
    while len(opts) < 4:
        opts.append(base + 'ْ')
    random.shuffle(opts)
    return opts

def make_pronoun_distractors(answer_str):
    """Generate pronoun or gender variants"""
    pool = ["هُوَ فِي الْغُرْفَةِ", "هِيَ فِي الْمَطْبَخِ", "هُوَ فِي الْحَمَّامِ", "هُوَ عَلَى الْمَكْتَبِ", "هِيَ عَلَى السَّرِيرِ", "هُوَ فِي الْمَسْجِدِ", "هُوَ فِي الدُّكَّانِ"]
    opts = [answer_str]
    for p in pool:
        if p != answer_str and p not in opts:
            opts.append(p)
        if len(opts) == 4:
            break
    random.shuffle(opts)
    return opts

# Test
print("Vocalization for الْمَدْرَسَةِ:", make_vocalization_distractors("الْمَدْرَسَةِ"))
print("Pronoun for هُوَ فِي الْغُرْفَةِ:", make_pronoun_distractors("هُوَ فِي الْغُرْفَةِ"))
