import pdfkit
from jinja2 import Environment, FileSystemLoader

# Load the HTML template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('a1.html')  # Make sure the template filename is correct

# Replace placeholders with "CREDENTIAL"
rendered_html = template.render(
    title="CREDENTIAL",
    date="CREDENTIAL",
    supplier_name="CREDENTIAL",
    supplier_cnpj="CREDENTIAL",
    supplier_address="CREDENTIAL",
    client_name="CREDENTIAL",
    client_cnpj="CREDENTIAL",
    client_address="CREDENTIAL",
    invoice_number="CREDENTIAL",
    invoice_month="CREDENTIAL",
    description="CREDENTIAL",
    period="CREDENTIAL",
    due_date="CREDENTIAL",
    amount="CREDENTIAL",
    bank_details="CREDENTIAL",
    pix="CREDENTIAL"
)

# Generate PDF
pdfkit.from_string(rendered_html, 'output.pdf')
