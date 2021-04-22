def basicMatch(message, snippet):
    # Check without regard to case if snippet is a substring of message
    return snippet.upper() in message.upper()

# print(basicMatch("Codecademy taught me to code", "code"))
# print(basicMatch("A really long string", "on"))
# print(basicMatch("Welcome to the internet", "hello"))
# print(basicMatch("CaseInsEnSiTiVE", "caseinsensitive"))

def intermediateMatch(message, snippet, decodings):
    # Render case insensitive
    message_alter = message.upper()
    snippet = snippet.upper()
    # Check if snippet is a substring of message
    if snippet in message_alter:
        return True

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    # Find first occurence of first character in snippet
    start = message_alter.find(snippet[0])
    # Determine if the first character of snippet is not encoded in message
    if (start == -1) and (snippet[0] not in decoding_dict.values()):
        return False

    # Find all possiblilities of decoding the first character in snippet
    possible_start_decodings = {}
    for coded, decoded in decoding_dict.items():
        if (decoded == snippet[0]) and (message_alter.find(decoded) <= start):
            possible_start_decodings[coded] = None
    
    earliest = []
    # Find earliest occurence of any possibile decoding
    for possibility in possible_start_decodings:
        possible_start_decodings[possibility] = message_alter.find(possibility)
        if (earliest == []) or (earliest[1] < possible_start_decodings[possibility]):
            earliest = [possibility, possible_start_decodings[possibility]]

    if earliest:
        # Decode first character of snippet in message
        message_alter = message_alter.replace(earliest[0], snippet[0], 1)
        # Find new first occurence of first character in snippet
        start = message_alter.find(snippet[0])

    matches = False
    index = 1
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message_alter) - len(snippet)):
        # Check if letter is the same in message and snippet
        if message_alter[start + index] == snippet[index]:
            index += 1
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message_alter[start + index: start + index + len(coded)]:
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded, 1)
                    # Allow for decoding to occur only once
                    index += 1
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                return intermediateMatch(message[start + 1:], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            matches = True if (snippet.upper() in message_alter.upper()) else False
            break

    return matches

# print(intermediateMatch("Codecademy is great", "codecademy", []))
# print(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
# print(intermediateMatch("Codec%65demy is great", "codec%65demy", [["%65", "A"]]))
# print(intermediateMatch("Codec%65demy is great", "codecademy", [["%65", "A"], ["%67", "D"]]))
# print(intermediateMatch("Co%67ec%65demy is great", "codec%65demy", [["%65", "A"], ["%67", "D"]]))
# print(intermediateMatch("Co%67eca%68emy is great", "codecademy", [["%67", "D"], ["%68", "D"]]))
# print(intermediateMatch("Co%67eca%67emy is great", "co%67ecademy", [ ["%67", "D"]]))
# print(intermediateMatch("Codecademy is great", "codec%65demy", [["%65", "A"]]))
# print(intermediateMatch("abc%6efg", "abcdefg", [["e", "d"], ["%6", "e"]]))

def hardMatch(message, snippet, decodings):
    # Render case insensitive
    message_alter = message.upper()
    snippet = snippet.upper()
    # Check if snippet is a substring of message
    if snippet in message_alter:
        return True

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    # Find first occurence of first character in snippet
    start = message_alter.find(snippet[0])
    # Determine if the first character of snippet is not encoded in message
    if (start == -1) and (snippet[0] not in decoding_dict.values()):
        return False

    # Find decoding path to first character in snippet
    path = [snippet[0]]
    added_new = True
    while (path[-1] not in message_alter[:message_alter.find(path[-1])]) and added_new:
        added_new = False
        # Add new point along path
        for coded, decoded in decoding_dict.items():
            if decoded == path[-1]:
                path.append(coded.upper())
                added_new = True

    # Decode first character of snippet in message
    if path[-1] in message_alter:
        message_alter = message_alter.replace(path[-1], path[0], 1)
        # Find new first occurence of first character in snippet
        start = message_alter.find(snippet[0])

    matches = False
    index = 1
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message_alter) - len(snippet)):
        # Check if letter is the same in message and snippet
        if message_alter[start + index] == snippet[index]:
            index += 1
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message_alter[start + index: start + index + len(coded)]:
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded, 1)
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                return intermediateMatch(message[start + 1:], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            matches = True if (snippet.upper() in message_alter.upper()) else False
            break

    return matches

# print(hardMatch("Codecademy is great", "codecademy", []))
# print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "A"]]))
# print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "A"]]))
# print(hardMatch("Codec%65demy is great", "codecademy", [["%65", "$10"], ["$10", "B"]]))
