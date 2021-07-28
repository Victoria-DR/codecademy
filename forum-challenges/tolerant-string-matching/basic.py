def basicMatch(message, snippet):
    # Check without regard to case if snippet is a substring of message
    return snippet.upper() in message.upper()
