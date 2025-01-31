"""
Little Python is a chatbot created to tell you about python modules
based on user input.
Setup:
Kindly downoad the necessary packages using the following commands below one after the other on your command prompt:
    pip install nltk spacy
    python -m nltk.downloader all
    python -m spacy download en_core_web_sm
"""

import inspect
import random
import pkgutil
import nltk
from nltk.tokenize import word_tokenize

def get_installed_modules():
    """
    Returns a list of all installed Python modules.

    Returns:
        A list of strings, where each string is the name of an installed module.
    """
    modules = []
    for importer, modname, ispkg in pkgutil.iter_modules():
        modules.append(modname)
    return modules

def suggest():
    """
    Suggests a random Python module.
    
    Returns:
        A Python module chosen at random.
    """
    modules = get_installed_modules()
    random_module = random.choice(modules)
    return random_module
    

def get_module_docstring(module_name):
    """
    Gets the docstring of the specified Python module.

    Args:
        module_name: The name if the Python module.

    Returns:
        The docstring of the module, or a default message if the module
        cannot be found or has no docstring.
    """
    bot = 'Little Lithium'
    try:
        module = __import__(module_name)
        docstring = inspect.getmodule(module).__doc__
        if docstring:
            return docstring
        else:
            print(f"{bot}: Unfortunately, no docstring found for module '{module_name}'.")
            print('Let me suggest a module that has a docstring.')            
            random_module = suggest()
            print(f"Suggestion: '{random_module}'")
            return random_module
    except ImportError:
        return f"Module '{module_name}' not found."


def preprocess(input_sentence):
    """
    Processes a sentence breaking it down to individual tokens
    and assigning part-of-speech (pos) tags to each token.

    Args:
        input_sentence: This is the sentence to be processed.
        
    Returns:
        Part-of-speech (pos) tags for each token of the sentence.
    """
    
    words = word_tokenize(input_sentence)
    return words

def recognize_intent(tokens):
    """
    Analyze the tokens and their part-of-speech tags.

    Args:
        tokens: A list of each token and their pos tag.

    Returns:
        True
    """
    keywords = get_installed_modules()
    tokens = [token.lower() for token in tokens]
    # if any(token in keywords for token in tokens):
    for i in tokens:
        if i in keywords:
            module = i
            return module
        else:
            print('Seems you did not include a valid Python module in your query.\nLet me suggest one for you.')
            random_module = suggest()
            print(f"Suggestion: '{random_module}'")
            return random_module



# Interact with the chatbot   
def chatbot():
    """
    Processes user input and returns an appropriate response.

    Returns:
        Appropriate response.
    """
    bot = 'Little Lithium'
    print(f'Hi! I am {bot}. \nDisclaimer: Responses are obtained verbatim from the Python official Docstrings for each module')   # expand
    user = input(f'{bot}: What is your name?\nUser: ')
    print(f'Hello, {user}, kindly ask me about any python module.')
    while True:
        
        user_input = input(f'{user}: ')
        if user_input.lower() in ['quit', 'bye', 'exit']:
            break
        processed_input = preprocess(user_input)
        intent = recognize_intent(processed_input)
        response = get_module_docstring(intent)    #intent
        print(f'\n{bot}: \n{intent}: ', response)
        print(f"{bot}: For more information about '{intent}' kindly visit input_website_link\n")
        print(f'{bot}: Ask about another Python module.')
        
    
    
    # return response
    # Add default responses
    # Add Try Except



chatbot()
