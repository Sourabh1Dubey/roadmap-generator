def generate_mermaid_code(input_data):
    # Initialize the Mermaid code variable
    mermaid_code = ''

    # Check if the input data is in the first format
    if 'choices' in input_data and len(input_data['choices']) > 0:
        message_content = input_data['choices'][0]['message']['content']
    # Check if the input data is in the second format
    elif 'result' in input_data:
        message_content = input_data['result']
    else:
        return mermaid_code

    # Check if backticks (`) are present in the message content
    if '```' in message_content:
        # Split the content by triple backticks to get the code block
        mermaid_section = message_content.split('```')[1].strip()
    elif '`' in message_content:
        # Split the content by single backticks to get the code block
        mermaid_section = message_content.split('`')[1].strip()
    else:
        return mermaid_code

    # Check if 'graph TD' or 'graph LR' or 'graph TB' is present in the mermaid section
    if 'graph TD' in mermaid_section or 'graph LR' in mermaid_section or 'graph TB' in mermaid_section:
        if 'graph TD' in mermaid_section:
            # Extract the Mermaid code after 'graph TD'
            mermaid_code = 'graph TD\n' + mermaid_section.split('graph TD', 1)[1].strip()
        elif 'graph LR' in mermaid_section:
            # Extract the Mermaid code after 'graph LR'
            mermaid_code = 'graph LR\n' + mermaid_section.split('graph LR', 1)[1].strip()
        elif 'graph TB' in mermaid_section:
            # Extract the Mermaid code after 'graph TB'
            mermaid_code = 'graph TB\n' + mermaid_section.split('graph TB', 1)[1].strip()

    # Replace '->' with '-->' only if '-->' is not already present
    mermaid_code = mermaid_code.replace(' -> ', ' --> ')

    # Find the index of 'clasDef' to remove extra content after it
    index_clas_def = mermaid_code.find('clasDef')
    if index_clas_def != -1:
        # Remove any content after 'clasDef'
        mermaid_code = mermaid_code[:index_clas_def].strip()

    return mermaid_code

