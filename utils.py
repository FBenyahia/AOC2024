def parse(file_path):
    """Create list of line

    Args:
        file_path (str): file path of the file you want to parse...

    Returns:
        List (List): List of line 
    """
    l = []
    with open(file_path, 'r') as f:
        for line in f:
            l.append(line)
        return l 

