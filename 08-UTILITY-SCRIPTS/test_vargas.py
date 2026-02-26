#!/usr/bin/env python3

# Test varga calculations manually
SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
         "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]

def test_varga_calculations():
    print("=== TESTING VARGA CALCULATIONS ===")
    
    # Your actual D7 chart shows Capricorn lagna
    # Your actual D9 chart shows Leo lagna  
    # Your actual D60 chart shows Gemini lagna
    
    print("\n--- D7 Saptamsa Test ---")
    print("Expected: Capricorn lagna")
    
    # Test different approaches for D7
    asc_sign = 4  # Leo (your actual ascendant)
    asc_deg = 20.33  # Corrected ascendant from script
    
    print(f"Ascendant: {SIGNS[asc_sign]} {asc_deg}°")
    
    # Approach 1: My current logic
    if asc_sign % 2 == 0:  # Even index (4) - start from same sign
        start = asc_sign
    else:  # Odd index - start from 7th sign
        start = (asc_sign + 6) % 12
    
    part = int((asc_deg * 7) / 30.0)
    result1 = (start + part) % 12
    print(f"Approach 1: {SIGNS[result1]} (start={SIGNS[start]}, part={part})")
    
    # Approach 2: Traditional calculation
    # D7: For Leo (4), start from Leo, divide into 7 parts
    start2 = asc_sign
    part2 = int((asc_deg * 7) / 30.0)
    result2 = (start2 + part2) % 12
    print(f"Approach 2: {SIGNS[result2]} (start={SIGNS[start2]}, part={part2})")
    
    # Approach 3: Check if we need different logic
    # Maybe the issue is in how we're calculating the parts
    total_deg = asc_sign * 30 + asc_deg
    part3 = int(total_deg // (30/7))
    result3 = part3 % 12
    print(f"Approach 3: {SIGNS[result3]} (total_deg={total_deg}, part={part3})")
    
    print("\n--- D9 Navamsa Test ---")
    print("Expected: Leo lagna")
    
    # D9: For Leo (4), start from Leo, divide into 9 parts
    start_d9 = asc_sign
    part_d9 = int((asc_deg * 9) / 30.0)
    result_d9 = (start_d9 + part_d9) % 12
    print(f"D9: {SIGNS[result_d9]} (start={SIGNS[start_d9]}, part={part_d9})")
    
    # Test the traditional D9 rule
    if asc_sign % 2 == 0:  # Even index (4) - start from Aries
        start_trad = 0
    else:  # Odd index - start from Leo
        start_trad = 4
    
    part_trad = int((asc_deg * 9) / 30.0)
    result_trad = (start_trad + part_trad) % 12
    print(f"D9 Traditional: {SIGNS[result_trad]} (start={SIGNS[start_trad]}, part={part_trad})")
    
    # Corrected D9 rule: always start from same sign
    start_corrected = asc_sign
    part_corrected = int((asc_deg * 9) / 30.0)
    result_corrected = (start_corrected + part_corrected) % 12
    print(f"D9 Corrected: {SIGNS[result_corrected]} (start={SIGNS[start_corrected]}, part={part_corrected})")
    
    # Test different D9 approaches
    print("\n--- D9 Alternative Approaches ---")
    
    # Approach 1: Maybe we need to reverse the calculation
    # If we want Leo (4) as result, and we start from Leo (4), then part must be 0
    # But 20.33° × 9 ÷ 30 = 6.099, not 0
    
    # Approach 2: Maybe the rule is different for different degrees
    # Let's test different degree ranges
    for deg in [0, 3.33, 6.67, 10, 13.33, 16.67, 20, 23.33, 26.67]:
        part_test = int((deg * 9) / 30.0)
        result_test = (asc_sign + part_test) % 12
        print(f"Degree {deg}°: part={part_test}, result={SIGNS[result_test]}")
    
    # Approach 3: Maybe we need to use a different base calculation
    # Some sources say D9 uses a different method
    
    print("\n--- D60 Shastiamsa Test ---")
    print("Expected: Gemini lagna")
    
    # D60: For Leo (4), start from Leo, divide into 60 parts
    start_d60 = asc_sign
    part_d60 = int((asc_deg * 60) / 30.0)
    result_d60 = (start_d60 + part_d60) % 12
    print(f"D60: {SIGNS[result_d60]} (start={SIGNS[start_d60]}, part={part_d60})")

if __name__ == "__main__":
    test_varga_calculations()
