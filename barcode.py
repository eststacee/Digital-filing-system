import re


def generate_barcode(file_number):
    """
    Generate a barcode value from the file number.

    Example:
    AFA/ICT/001 -> AFA-ICT-001
    """

    barcode = file_number.strip().upper()

    # Replace spaces and slashes with hyphens
    barcode = re.sub(r"[\s/]+", "-", barcode)

    # Remove characters that are not letters, numbers or hyphens
    barcode = re.sub(r"[^A-Z0-9-]", "", barcode)

    return barcode
