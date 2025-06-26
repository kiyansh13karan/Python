# 1. escape sequence character 

name = "KARAN\n"  # Adding a newline character at the end of the string
print("Original string with escape sequence character is : ", name)

# 2. Using escape sequence characters
escaped_name = "KARAN\tNAYAL"  # Adding a tab character between names
print("String with escape sequence characters (tab) is : ", escaped_name)

# 3. Using backslash to escape quotes
escaped_quotes = "KARAN said, \"Hello!\""  # Escaping double quotes
print("String with escaped quotes is : ", escaped_quotes)

# 4. Using backslash to escape single quotes
escaped_single_quote = 'KARAN said, \'Hello!\''  # Escaping single quotes
print("String with escaped single quotes is : ", escaped_single_quote)

# 5. Using backslash to escape backslash
escaped_backslash = "KARAN\\NAYAL"  # Escaping backslash
print("String with escaped backslash is : ", escaped_backslash)

# 6. Using raw string to avoid escape sequences
raw_string = r"KARAN\nNAYAL"  # Raw string treats backslashes
print("Raw string (no escape sequences) is : ", raw_string)

# 7. Using triple quotes for multi-line strings
multi_line_string = """KARAN
NAYAL
This is a multi-line string."""
print("Multi-line string is : ", multi_line_string)

# 8. Using escape sequence for carriage return
carriage_return_string = "KARAN\rNAYAL"  # Carriage return
print("String with carriage return is : ", carriage_return_string)

# 9. Using escape sequence for backspace
backspace_string = "KARAN\bNAYAL"  # Backspace
print("String with backspace is : ", backspace_string)

# 10. Using escape sequence for form feed
form_feed_string = "KARAN\fNAYAL"  # Form feed
print("String with form feed is : ", form_feed_string)

# 11. Using escape sequence for vertical tab
vertical_tab_string = "KARAN\vNAYAL"  # Vertical tab
print("String with vertical tab is : ", vertical_tab_string)

# 12. Using escape sequence for octal value
octal_string = "KARAN\101\102\103"  # Octal value for 'A', 'B', 'C'
print("String with octal values is : ", octal_string)

# 13. Using escape sequence for hexadecimal value
hexadecimal_string = "KARAN\x41\x42\x43"  # Hexadecimal
# value for 'A', 'B', 'C'
print("String with hexadecimal values is : ", hexadecimal_string)

# 14. Using escape sequence for Unicode characters
unicode_string = "KARAN\u0041\u0042\u0043"  #
# Unicode characters for 'A', 'B', 'C'
print("String with Unicode characters is : ", unicode_string)

# 15. Using escape sequence for Unicode code point
unicode_code_point_string = "KARAN\U00000041\U00000042\U00000043"  # Unicode code points for 'A', 'B', 'C'
print("String with Unicode code points is : ", unicode_code_point_string)

# 16. Using escape sequence for null character
null_character_string = "KARAN\0NAYAL"  # Null character
print("String with null character is : ", null_character_string)

# 17. Using escape sequence for single character
single_character_string = "KARAN\c"  # Single character escape sequence (not
# standard, but for demonstration)
print("String with single character escape sequence is : ", single_character_string)

# 18. Using escape sequence for double character
double_character_string = "KARAN\cc"  # Double character escape sequence (not
# standard, but for demonstration)
print("String with double character escape sequence is : ", double_character_string)

# 19. Using escape sequence for hexadecimal escape sequence 
hex_escape_string = "KARAN\x63\x61\x72"  # Hexadecimal escape sequence for 'c', 'a', 'r'
print("String with hexadecimal escape sequence is : ", hex_escape_string)

# 20. Using escape sequence for octal escape sequence
octal_escape_string = "KARAN\143\141\162"  # Octal escape sequence for 'c', 'a', 'r'
print("String with octal escape sequence is : ", octal_escape_string)

# 21. Using escape sequence for Unicode escape sequence
unicode_escape_string = "KARAN\u0063\u0061\u0072"
# Unicode escape sequence for 'c', 'a', 'r'
print("String with Unicode escape sequence is : ", unicode_escape_string)

# 22. Using escape sequence for Unicode code point escape sequence
unicode_code_point_escape_string = "KARAN\U00000063\U00000061\U00000072"
# Unicode code point escape sequence for 'c', 'a', 'r'
print("String with Unicode code point escape sequence is : ", unicode_code_point_escape_string)

# 23. Using escape sequence for combining characters
combining_characters_string = "KARAN\u0301NAYAL"  # Combining character (acute accent)
print("String with combining characters is : ", combining_characters_string)

# 24. Using escape sequence for control characters
control_characters_string = "KARAN\bNAYAL"  # Backspace control character
print("String with control characters is : ", control_characters_string)

# 25. Using escape sequence for special characters
special_characters_string = "KARAN\!NAYAL"  # Special character (exclamation mark)
print("String with special characters is : ", special_characters_string)


