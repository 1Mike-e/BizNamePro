import random
import spacy

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Define a list of questions to gather information from the user
questions = [
    "What is the primary product or service of your business idea?",
    "What words or adjectives describe your business (e.g., innovative, local, sustainable)?",
    "What is the target audience or customer demographic?",
    "What are some keywords related to your business idea?",
]

# Initialize an empty dictionary to store user responses
user_responses = {}


# Tokenize text using spaCy
def tokenize_text(text):
    doc = nlp(text)
    return [token.text for token in doc]


# Extract keywords from text
def extract_keywords(text):
    keywords = []
    doc = nlp(text)

    for token in doc:
        if token.pos_ in ["NOUN", "ADJ"]:  # Consider nouns and adjectives
            keywords.append(token.text.lower())

    return keywords


# Ask the user each question and store their responses
for question in questions:
    response = input(question + " ")
    user_responses[question] = response


# Generate a business name based on keywords
def generate_business_name_with_nlp(user_responses):
    keywords = extract_keywords(user_responses["What is the primary product or service of your business idea?"])
    adjectives = extract_keywords(
        user_responses["What words or adjectives describe your business (e.g., innovative, local, sustainable)?"])
    audience = extract_keywords(user_responses["What is the target audience or customer demographic?"])

    # Combine and shuffle keywords for a name suggestion
    combined_keywords = keywords + adjectives + audience
    random.shuffle(combined_keywords)

    # Join shuffled keywords to create a business name suggestion
    name_suggestion = " ".join(combined_keywords)

    return name_suggestion


# Generate and display a business name suggestion with NLP
suggested_name_with_nlp = generate_business_name_with_nlp(user_responses)
print(f"Based on your answers and NLP analysis, here's a suggested business name: {suggested_name_with_nlp}")
