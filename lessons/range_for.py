"""Use of range in For Loops"""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
                    
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")