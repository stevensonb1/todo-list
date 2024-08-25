import uuid

def generate_unique_id():
    """
    Generate and return a unique identifier based on RFC 4122.
    """ 
    return str(uuid.uuid4())

def split_string(string: str, max_characters: int):
    """
    Splits a string into multiple lines, each with 
    a maximum number of characters.
    """
    lines = []
    current_line = ""

    for word in string.split():
        if len(current_line) + len(word) + 1 <= max_characters:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    
    if current_line:
        lines.append(current_line.strip())

    return '\n'.join(lines)
