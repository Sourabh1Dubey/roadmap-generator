from flask import Flask, request, render_template
from filter import generate_line_with_keywords
from Main import make_api_call
from converter import generate_mermaid_code
from mermaid_key import add_links_to_mermaid
from trial import generate_html_with_mermaid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            textarea_content = request.form['textarea_content']
            
            # Generate the line with keywords
            line_with_keywords = generate_line_with_keywords(textarea_content)
            print("Line with Keywords:", line_with_keywords)
            
            # Make API call
            api_response = make_api_call(line_with_keywords)
            print(api_response)

            mermaid = generate_mermaid_code(api_response)
            print(mermaid)

            mermaid_code_with_links = add_links_to_mermaid(mermaid)
            print("Mermaid code after adding links:", mermaid_code_with_links)

            output = generate_html_with_mermaid(mermaid_code_with_links)
            return output
        
     
        return render_template('interface.html')
    except Exception as e:
        error_message = str(e)  # Get the error message
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
