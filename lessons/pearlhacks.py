"""Pearl Hacks: Gender Bias and Hiring Process."""

# change pronouns 

def replace_pronouns(text):
    words = text.split()
    revised_words = []
    for word in words:
        if word.lower() == "she" or word.lower() == "he":
            revised_words.append("the applicant")
        else:
            revised_words.append(word)
    revised_text = " ".join(revised_words)
    return revised_text

def main():
    passage = input("Enter the passage of text: ")
    revised_passage = replace_pronouns(passage)
    print("Revised passage:")
    print(revised_passage)

if __name__ == "__main__":
    main()