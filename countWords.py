intro = input("Enter your Introduction: ")

characterCount = 0
wordCount = 1

for character in intro:
    characterCount += 1
    
    if character == " ":
        wordCount += 1

print("Number of Words:", wordCount)
print("Number of Characters:", characterCount)