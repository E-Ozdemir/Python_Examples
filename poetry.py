!pip install -q streamlit
%%writefile app.py
# bos file olusturur

import streamlit as st #uygulama yapmamiza ve basit web sayfasi yapmamiza yarayan kütüphane.

st.title('Kitaya dönüstürücü uygulama')

path = None
path = st.file_uploader('Upload your text file: ',type = ['txt']) 
#file_uploader dosyayi yüklememize yariyor hangi tip yazarsak sadece o dosyalari okuyabilir.

if path :  # artik None degilse calis diyoruz burada 
  with open(path,'r', encoding='utf-8') as ff:
    new_lines = ff.readlines()

  counter = 0
  with open('istiklal.txt','w') as f:
    for i in dortluk:
      counter += 1
      if counter % 4 == 0: # her dört satirdan sonra bos bir new line yazdiriyoruz.
        counter = 0
        f.write(i+'\n')
      else:
        f.write(i)
