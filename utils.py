def sanitize_text(text):
    """
    Sanitize extracted text data by removing unwanted characters and whitespace.

    Args:
        text (str): Text data to be sanitized.

    Returns:
        str: Sanitized text data.
    """
    # Implement your text sanitization logic here
    # Example: Removing special characters and extra whitespace
    sanitized_text = text.replace('\n', '').strip()
    return sanitized_text

