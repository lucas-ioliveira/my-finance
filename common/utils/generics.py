import os
import uuid
from datetime import datetime

class Generics:

    @staticmethod
    def get_expense_receipt_path_advanced(instance, filename):
        ext = os.path.splitext(filename)[1]
        new_filename = f"{uuid.uuid4()}{ext}"
        now = datetime.now()
        year = now.strftime('%Y')
        month = now.strftime('%m')
        return f'receipts/user_{instance.user.id}/{year}/{month}/{new_filename}'
