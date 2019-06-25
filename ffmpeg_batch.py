  GNU nano 2.5.3            File: ffmpeg_batch.py                               

# coding: utf-8

# In[6]:


import glob
import os


# In[7]:


media_list = glob.glob("/srv/dsu-backup/Backup-Area/fedora-export/nearby-export$


# In[11]:


for file_path in media_list:
    head, tail = os.path.split(file_path)
    file_name = os.path.splitext(tail)[0]
    #cmd = "ffmpeg -hide_banner -i " + file_path + " -acodec alac /srv/dsu-back$
    cmd = "ffmpeg -hide_banner -i " + file_path + " -c:v libx264 -profile:v hig$

    os.system(cmd)
    
    print(file_name)


