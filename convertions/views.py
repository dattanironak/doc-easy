from datetime import datetime
import json
from django.http import JsonResponse
import os
from PIL import Image
from django.core.files.storage import FileSystemStorage
import img2pdf
from django.conf import settings
from requests import options, request
import pdfkit
from DocumentManipulation.settings import MEDIA_ROOT,MEDIA_URL
import groupdocs_conversion_cloud
from shutil import copyfile # to EXCEL to PDF 

def returnFile(path):
    print(path)

    path = path[len('E:\\Projects\\New WinRAR ZIP archive\\'):]
    print(path)
    return JsonResponse({"filePath":path})


# Converts single image to pdf and returns path to that PDF
def singleImage_to_PDF(uploaded_file):
    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)  # saves file
    print("Filename : ", filename)
    img_path = os.path.join(settings.MEDIA_ROOT, filename)  # stored image path
    print("img_path : ", img_path)
    if ".JPG" in img_path:
        pdf_path = img_path.replace(".JPG", "_Coverted.pdf")
    elif ".jpg" in img_path:
        pdf_path = img_path.replace(".jpg", "_Coverted.pdf")
    elif ".JPEG" in img_path:
        pdf_path = img_path.replace(".JPEG", "_Coverted.pdf")
    elif ".jpeg" in img_path:
        pdf_path = img_path.replace(".jpeg", "_Coverted.pdf")
    elif ".PNG" in img_path:
        pdf_path = img_path.replace(".PNG", "_Coverted.pdf")
    elif ".png" in img_path:
        pdf_path = img_path.replace(".png", "_Coverted.pdf")
    image = Image.open(img_path)  # opening image
    print(image)
    pdf_bytes = img2pdf.convert(image.filename)  # converting into chunks using img2pdf
    file = open(pdf_path, "wb")  # opening or creating pdf file
    file.write(pdf_bytes)  # writing pdf files with chunks
    image.close()  # closig image
    # os.remove(img_path)  # removig image
    file.close()  # closig file
    return pdf_path

def ImgtoPDF(request):
    print(request)
    if request.method == 'POST' and request.FILES:
        print(request.FILES)
        for name,file in request.FILES.items():
            uploaded_image =file
            break
    
        print(uploaded_image)
        path = singleImage_to_PDF(uploaded_image)

        return returnFile(path)
    else:
        return JsonResponse({"err":"No Files were received"})

# this function will return current timeStamp to differenciate pdf names
def return_Time():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return timestampStr

# this function will DELETE the files which are  sent as parameter from media folder
def delete_Files(file_list):
    for file_name in file_list:
        file_path = MEDIA_ROOT + file_name
        print("file_path : ", file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
#WORD to PDF############################################################################
#DOnE

def WORDToPDF_Func(filename):
    word_path = MEDIA_ROOT + filename
    pdf_name = filename.replace(".docx",".pdf")
    pdf_path = MEDIA_ROOT + pdf_name
    instructions = {
        'parts': [
            {
                'file': 'document'
            }
        ]
    }
    response = request(
        'POST',
        'https://api.pspdfkit.com/build',
        headers={
            'Authorization': 'Bearer pdf_live_dM9fhAsWkOXv2ctQsusElVRhESAu41mTwtU5WrtA1sF'
        },
        files={
            'document': open(word_path, 'rb')
        },
        data={
            'instructions': json.dumps(instructions)
        },
        stream=True
    )
    if response.ok:
        with open(pdf_path, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=8096):
                fd.write(chunk)
    else:
        print(response.text)
        exit()
    #
    to_delete_files = []
    to_delete_files.append(filename)
    delete_Files(to_delete_files)  # deletes user uploaded files
    #
    return pdf_name, pdf_path

def WORDtoPDF(request):
    print(request.FILES)
    if request.method == 'POST' and request.FILES:
        fs = FileSystemStorage()

        pdfName = ""
        uploaded_word_file: object
        for name,word in request.FILES.items():
            uploaded_word_file = word

        newFileName = uploaded_word_file.name.replace(".docx",(return_Time()+".docx"))
        file_name = fs.save(uploaded_word_file.name, uploaded_word_file)
        print(newFileName)
        converted_pdf_name, converted_pdf_path = WORDToPDF_Func(file_name)
        print("converted_pdf_name : ", converted_pdf_name)
        print("converted_pdf_path : ", converted_pdf_path)

        return returnFile(converted_pdf_path)
    else:
        return JsonResponse({ 'err':"something went wrong"})

def PPTtoPDF_Func(filename):
    ppt_path = MEDIA_ROOT + filename
    if ".pptx" in filename:
        pdf_name = filename.replace(".pptx",".pdf")
    elif ".ppt" in filename:
        pdf_name = filename.replace(".ppt",".pdf")
    pdf_path = MEDIA_ROOT + pdf_name
    instructions = {
        'parts': [
            {
            'file': 'document'
            }
        ]
    }
    response = request(
    'POST',
    'https://api.pspdfkit.com/build',
    headers = {
        'Authorization': 'Bearer pdf_live_dM9fhAsWkOXv2ctQsusElVRhESAu41mTwtU5WrtA1sF'
    },
    files = {
        'document': open(ppt_path, 'rb')
    },
    data = {
        'instructions': json.dumps(instructions)
    },
    stream = True
    )
    if response.ok:
        with open(pdf_path, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=8096):
                fd.write(chunk)
    else:
        print(response.text)
        exit()
    #
    to_delete_files = []
    to_delete_files.append(filename)
    delete_Files(to_delete_files)  # deletes user uploaded files
    #
    return pdf_name, pdf_path

def PPTtoPDF(request):
    if request.method == 'POST' and request.FILES:
       
        fs = FileSystemStorage()
        uploaded_ppt :object
        for name,ppt in request.FILES.items():
            uploaded_ppt = ppt

        file_name = fs.save(uploaded_ppt.name, uploaded_ppt)
        converted_pdf_name, converted_pdf_path = PPTtoPDF_Func(file_name)
        print("converted_pdf_name : ", converted_pdf_name)
        print("converted_pdf_path : ", converted_pdf_path)

        return returnFile(converted_pdf_path)
    else:
        return JsonResponse({ 'err':"something went wrong"})


def excelToPDF_Func(filename):
    excel_path = MEDIA_ROOT + filename
    if ".xlsx" in filename:
        pdf_name = filename.replace(".xlsx",".pdf")
    elif ".xls" in filename:
        pdf_name = filename.replace(".xls",".pdf")
    pdf_path = MEDIA_ROOT + pdf_name
    client_id = "2e818d52-2be0-4ef1-97c1-1778fb591bef"
    client_key = "a898e4b606d84a88d4bca3e2476394c2"
    convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(client_id, client_key)
    try:
        request = groupdocs_conversion_cloud.ConvertDocumentDirectRequest("pdf", excel_path)
        result = convert_api.convert_document_direct(request)       
        copyfile(result, pdf_path)
    except groupdocs_conversion_cloud.ApiException as e:
        print("Exception when calling get_supported_conversion_types: {0}".format(e.message))
    #
    to_delete_files = []
    to_delete_files.append(filename)
    delete_Files(to_delete_files)  # deletes user uploaded files
    #
    return pdf_name, pdf_path

def ExcelToPDF(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = []
        fs = FileSystemStorage()
        origial_excel  :object
        for name,excel in request.FILES.items():
            origial_excel = excel
       
        file_name = fs.save(origial_excel.name, origial_excel)
        converted_pdf_name, converted_pdf_path = excelToPDF_Func(file_name)
        print("converted_pdf_name : ", converted_pdf_name)
        print("converted_pdf_path : ", converted_pdf_path)
        return returnFile(converted_pdf_path)
    else:
        return JsonResponse({ 'err':"something went wrong"})


def TexttoPDF(request):
    pass
