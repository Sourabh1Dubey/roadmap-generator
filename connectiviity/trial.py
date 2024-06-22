def generate_html_with_mermaid(mermaid_code):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mermaid Example</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
        <style>
            body {{
                font-family: Arial, sans-serif;
  background: url(https://source.unsplash.com/TV2gg2kZD1o/1600x800);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                background-color: grey;
                padding: 30px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                border-radius: 12px;
                text-align: center;
                width: 80vw;
                height: 80vh;
                display: flex;
                justify-content: center;
                align-items: center;
                border: 1px solid #0097a7;
            }}
            .mermaid {{
                text-align: center;
                width: 100%;
                height: 100%;
            }}
            .mermaid svg {{
                width: 100%;
                height: 100%;
            }}
            h1 {{
                color: #00796b; /* Custom title color */
                margin-bottom: 20px;
            }}
            /* Custom CSS for links */
            .mermaid a {{
                text-decoration: none;  /* Remove underline */
                color: inherit;         /* Inherit the natural text color */
                transition: transform 0.3s; /* Smooth transition for transform */
            }}
            .mermaid a:hover {{
                color: #00796b;         /* Change color on hover */
                text-decoration: underline; /* Add underline on hover */
                transform: scale(1.1);  /* Scale up the text size on hover */
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="mermaid">
                {mermaid_code}
            </div>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true, themeCSS: `
                .node rect, .node circle {{
                    stroke-width: 24px;
                }}
                .node text {{
                    font-size: 18px;
                }}
                svg {{
                    font-size: 22px;
                }}
            ` }});
        </script>
    </body>
    </html>
    """
    return html_template
