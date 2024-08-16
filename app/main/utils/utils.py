""" 
Utils module
"""
from flask import jsonify, abort
import base64
from openpyxl import Workbook, load_workbook

def response_error(error, status_code: int = 400, message: str = None, field: str = None):
    """
    This function implements the error response method for the olds functions this return a tuple
    """
    result = {"success": False, "error": str(error), "status": status_code}
    if message:
        result["message"] = message

    if field:
        result["field"] = field

    if status_code:
        result["status"] = int(status_code)

    return result, status_code

def is_empty_or_none(data) -> bool:
    """This method returns a boolean when data is empty or None
    receives any type of data
    Args:
        data (Any): _description_
    Returns:
        boolean
    """
    if data is None:
        return True

    if isinstance(data, str) and not str(data).strip():
        return True

    if isinstance(data, (dict, tuple, list)) and not data:
        return True

    return False

def abort_request(error, status_code: int = 400, message: str = None, field: str = None):
    """
    This function replace the old response error function this abort the operation
    """
    result, code = response_error(error, status_code, message, field)
    response = jsonify(result)
    response.status_code = code

    abort(response)

def response_success(results, message, row_total, title=None, status_code=200, internal=False):
    """
    This method helps to return a successful response to the endpoint.
    """
    response = {
        "success": True,
        "title": title,
        "message": message,
        "results": results,
        "rowTotal": row_total,
        "status": status_code,
    }
    response = response if internal else jsonify(response)
    return response

def create_workbook(base64_file, filename):
    """ 
    This method create a new workbook base on a base64 file
    """

    base64_excel = base64_file.encode("utf-8")

    try:
        decoded_excel = base64.b64decode(base64_excel)

    except base64.binascii.Error:
        return response_error("invalid base64_file", 400, "Archivo base64 no válido.")

    excel_filename = filename
    # save excel data in a temporary file
    with open(excel_filename, "wb") as decoded_file:
        decoded_file.write(decoded_excel)

    # read_tmp_excel_file
    workbook = load_workbook(excel_filename)
    worksheet = workbook.active

    return worksheet

