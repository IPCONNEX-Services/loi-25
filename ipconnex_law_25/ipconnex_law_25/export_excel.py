import openpyxl
import frappe
import json
from frappe.utils import get_site_path
import os
import zipfile
import pyzipper
 
def create_secure_files(input_files, output_zip, password):
    password_bytes = password.encode('utf-8')
    output_path = frappe.utils.get_bench_path()+ "/sites/" + frappe.utils.get_path('public', 'files', 'output.zip')[2:]

    with pyzipper.AESZipFile(output_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password_bytes)
        for file in input_files:
            zipf.write(file, arcname=os.path.basename(file))
 
@frappe.whitelist(allow_guest=True)
def generate_excel(data):

    data = json.loads(data)

    
    wb = openpyxl.Workbook()
    ws = wb.active

    for key, value in data.items():
        ws.append([key, value])

    
    # Save Excel workbook in the site private files directory
    file_path = frappe.utils.get_bench_path()+ "/sites/" + frappe.utils.get_path('public', 'files', 'output.xlsx')[2:]
    wb.save(file_path)
        # Example usage
    input_files = [file_path]
    output_zip = 'output.zip'
    password = '1234'

    create_secure_files(input_files, output_zip, password)

    return  True




