import subprocess
import tempfile


def generate_pdf_response(url: str, filename: str):
    """Generate a PDF from a URL using wkhtmltopdf and return a Flask response tuple."""

    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        subprocess.check_call(["wkhtmltopdf", url, tmp.name])

        # Move cursor to start before reading
        tmp.seek(0)
        pdf_data = tmp.read()

        return (
            pdf_data,
            200,
            {
                "Content-Type": "application/pdf",
                "Content-Disposition": f'attachment; filename="{filename}"',
            },
        )
