import re

def extract_labels(mermaid_code):
    # Define a regular expression pattern to find node labels
    label_pattern = r'\b[A-Za-z_][A-Za-z0-9_\s\']*?(?=\])\b'
    
    # Find all matches of node labels in the Mermaid code
    labels = re.findall(label_pattern, mermaid_code)
    
    # Remove duplicates
    unique_labels = set(labels)
    
    return unique_labels

# Test the function
mermaid_code = """graph LR
A[User] --> B[Search Train]
 B --> C[Select Train]
 C --> D[Select Date]
 D --> E[Select Time]
 E --> F[Enter Pasenger Details]
 F --> G[Review Boking]
 G --> H[Bok Ticket]
 H --> I[Confirmation]
 I --> J[Print/Save Ticket]
 J --> K[Home]
 K --> A[Home]
"""
labels = extract_labels(mermaid_code)
print("Labels extracted:", labels)
