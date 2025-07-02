from django import forms

class ExcelUploadForm(forms.Form):
    admission_file = forms.FileField(label="Upload Admission Details Excel File", required=False)
    students_file = forms.FileField(label="Upload Students Excel File", required=False)
    company_file = forms.FileField(label="Upload Company Info Excel File", required=False)
