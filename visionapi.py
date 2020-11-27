
from google.cloud import vision
import io,os
import csv

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'json 파일 입력'
client = vision.ImageAnnotatorClient()
path = r'C:\Users\adrie\Documents\Python Venv\snackgray2.jpg'
#path = r'C:\Users\adrie\Documents\Python Venv\imagegray.jpg'

with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

price_candidate = []
card_number_candidate = []
date_candidate = []

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')


name =""
for text in texts[1:]:
    content = text.description
    #content = content.replace(',','')
    #print("{}".format(content), end="")
    #print(content, end="")
    name+=content

print(name)

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))




f = open(r'C:\Users\adrie\Desktop\total1.csv', "rt")
reader = csv.reader(f)

col1=[]
col2=[]
col3=[]
col4=[]
col5=[]

for row in reader:

    col1.append(row[0])
    col2.append(row[1])
    col3.append(row[2])
    col4.append(row[3])
    col5.append(row[4])

del col1[200:]
del col2[21:]
#del col3[1288:]
del col4[115:]
del col5[70:]

# print(col1)
# print(col2)
list =[col1, col2, col3, col4, col5]
print(list[0])
case = ["논비건","세미", "페스코", "락토오보", "오보", "비건"]
k=0
for i in range(5):
    for j in list[i]:
        if j in name:
            k+=1
            if k==1:
                print(case[i])
                break


