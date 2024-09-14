def reverse_words_in_string(s):
    # Split the string into words
    words = s.split()
    
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back into a single string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

# Example usage
input_string = "Hello World"
reversed_string = reverse_words_in_string(input_string)
print(reversed_string)