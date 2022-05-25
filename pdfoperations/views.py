import datetime
from distutils.util import convert_path
from http.client import HTTPResponse
from tkinter import BROWSE
from django.http import FileResponse, JsonResponse
import os
from django.shortcuts import render
from PIL import Image
from django.core.files.storage import FileSystemStorage
from fpdf import FPDF
import img2pdf
from django.conf import settings
import io
import PyPDF2
from pylovepdf.ilovepdf import ILovePdf 
from PyPDF2 import PdfFileWriter, PdfFileReader

from DocumentManipulation.settings import MEDIA_ROOT # to Unlock PDF, to Lock PDF

def returnFile(path):
    print(path)

    path = path[len('E:\\Projects\\New WinRAR ZIP archive\\'):]
    print(path)
    return JsonResponse({"filePath":path})



###################################################################################################
##########################################-MERGE TWO PDF-##########################################
#################################################DONE##############################################

def mergePDFs(pdfs,name):
    mergeFile = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        mergeFile.append(PyPDF2.PdfFileReader(pdf, 'rb'))

    img_path = os.path.join(settings.MEDIA_ROOT, name) # stored image path
    mergeFile.write(img_path)         
    return img_path

def mergePDF(request):
    logf = open("download.log", "w")
    try:
        if request.method == 'POST' and request.FILES:
            pdfName = ""
            pdfs = []
            print(request.FILES)
            for name,pdf in request.FILES.items():
                # print(pdf)
                # pdfs.append(io.BytesIO(pdf.read()))
                pdfs.append(pdf)
            # print(pdfs)
            path = mergePDFs(pdfs,"Merged.pdf")

            return returnFile(path)

        else:
            return JsonResponse({"err":"No Files were received"}) 
    except Exception as e:
        logf.write(str(e))
        print(e)
        return JsonResponse({"err":"Something went Wrong"}) 

def CompressPDF_Func(filename):

    pdf_path = settings.MEDIA_ROOT + filename
    public_key = 'project_public_0eed65dc44084dc02fccb90b7d4c7f3c_WMfTObe104a679401ae2b10300f3e09ecce2a'
    api = ILovePdf(public_key, verify_ssl=True)
    task = api.new_task('compress')
    task.add_file(pdf_path)
    task.set_output_folder(settings.MEDIA_ROOT)
    
    task.execute()
    compressed_pdf_name = task.download()
    task.delete_current_task()
    return settings.MEDIA_ROOT + compressed_pdf_name

def CompressPDF(request):
    logf = open("download.log", "w")
    try:
        if request.method == 'POST' and request.FILES:
            fs = FileSystemStorage()
            pdfs = []
            pdfName = ''
            for name,pdf in request.FILES.items():
                    pdfs.append(io.BytesIO(pdf.read()))
                    pdfName = pdf.name
            uploaded_pdf = pdfs[0]
            print(pdfName)
            file_name = fs.save(pdfName, uploaded_pdf) # Saving uploaded file with updated names
            
            path = CompressPDF_Func(file_name)
            fs.delete(pdfName)
            return returnFile(path)
        else:
            return JsonResponse({"err":"No Files were received"}) 
    except Exception as e:
        logf.write(str(e))
        return JsonResponse({"err":"Something went Wrong"})


# this function will return current timeStamp to differenciate pdf names
def return_Time():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return timestampStr

# ########################################################################################

# # this function will DELETE the files which are  sent as parameter from media folder
def delete_Files(file_list):
    for file_name in file_list:
        file_path = MEDIA_ROOT + file_name
        print("file_path : ", file_path)
        if os.path.exists(file_path):
            os.remove(file_path)

########################################################################################

#Unlock PDF#############################################################################
#DOnE

def UnlockPDF_Func(filename, password):
    pdf_path = MEDIA_ROOT + filename
    print("pdf_path : ", pdf_path)
    if '-protected.pdf' in filename:
        decrypted_pdf_name = filename.replace('-protected.pdf','-decrypted.pdf')
    else:
        decrypted_pdf_name = filename.replace('.pdf','-decrypted.pdf')
    print("decrypted_pdf_name : ", decrypted_pdf_name)
    decrypted_pdf_path = MEDIA_ROOT + decrypted_pdf_name
    print("decrypted_pdf_path : ", decrypted_pdf_path)
    out = PdfFileWriter()
    file = PdfFileReader(pdf_path)
    if file.isEncrypted:
        file.decrypt(password)
        for idx in range(file.numPages):
            page = file.getPage(idx)
            out.addPage(page)
        with open(decrypted_pdf_path, "wb") as f:
            out.write(f)
        print("File decrypted Successfully.")
    else:
        print("File already decrypted.")
    #
    to_delete_files = []
    to_delete_files.append(filename)
    delete_Files(to_delete_files)  # deletes user uploaded files
    #
    return decrypted_pdf_name, decrypted_pdf_path

def UnlockPDF(request):
    if request.method == 'POST' and request.FILES:
        fs = FileSystemStorage()
        uploaded_protected_pdf :object
        for name,pdf in request.FILES.items():
            if name != 'password':
                uploaded_protected_pdf = pdf
                break

        password = request.POST['password']
        file_name = fs.save(uploaded_protected_pdf.name, uploaded_protected_pdf) # Saving uploaded file with updated unique names
        unlocked_pdf_name, unlocked_pdf_path = UnlockPDF_Func(file_name, password)
        print("unlocked_pdf_name : ", unlocked_pdf_name)
        print("unlocked_pdf_path : ", unlocked_pdf_path)
        return returnFile(unlocked_pdf_path)
        # converted_pdf = open(compressed_pdf_path, 'rb')
        # return FileResponse(converted_pdf, content_type='application/pdf')
    else:
        return JsonResponse({"err":"Something went Wrong"})

#Protect PDF############################################################################
#DOnE

def ProtectPDF_Func(filename, password):
    pdf_path = MEDIA_ROOT + filename
    encrypted_pdf_name = filename.replace('.pdf','-protected.pdf')
    print("encrypted_pdf_name : ", encrypted_pdf_name)
    encrypted_pdf_path = MEDIA_ROOT + encrypted_pdf_name
    print("encrypted_pdf_path : ", encrypted_pdf_path)
    print("password : ", password)
    out = PdfFileWriter()
    file = PdfFileReader(pdf_path)
    num = file.numPages
    for idx in range(num):
        page = file.getPage(idx)
        out.addPage(page)
    out.encrypt(password)
    with open(encrypted_pdf_path, "wb") as f:
        out.write(f)
    #
    to_delete_files = []
    to_delete_files.append(filename)
    delete_Files(to_delete_files)  # deletes user uploaded files
    #
    return encrypted_pdf_name, encrypted_pdf_path

def ProtectPDF(request):
    print(request.POST)
    if request.method == 'POST' and request.FILES:
        fs = FileSystemStorage()
        uploaded_pdf  :object
        for name,pdf in request.FILES.items():
            if name != 'password':
                uploaded_pdf = pdf
                break
        password = request.POST['password']
        file_name = fs.save(uploaded_pdf.name, uploaded_pdf) # Saving uploaded file with updated unique names
        encrypted_pdf_name, encrypted_pdf_path = ProtectPDF_Func(file_name, password)
        print("encrypted_pdf_name : ", encrypted_pdf_name)
        print("encrypted_pdf_path : ", encrypted_pdf_path)
        return returnFile(encrypted_pdf_path)
        # converted_pdf = open(compressed_pdf_path, 'rb')
        # return FileResponse(converted_pdf, content_type='application/pdf')
    else:
        return JsonResponse({"err":"Something went Wrong"})


def SplitPDF_Func(filename):
    pdf_path = MEDIA_ROOT + filename
    print("pdf_path : ", pdf_path)
    public_key = 'project_public_0eed65dc44084dc02fccb90b7d4c7f3c_WMfTObe104a679401ae2b10300f3e09ecce2a'
    ilovepdf = ILovePdf(public_key, verify_ssl=True)
    task = ilovepdf.new_task('split')
    task.add_file(pdf_path)
    task.set_output_folder(MEDIA_ROOT)
    task.execute()
    splitted_zipfile_name = task.download()
    # print("splitted_zipfile_name : ", splitted_zipfile_name)
    task.delete_current_task()
    splitted_zipfile_path = MEDIA_ROOT + splitted_zipfile_name
    print("splitted_zipfile_path : ", splitted_zipfile_path)
    #

    to_delete_files = []
    to_delete_files.append(filename)
    delete_Files(to_delete_files)  # deletes user uploaded files
    #
    return splitted_zipfile_name, splitted_zipfile_path

def Split(request):
    try:
        if request.method == 'POST' and request.FILES:
            fs = FileSystemStorage()
            uploaded_pdf  :object
            for name,pdf in request.FILES.items():
                uploaded_pdf = pdf
                break
            file_name = fs.save(uploaded_pdf.name, uploaded_pdf) # Saving uploaded file with updated unique names
            splitted_zipfile_name, splitted_zipfile_path = SplitPDF_Func(file_name)
            print("splitted_zipfile_name : ", splitted_zipfile_name)
            print("splitted_zipfile_path : ", splitted_zipfile_path)

            return returnFile(splitted_zipfile_path)
        else:
            return JsonResponse({"err":"Something went Wrong"})
    except Exception as e:
            return JsonResponse({"err":"Something went Wrong"})


def extract(request):
    pass








# # this function will return current timeStamp to differenciate pdf names
# def return_Time():
#     dateTimeObj = datetime.now()
#     timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
#     return timestampStr

# ########################################################################################

# # this function will DELETE the files which are  sent as parameter from media folder
# def delete_Files(file_list):
#     for file_name in file_list:
#         file_path = settings.MEDIA_ROOT + file_name
#         print("file_path : ", file_path)
#         if os.path.exists(file_path):
#             os.remove(file_path)

# ########################################################################################

# # this function will Save document details to database
# def save_DocDetails_to_DB(file_name, request, fileType):
#     uploaded_docDetails = uploaded_DocDetails.objects.all()
#     print("uploaded_docDetails : ", uploaded_docDetails)
#     file_path = settings.MEDIA_ROOT + file_name
#     print("file_path : ", file_path)
#     if request.user.is_authenticated:
#         print("datetime.now() : ", datetime.now())
#         docDetails_Object = uploaded_DocDetails(fileName=file_name, filePath=file_path, typrOfFile=fileType, UserName=request.user.username)
#     else:
#         print("datetime.now() : ", datetime.now())
#         docDetails_Object = uploaded_DocDetails(fileName=file_name, filePath=file_path, typrOfFile=fileType)
#     docDetails_Object.save()

