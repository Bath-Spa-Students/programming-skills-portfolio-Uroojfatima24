glossary = {
    'Identation': 'Indentation is the use of spaces at the beginning of a line to define the structure and scope of code blocks.',
    'Comment': 'A comment is a text note within the code that is not executed and is used to provide explanations or for human readers.',
    'Variable': 'A symbolic name for a value that can be stored and manipulated in a program.',
    'String': 'A string is a sequence of characters enclosed in single, double, or triple quotes, used to represent text data.',
    'List': 'An ordered collection of elements, which can be of different data types, enclosed in square brackets, and separated by commas.'
}

# Add five more terms to the glossary
glossary['Dictionary'] = 'A collection of key-value pairs.'
glossary['Float'] = 'A data type in Python used to represent real numbers with a decimal point.'
glossary['Boolean'] = 'A data type with two values: True or False.'
glossary['Module'] = 'A file containing Python code that can be imported and used in other programs.'
glossary['Integer'] = 'A data type in Python used to represent whole numbers without a decimal point.'

# Loop through the dictionary and print the terms and their meanings
for term, definition in glossary.items():
    print(f"{term}:\n{definition}\n")
