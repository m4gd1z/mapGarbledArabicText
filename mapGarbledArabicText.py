# Arabic character mapping including diacritics
# There are 256 unicode Arabic characters. This script does not 
# map all of them, but should catch those commonly used.
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
    'Ò': 'ز',  # Zayn
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
    'Ä': 'ؤ',  # Waw with hamza
    'Æ': 'ئ',  # Ya with Hamza
    'Á': 'ء',  # Hamza
    'Â': 'أ',  # Alif with Hamza above (depends on author)
    'Ã': 'أ',  # Alif with Hamza above (depends on author)
    'Å': 'إ',  # Alif with Hamza below (newly added)

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
# Edit the paths to the input and output files
input_file_path = '/path/to/input.sql'
output_file_path = '/path/to/output.sql'

with open(input_file_path, 'r', encoding='utf-8') as file:
    garbled_text = file.read()

# Convert garbled text to Arabic
corrected_text = ''.join(windows_1256_to_arabic.get(char, char) for char in garbled_text)

# Write the corrected Arabic text to an output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(corrected_text)

print("Corrected Arabic text written to output.txt")
