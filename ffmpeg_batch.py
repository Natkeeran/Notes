# coding: utf-8

# In[6]:


import glob
import os


# In[7]:


media_list = glob.glob("/srv/dsu-backup/Backup-Area/fedora-export/nearby-exports/*.mp4")


# In[11]:


for file_path in media_list:
    head, tail = os.path.split(file_path)
    file_name = os.path.splitext(tail)[0]
    #cmd = "ffmpeg -hide_banner -i " + file_path + " -acodec alac /srv/dsu-backup/Backup-Area/fedora-export/nearby_audio/" + file_name + ".m4a"
    cmd = "ffmpeg -hide_banner -i " + file_path + " -c:v libx264 -profile:v high -c:a aac -profile:a aac_low -strict -2 /srv/dsu-backup/Backup-Area/fedora-export/nearby_video/" + file_name + ".mp4"

    os.system(cmd)

    print(file_name)
