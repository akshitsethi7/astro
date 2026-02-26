#!/usr/bin/env python3

# Test D7 Saptamsa calculation
SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
         "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]

def test_d7_calculation():
    print("=== TESTING D7 SAPTAMSA CALCULATION ===")
    
    # Your actual D7 chart shows Capricorn lagna
    # Your ascendant: Leo 20.33° (from script)
    asc_sign = 4  # Leo (index 4)
    asc_deg = 20.33  # 20.33° in Leo
    
    print(f"Ascendant: {SIGNS[asc_sign]} {asc_deg}°")
    print(f"Expected D7 lagna: Capricorn")
    print()
    
    # Current calculation: start from same sign, divide into 7 parts
    start = asc_sign  # Leo (4)
    part = int((asc_deg * 7) / 30.0)  # 20.33 * 7 / 30 = 4.74 → part 4
    result = (start + part) % 12  # (4 + 4) % 12 = 8 → Sagittarius
    
    print(f"Current calculation:")
    print(f"  Start: {SIGNS[start]} (index {start})")
    print(f"  Part: {part} (from {asc_deg * 7 / 30:.2f})")
    print(f"  Result: {SIGNS[result]} (index {result})")
    print(f"  Expected: Capricorn (index 9)")
    print()
    
    # To get Capricorn (index 9), we need: start + part = 9
    # So: 4 + part = 9 → part = 5
    # But: 20.33 * 7 / 30 = 4.74 → part 4
    
    # The issue is that the traditional D7 rule is different
    # Let me test different approaches
    
    print("Testing different D7 approaches:")
    
    # Approach 1: Maybe we need to use total degrees
    total_deg = asc_sign * 30 + asc_deg  # 4 * 30 + 20.33 = 140.33
    part1 = int(total_deg // (30/7))  # 140.33 / 4.29 = 32.7 → part 32
    result1 = part1 % 12  # 32 % 12 = 8 → Sagittarius
    print(f"Approach 1 (total degrees): {SIGNS[result1]} (part {part1})")
    
    # Approach 2: Maybe we need different starting point
    # For Leo, maybe start from a different sign
    for start_test in range(12):
        part_test = int((asc_deg * 7) / 30.0)
        result_test = (start_test + part_test) % 12
        if result_test == 9:  # Capricorn
            print(f"Approach 2: Start from {SIGNS[start_test]} gives Capricorn")
            break
    
    # Approach 3: Maybe the rule is completely different
    # Some sources say D7 uses a different method
    print("Traditional D7 rule might be different from what I implemented")

if __name__ == "__main__":
    test_d7_calculation()
