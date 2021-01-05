
#!/usr/bin/env python
# coding: utf-8

# In[63]:

import pandas as pd
import glob, os, shutil, csv,sys,pprint,string,re,zipfile,time
import win32com.client
from win32com.client import Dispatch


#converting the mapping file to key value pairs
with open(variables_file, 'r') as f:
        d = dict(filter(None, csv.reader(f)))
        
#function to get the folder detail of a particular file name
def get_folder_details(file_name):
    if file_name in d:
        folder_name = d.get(file_name)
        return folder_name
    
#function to move file to destination folder    
def file_move(x):
    for eachKey in d.keys():
        if x.startswith(eachKey) and os.path.isfile(os.path.join(path,x)):
            value = get_folder_details(eachKey)
            #if the folder already exist - Move the file to the foler
            if(os.path.exists(value)):
                shutil.move(os.path.join(path,x),value)
            #if the folder does not exist - create the folder and move the file
            else:
                os.mkdir(value)
                shutil.move(os.path.join(path,x),value)
        else:
            continue


# In[65]:


def file_extract(message,Processed):
    f_date = message.SentOn.strftime("%d-%b-%y %H-%M-%S") # extract the email sent time
    atts = message.Attachments
    nbr_att = atts.Count
    for x in range(nbr_att):
        file = atts.Item(x+1) #go throzugh each attachment in the email
        f_name,f_ext = os.path.splitext(str(file)) #split file name and extension
        if not f_ext in ('.jpeg','.jpg','.gif','.tiff','.png'):
            file.SaveAsFile(path + str(file)) #save file to the path
            old_name = str(file)
            new_name = '{} - {}{}'.format(f_name,f_date,f_ext) #get email sent date and attach to the file name
            os.rename(os.path.join(path, old_name), os.path.join(path, new_name)) # rename file
            x = new_name    
            #unzip file
            if f_ext in ('.zip'):    
                file_name = os.path.join(path+str(new_name)) # get full path of files
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(path) # extract file to dir
                zip_ref.close() # close file
                os.remove(file_name) # delete zipped file
                zipinfos = zip_ref.infolist()
                for z in zipinfos: 
                    z_name=os.path.splitext(z.filename)[0]
                    z_ext=os.path.splitext(z.filename)[1]
                    z_size = z.file_size
                    y = '{} - {}{}'.format(z_name,f_date,z_ext) 
                    os.rename(os.path.join(path, z.filename), os.path.join(path,y)) #rename each file in zip folder
                for a in list_name:
                    if y.startswith(a):
                        list_of_files = glob.glob(os.path.join(path+a+"*"+f_date+z_ext))
                        latest_file = max(list_of_files, key=os.path.getsize)
                        for f in list_of_files:
                            if os.path.getsize(f) < os.path.getsize(latest_file):
                                os.remove(f)
                    file_move(y) #move files in zip folder to destination folder
            file_move(x)
    message.Move(Processed)


# In[66]:


for message in list(Inbox.Items):
    if message.Class == 43:
        if message.SenderEmailType == "SMTP": # email type is smtp
            sender = message.SenderEmailAddress
            if regex.match(sender):
                file_extract(message,Processed)
        else:
            if message.Sender.GetExchangeUser() is None: # email type is ex
                continue 
            sender = message.Sender.GetExchangeUser().PrimarySmtpAddress  
            if regex.match(sender):
                file_extract(message,Processed)


# In[ ]:







