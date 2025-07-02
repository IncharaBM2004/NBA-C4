
import pandas as pd
from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
from .models import AdmissionDetails, Students, company_info
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import FileResponse
from django.conf import settings
import os
from django.http import HttpResponse, HttpResponseNotFound




 
def upload_excel(request):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Process AdmissionDetails file
                if 'admission_file' in request.FILES:
                    admission_file = request.FILES['admission_file']
                    admission_df = pd.read_excel(admission_file)
                    admission_df = admission_df.where(pd.notnull(admission_df), None)
                    for _, row in admission_df.iterrows():
                        AdmissionDetails.objects.update_or_create(
                            sname=row['sname'],
                            gender=row.get('gender'),
                            admission_year=row['admission_year'],
                            admission_mode=row.get('admission_mode'),
                            first_year_left=row.get('first_year_left'),
                            special_adid=row.get('special_adid'),
                        )

                # Process Students file
                if 'students_file' in request.FILES:
                    students_file = request.FILES['students_file']
                    students_df = pd.read_excel(students_file)
               
                    for _, row in students_df.iterrows():
                        try:
                            admission_detail = AdmissionDetails.objects.get(
                                sname=row['sname'], admission_year=row['admission_year']
                            )

                            

                            Students.objects.update_or_create(
                                admission_details=admission_detail,
                                dept=row.get('dept',None),
                                usn=row.get('usn',None),
                                sem1_sub1_internal=row.get('sem1_sub1_internal',None),
                                sem1_sub1_external=row.get('sem1_sub1_external'),
                                sem1_sub1=row.get('sem1_sub1'),
                                sem1_sub1_res=row.get('sem1_sub1_res'),
                                sem1_sub2_internal=row.get('sem1_sub2_internal'),
                                sem1_sub2_external=row.get('sem1_sub2_external'),
                                sem1_sub2=row.get('sem1_sub2'),
                                sem1_sub2_res=row.get('sem1_sub2_res'),
                                sem1_sub3_internal=row.get('sem1_sub3_internal'),
                                sem1_sub3_external=row.get('sem1_sub3_external'),
                                sem1_sub3=row.get('sem1_sub3'),
                                sem1_sub3_res=row.get('sem1_sub3_res'),
                                sem1_sub4_internal=row.get('sem1_sub4_internal'),
                                sem1_sub4_external=row.get('sem1_sub4_external'),
                                sem1_sub4=row.get('sem1_sub4'),
                                sem1_sub4_res=row.get('sem1_sub4_res'),
                                sem1_sub5_internal=row.get('sem1_sub5_internal'),
                                sem1_sub5_external=row.get('sem1_sub5_external'),
                                sem1_sub5=row.get('sem1_sub5'),
                                sem1_sub5_res=row.get('sem1_sub5_res'),
                                sem1_sub6_internal=row.get('sem1_sub6_internal'),
                                sem1_sub6_external=row.get('sem1_sub6_external'),
                                sem1_sub6=row.get('sem1_sub6'),
                                sem1_sub6_res=row.get('sem1_sub6_res'),
                                sem1_sub7_internal=row.get('sem1_sub7_internal'),
                                sem1_sub7_external=row.get('sem1_sub7_external'),
                                sem1_sub7=row.get('sem1_sub7'),
                                sem1_sub7_res=row.get('sem1_sub7_res'),
                                sem1_sub8_internal=row.get('sem1_sub8_internal'),
                                sem1_sub8_external=row.get('sem1_sub8_external'),
                                sem1_sub8=row.get('sem1_sub8'),
                                sem1_sub8_res=row.get('sem1_sub8_res'),
                                sem1_sub9_internal=row.get('sem1_sub9_internal'),
                                sem1_sub9_external=row.get('sem1_sub9_external'),
                                sem1_sub9=row.get('sem1_sub9'),
                                sem1_sub9_res=row.get('sem1_sub9_res'),
                                sem1_sub10_internal = row.get('sem1_sub10_internals', None),
                                sem1_sub10_external = row.get('sem1_sub10_externals', None),
                                sem1_sub10 = row.get('sem1_sub10', None),
                                sem1_sub10_res = row.get('sem1_sub10_res', None),
                                sem1_total = row.get('sem1_total', None),
                                sem1_cgpa = row.get('sem1_cgpa', None),
                            
                            sem2_sub1_internal = row.get('sem2_sub1_internals', None),
                            sem2_sub1_external = row.get('sem2_sub1_externals', None),
                            sem2_sub1 = row.get('sem2_sub1', None),
                            sem2_sub1_res = row.get('sem2_sub2_res', None),
                            sem2_sub2_internal = row.get('sem2_sub2_internals', None),
                            sem2_sub2_external = row.get('sem2_sub2_externals', None),
                            sem2_sub2 = row.get('sem2_sub2', None),
                            sem2_sub2_res = row.get('sem2_sub2_res', None),
                            sem2_sub3_internal = row.get('sem2_sub3_internals', None),
                            sem2_sub3_external = row.get('sem2_sub3_externals', None),
                            sem2_sub3 = row.get('sem2_sub3', None),
                            sem2_sub3_res = row.get('sem2_sub3_res', None),
                            sem2_sub4_internal = row.get('sem2_sub4_internals', None),
                            sem2_sub4_external = row.get('sem2_sub4_externals', None),
                            sem2_sub4 = row.get('sem2_sub4', None),
                            sem2_sub4_res = row.get('sem2_sub4_res', None),
                            sem2_sub5_internal = row.get('sem2_sub5_internals', None),
                            sem2_sub5_external = row.get('sem2_sub5_externals', None),
                            sem2_sub5 = row.get('sem2_sub5', None),
                            sem2_sub5_res = row.get('sem2_sub5_res', None),
                            sem2_sub6_internal = row.get('sem2_sub6_internals', None),
                            sem2_sub6_external = row.get('sem2_sub6_externals', None),
                            sem2_sub6 = row.get('sem2_sub6', None),
                            sem2_sub6_res = row.get('sem2_sub6_res', None),
                            sem2_sub7_internal = row.get('sem2_sub7_internals', None),
                            sem2_sub7_external = row.get('sem2_sub7_externals', None),
                            sem2_sub7 = row.get('sem2_sub7', None),
                            sem2_sub7_res = row.get('sem2_sub7_res', None),
                            sem2_sub8_internal = row.get('sem2_sub8_internals', None),
                            sem2_sub8_external = row.get('sem2_sub8_externals', None),
                            sem2_sub8 = row.get('sem2_sub8', None),
                            sem2_sub8_res = row.get('sem2_sub8_res', None),
                            sem2_sub9_internal = row.get('sem2_sub9_internals', None),
                            sem2_sub9_external = row.get('sem2_sub9_externals', None),
                            sem2_sub9 = row.get('sem2_sub9', None),
                            sem2_sub9_res = row.get('sem2_sub9_res', None),
                            sem2_sub10_internal = row.get('sem2_sub10_internals', None),
                            sem2_sub10_external = row.get('sem2_sub10_externals', None),
                            sem2_sub10 = row.get('sem2_sub10', None),
                            sem2_sub10_res = row.get('sem2_sub10_res', None),
                            sem2_total = row.get('sem2_total', None),
                            sem2_cgpa = row.get('sem2_cgpa', None),  

                            sem3_sub1_internal = row.get('sem3_sub1_internals', None),
                            sem3_sub1_external = row.get('sem3_sub1_externals', None),
                            sem3_sub1 = row.get('sem3_sub1', None),
                            sem3_sub1_res = row.get('sem3_sub2_res', None),
                            sem3_sub2_internal = row.get('sem3_sub2_internals', None),
                            sem3_sub2_external = row.get('sem3_sub2_externals', None),
                            sem3_sub2 = row.get('sem3_sub2', None),
                            sem3_sub2_res = row.get('sem3_sub2_res', None),
                            sem3_sub3_internal = row.get('sem3_sub3_internals', None),
                            sem3_sub3_external = row.get('sem3_sub3_externals', None),
                            sem3_sub3 = row.get('sem3_sub3', None),
                            sem3_sub3_res = row.get('sem3_sub3_res', None),
                            sem3_sub4_internal = row.get('sem3_sub4_internals', None),
                            sem3_sub4_external = row.get('sem3_sub4_externals', None),
                            sem3_sub4 = row.get('sem3_sub4', None),
                            sem3_sub4_res = row.get('sem3_sub4_res', None),
                            sem3_sub5_internal = row.get('sem3_sub5_internals', None),
                            sem3_sub5_external = row.get('sem3_sub5_externals', None),
                            sem3_sub5 = row.get('sem3_sub5', None),
                            sem3_sub5_res = row.get('sem3_sub5_res', None),
                            sem3_sub6_internal = row.get('sem3_sub6_internals', None),
                            sem3_sub6_external = row.get('sem3_sub6_externals', None),
                            sem3_sub6 = row.get('sem3_sub6', None),
                            sem3_sub6_res = row.get('sem3_sub6_res', None),
                            sem3_sub7_internal = row.get('sem3_sub7_internals', None),
                            sem3_sub7_external = row.get('sem3_sub7_externals', None),
                            sem3_sub7 = row.get('sem3_sub7', None),
                            sem3_sub7_res = row.get('sem3_sub7_res', None),
                            sem3_sub8_internal = row.get('sem3_sub8_internals', None),
                            sem3_sub8_external = row.get('sem3_sub8_externals', None),
                            sem3_sub8 = row.get('sem3_sub8', None),
                            sem3_sub8_res = row.get('sem3_sub8_res', None),
                            sem3_sub9_internal = row.get('sem3_sub9_internals', None),
                            sem3_sub9_external = row.get('sem3_sub9_externals', None),
                            sem3_sub9 = row.get('sem3_sub9', None),
                            sem3_sub9_res = row.get('sem3_sub9_res', None),
                            sem3_sub10_internal = row.get('sem3_sub10_internals', None),
                            sem3_sub10_external = row.get('sem3_sub10_externals', None),
                            sem3_sub10 = row.get('sem3_sub10', None),
                            sem3_sub10_res = row.get('sem3_sub10_res', None),
                            sem3_total = row.get('sem3_total', None),
                            sem3_cgpa = row.get('sem3_cgpa', None),

                            sem4_sub1_internal = row.get('sem4_sub1_internals', None),
                            sem4_sub1_external = row.get('sem4_sub1_externals', None),
                            sem4_sub1 = row.get('sem4_sub1', None),
                            sem4_sub1_res = row.get('sem4_sub2_res', None),
                            sem4_sub2_internal = row.get('sem4_sub2_internals', None),
                            sem4_sub2_external = row.get('sem4_sub2_externals', None),
                            sem4_sub2 = row.get('sem4_sub2', None),
                            sem4_sub2_res = row.get('sem4_sub2_res', None),
                            sem4_sub3_internal = row.get('sem4_sub3_internals', None),
                            sem4_sub3_external = row.get('sem4_sub3_externals', None),
                            sem4_sub3 = row.get('sem4_sub3', None),
                            sem4_sub3_res = row.get('sem4_sub3_res', None),
                            sem4_sub4_internal = row.get('sem4_sub4_internals', None),
                            sem4_sub4_external = row.get('sem4_sub4_externals', None),
                            sem4_sub4 = row.get('sem4_sub4', None),
                            sem4_sub4_res = row.get('sem4_sub4_res', None),
                            sem4_sub5_internal = row.get('sem4_sub5_internals', None),
                            sem4_sub5_external = row.get('sem4_sub5_externals', None),
                            sem4_sub5 = row.get('sem4_sub5', None),
                            sem4_sub5_res = row.get('sem4_sub5_res', None),
                            sem4_sub6_internal = row.get('sem4_sub6_internals', None),
                            sem4_sub6_external = row.get('sem4_sub6_externals', None),
                            sem4_sub6 = row.get('sem4_sub6', None),
                            sem4_sub6_res = row.get('sem4_sub6_res', None),
                            sem4_sub7_internal = row.get('sem4_sub7_internals', None),
                            sem4_sub7_external = row.get('sem4_sub7_externals', None),
                            sem4_sub7 = row.get('sem4_sub7', None),
                            sem4_sub7_res = row.get('sem4_sub7_res', None),
                            sem4_sub8_internal = row.get('sem4_sub8_internals', None),
                            sem4_sub8_external = row.get('sem4_sub8_externals', None),
                            sem4_sub8 = row.get('sem4_sub8', None),
                            sem4_sub8_res = row.get('sem4_sub8_res', None),
                            sem4_sub9_internal = row.get('sem4_sub9_internals', None),
                            sem4_sub9_external = row.get('sem4_sub9_externals', None),
                            sem4_sub9 = row.get('sem4_sub9', None),
                            sem4_sub9_res = row.get('sem4_sub9_res', None),
                            sem4_sub10_internal = row.get('sem4_sub10_internals', None),
                            sem4_sub10_external = row.get('sem4_sub10_externals', None),
                            sem4_sub10 = row.get('sem4_sub10', None),
                            sem4_sub10_res = row.get('sem4_sub10_res', None),
                            sem4_total = row.get('sem4_total', None),
                            sem4_cgpa = row.get('sem4_cgpa', None),

                            sem5_sub1_internal = row.get('sem5_sub1_internals', None),
                            sem5_sub1_external = row.get('sem5_sub1_externals', None),
                            sem5_sub1 = row.get('sem5_sub1', None),
                            sem5_sub1_res = row.get('sem5_sub2_res', None),
                            sem5_sub2_internal = row.get('sem5_sub2_internals', None),
                            sem5_sub2_external = row.get('sem5_sub2_externals', None),
                            sem5_sub2 = row.get('sem5_sub2', None),
                            sem5_sub2_res = row.get('sem5_sub2_res', None),
                            sem5_sub3_internal = row.get('sem5_sub3_internals', None),
                            sem5_sub3_external = row.get('sem5_sub3_externals', None),
                            sem5_sub3 = row.get('sem5_sub3', None),
                            sem5_sub3_res = row.get('sem5_sub3_res', None),
                            sem5_sub4_internal = row.get('sem5_sub4_internals', None),
                            sem5_sub4_external = row.get('sem5_sub4_externals', None),
                            sem5_sub4 = row.get('sem5_sub4', None),
                            sem5_sub4_res = row.get('sem5_sub4_res', None),
                            sem5_sub5_internal = row.get('sem5_sub5_internals', None),
                            sem5_sub5_external = row.get('sem5_sub5_externals', None),
                            sem5_sub5 = row.get('sem5_sub5', None),
                            sem5_sub5_res = row.get('sem5_sub5_res', None),
                            sem5_sub6_internal = row.get('sem5_sub6_internals', None),
                            sem5_sub6_external = row.get('sem5_sub6_externals', None),
                            sem5_sub6 = row.get('sem5_sub6', None),
                            sem5_sub6_res = row.get('sem5_sub6_res', None),
                            sem5_sub7_internal = row.get('sem5_sub7_internals', None),
                            sem5_sub7_external = row.get('sem5_sub7_externals', None),
                            sem5_sub7 = row.get('sem5_sub7', None),
                            sem5_sub7_res = row.get('sem5_sub7_res', None),
                            sem5_sub8_internal = row.get('sem5_sub8_internals', None),
                            sem5_sub8_external = row.get('sem5_sub8_externals', None),
                            sem5_sub8 = row.get('sem5_sub8', None),
                            sem5_sub8_res = row.get('sem5_sub8_res', None),
                            sem5_sub9_internal = row.get('sem5_sub9_internals', None),
                            sem5_sub9_external = row.get('sem5_sub9_externals', None),
                            sem5_sub9 = row.get('sem5_sub9', None),
                            sem5_sub9_res = row.get('sem5_sub9_res', None),
                            sem5_sub10_internal = row.get('sem5_sub10_internals', None),
                            sem5_sub10_external = row.get('sem5_sub10_externals', None),
                            sem5_sub10 = row.get('sem5_sub10', None),
                            sem5_sub10_res = row.get('sem5_sub10_res', None),
                            sem5_total = row.get('sem5_total', None),
                            sem5_cgpa = row.get('sem5_cgpa', None),

                            sem6_sub1_internal = row.get('sem6_sub1_internals', None),
                            sem6_sub1_external = row.get('sem6_sub1_externals', None),
                            sem6_sub1 = row.get('sem6_sub1', None),
                            sem6_sub1_res = row.get('sem6_sub2_res', None),
                            sem6_sub2_internal = row.get('sem6_sub2_internals', None),
                            sem6_sub2_external = row.get('sem6_sub2_externals', None),
                            sem6_sub2 = row.get('sem6_sub2', None),
                            sem6_sub2_res = row.get('sem6_sub2_res', None),
                            sem6_sub3_internal = row.get('sem6_sub3_internals', None),
                            sem6_sub3_external = row.get('sem6_sub3_externals', None),
                            sem6_sub3 = row.get('sem6_sub3', None),
                            sem6_sub3_res = row.get('sem6_sub3_res', None),
                            sem6_sub4_internal = row.get('sem6_sub4_internals', None),
                            sem6_sub4_external = row.get('sem6_sub4_externals', None),
                            sem6_sub4 = row.get('sem6_sub4', None),
                            sem6_sub4_res = row.get('sem6_sub4_res', None),
                            sem6_sub5_internal = row.get('sem6_sub5_internals', None),
                            sem6_sub5_external = row.get('sem6_sub5_externals', None),
                            sem6_sub5 = row.get('sem6_sub5', None),
                            sem6_sub5_res = row.get('sem6_sub5_res', None),
                            sem6_sub6_internal = row.get('sem6_sub6_internals', None),
                            sem6_sub6_external = row.get('sem6_sub6_externals', None),
                            sem6_sub6 = row.get('sem6_sub6', None),
                            sem6_sub6_res = row.get('sem6_sub6_res', None),
                            sem6_sub7_internal = row.get('sem6_sub7_internals', None),
                            sem6_sub7_external = row.get('sem6_sub7_externals', None),
                            sem6_sub7 = row.get('sem6_sub7', None),
                            sem6_sub7_res = row.get('sem6_sub7_res', None),
                            sem6_sub8_internal = row.get('sem6_sub8_internals', None),
                            sem6_sub8_external = row.get('sem6_sub8_externals', None),
                            sem6_sub8 = row.get('sem6_sub8', None),
                            sem6_sub8_res = row.get('sem6_sub8_res', None),
                            sem6_sub9_internal = row.get('sem6_sub9_internals', None),
                            sem6_sub9_external = row.get('sem6_sub9_externals', None),
                            sem6_sub9 = row.get('sem6_sub9', None),
                            sem6_sub9_res = row.get('sem6_sub9_res', None),
                            sem6_sub10_internal = row.get('sem6_sub10_internals', None),
                            sem6_sub10_external = row.get('sem6_sub10_externals', None),
                            sem6_sub10 = row.get('sem6_sub10', None),
                            sem6_sub10_res = row.get('sem6_sub10_res', None),
                            sem6_total = row.get('sem6_total', None),
                            sem6_cgpa = row.get('sem6_cgpa', None),

                            sem7_sub1_internal = row.get('sem7_sub1_internals', None),
                            sem7_sub1_external = row.get('sem7_sub1_externals', None),
                            sem7_sub1 = row.get('sem7_sub1', None),
                            sem7_sub1_res = row.get('sem7_sub2_res', None),
                            sem7_sub2_internal = row.get('sem7_sub2_internals', None),
                            sem7_sub2_external = row.get('sem7_sub2_externals', None),
                            sem7_sub2 = row.get('sem7_sub2', None),
                            sem7_sub2_res = row.get('sem7_sub2_res', None),
                            sem7_sub3_internal = row.get('sem7_sub3_internals', None),
                            sem7_sub3_external = row.get('sem7_sub3_externals', None),
                            sem7_sub3 = row.get('sem7_sub3', None),
                            sem7_sub3_res = row.get('sem7_sub3_res', None),
                            sem7_sub4_internal = row.get('sem7_sub4_internals', None),
                            sem7_sub4_external = row.get('sem7_sub4_externals', None),
                            sem7_sub4 = row.get('sem7_sub4', None),
                            sem7_sub4_res = row.get('sem7_sub4_res', None),
                            sem7_sub5_internal = row.get('sem7_sub5_internals', None),
                            sem7_sub5_external = row.get('sem7_sub5_externals', None),
                            sem7_sub5 = row.get('sem7_sub5', None),
                            sem7_sub5_res = row.get('sem7_sub5_res', None),
                            sem7_sub6_internal = row.get('sem7_sub6_internals', None),
                            sem7_sub6_external = row.get('sem7_sub6_externals', None),
                            sem7_sub6 = row.get('sem7_sub6', None),
                            sem7_sub6_res = row.get('sem7_sub6_res', None),
                            sem7_sub7_internal = row.get('sem7_sub7_internals', None),
                            sem7_sub7_external = row.get('sem7_sub7_externals', None),
                            sem7_sub7 = row.get('sem7_sub7', None),
                            sem7_sub7_res = row.get('sem7_sub7_res', None),
                            sem7_sub8_internal = row.get('sem7_sub8_internals', None),
                            sem7_sub8_external = row.get('sem7_sub8_externals', None),
                            sem7_sub8 = row.get('sem7_sub8', None),
                            sem7_sub8_res = row.get('sem7_sub8_res', None),
                            sem7_sub9_internal = row.get('sem7_sub9_internals', None),
                            sem7_sub9_external = row.get('sem7_sub9_externals', None),
                            sem7_sub9 = row.get('sem7_sub9', None),
                            sem7_sub9_res = row.get('sem7_sub9_res', None),
                            sem7_sub10_internal = row.get('sem7_sub10_internals', None),
                            sem7_sub10_external = row.get('sem7_sub10_externals', None),
                            sem7_sub10 = row.get('sem7_sub10', None),
                            sem7_sub10_res = row.get('sem7_sub10_res', None),
                            sem7_total = row.get('sem7_total', None),
                            sem7_cgpa = row.get('sem7_cgpa', None),
                           

                            sem8_sub1_internal = row.get('sem8_sub1_internals', None),
                            sem8_sub1_external = row.get('sem8_sub1_externals', None),
                            sem8_sub1 = row.get('sem8_sub1', None),
                            sem8_sub1_res = row.get('sem8_sub2_res', None),
                            sem8_sub2_internal = row.get('sem8_sub2_internals', None),
                            sem8_sub2_external = row.get('sem8_sub2_externals', None),
                            sem8_sub2 = row.get('sem8_sub2', None),
                            sem8_sub2_res = row.get('sem8_sub2_res', None),
                            sem8_sub3_internal = row.get('sem8_sub3_internals', None),
                            sem8_sub3_external = row.get('sem8_sub3_externals', None),
                            sem8_sub3 = row.get('sem8_sub3', None),
                            sem8_sub3_res = row.get('sem8_sub3_res', None),
                            sem8_sub4_internal = row.get('sem8_sub4_internals', None),
                            sem8_sub4_external = row.get('sem8_sub4_externals', None),
                            sem8_sub4 = row.get('sem8_sub4', None),
                            sem8_sub4_res = row.get('sem8_sub4_res', None),
                            sem8_sub5_internal = row.get('sem8_sub5_internals', None),
                            sem8_sub5_external = row.get('sem8_sub5_externals', None),
                            sem8_sub5 = row.get('sem8_sub5', None),
                            sem8_sub5_res = row.get('sem8_sub5_res', None),
                            sem8_sub6_internal = row.get('sem8_sub6_internals', None),
                            sem8_sub6_external = row.get('sem8_sub6_externals', None),
                            sem8_sub6 = row.get('sem8_sub6', None),
                            sem8_sub6_res = row.get('sem8_sub6_res', None),
                            sem8_sub7_internal = row.get('sem8_sub7_internals', None),
                            sem8_sub7_external = row.get('sem8_sub7_externals', None),
                            sem8_sub7 = row.get('sem8_sub7', None),
                            sem8_sub7_res = row.get('sem8_sub7_res', None),
                            sem8_sub8_internal = row.get('sem8_sub8_internals', None),
                            sem8_sub8_external = row.get('sem8_sub8_externals', None),
                            sem8_sub8 = row.get('sem8_sub8', None),
                            sem8_sub8_res = row.get('sem8_sub8_res', None),
                            sem8_sub9_internal = row.get('sem8_sub9_internals', None),
                            sem8_sub9_external = row.get('sem8_sub9_externals', None),
                            sem8_sub9 = row.get('sem8_sub9', None),
                            sem8_sub9_res = row.get('sem8_sub9_res', None),
                            sem8_sub10_internal = row.get('sem8_sub10_internals', None),
                            sem8_sub10_external = row.get('sem8_sub10_externals', None),
                            sem8_sub10 = row.get('sem8_sub10', None),
                            sem8_sub10_res = row.get('sem8_sub10_res', None),
                            sem8_total = row.get('sem8_total', None),
                            sem8_cgpa = row.get('sem8_cgpa', None),
                            placed_in_company=row.get('placed_in_company',None),
                            higher_studies=row.get('higher_studies',None),
                            entrepreneur=row.get('entrepreneur',None),	


                            )
                        except AdmissionDetails.DoesNotExist:
                            messages.error(request, f"Admission details not found for {row['sname']}.")

                # Process CompanyInfo file
                if 'company_file' in request.FILES:
                    company_file = request.FILES['company_file']
                    company_df = pd.read_excel(company_file)
                    company_df = company_df.where(pd.notnull(company_df), None)
                    for _, row in company_df.iterrows():
                        try:
                            admission_detail = AdmissionDetails.objects.get(
                                sname=row['sname'], admission_year=row['admission_year']
                            )
                            company_info.objects.update_or_create(
                                admission_details=admission_detail,
                                enrollement_no=row['enrollement_no'],
                                employer_name=row['employer_name'],
                                appointment_letter_no=row['appointment_letter_no'],
                            )
                        except AdmissionDetails.DoesNotExist:
                            messages.error(request, f"Admission details not found for {row['sname']}.")
# Redirect after success
                messages.success(request, "Files uploaded and data saved successfully!")
                return redirect('upload_success')  # Replace with your actual success URL

            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return render(request, 'mininba/upload_excel.html', {'form': form})
    else:
        form = ExcelUploadForm()

    # Render upload form
    return render(request, 'mininba/upload_excel.html', {'form': form})  
# Success page view after successful upload
def upload_success(request):
    return render(request, 'mininba/upload_success.html')




def student_count(request):
    """
    View to calculate and display student counts for multiple years,
    excluding lateral entries and considering only those where first_year_left is 'No'.
    """

    # Counts for years excluding lateral and with first_year_left = "No"
    count_2024_no_lateral = AdmissionDetails.objects.filter(
        admission_year=2024, first_year_left__iexact="No"
    ).exclude(admission_mode__iexact="lateral").count()

    count_2023_no_lateral = AdmissionDetails.objects.filter(
        admission_year=2023, first_year_left__iexact="No"
    ).exclude(admission_mode__iexact="lateral").count()

    count_2022_no_lateral = AdmissionDetails.objects.filter(
        admission_year=2022, first_year_left__iexact="No"
    ).exclude(admission_mode__iexact="lateral").count()

    count_2021_no_lateral = AdmissionDetails.objects.filter(
        admission_year=2021, first_year_left__iexact="No"
    ).exclude(admission_mode__iexact="lateral").count()

    count_2020_no_lateral = AdmissionDetails.objects.filter(
        admission_year=2020, first_year_left__iexact="No"
    ).exclude(admission_mode__iexact="lateral").count()

    count_2019_no_lateral = AdmissionDetails.objects.filter(
        admission_year=2019, first_year_left__iexact="No"
    ).exclude(admission_mode__iexact="lateral").count()

    count_2018_no_lateral = AdmissionDetails.objects.filter(
        admission_year=2018, first_year_left__iexact="No"
    ).exclude(admission_mode__iexact="lateral").count()

    # General counts for years excluding lateral entries
    count_2024 = AdmissionDetails.objects.filter(
        admission_year=2024
    ).exclude(admission_mode__iexact="lateral").count()

    count_2023 = AdmissionDetails.objects.filter(
        admission_year=2023
    ).exclude(admission_mode__iexact="lateral").count()

    count_2022 = AdmissionDetails.objects.filter(
        admission_year=2022
    ).exclude(admission_mode__iexact="lateral").count()

    count_2021 = AdmissionDetails.objects.filter(
        admission_year=2021 
    ).exclude(admission_mode__iexact="lateral").count()

    count_2020 = AdmissionDetails.objects.filter(
        admission_year=2020
    ).exclude(admission_mode__iexact="lateral").count()

    count_2019 = AdmissionDetails.objects.filter(
        admission_year=2019
    ).exclude(admission_mode__iexact="lateral").count()

    count_2018 = AdmissionDetails.objects.filter(
        admission_year=2018
    ).exclude(admission_mode__iexact="lateral").count()

    # Student lateral entry count
    count_2024_lateral = AdmissionDetails.objects.filter(
        admission_year=2024, admission_mode__iexact="lateral"
    ).count()

    count_2023_lateral = AdmissionDetails.objects.filter(
        admission_year=2023, admission_mode__iexact="lateral"
    ).count()

    count_2022_lateral = AdmissionDetails.objects.filter(
        admission_year=2022, admission_mode__iexact="lateral"
    ).count()

    count_2021_lateral = AdmissionDetails.objects.filter(
        admission_year=2021, admission_mode__iexact="lateral"
    ).count()

    count_2020_lateral = AdmissionDetails.objects.filter(
        admission_year=2020, admission_mode__iexact="lateral"
    ).count()

    count_2019_lateral = AdmissionDetails.objects.filter(
        admission_year=2019, admission_mode__iexact="lateral"
    ).count()

    count_2018_lateral = AdmissionDetails.objects.filter(
        admission_year=2018, admission_mode__iexact="lateral"
    ).count()

    # Special aided
    count_2024_special = AdmissionDetails.objects.filter(
        admission_year=2024, special_adid="yes"
    ).count()

    count_2023_special = AdmissionDetails.objects.filter(
        admission_year=2023, special_adid="yes"
    ).count()

    count_2022_special = AdmissionDetails.objects.filter(
        admission_year=2022, special_adid="yes"
    ).count()

    count_2021_special = AdmissionDetails.objects.filter(
        admission_year=2021, special_adid="yes"
    ).count()

    count_2020_special = AdmissionDetails.objects.filter(
        admission_year=2020, special_adid="yes"
    ).count()

    count_2019_special = AdmissionDetails.objects.filter(
        admission_year=2019, special_adid="yes"
    ).count()

    count_2018_special = AdmissionDetails.objects.filter(
        admission_year=2018, special_adid="yes"
    ).count()
      # N + N2 + N3 
    count20 = count_2020_no_lateral+count_2020_lateral+count_2020_special
    count19 = count_2019_no_lateral+count_2019_lateral+count_2019_special
    count18 = count_2018_no_lateral+count_2018_lateral+count_2018_special
    
    
    

    # N1 + N2 + N
    total1_count = count_2024_no_lateral + count_2024_lateral + count_2024_special
    total2_count = count_2023_no_lateral + count_2023_lateral + count_2023_special
    total3_count = count_2022_no_lateral + count_2022_lateral + count_2022_special
    total4_count = count_2021_no_lateral + count_2021_lateral + count_2021_special
    total5_count = count_2020_no_lateral + count_2020_lateral + count_2020_special
    total6_count = count_2019_no_lateral + count_2019_lateral + count_2019_special
    total7_count = count_2018_no_lateral + count_2018_lateral + count_2018_special
     
     #(N1/N)*100
    s1= (count_2019_no_lateral/count_2019_lateral)*100
    s2= (count_2020_no_lateral/count_2020_lateral)*100
    s3= (count_2021_no_lateral/count_2021_lateral)*100
    s4= (count_2022_no_lateral/count_2022_lateral)*100
    


      # students without backlog count
    students_passed_count_2024 = Students.objects.filter(
        admission_details__admission_year=2024,
        sem1_sub1_res='p',
        sem1_sub2_res='p',
        sem1_sub3_res='p',
        sem1_sub4_res='p',
        sem1_sub5_res='p',
        sem1_sub6_res='p',
        sem1_sub7_res='p',
        sem1_sub8_res='p',
        sem2_sub1_res='p',
        sem2_sub2_res='p',
        sem2_sub3_res='p',
        sem2_sub4_res='p',
        sem2_sub5_res='p',
        sem2_sub6_res='p',
        sem2_sub7_res='p',
        sem2_sub8_res='p',
    ).count()
    
    students_passed_count_2023 = Students.objects.filter(
        admission_details__admission_year=2023,
        sem1_sub1_res='p',
        sem1_sub2_res='p',
        sem1_sub3_res='p',
        sem1_sub4_res='p',
        sem1_sub5_res='p',
        sem1_sub6_res='p',
        sem1_sub7_res='p',
        sem1_sub8_res='p',
        sem2_sub1_res='p',
        sem2_sub2_res='p',
        sem2_sub3_res='p',
        sem2_sub4_res='p',
        sem2_sub5_res='p',
        sem2_sub6_res='p',
        sem2_sub7_res='p',
        sem2_sub8_res='p',
       
    ).count()

    students_passed_count_2022 = Students.objects.filter(
        admission_details__admission_year=2022,
        sem1_sub1_res='p',
        sem1_sub2_res='p',
        sem1_sub3_res='p',
        sem1_sub4_res='p',
        sem1_sub5_res='p',
        sem1_sub6_res='p',
        sem1_sub7_res='p',
        sem1_sub8_res='p',
        sem2_sub1_res='p',
        sem2_sub2_res='p',
        sem2_sub3_res='p',
        sem2_sub4_res='p',
        sem2_sub5_res='p',
        sem2_sub6_res='p',
        sem2_sub7_res='p',
        sem2_sub8_res='p',
    ).count()


    students_passed_count_2021 = Students.objects.filter(
        admission_details__admission_year=2021,
        sem1_sub1_res='p',
        sem1_sub2_res='p',
        sem1_sub3_res='p',
        sem1_sub4_res='p',
        sem1_sub5_res='p',
        sem1_sub6_res='p',
        sem1_sub7_res='p',
        sem1_sub8_res='p',
        sem2_sub1_res='p',
        sem2_sub2_res='p',
        sem2_sub3_res='p',
        sem2_sub4_res='p',
        sem2_sub5_res='p',
        sem2_sub6_res='p',
        sem2_sub7_res='p',
        sem2_sub8_res='p',
    ).count()

    students_passed_count_2020 = Students.objects.filter(
        admission_details__admission_year=2020,
        sem1_sub1_res='p',
        sem1_sub2_res='p',
        sem1_sub3_res='p',
        sem1_sub4_res='p',
        sem1_sub5_res='p',
        sem1_sub6_res='p',
        sem1_sub7_res='p',
        sem1_sub8_res='p',
        sem2_sub1_res='p',
        sem2_sub2_res='p',
        sem2_sub3_res='p',
        sem2_sub4_res='p',
        sem2_sub5_res='p',
        sem2_sub6_res='p',
        sem2_sub7_res='p',
        sem2_sub8_res='p',
    ).count()

    students_passed_count_2019 = Students.objects.filter(
        admission_details__admission_year=2019,
        sem1_sub1_res='p',
        sem1_sub2_res='p',
        sem1_sub3_res='p',
        sem1_sub4_res='p',
        sem1_sub5_res='p',
        sem1_sub6_res='p',
        sem1_sub7_res='p',
        sem1_sub8_res='p',
        sem2_sub1_res='p',
        sem2_sub2_res='p',
        sem2_sub3_res='p',
        sem2_sub4_res='p',
        sem2_sub5_res='p',
        sem2_sub6_res='p',
        sem2_sub7_res='p',
        sem2_sub8_res='p',
    ).count()

    students_passed_count_2018 = Students.objects.filter(
        admission_details__admission_year=2018,
        sem1_sub1_res='p',
        sem1_sub2_res='p',
        sem1_sub3_res='p',
        sem1_sub4_res='p',
        sem1_sub5_res='p',
        sem1_sub6_res='p',
        sem1_sub7_res='p',
        sem1_sub8_res='p',
        sem2_sub1_res='p',
        sem2_sub2_res='p',
        sem2_sub3_res='p',
        sem2_sub4_res='p',
        sem2_sub5_res='p',
        sem2_sub6_res='p',
        sem2_sub7_res='p',
        sem2_sub8_res='p',
    ).count()
     
    students_passed_count_2023_2nd = Students.objects.filter(
        admission_details__admission_year=2023,
        sem3_sub1_res='p',
        sem3_sub2_res='p',
        sem3_sub3_res='p',
        sem3_sub4_res='p',
        sem3_sub5_res='p',
        sem3_sub6_res='p',
        sem3_sub7_res='p',
        sem3_sub8_res='p',
        sem4_sub1_res='p',
        sem4_sub2_res='p',
        sem4_sub3_res='p',
        sem4_sub4_res='p',
        sem4_sub5_res='p',
        sem4_sub6_res='p',
        sem4_sub7_res='p',
        sem4_sub8_res='p',
       
    ).count()
     
    students_passed_count_2022_2nd = Students.objects.filter(
        admission_details__admission_year=2022,
        sem3_sub1_res='p',
        sem3_sub2_res='p',
        sem3_sub3_res='p',
        sem3_sub4_res='p',
        sem3_sub5_res='p',
        sem3_sub6_res='p',
        sem3_sub7_res='p',
        sem3_sub8_res='p',
        sem4_sub1_res='p',
        sem4_sub2_res='p',
        sem4_sub3_res='p',
        sem4_sub4_res='p',
        sem4_sub5_res='p',
        sem4_sub6_res='p',
        sem4_sub7_res='p',
        sem4_sub8_res='p',
        
    ).count()
    
    students_passed_count_2021_2nd = Students.objects.filter(
        admission_details__admission_year=2021,
        sem3_sub1_res='p',
        sem3_sub2_res='p',
        sem3_sub3_res='p',
        sem3_sub4_res='p',
        sem3_sub5_res='p',
        sem3_sub6_res='p',
        sem3_sub7_res='p',
        sem3_sub8_res='p',
        sem4_sub1_res='p',
        sem4_sub2_res='p',
        sem4_sub3_res='p',
        sem4_sub4_res='p',
        sem4_sub5_res='p',
        sem4_sub6_res='p',
        sem4_sub7_res='p',
        sem4_sub8_res='p',
    ).count()

    students_passed_count_2020_2nd = Students.objects.filter(
        admission_details__admission_year=2020,
        sem3_sub1_res='p',
        sem3_sub2_res='p',
        sem3_sub3_res='p',
        sem3_sub4_res='p',
        sem3_sub5_res='p',
        sem3_sub6_res='p',
        sem3_sub7_res='p',
        sem3_sub8_res='p',
        sem4_sub1_res='p',
        sem4_sub2_res='p',
        sem4_sub3_res='p',
        sem4_sub4_res='p',
        sem4_sub5_res='p',
        sem4_sub6_res='p',
        sem4_sub7_res='p',
        sem4_sub8_res='p',
        
    ).count()

    students_passed_count_2019_2nd = Students.objects.filter(
        admission_details__admission_year=2019,
        sem3_sub1_res='p',
        sem3_sub2_res='p',
        sem3_sub3_res='p',
        sem3_sub4_res='p',
        sem3_sub5_res='p',
        sem3_sub6_res='p',
        sem3_sub7_res='p',
        sem3_sub8_res='p',
        sem4_sub1_res='p',
        sem4_sub2_res='p',
        sem4_sub3_res='p',
        sem4_sub4_res='p',
        sem4_sub5_res='p',
        sem4_sub6_res='p',
        sem4_sub7_res='p',
        sem4_sub8_res='p',
        
    ).count()
     
    students_passed_count_2018_2nd = Students.objects.filter(
        admission_details__admission_year=2018,
        sem3_sub1_res='p',
        sem3_sub2_res='p',
        sem3_sub3_res='p',
        sem3_sub4_res='p',
        sem3_sub5_res='p',
        sem3_sub6_res='p',
        sem3_sub7_res='p',
        sem3_sub8_res='p',
        sem4_sub1_res='p',
        sem4_sub2_res='p',
        sem4_sub3_res='p',
        sem4_sub4_res='p',
        sem4_sub5_res='p',
        sem4_sub6_res='p',
        sem4_sub7_res='p',
        sem4_sub8_res='p',
    ).count()

    students_passed_count_2022_3nd = Students.objects.filter(
        admission_details__admission_year=2022,
        sem5_sub1_res='p',
        sem5_sub2_res='p',
        sem5_sub3_res='p',
        sem5_sub4_res='p',
        sem5_sub5_res='p',
        sem5_sub6_res='p',
        sem5_sub7_res='p',
        sem5_sub8_res='p',
        sem6_sub1_res='p',
        sem6_sub2_res='p',
        sem6_sub3_res='p',
        sem6_sub4_res='p',
        sem6_sub5_res='p',
        sem6_sub6_res='p',
        sem6_sub7_res='p',
        sem6_sub8_res='p',
        
    
    ).count()

    students_passed_count_2021_3nd = Students.objects.filter(
        admission_details__admission_year=2021,
        sem5_sub1_res='p',
        sem5_sub2_res='p',
        sem5_sub3_res='p',
        sem5_sub4_res='p',
        sem5_sub5_res='p',
        sem5_sub6_res='p',
        sem5_sub7_res='p',
        sem5_sub8_res='p',
        sem6_sub1_res='p',
        sem6_sub2_res='p',
        sem6_sub3_res='p',
        sem6_sub4_res='p',
        sem6_sub5_res='p',
        sem6_sub6_res='p',
        sem6_sub7_res='p',
        sem6_sub8_res='p',
    ).count()

    students_passed_count_2020_3nd = Students.objects.filter(
        admission_details__admission_year=2020,
        sem5_sub1_res='p',
        sem5_sub2_res='p',
        sem5_sub3_res='p',
        sem5_sub4_res='p',
        sem5_sub5_res='p',
        sem5_sub6_res='p',
        sem5_sub7_res='p',
        sem5_sub8_res='p',
        sem6_sub1_res='p',
        sem6_sub2_res='p',
        sem6_sub3_res='p',
        sem6_sub4_res='p',
        sem6_sub5_res='p',
        sem6_sub6_res='p',
        sem6_sub7_res='p',
        sem6_sub8_res='p',
       
    ).count()
     
    students_passed_count_2019_3nd = Students.objects.filter(
        admission_details__admission_year=2019,
        sem5_sub1_res='p',
        sem5_sub2_res='p',
        sem5_sub3_res='p',
        sem5_sub4_res='p',
        sem5_sub5_res='p',
        sem5_sub6_res='p',
        sem5_sub7_res='p',
        sem5_sub8_res='p',
        sem6_sub1_res='p',
        sem6_sub2_res='p',
        sem6_sub3_res='p',
        sem6_sub4_res='p',
        sem6_sub5_res='p',
        sem6_sub6_res='p',
        sem6_sub7_res='p',
        sem6_sub8_res='p',

    ).count()

    students_passed_count_2018_3nd = Students.objects.filter(
        admission_details__admission_year=2018,
        sem5_sub1_res='p',
        sem5_sub2_res='p',
        sem5_sub3_res='p',
        sem5_sub4_res='p',
        sem5_sub5_res='p',
        sem5_sub6_res='p',
        sem5_sub7_res='p',
        sem5_sub8_res='p',
        sem6_sub1_res='p',
        sem6_sub2_res='p',
        sem6_sub3_res='p',
        sem6_sub4_res='p',
        sem6_sub5_res='p',
        sem6_sub6_res='p',
        sem6_sub7_res='p',
        sem6_sub8_res='p',
    ).count()

    students_passed_count_2021_4nd = Students.objects.filter(
        admission_details__admission_year=2021,
        sem7_sub1_res='p',
        sem7_sub2_res='p',
        sem7_sub3_res='p',
        sem7_sub4_res='p',
        sem7_sub5_res='p',
        sem7_sub6_res='p',
        sem7_sub7_res='p',
        sem7_sub8_res='p',
        sem8_sub1_res='p',
        sem8_sub2_res='p',
        sem8_sub3_res='p',
        sem8_sub4_res='p',
        sem8_sub5_res='p',
        sem8_sub6_res='p',
        sem8_sub7_res='p',
        sem8_sub8_res='p',
    ).count()

    students_passed_count_2020_4nd = Students.objects.filter(
        admission_details__admission_year=2020,
        sem7_sub1_res='p',
        sem7_sub2_res='p',
        sem7_sub3_res='p',
        sem7_sub4_res='p',
        sem7_sub5_res='p',
        sem7_sub6_res='p',
        sem7_sub7_res='p',
        sem7_sub8_res='p',
        sem8_sub1_res='p',
        sem8_sub2_res='p',
        sem8_sub3_res='p',
        sem8_sub4_res='p',
        sem8_sub5_res='p',
        sem8_sub6_res='p',
        sem8_sub7_res='p',
        sem8_sub8_res='p',
    ).count()

    students_passed_count_2019_4nd = Students.objects.filter(
        admission_details__admission_year=2019,
        sem7_sub1_res='p',
        sem7_sub2_res='p',
        sem7_sub3_res='p',
        sem7_sub4_res='p',
        sem7_sub5_res='p',
        sem7_sub6_res='p',
        sem7_sub7_res='p',
        sem7_sub8_res='p',
        sem8_sub1_res='p',
        sem8_sub2_res='p',
        sem8_sub3_res='p',
        sem8_sub4_res='p',
        sem8_sub5_res='p',
        sem8_sub6_res='p',
        sem8_sub7_res='p',
        sem8_sub8_res='p',
    ).count()

    students_passed_count_2018_4nd = Students.objects.filter(
        admission_details__admission_year=2018,
        sem7_sub1_res='p',
        sem7_sub2_res='p',
        sem7_sub3_res='p',
        sem7_sub4_res='p',
        sem7_sub5_res='p',
        sem7_sub6_res='p',
        sem7_sub7_res='p',
        sem7_sub8_res='p',
        sem8_sub1_res='p',
        sem8_sub2_res='p',
        sem8_sub3_res='p',
        sem8_sub4_res='p',
        sem8_sub5_res='p',
        sem8_sub6_res='p',
        sem8_sub7_res='p',
        sem8_sub8_res='p',
    ).count()
       # total  count with and without backlogs
    students_2024 = Students.objects.filter(
        admission_details__admission_year=2024
    ).count()

    sem1_and_sem2_count_2023 = Students.objects.filter(
            admission_details__admission_year=2023
        ).filter(
            sem1_sub1_res__isnull=False, 
            sem1_sub2_res__isnull=False, 
            sem1_sub3_res__isnull=False, 
            sem1_sub4_res__isnull=False, 
            sem1_sub5_res__isnull=False, 
            sem1_sub6_res__isnull=False, 
            sem1_sub7_res__isnull=False, 
            sem1_sub8_res__isnull=False,    
            sem2_sub1_res__isnull=False, 
            sem2_sub2_res__isnull=False, 
            sem2_sub3_res__isnull=False, 
            sem2_sub4_res__isnull=False, 
            sem2_sub5_res__isnull=False, 
            sem2_sub6_res__isnull=False, 
            sem2_sub7_res__isnull=False, 
            sem2_sub8_res__isnull=False, 
        ).count()

    sem1_and_sem2_count_2022 = Students.objects.filter(
            admission_details__admission_year=2022
        ).filter(
            sem1_sub1_res__isnull=False, 
            sem1_sub2_res__isnull=False, 
            sem1_sub3_res__isnull=False, 
            sem1_sub4_res__isnull=False, 
            sem1_sub5_res__isnull=False, 
            sem1_sub6_res__isnull=False, 
            sem1_sub7_res__isnull=False, 
            sem1_sub8_res__isnull=False,
            sem2_sub1_res__isnull=False, 
            sem2_sub2_res__isnull=False, 
            sem2_sub3_res__isnull=False, 
            sem2_sub4_res__isnull=False, 
            sem2_sub5_res__isnull=False, 
            sem2_sub6_res__isnull=False, 
            sem2_sub7_res__isnull=False, 
            sem2_sub8_res__isnull=False,
        ).count() 

    sem1_and_sem2_count_2021 = Students.objects.filter(
            admission_details__admission_year=2021
        ).filter(
            sem1_sub1_res__isnull=False, 
            sem1_sub2_res__isnull=False, 
            sem1_sub3_res__isnull=False, 
            sem1_sub4_res__isnull=False, 
            sem1_sub5_res__isnull=False, 
            sem1_sub6_res__isnull=False, 
            sem1_sub7_res__isnull=False, 
            sem1_sub8_res__isnull=False,
            sem2_sub1_res__isnull=False, 
            sem2_sub2_res__isnull=False, 
            sem2_sub3_res__isnull=False, 
            sem2_sub4_res__isnull=False, 
            sem2_sub5_res__isnull=False, 
            sem2_sub6_res__isnull=False, 
            sem2_sub7_res__isnull=False, 
            sem2_sub8_res__isnull=False,
        ).count()   

    sem1_and_sem2_count_2020 = Students.objects.filter(
            admission_details__admission_year=2020
        ).filter(
            sem1_sub1_res__isnull=False, 
            sem1_sub2_res__isnull=False, 
            sem1_sub3_res__isnull=False, 
            sem1_sub4_res__isnull=False, 
            sem1_sub5_res__isnull=False, 
            sem1_sub6_res__isnull=False, 
            sem1_sub7_res__isnull=False, 
            sem1_sub8_res__isnull=False,
            sem2_sub1_res__isnull=False, 
            sem2_sub2_res__isnull=False, 
            sem2_sub3_res__isnull=False, 
            sem2_sub4_res__isnull=False, 
            sem2_sub5_res__isnull=False, 
            sem2_sub6_res__isnull=False, 
            sem2_sub7_res__isnull=False, 
            sem2_sub8_res__isnull=False,
        ).count()  

    sem1_and_sem2_count_2019 = Students.objects.filter(
            admission_details__admission_year=2019
        ).filter(
            sem1_sub1_res__isnull=False, 
            sem1_sub2_res__isnull=False, 
            sem1_sub3_res__isnull=False, 
            sem1_sub4_res__isnull=False, 
            sem1_sub5_res__isnull=False, 
            sem1_sub6_res__isnull=False, 
            sem1_sub7_res__isnull=False, 
            sem1_sub8_res__isnull=False,
            sem2_sub1_res__isnull=False, 
            sem2_sub2_res__isnull=False, 
            sem2_sub3_res__isnull=False, 
            sem2_sub4_res__isnull=False, 
            sem2_sub5_res__isnull=False, 
            sem2_sub6_res__isnull=False, 
            sem2_sub7_res__isnull=False, 
            sem2_sub8_res__isnull=False,
        ).count() 

    sem1_and_sem2_count_2018 = Students.objects.filter(
            admission_details__admission_year=2018
        ).filter(
            sem1_sub1_res__isnull=False, 
            sem1_sub2_res__isnull=False, 
            sem1_sub3_res__isnull=False, 
            sem1_sub4_res__isnull=False, 
            sem1_sub5_res__isnull=False, 
            sem1_sub6_res__isnull=False, 
            sem1_sub7_res__isnull=False, 
            sem1_sub8_res__isnull=False,
            sem2_sub1_res__isnull=False, 
            sem2_sub2_res__isnull=False, 
            sem2_sub3_res__isnull=False, 
            sem2_sub4_res__isnull=False, 
            sem2_sub5_res__isnull=False, 
            sem2_sub6_res__isnull=False, 
            sem2_sub7_res__isnull=False, 

        ).count() 
    
    sem3_and_sem4_count_2023 = Students.objects.filter(
            admission_details__admission_year=2023
        ).filter(
            sem3_sub1_res__isnull=False, 
            sem3_sub2_res__isnull=False, 
            sem3_sub3_res__isnull=False, 
            sem3_sub4_res__isnull=False, 
            sem3_sub5_res__isnull=False, 
            sem3_sub6_res__isnull=False, 
            sem3_sub7_res__isnull=False, 
            sem3_sub8_res__isnull=False,
            sem4_sub1_res__isnull=False, 
            sem4_sub2_res__isnull=False, 
            sem4_sub3_res__isnull=False, 
            sem4_sub4_res__isnull=False, 
            sem4_sub5_res__isnull=False, 
            sem4_sub6_res__isnull=False, 
            sem4_sub7_res__isnull=False, 
            sem4_sub8_res__isnull=False,
        ).count() 

    sem3_and_sem4_count_2022 = Students.objects.filter(
            admission_details__admission_year=2022
        ).filter(
            sem3_sub1_res__isnull=False, 
            sem3_sub2_res__isnull=False, 
            sem3_sub3_res__isnull=False, 
            sem3_sub4_res__isnull=False, 
            sem3_sub5_res__isnull=False, 
            sem3_sub6_res__isnull=False, 
            sem3_sub7_res__isnull=False, 
            sem3_sub8_res__isnull=False,
            sem4_sub1_res__isnull=False, 
            sem4_sub2_res__isnull=False, 
            sem4_sub3_res__isnull=False, 
            sem4_sub4_res__isnull=False, 
            sem4_sub5_res__isnull=False, 
            sem4_sub6_res__isnull=False, 
            sem4_sub7_res__isnull=False, 
            sem4_sub8_res__isnull=False,
        ).count()    


    sem3_and_sem4_count_2021 = Students.objects.filter(
            admission_details__admission_year=2021
        ).filter(
            sem3_sub1_res__isnull=False, 
            sem3_sub2_res__isnull=False, 
            sem3_sub3_res__isnull=False, 
            sem3_sub4_res__isnull=False, 
            sem3_sub5_res__isnull=False, 
            sem3_sub6_res__isnull=False, 
            sem3_sub7_res__isnull=False, 
            sem3_sub8_res__isnull=False,
            sem4_sub1_res__isnull=False, 
            sem4_sub2_res__isnull=False, 
            sem4_sub3_res__isnull=False, 
            sem4_sub4_res__isnull=False, 
            sem4_sub5_res__isnull=False, 
            sem4_sub6_res__isnull=False, 
            sem4_sub7_res__isnull=False, 
            sem4_sub8_res__isnull=False, 
        ).count() 

    sem3_and_sem4_count_2020 = Students.objects.filter(
            admission_details__admission_year=2020
        ).filter(
           sem3_sub1_res__isnull=False, 
            sem3_sub2_res__isnull=False, 
            sem3_sub3_res__isnull=False, 
            sem3_sub4_res__isnull=False, 
            sem3_sub5_res__isnull=False, 
            sem3_sub6_res__isnull=False, 
            sem3_sub7_res__isnull=False, 
            sem3_sub8_res__isnull=False,
            sem4_sub1_res__isnull=False, 
            sem4_sub2_res__isnull=False, 
            sem4_sub3_res__isnull=False, 
            sem4_sub4_res__isnull=False, 
            sem4_sub5_res__isnull=False, 
            sem4_sub6_res__isnull=False, 
            sem4_sub7_res__isnull=False, 
            sem4_sub8_res__isnull=False,
            
        ).count() 

    sem3_and_sem4_count_2019 = Students.objects.filter(
            admission_details__admission_year=2019
        ).filter(
           sem3_sub1_res__isnull=False, 
            sem3_sub2_res__isnull=False, 
            sem3_sub3_res__isnull=False, 
            sem3_sub4_res__isnull=False, 
            sem3_sub5_res__isnull=False, 
            sem3_sub6_res__isnull=False, 
            sem3_sub7_res__isnull=False, 
            sem3_sub8_res__isnull=False,
            sem4_sub1_res__isnull=False, 
            sem4_sub2_res__isnull=False, 
            sem4_sub3_res__isnull=False, 
            sem4_sub4_res__isnull=False, 
            sem4_sub5_res__isnull=False, 
            sem4_sub6_res__isnull=False, 
            sem4_sub7_res__isnull=False, 
            sem4_sub8_res__isnull=False, 
        ).count() 

    sem3_and_sem4_count_2018 = Students.objects.filter(
            admission_details__admission_year=2018
        ).filter(
            sem3_sub1_res__isnull=False, 
            sem3_sub2_res__isnull=False, 
            sem3_sub3_res__isnull=False, 
            sem3_sub4_res__isnull=False, 
            sem3_sub5_res__isnull=False, 
            sem3_sub6_res__isnull=False, 
            sem3_sub7_res__isnull=False, 
            sem3_sub8_res__isnull=False,
            sem4_sub1_res__isnull=False, 
            sem4_sub2_res__isnull=False, 
            sem4_sub3_res__isnull=False, 
            sem4_sub4_res__isnull=False, 
            sem4_sub5_res__isnull=False, 
            sem4_sub6_res__isnull=False, 
            sem4_sub7_res__isnull=False, 
            sem4_sub8_res__isnull=False, 
           
        ).count() 

    sem5_and_sem6_count_2022 = Students.objects.filter(
            admission_details__admission_year=2022
        ).filter(
            sem5_sub1_res__isnull=False, 
            sem5_sub2_res__isnull=False, 
            sem5_sub3_res__isnull=False, 
            sem5_sub4_res__isnull=False, 
            sem5_sub5_res__isnull=False, 
            sem5_sub6_res__isnull=False, 
            sem5_sub7_res__isnull=False, 
            sem5_sub8_res__isnull=False,
            sem6_sub1_res__isnull=False, 
            sem6_sub2_res__isnull=False, 
            sem6_sub3_res__isnull=False, 
            sem6_sub4_res__isnull=False, 
            sem6_sub5_res__isnull=False, 
            sem6_sub6_res__isnull=False, 
            sem6_sub7_res__isnull=False, 
            sem6_sub8_res__isnull=False,
        ).count() 

    sem5_and_sem6_count_2021 = Students.objects.filter(
            admission_details__admission_year=2021
        ).filter(
            sem5_sub1_res__isnull=False, 
            sem5_sub2_res__isnull=False, 
            sem5_sub3_res__isnull=False, 
            sem5_sub4_res__isnull=False, 
            sem5_sub5_res__isnull=False, 
            sem5_sub6_res__isnull=False, 
            sem5_sub7_res__isnull=False, 
            sem5_sub8_res__isnull=False,
            sem6_sub1_res__isnull=False, 
            sem6_sub2_res__isnull=False, 
            sem6_sub3_res__isnull=False, 
            sem6_sub4_res__isnull=False, 
            sem6_sub5_res__isnull=False, 
            sem6_sub6_res__isnull=False, 
            sem6_sub7_res__isnull=False, 
            sem6_sub8_res__isnull=False,
        ).count() 

    sem5_and_sem6_count_2020 = Students.objects.filter(
            admission_details__admission_year=2020
        ).filter(
            sem5_sub1_res__isnull=False, 
            sem5_sub2_res__isnull=False, 
            sem5_sub3_res__isnull=False, 
            sem5_sub4_res__isnull=False, 
            sem5_sub5_res__isnull=False, 
            sem5_sub6_res__isnull=False, 
            sem5_sub7_res__isnull=False, 
            sem5_sub8_res__isnull=False,
            sem6_sub1_res__isnull=False, 
            sem6_sub2_res__isnull=False, 
            sem6_sub3_res__isnull=False, 
            sem6_sub4_res__isnull=False, 
            sem6_sub5_res__isnull=False, 
            sem6_sub6_res__isnull=False, 
            sem6_sub7_res__isnull=False, 
            sem6_sub8_res__isnull=False, 
            
        ).count() 

    sem5_and_sem6_count_2019 = Students.objects.filter(
            admission_details__admission_year=2019
        ).filter(
            sem5_sub1_res__isnull=False, 
            sem5_sub2_res__isnull=False, 
            sem5_sub3_res__isnull=False, 
            sem5_sub4_res__isnull=False, 
            sem5_sub5_res__isnull=False, 
            sem5_sub6_res__isnull=False, 
            sem5_sub7_res__isnull=False, 
            sem5_sub8_res__isnull=False,
            sem6_sub1_res__isnull=False, 
            sem6_sub2_res__isnull=False, 
            sem6_sub3_res__isnull=False, 
            sem6_sub4_res__isnull=False, 
            sem6_sub5_res__isnull=False, 
            sem6_sub6_res__isnull=False, 
            sem6_sub7_res__isnull=False, 
            sem6_sub8_res__isnull=False,  
        ).count() 

    sem5_and_sem6_count_2018 = Students.objects.filter(
            admission_details__admission_year=2018
        ).filter(
            sem5_sub1_res__isnull=False, 
            sem5_sub2_res__isnull=False, 
            sem5_sub3_res__isnull=False, 
            sem5_sub4_res__isnull=False, 
            sem5_sub5_res__isnull=False, 
            sem5_sub6_res__isnull=False, 
            sem5_sub7_res__isnull=False, 
            sem5_sub8_res__isnull=False,
            sem6_sub1_res__isnull=False, 
            sem6_sub2_res__isnull=False, 
            sem6_sub3_res__isnull=False, 
            sem6_sub4_res__isnull=False, 
            sem6_sub5_res__isnull=False, 
            sem6_sub6_res__isnull=False, 
            sem6_sub7_res__isnull=False, 
            sem6_sub8_res__isnull=False,
        ).count() 

    sem7_and_sem8_count_2021 = Students.objects.filter(
            admission_details__admission_year=2021
        ).filter(
            sem7_sub1_res__isnull=False, 
            sem7_sub2_res__isnull=False, 
            sem7_sub3_res__isnull=False, 
            sem7_sub4_res__isnull=False, 
            sem7_sub5_res__isnull=False, 
            sem7_sub6_res__isnull=False, 
            sem7_sub7_res__isnull=False, 
            sem7_sub8_res__isnull=False,
            sem8_sub1_res__isnull=False, 
            sem8_sub2_res__isnull=False, 
            sem8_sub3_res__isnull=False, 
            sem8_sub4_res__isnull=False, 
            sem8_sub5_res__isnull=False, 
            sem8_sub6_res__isnull=False, 
            sem8_sub7_res__isnull=False, 
            sem8_sub8_res__isnull=False, 
        ).count() 

    sem7_and_sem8_count_2020 = Students.objects.filter(
            admission_details__admission_year=2020
        ).filter(
            sem7_sub1_res__isnull=False, 
            sem7_sub2_res__isnull=False, 
            sem7_sub3_res__isnull=False, 
            sem7_sub4_res__isnull=False, 
            sem7_sub5_res__isnull=False, 
            sem7_sub6_res__isnull=False, 
            sem7_sub7_res__isnull=False, 
            sem7_sub8_res__isnull=False,
            sem8_sub1_res__isnull=False, 
            sem8_sub2_res__isnull=False, 
            sem8_sub3_res__isnull=False, 
            sem8_sub4_res__isnull=False, 
            sem8_sub5_res__isnull=False, 
            sem8_sub6_res__isnull=False, 
            sem8_sub7_res__isnull=False, 
            sem8_sub8_res__isnull=False, 
        ).count()     


    sem7_and_sem8_count_2019 = Students.objects.filter(
            admission_details__admission_year=2019
        ).filter(
            sem7_sub1_res__isnull=False, 
            sem7_sub2_res__isnull=False, 
            sem7_sub3_res__isnull=False, 
            sem7_sub4_res__isnull=False, 
            sem7_sub5_res__isnull=False, 
            sem7_sub6_res__isnull=False, 
            sem7_sub7_res__isnull=False, 
            sem7_sub8_res__isnull=False,
            sem8_sub1_res__isnull=False, 
            sem8_sub2_res__isnull=False, 
            sem8_sub3_res__isnull=False, 
            sem8_sub4_res__isnull=False, 
            sem8_sub5_res__isnull=False, 
            sem8_sub6_res__isnull=False, 
            sem8_sub7_res__isnull=False, 
            sem8_sub8_res__isnull=False,  
        ).count() 


    sem7_and_sem8_count_2018 = Students.objects.filter(
            admission_details__admission_year=2018
        ).filter(
            sem7_sub1_res__isnull=False, 
            sem7_sub2_res__isnull=False, 
            sem7_sub3_res__isnull=False, 
            sem7_sub4_res__isnull=False, 
            sem7_sub5_res__isnull=False, 
            sem7_sub6_res__isnull=False, 
            sem7_sub7_res__isnull=False, 
            sem7_sub8_res__isnull=False,
            sem8_sub1_res__isnull=False, 
            sem8_sub2_res__isnull=False, 
            sem8_sub3_res__isnull=False, 
            sem8_sub4_res__isnull=False, 
            sem8_sub5_res__isnull=False, 
            sem8_sub6_res__isnull=False, 
            sem8_sub7_res__isnull=False, 
            sem8_sub8_res__isnull=False,  
        ).count() 

        #total number of students without backlock
    sum0=students_passed_count_2020+students_passed_count_2020_2nd+students_passed_count_2020_3nd+students_passed_count_2020_4nd 
    sum1=students_passed_count_2019+students_passed_count_2019_2nd+students_passed_count_2019_3nd+students_passed_count_2020_4nd              
    sum2=students_passed_count_2018+students_passed_count_2018_2nd+students_passed_count_2018_3nd+students_passed_count_2020_4nd 
        #success index (SI=Y/X)
    div0=(sum0/count20)
    div1=(sum1/count19)
    div2=(sum2/count18)
       #with backlogs
    abc=sem1_and_sem2_count_2020
    abc1=sem1_and_sem2_count_2019
    abc2=sem1_and_sem2_count_2018
     #success index
    SI=(abc/count20)
    SI1=(abc1/count19)
    SI2=(abc2/count18)

     # academic performance
    students_placed_count_2020 = Students.objects.filter(
        admission_details__admission_year=2020,
        placed_in_company='YES'
    ).count()

    students_placed_count_2019 = Students.objects.filter(
        admission_details__admission_year=2019,
        placed_in_company='YES'
    ).count()

    students_placed_count_2018 = Students.objects.filter(
        admission_details__admission_year=2018,
        placed_in_company='YES'
    ).count()
    
   

     # academic performance
    students_higher_count_2020 = Students.objects.filter(
        admission_details__admission_year=2020,
        higher_studies='YES'
    ).count()

    students_higher_count_2019 = Students.objects.filter(
        admission_details__admission_year=2019,
        higher_studies='YES'
    ).count()

    students_higher_count_2018 = Students.objects.filter(
        admission_details__admission_year=2018,
        higher_studies='YES'
    ).count()


    students_bus_count_2020 = Students.objects.filter(
        admission_details__admission_year=2020,
        entrepreneur='YES'
    ).count()

    students_bus_count_2019 = Students.objects.filter(
        admission_details__admission_year=2019,
        entrepreneur='YES'
    ).count()

    students_bus_count_2018 = Students.objects.filter(
        admission_details__admission_year=2018,
        entrepreneur='YES'
    ).count()

     # X+y+z
    std_1_2020 = (students_placed_count_2020 + students_higher_count_2020 + students_bus_count_2020)
    std_1_2019 = (students_placed_count_2019 + students_higher_count_2019 + students_bus_count_2019)
    std_1_2018 = (students_placed_count_2018 + students_higher_count_2018 + students_bus_count_2018)


    p1= (students_placed_count_2020 + students_higher_count_2020 + students_bus_count_2020)/total5_count
    p2 = (students_placed_count_2019 + students_higher_count_2019 + students_bus_count_2019)/total6_count
    p3 = (students_placed_count_2018 + students_higher_count_2018 + students_bus_count_2018)/total7_count


    pt=(p1 + p2 + p3)/3

     #academic performance of students in 2ndyear
    admission_2022 = AdmissionDetails.objects.filter(admission_year=2022)

    if admission_2022.exists():
        # Get all students linked to the year 2020
        students_2022 = Students.objects.filter(admission_details__admission_year=2022)

        # Initialize a list to store CGPAs
        cgpas = []

        # Loop through the students and gather sem2_cgpa and sem4_cgpa
        for student in students_2022:
            if student.sem3_cgpa is not None:
                cgpas.append(student.sem3_cgpa)
            if student.sem4_cgpa is not None:
                cgpas.append(student.sem4_cgpa)

        # Calculate the mean CGPA for sem2 and sem4
        total_mean_cgpa_2022 = sum(cgpas) / len(cgpas) 
    else:
        total_mean_cgpa_2022 = 0  # No students for the year 2020


    admission_2021 = AdmissionDetails.objects.filter(admission_year=2021)

    if admission_2021.exists():
        # Get all students linked to the year 2020
        students_2021 = Students.objects.filter(admission_details__admission_year=2021)

        # Initialize a list to store CGPAs
        cgpas = []

        # Loop through the students and gather sem2_cgpa and sem4_cgpa
        for student in students_2021:
            if student.sem3_cgpa is not None:
                cgpas.append(student.sem3_cgpa)
            if student.sem4_cgpa is not None:
                cgpas.append(student.sem4_cgpa)

        # Calculate the mean CGPA for sem2 and sem4
        total_mean_cgpa_2021 = sum(cgpas) / len(cgpas) 
    else:
        total_mean_cgpa_2021 = 0  # No students for the year 2020  


    admission_2020 = AdmissionDetails.objects.filter(admission_year=2020)

    if admission_2020.exists():
        # Get all students linked to the year 2020
        students_2020 = Students.objects.filter(admission_details__admission_year=2020)

        # Initialize a list to store CGPAs
        cgpas = []

        # Loop through the students and gather sem2_cgpa and sem4_cgpa
        for student in students_2020:
            if student.sem3_cgpa is not None:
                cgpas.append(student.sem3_cgpa)
            if student.sem4_cgpa is not None:
                cgpas.append(student.sem4_cgpa)

        # Calculate the mean CGPA for sem2 and sem4
        total_mean_cgpa_2020 = sum(cgpas) / len(cgpas) 
    else:
        total_mean_cgpa_2020 = 0  # No students for the year 2020  


    # meanapi
    api21=  (total_mean_cgpa_2022)*(sem3_and_sem4_count_2022/sem3_and_sem4_count_2022)  
    api22=  (total_mean_cgpa_2020)*(sem3_and_sem4_count_2020/sem3_and_sem4_count_2020) 
    api23=  (total_mean_cgpa_2021)*(sem3_and_sem4_count_2021/sem3_and_sem4_count_2021) 

    # 3re year academic performance

    admission_2021 = AdmissionDetails.objects.filter(admission_year=2021)

    if admission_2021.exists():
        # Get all students linked to the year 2020
        students_2021 = Students.objects.filter(admission_details__admission_year=2021)

        # Initialize a list to store CGPAs
        cgpas = []

        # Loop through the students and gather sem2_cgpa and sem4_cgpa
        for student in students_2021:
            if student.sem5_cgpa is not None:
                cgpas.append(student.sem5_cgpa)
            if student.sem6_cgpa is not None:
                cgpas.append(student.sem6_cgpa)

        # Calculate the mean CGPA for sem2 and sem4
        total_mean_cgpa_2021_3 = sum(cgpas) / len(cgpas) 
    else:
        total_mean_cgpa_2021_3 = 0  





    admission_2020 = AdmissionDetails.objects.filter(admission_year=2020)

    if admission_2020.exists():
        # Get all students linked to the year 2020
        students_2020 = Students.objects.filter(admission_details__admission_year=2020)

        # Initialize a list to store CGPAs
        cgpas = []

        # Loop through the students and gather sem2_cgpa and sem4_cgpa
        for student in students_2020:
            if student.sem5_cgpa is not None:
                cgpas.append(student.sem5_cgpa)
            if student.sem6_cgpa is not None:
                cgpas.append(student.sem6_cgpa)

        # Calculate the mean CGPA for sem2 and sem4
        total_mean_cgpa_2020_3 = sum(cgpas) / len(cgpas) 
    else:
        total_mean_cgpa_2020_3 = 0  

    admission_2019 = AdmissionDetails.objects.filter(admission_year=2019)
    if admission_2019.exists():
        # Get all students linked to the year 2020
        students_2019 = Students.objects.filter(admission_details__admission_year=2019)

        # Initialize a list to store CGPAs
        cgpas = []

        # Loop through the students and gather sem2_cgpa and sem4_cgpa
        for student in students_2019:
            if student.sem5_cgpa is not None:
                cgpas.append(student.sem5_cgpa)
            if student.sem6_cgpa is not None:
                cgpas.append(student.sem6_cgpa)

        # Calculate the mean CGPA for sem2 and sem4
        total_mean_cgpa_2019_3 = sum(cgpas) / len(cgpas) 
    else:
        total_mean_cgpa_2019_3 = 0   


    api31=  (total_mean_cgpa_2021_3)*(sem5_and_sem6_count_2021/sem5_and_sem6_count_2021)  
    api32=  (total_mean_cgpa_2020_3)*(sem5_and_sem6_count_2020/sem5_and_sem6_count_2020) 
    api33=  (total_mean_cgpa_2019_3)*(sem5_and_sem6_count_2019/sem5_and_sem6_count_2019)    


    company_details = company_info.objects.select_related('admission_details').all() 
     
    




    context = {
        'company_details':company_details,
        'total_mean_cgpa_2021_3': total_mean_cgpa_2021_3,
        'total_mean_cgpa_2020_3': total_mean_cgpa_2020_3,
        'total_mean_cgpa_2019_3': total_mean_cgpa_2019_3,
        'api31':api31,
        'api32':api32,
        'api33':api33,


        'api21':api21,
        'api22':api22,
        'api23':api23,

        'total_mean_cgpa_2022': total_mean_cgpa_2022,
        'total_mean_cgpa_2020': total_mean_cgpa_2020,
        'total_mean_cgpa_2021': total_mean_cgpa_2021,
        'pt':pt,
        'p1':p1,
        'p2':p2,
        'p3':p3,
        'std_1_2020':std_1_2020,
        'std_1_2019':std_1_2019,
        'std_1_2018':std_1_2018,

        'students_bus_count_2018':students_bus_count_2018,
        'students_bus_count_2019':students_bus_count_2019,
        'students_bus_count_2020':students_bus_count_2020,
       


        'students_higher_count_2020':students_higher_count_2020,
        'students_higher_count_2019':students_higher_count_2018,
        'students_higher_count_2018':students_higher_count_2018,


        'students_placed_count_2020':students_placed_count_2020,
        'students_placed_count_2019':students_placed_count_2019,
        'students_placed_count_2018':students_placed_count_2018,
        'sem7_and_sem8_count_2020':sem7_and_sem8_count_2020,
        'sem7_and_sem8_count_2019':sem7_and_sem8_count_2019,
        'sem7_and_sem8_count_2018':sem7_and_sem8_count_2018,
        'sem7_and_sem8_count_2021':sem7_and_sem8_count_2021,

        'sem5_and_sem6_count_2022':sem5_and_sem6_count_2022,
        'sem5_and_sem6_count_2021':sem5_and_sem6_count_2021,
        'sem5_and_sem6_count_2020':sem5_and_sem6_count_2020,
        'sem5_and_sem6_count_2019':sem5_and_sem6_count_2019,
        'sem5_and_sem6_count_2018':sem5_and_sem6_count_2018,
        
        'sem3_and_sem4_count_2023':sem3_and_sem4_count_2023,
        'sem3_and_sem4_count_2022':sem3_and_sem4_count_2022,
        'sem3_and_sem4_count_2021':sem3_and_sem4_count_2021,
        'sem3_and_sem4_count_2020':sem3_and_sem4_count_2020,
        'sem3_and_sem4_count_2019':sem3_and_sem4_count_2019,
        'sem3_and_sem4_count_2018':sem3_and_sem4_count_2018,

        'sem1_and_sem2_count_2023': sem1_and_sem2_count_2023,
        'sem1_and_sem2_count_2022': sem1_and_sem2_count_2022,
        'sem1_and_sem2_count_2021': sem1_and_sem2_count_2021,
        'sem1_and_sem2_count_2020': sem1_and_sem2_count_2020,
        'sem1_and_sem2_count_2019': sem1_and_sem2_count_2019,
        'sem1_and_sem2_count_2018': sem1_and_sem2_count_2018,
        'students_2024':students_2024,

        'students_passed_count_2021_4nd':students_passed_count_2021_4nd,
        'students_passed_count_2020_4nd':students_passed_count_2020_4nd,
        'students_passed_count_2019_4nd':students_passed_count_2019_4nd,
        'students_passed_count_2018_4nd':students_passed_count_2018_4nd,

        'students_passed_count_2022_3nd':students_passed_count_2022_3nd,
        'students_passed_count_2021_3nd':students_passed_count_2021_3nd,
        'students_passed_count_2020_3nd':students_passed_count_2020_3nd,
        'students_passed_count_2019_3nd':students_passed_count_2019_3nd,
        'students_passed_count_2018_3nd':students_passed_count_2018_3nd,

        'students_passed_count_2023_2nd':students_passed_count_2023_2nd,
        'students_passed_count_2022_2nd':students_passed_count_2022_2nd,
        'students_passed_count_2021_2nd':students_passed_count_2021_2nd,
        'students_passed_count_2020_2nd':students_passed_count_2020_2nd,
        'students_passed_count_2019_2nd':students_passed_count_2019_2nd,
        'students_passed_count_2018_2nd':students_passed_count_2018_2nd,

        'students_passed_count_2024':students_passed_count_2024,
        'students_passed_count_2023':students_passed_count_2023,
        'students_passed_count_2022':students_passed_count_2022,
        'students_passed_count_2021':students_passed_count_2021,
        'students_passed_count_2020':students_passed_count_2020,
        'students_passed_count_2019':students_passed_count_2019,
        'students_passed_count_2018':students_passed_count_2018,
        
        'count_2024': count_2024,
        'count_2023': count_2023,
        'count_2022': count_2022,
        'count_2021': count_2021,
        'count_2020': count_2020,
        'count_2019': count_2019,
        'count_2018': count_2018,
        'count_2024_no_lateral': count_2024_no_lateral,
        'count_2023_no_lateral': count_2023_no_lateral,
        'count_2022_no_lateral': count_2022_no_lateral,
        'count_2021_no_lateral': count_2021_no_lateral,
        'count_2020_no_lateral': count_2020_no_lateral,
        'count_2019_no_lateral': count_2019_no_lateral,
        'count_2018_no_lateral': count_2018_no_lateral,
        'count_2024_lateral': count_2024_lateral,
        'count_2023_lateral': count_2023_lateral,
        'count_2022_lateral': count_2022_lateral,
        'count_2021_lateral': count_2021_lateral,
        'count_2020_lateral': count_2020_lateral,
        'count_2019_lateral': count_2019_lateral,
        'count_2018_lateral': count_2018_lateral,
        'count_2024_special': count_2024_special,
        'count_2023_special': count_2023_special,
        'count_2022_special': count_2022_special,
        'count_2021_special': count_2021_special,
        'count_2020_special': count_2020_special,
        'count_2019_special': count_2019_special,
        'count_2018_special': count_2018_special,
        'total1_count': total1_count,
        'total2_count': total2_count,
        'total3_count': total3_count,
        'total4_count': total4_count,
        'total5_count': total5_count,
        'total6_count': total6_count,
        'total7_count': total7_count,
        'count20':count20,
        'count19':count19,
        'count18':count18,
        'div0':div0,
        'div1':div1,
        'div2':div2,
        's1':s1,
        's2':s2,
        's3':s3,
        's4':s4,
        'sum0':sum0,
        'sum1':sum1,
        'sum2':sum2,
        'SI':SI,
        'SI1':SI1,
        'SI2':SI2,
        'abc':abc,
        'abc1':abc1,
        'abc2':abc2,
        'name': request.POST.get('name', 'Default Name'),
        'table_data': [
            {'id': 1, 'value': 'Value 1'},
            {'id': 2, 'value': 'Value 2'},
        ]
    }

    
    return render(request, 'mininba/student_count.html', context)

def instruction_view(request):
    return render(request, 'mininba/instruction.html') 


def serve_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        return HttpResponseNotFound("File not found.")



