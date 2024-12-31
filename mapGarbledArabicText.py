# Define the mapping
# Comprehensive mapping including diacritics
# Comprehensive mapping for all 256 Arabic characters
# Comprehensive mapping for Arabic characters including previously missing characters
# Comprehensive mapping for Arabic characters with corrections
# Comprehensive mapping for Arabic characters with corrections
# Comprehensive mapping for Arabic characters including previously missing characters
windows_1256_to_arabic = {
    # Arabic letters
    'Ç': 'ا',  # Alif
    'È': 'ب',  # Ba
    'Ê': 'ت',  # Ta
    'Ë': 'ث',  # Tha
    'Ì': 'ج',  # Jeem
    'Í': 'ح',  # Ha
    'Î': 'خ',  # Kha
    'Ï': 'د',  # Dal
    'Ð': 'ذ',  # Thal
    'Ñ': 'ر',  # Ra
    'Ò': 'ز',  # Zay
    'Ó': 'س',  # Seen
    'Ô': 'ش',  # Sheen
    'Õ': 'ص',  # Sad
    'Ö': 'ض',  # Dad
    'Ø': 'ط',  # Tah
    'Ù': 'ظ',  # Zah
    'Ú': 'ع',  # Ain
    'Û': 'غ',  # Ghayn
    'Ý': 'ف',  # Fa
    'Þ': 'ق',  # Qaf
    'ß': 'ك',  # Kaf
    'á': 'ل',  # Lam
    'ã': 'م',  # Meem
    'ä': 'ن',  # Noon
    'å': 'ه',  # Ha
    'æ': 'و',  # Waw
    'í': 'ي',  # Ya
    'ì': 'ي',  # Ya (2nd expected character)
    'É': 'ه',  # Ta Marbuta
    'Ü': 'ى',  # Alif Maqsura
    'Ä': 'ؤ',  # Waw with hamza was 'ئ',  # Ya with Hamza
    'Æ': 'ئ',  # Ya with Hamza
    'Á': 'ء',  # Hamza
    'Â': 'أ',  # Alif with Hamza
    'Å': 'إ',  # Alif with Hamza below (newly added)
    'Ã': 'أ',  # Alif with Hamza above

    # Diacritics
    'à': 'ً',  # Tanween Fath
    'ð': 'ً',  # Tanween Fath 2 
    'â': 'ٍ',  # Tanween Kasra
    'ã': 'م',# fixed from 'ٌ',  # Tanween Dhamma
    'î': 'َ',  # Fathah
    'ï': 'ِ',  # Kasrah
    'ø': 'ُ',  # Dhammah
    'ó': 'ْ',  # Sukoon
    'ò': 'ٰ',  # Madda
    'õ': 'ٓ',  # Hamzat Wasl
    'ú': 'ٔ',  # Hamza

    # Arabic punctuation
    '¢': '،',  # Arabic comma
    '£': '؛',  # Arabic semicolon
    '¥': '؟',  # Arabic question mark
    '¦': '٭',  # Arabic asterisk
    '¡': '۔',  #Arabic full stop

    # Additional characters for completeness
    ' ': ' ',  # Space
    
    # Add more mappings as necessary for other characters
}

# Read garbled text from an input file
input_file_path = '/Users/m2/Desktop/input.sql'
output_file_path = '/Users/m2/Desktop/output.sql'

with open(input_file_path, 'r', encoding='utf-8') as file:
    garbled_text = file.read()

# Convert garbled text to Arabic
corrected_text = ''.join(windows_1256_to_arabic.get(char, char) for char in garbled_text)

# Write the corrected Arabic text to an output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(corrected_text)

print("Corrected Arabic text written to output.txt")
