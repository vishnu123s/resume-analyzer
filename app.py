resume = input("Paste Resume Skills:\n")

skills = resume.lower()
score = 0

print("\n===== ANALYSIS =====\n")

if "python" in skills:
    print("✅ Python Found")
    score += 20
else:
    print("❌ Python Missing")

if "sql" in skills:
    print("✅ SQL Found")
    score += 20
else:
    print("❌ SQL Missing")

if "html" in skills:
    print("✅ HTML Found")
    score += 20
else:
    print("❌ HTML Missing")

if "css" in skills:
    print("✅ CSS Found")
    score += 20
else:
    print("❌ CSS Missing")

if "cloud" in skills:
    print("✅ Cloud Found")
    score += 20
else:
    print("❌ Cloud Missing")

print(f"\nResume Score: {score}/100")