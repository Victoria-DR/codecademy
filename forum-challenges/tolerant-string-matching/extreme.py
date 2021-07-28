def extremeMatch(message, snippet, decodings):
    # Render case insensitive
    message_alter = message.upper()
    snippet = snippet.upper()
    # Check if snippet is a substring of message
    if snippet in message_alter:
        return True

    # Convert decodings into a dictionary
    decoding_dict = {x[0]: x[1] for x in decodings}

    matches = False
    start = 0
    index = 0
    times_decoded = 0
    # Run while snippet is not yet determined to be in message
    while (not matches) and (start <= len(message_alter) - len(snippet)):
        # Check for cycles in decodings
        if times_decoded > len(decodings):
            return False

        # Check if letter is the same in message and snippet
        if message_alter[start + index] == snippet[index]:
            index += 1
            times_decoded = 0
        else:
            # Decode a character
            char_decoded = False
            for coded, decoded in decoding_dict.items():
                if coded == message_alter[start + index: start + index + len(coded)]:
                    message_alter = message_alter[:start + index] + message_alter[start + index:].replace(coded, decoded.upper(), 1)
                    times_decoded += 1
                    char_decoded = True
                    break
            # Repeat entire process with new start point
            if not char_decoded:
                return extremeMatch(message[start + 1:], snippet, decodings)

        # Determine if snippet is a substring of message
        if index == len(snippet):
            matches = True if (snippet.upper() in message_alter.upper()) else False
            break

    return matches
