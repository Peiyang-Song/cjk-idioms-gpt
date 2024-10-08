import re


# given input text that contains a list of idioms, extract all idioms
def extract_idioms(raw):

    # captures all text between (1) a number followed by a period and white
    # spaces and (2) a newline symbol
    # generated by ChatGPT

    pattern = r'(\d+\.\s*)(.*?)(?=\n)'

    # the last idiom may not end with a newline symbol
    # append it

    raw += '\n'

    # ChatGPT: The re.DOTALL flag is used here to ensure that the dot (.) in the
    # pattern matches newline characters as well, which is necessary if your
    # text spans multiple lines and you still want to capture everything up to
    # the first newline character after the number-period sequence.

    matches = re.findall(pattern, raw, flags=re.DOTALL)

    # the first element in each match is the number and the period
    return [match[1] for match in matches]

# same as extract_idioms, as both are extracting from a list
def extract_sentences(raw):
    return extract_idioms(raw)


# remove all irrelevant information from the idioms
def remove_irrelevant(text):
    # remove the content included between one pair of parentheses
    remove_english = re.sub(r'\(.*?\)', '', text)
    remove_japanese = re.sub(r'\（.*?\）', '', remove_english)

    # remove ascii characters, including letters, spaces, etc.
    remove_ascii = re.sub(r'[\x00-\x7F]+', '', remove_japanese)

    return remove_ascii

# get the score
def extract_score(text):
    # taking the digits that appeared first
    return int(re.search(r'\d+', text).group())