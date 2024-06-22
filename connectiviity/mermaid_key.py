import re

def add_links_to_mermaid(mermaid_code):
    # Define a regular expression pattern to find node labels
    label_pattern = r'(\b\w+\b)\[(.*?)\]'
    
    # Find all matches of node labels in the Mermaid code
    labels = re.findall(label_pattern, mermaid_code)
    
    # Format labels with Wikipedia links without target="_blank"
    modified_mermaid_code = mermaid_code
    for label_id, text in labels:
        keyword = text.strip()
        link = f'https://www.wikipedia.org/wiki/{keyword.replace(" ", "_")}'
        modified_label = f'{label_id}[<a href="{link}">{keyword}</a>]'
        modified_mermaid_code = modified_mermaid_code.replace(f'{label_id}[{text}]', modified_label)
    
    return modified_mermaid_code
