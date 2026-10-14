import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Load the base dataset
with open('data/madinah_books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper to build a question object
def make_q(q_id, b_num, u_num, t_num, badge_ar, badge_ur, badge_en, t_title_ar, t_title_ur, t_title_en, g_ur, g_en, q_type, p_ar, p_ur, p_en, ans, opts, em, hint_ur, hint_en):
    # Ensure answer is in options
    if ans not in opts:
        opts[0] = ans
    return {
        "id": q_id,
        "book": b_num,
        "unit_num": u_num,
        "tamreen_num": t_num,
        "badge_ar": badge_ar,
        "badge_ur": badge_ur,
        "badge_en": badge_en,
        "tamreen_title_ar": t_title_ar,
        "tamreen_title_ur": t_title_ur,
        "tamreen_title_en": t_title_en,
        "grammar_goal_ur": g_ur,
        "grammar_goal_en": g_en,
        "type": q_type,
        "strict_tashkeel": True,
        "prompt_ar": p_ar,
        "prompt_ur": p_ur,
        "prompt_en": p_en,
        "answer": ans,
        "options": opts,
        "emoji": em,
        "hint_ur": hint_ur,
        "hint_en": hint_en,
        "explanation_ur": f"درست جواب: '{ans}' ({g_ur})",
        "explanation_en": f"Correct answer: '{ans}' ({g_en})"
    }

print("make_q helper ready")
