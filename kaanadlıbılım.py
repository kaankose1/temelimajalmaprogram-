#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess

def disk_image():
    device = input("Disk bölümü adı (örn: /dev/sda): ")
    image_name = input("İmaj dosyasının adı: ")
    try:
        subprocess.run(["dd", "if="+device, "of="+image_name, "bs=4M"])
        print("Disk bölümü imajı başarıyla alındı!")
    except:
        print("Bir hata oluştu, imaj alınamadı.")

disk_image()


# In[ ]:




