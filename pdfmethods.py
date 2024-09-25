from reportlab.platypus import TableStyle, Spacer, KeepTogether
from reportlab.platypus import SimpleDocTemplate, Paragraph, ListFlowable, ListItem, Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import re
from bs4 import BeautifulSoup

from reportlab.platypus import Image, Table

styles = getSampleStyleSheet()
heading_one_style = ParagraphStyle(name='Heading1', parent=styles['Heading1'], fontSize=14, spaceAfter=6)
heading_two_style = ParagraphStyle(name='Heading2', parent=styles['Heading2'], fontSize=12, spaceAfter=6)
heading_three_style = ParagraphStyle(name='Heading3', parent=styles['Heading3'], fontSize=10, spaceAfter=6)
paragraph_style = ParagraphStyle(name='Normal', parent=styles['Normal'], fontSize=10, spaceAfter=6)





custom_italic_style = ParagraphStyle(
    name='Italic8',
    parent=getSampleStyleSheet()['Normal'],  
    fontName='Helvetica-Oblique',           
    fontSize=8,                              
    leading=10,                              
)

def create_image_paragraph_table(image_path, page_width_cm=20):
    """
    Creates a Table object containing a scaled Image and a Paragraph.

    :param image_path: Path to the image file.
    :param paragraph_text: Text for the paragraph.
    :param page_width_cm: Total page width in centimeters (default is 21 cm for A4).
    :return: A Table object containing the image and paragraph.
    """
    max_image_width = (page_width_cm*.8) * cm  

    # Create the Image object
    img = Image(image_path)

    aspect = img.imageHeight / float(img.imageWidth)
    img_width = min(max_image_width, img.imageWidth) 
    img_height = img_width * aspect

    img.drawWidth = img_width
    img.drawHeight = img_height

    data = [[img]]
    table = Table(data, colWidths=[img_width, (page_width_cm * cm) - img_width - 2 * cm])  
    table.setStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),  
        ('LEFTPADDING', (0, 0), (-1, -1), 5),  
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ])

    return table

def add_header(canvas, doc, header_text):
    """
    Adds a header to each page of the document.
    
    :param canvas: The canvas object from ReportLab.
    :param doc: The document object (SimpleDocTemplate).
    :param header_text: The text to display in the header.
    """
    canvas.saveState()
    # the header text
    canvas.setFont('Helvetica', 10)
    canvas.drawString(cm, A4[1] - 1.5 * cm, header_text)
    # gray line
    canvas.setStrokeColor(colors.grey)
    canvas.setLineWidth(0.5)
    canvas.line(cm, A4[1] - 1.7 * cm, A4[0] - cm, A4[1] - 1.7 * cm)
    canvas.restoreState()

def add_footer(canvas, doc, footer_text):
    """
    Adds a footer to each page of the document.
    
    :param canvas: The canvas object from ReportLab.
    :param doc: The document object (SimpleDocTemplate).
    :param footer_text: The text to display in the footer.
    """
    canvas.saveState()
    # Draw the footer text and page number
    canvas.setFont('Helvetica', 10)
    page_number_text = f"{footer_text} - Page {doc.page}"
    canvas.drawString(cm, 1 * cm, page_number_text)
    # Draw a gray line
    canvas.setStrokeColor(colors.grey)
    canvas.setLineWidth(0.5)
    canvas.line(cm, 1.5 * cm, A4[0] - cm, 1.5 * cm)
    canvas.restoreState()

def on_first_page(canvas, doc, footer_text):
    """
    Handles the first page layout without a header.
    
    :param canvas: The canvas object from ReportLab.
    :param doc: The document object (SimpleDocTemplate).
    :param footer_text: The text to display in the footer.
    """
    add_footer(canvas, doc, footer_text)

def on_later_pages(canvas, doc, header_text, footer_text):
    """
    Handles the layout for subsequent pages with both header and footer.
    
    :param canvas: The canvas object from ReportLab.
    :param doc: The document object (SimpleDocTemplate).
    :param header_text: The text to display in the header.
    :param footer_text: The text to display in the footer.
    """
    add_header(canvas, doc, header_text)
    add_footer(canvas, doc, footer_text)


def generate_pdf_with_header_footer(flowables, file_path, header_text, footer_text):
    """
    Generates a PDF document from a list of flowables, adding headers and footers.
    
    :param flowables: List of flowable elements (e.g., Paragraphs, Tables, ListFlowable).
    :param file_path: Full file path (including the name) where the PDF will be saved.
    :param header_text: The text to display in the header of each page.
    :param footer_text: The text to display in the footer of each page.
    """
    
    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
        leftMargin=2 * cm,
        rightMargin=2 * cm
    )
    
    try:
        
        doc.build(flowables,
                  onFirstPage=lambda canvas, doc: on_first_page(canvas, doc, footer_text),
                  onLaterPages=lambda canvas, doc: on_later_pages(canvas, doc, header_text, footer_text))
        print(f"PDF successfully created at: {file_path}")
    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")

def create_colored_table(df, alpha=0.6):
    """
    Creates a ReportLab Table from a DataFrame, coloring each row based on the 'color' column
    with an adjustable alpha value. Includes DataFrame index as the first column and formats
    numeric values to three decimal places, and adds a caption above the table.

    :param df: The DataFrame containing data and color information.
    :param alpha: The alpha value for row background colors (default is 0.6).
    :param caption: The caption to be placed above the table.
    :return: A KeepTogether object containing a Paragraph object for the caption and the styled Table object.
    """
    
    headers = [df.index.name if df.index.name else 'Index'] + list(df.columns[:-1])  

    data = [headers] + [
        [str(index)] + [f"{x:.3f}" if isinstance(x, (float)) else str(x) for x in row[:-1]]
        for index, row in df.iterrows()
    ]

    table = Table(data)

    table_style = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  
        ('GRID', (0, 0), (-1, -1), 0.5, colors.white),  
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), 
        ('FONTSIZE', (0, 0), (-1, -1), 8)
    ]

    for i, color in enumerate(df['color'], start=1):  
        rl_color = colors.Color(color[0], color[1], color[2], alpha)
        table_style.append(('BACKGROUND', (0, i), (-1, i), rl_color))

    table.setStyle(TableStyle(table_style))

    return table


def parse_markdown_table(markdown_table):
    """
    Parses a markdown table into a list of lists suitable for ReportLab's Table,
    rounding float values to two decimal places.
    
    :param markdown_table: A string containing a markdown-formatted table.
    :return: A list of lists representing the table data.
    """
    lines = markdown_table.strip().split('\n')
    data = []

    # Iterate through lines and skip the alignment row
    for i, line in enumerate(lines):
        # Skip the alignment row which typically looks like this: | :---- | :---: | ----: |
        if i == 1 and re.match(r'^\s*\|?(\s*:?-+:?\s*\|)+\s*$', line):
            continue  # Skip alignment row

        # Use regex to split the line into table cells, ignoring leading and trailing pipes
        cells = re.split(r'\s*\|\s*', line.strip('|'))

        # Process cells to round floats to two decimal places
        processed_cells = []
        for cell in cells:
            try:
                # Try to convert the cell to a float and round it
                float_value = float(cell)
                processed_cells.append(f"{float_value:.2f}")
            except ValueError:
                # If conversion fails, just use the original cell
                processed_cells.append(cell.strip())

        data.append(processed_cells)

    return data

def format_text(text):
    """
    Replace markdown bold and italic markers with HTML equivalents.
    """
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # Bold
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)      # Italic
    return text

def markdown_table_to_reportlab(markdown_table):
    """
    Converts a markdown table to a ReportLab Table flowable.
    
    :param markdown_table: A string containing a markdown-formatted table.
    :return: A ReportLab Table flowable.
    """
    data = parse_markdown_table(markdown_table)
    
    # Define table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8)
    ])
    
    # Create the ReportLab Table
    reportlab_table = Table(data)
    reportlab_table.setStyle(table_style)
    
    return reportlab_table

def collect_list_elements(lines):
    list_items = []
    list_item_pattern = re.compile(r'^\d+\.\s+(.*)')  # Matches numbered list items
    
    for line in lines:
        match = list_item_pattern.match(line.strip())
        if match:
            formatted_text = format_text(match.group(1))
            list_items.append(ListItem(Paragraph(formatted_text, paragraph_style)))
    
    return ListFlowable(list_items, bulletType='1') if list_items else None


def markdown_to_flowables(markdown_text):
    heading_two_pattern = re.compile(r'^## (.*)')
    heading_three_pattern = re.compile(r'^### (.*)')
    list_item_pattern = re.compile(r'^\d+\.\s+.*')
    table_pattern = re.compile(r'^\|.*\|$')  # Pattern to detect table rows
    
    flowables = []
    current_lines = markdown_text.splitlines()

    # Temporary buffers for lines when collecting lists, tables, or paragraphs
    list_lines = []
    table_lines = []
    inside_list = False
    inside_table = False

    for line in current_lines:
        line = line.strip()
        if not line:
            continue

        # Detect headers and add them directly, finalize any ongoing lists or tables
        if heading_two_pattern.match(line):
            if inside_list:
                list_flowable = collect_list_elements(list_lines)
                if list_flowable:
                    flowables.append(list_flowable)
                list_lines = []
                inside_list = False
            if inside_table:
                table_flowable = markdown_table_to_reportlab('\n'.join(table_lines))
                if table_flowable:
                    flowables.append(table_flowable)
                table_lines = []
                inside_table = False

            formatted_text = format_text(heading_two_pattern.match(line).group(1))
            flowables.append(Paragraph(formatted_text, heading_two_style))

        elif heading_three_pattern.match(line):
            if inside_list:
                list_flowable = collect_list_elements(list_lines)
                if list_flowable:
                    flowables.append(list_flowable)
                list_lines = []
                inside_list = False
            if inside_table:
                table_flowable = markdown_table_to_reportlab('\n'.join(table_lines))
                if table_flowable:
                    flowables.append(table_flowable)
                table_lines = []
                inside_table = False

            formatted_text = format_text(heading_three_pattern.match(line).group(1))
            flowables.append(Paragraph(formatted_text, heading_three_style))

        # Check for list items and collect them
        elif list_item_pattern.match(line):
            if not inside_list:
                # Finalize any ongoing table before starting a list
                if inside_table:
                    table_flowable = markdown_table_to_reportlab('\n'.join(table_lines))
                    if table_flowable:
                        flowables.append(table_flowable)
                    table_lines = []
                    inside_table = False

            inside_list = True
            list_lines.append(line)

        # Check for tables
        elif table_pattern.match(line):
            inside_table = True
            table_lines.append(line)

        else:
            # Finalize any ongoing lists or tables before adding paragraphs
            if inside_list:
                list_flowable = collect_list_elements(list_lines)
                if list_flowable:
                    flowables.append(list_flowable)
                list_lines = []
                inside_list = False

            if inside_table:
                table_flowable = markdown_table_to_reportlab('\n'.join(table_lines))
                if table_flowable:
                    flowables.append(table_flowable)
                table_lines = []
                inside_table = False

            # Add formatted paragraph
            formatted_text = format_text(line)
            flowables.append(Paragraph(formatted_text, paragraph_style))

    # Final checks if the text ends with a list or table
    if inside_list:
        list_flowable = collect_list_elements(list_lines)
        if list_flowable:
            flowables.append(list_flowable)
    
    if inside_table:
        table_flowable = markdown_table_to_reportlab('\n'.join(table_lines))
        if table_flowable:
            flowables.append(table_flowable)
    
    return flowables

#
# header_text = "Proof of concept: llm assissted reporting"
# footer_text = "Draft survey: llm assissted reporting"
#
# bottom_legend_caption = "Cluster analysis results: average pcs/m and proportion of buffer for feature variables"
#
# scatter_pdf = pdfmethods.create_image_paragraph_table('bernlakes/scatter_plot_likelihood.jpg')
# city_results_table = pdfmethods.create_colored_table(map_legend_markers['city_results'].data)
# # cluster_results_table = pdfmethods.create_colored_table(map_legend_markers['cluster_results'].data)
# situation_map = pdfmethods.create_image_paragraph_table('bernlakes/situation_map.jpg')
# map_bottom_legend = Table([[Paragraph(bottom_legend_caption,custom_italic_style)] ,  [city_results_table]]) # [cluster_results_table],
#
# pdfs = []
#
# pdfs.extend(markdown_to_flowables('\n' + title))
# pdfs.extend(markdown_to_flowables(executive_summary))
# pdfs.extend(markdown_to_flowables('\n' + finished_summary))
# pdfs.extend([scatter_pdf, KeepTogether([situation_map, map_bottom_legend])])
# pdfs.extend(markdown_to_flowables(finished_faq_summary))
# pdfs.extend(markdown_to_flowables('\n' + finished_summary_strat))
#
# pdftable = data['landuse_profile'].copy()
# pdftable = adjust_multiindex_columns(pdftable, rate='')
# pdftable = pdftable[[' buildings', ' forest', ' undefined', ' streets', ' public-services', ' recreation']]
# pdfs.extend(markdown_to_flowables('\n' + pdftable.to_markdown()))
#
# pdftable = data['landuse_rates'].copy()
# pdftable = pdftable.round(2)
# pdftable = adjust_multiindex_columns(pdftable, rate='')
# pdftable = pdftable[[' buildings', ' forest', ' undefined', ' streets', ' public-services', ' recreation']].round(2)
# pdfs.extend(markdown_to_flowables('\n' + pdftable.to_markdown()))
#
# pdfs.extend(markdown_to_flowables('\n' + finished_faq_summary_strat))
#
#
#
# pdfs.extend(markdown_to_flowables('\n' + finished_summary_linear))
# pdfs.extend(markdown_to_flowables('\n' + finished_faq_summary_linear))
# pdfs.extend(markdown_to_flowables('\n' + finished_summary_grid))
# boxplots_forecasts =  pdfmethods.create_image_paragraph_table('bernlakes/boxplots_observed_expected.jpeg')
# pdfs.extend([boxplots_forecasts])
# pdfs.extend(markdown_to_flowables('\n' + finished_faq_summary_grid))
# file_path = 'test_pdf.pdf'
# pdfmethods.generate_pdf_with_header_footer(pdfs, file_path, header_text, footer_text)