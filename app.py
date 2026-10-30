resume = input("Paste Resume Skills:\n")

skills = resume.lower()
score = 0
missing = []

print("\n===== ANALYSIS =====\n")

for skill in ["python", "sql", "html", "css", "cloud"]:

    if skill in skills:
        print(f"✅ {skill.upper()} Found")
        score += 20
    else:
        print(f"❌ {skill.upper()} Missing")
        missing.append(skill)

print(f"\nResume Score: {score}/100")

print("\nSuggestions:")

if missing:
    for skill in missing:
        print(f"- Learn {skill.upper()}")
else:
    print("Excellent Resume!")