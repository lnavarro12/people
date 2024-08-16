from openpyxl.reader import excel
from openpyxl.workbook import workbook
import os
import requests
from openpyxl import Workbook, load_workbook
from app.main.utils.utils import (
    response_error,
    is_empty_or_none,
    create_workbook,
)

def upload_corporate_client(args):
    """ This method upload a new corporate client """
    base_64 = args.get('base_64')

    if is_empty_or_none(base_64):
        return response_error("base_64 cannot be empty", 400)
    
    # create a workbook
    try:
        workbook = create_workbook(base_64, "cliente_empresa.xlsx")

    except Exception as e:
        return response_error(str(e), 400)
    

    return ""
