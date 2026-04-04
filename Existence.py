import time

def run_system_check():
    print("--- TruthOS v21.0: System Design of Life ---")
    time.sleep(1)

    levels = [
        ("LEVEL 1", "Creator", "Phone has a maker; Humans are 100x more complex. Soul = Hardware."),
        ("LEVEL 2", "One Boss", "Nature moves in 1 direction. Many bosses = System crash."),
        ("LEVEL 3", "The Exam", "The Teacher stays quiet during the exam. Pain is a test."),
        ("LEVEL 4", "The GPS", "Heart is just a compass. Religion is the GPS map. Don't 'agak agak'."),
        ("LEVEL 5", "Versions", "One core code, different languages. Race to do good. No 'Force Install'.")
    ]

    for lvl, title, logic in levels:
        print(f"\n[{lvl}] {title}")
        print(f">> {logic}")
        time.sleep(0.5)

    print("\n" + "="*40)
    print("FINAL ANALYSIS: Finding the 'Original File'")
    print("="*40)
    
    checks = [
        "One Creator (No partners)",
        "One Message, Language & Direction (Unity)",
        "Zero Edits (Memorized perfectly)",
        "Science Facts (Proven data)"
    ]

    for check in checks:
        print(f"[✔] {check}")

    print("\n>>> RESULT: Islam is the 100% Original OS.")
    print(">>> Status: Matches the Science of the Universe.")
    print("="*40)

if __name__ == "__main__":
    run_system_check()
