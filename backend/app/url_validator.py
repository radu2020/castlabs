import re

def is_valid_url(url):
    """Check if the given URL has a proper structure."""
    if not url:
        return False
    
    # Create regular expression
    protocol = r'^(https?|ftp)://'  # Must start with http, https, or ftp
    domain = r'([a-zA-Z0-9.-]+)'  # Allow letters, numbers, dots, and dashes
    port = r'(:\d{1,5})?'  # Optional port number
    path = r'(/.*)?$'  # Optional path after domain
    
    pattern = f"{protocol}{domain}{port}{path}"
    
    # Match url against regular expression
    return re.match(pattern, url, re.IGNORECASE) is not None