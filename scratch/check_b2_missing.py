from build_b2_expanded_curriculum import get_b2_complete_curriculum

u = get_b2_complete_curriculum()
missing = [i for i in range(1, 32) if i not in u]
print(f"Missing units in Book 2: {missing}")
