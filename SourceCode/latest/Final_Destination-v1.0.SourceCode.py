####################################################################################################
#Intro

v = "1.0"
f0=("""                                                                                
                        ,:++.                                                   
                        %#::. ..  ..    ..    ..     .                          
                        %+    :#  .@.   :#    %#     M.                         
                        %+    :#  ,@@,  :%   .##:    M.                         
                        %@%#. :#  ,#:@, :%   #:,@.   M.                         
                        %%..  :#  :% ,@,:%  ,@,,#+   M.                         
                        %+    :#  :%  ,@%+  #%+++M.  M.                         
                        %+    :#  :%   ,@+ :#    +#  M...                       
                        ++    ,%  :+    ,: %,    .#..##@%                       
 .+++:.                                                                         
 ,@:+%@#.  ,::+    ,,.,,,,,,, ,.  ,.    ,.    ,   ,,,,,,,..,    ,:+,   .,    ., 
 ,@   .%@. %%::  ,#%,.%%#@%%+ @,  %#.   @,   .M:  +%%@%%%.:#  .%#::##. .M:   ,# 
 ,@    .M, %:    @:     ,#    @,  %##.  @,   %+@.    @,   :#  %%    #+ .@@:  ,# 
 ,@    .M. %+,,  %#,    ,#    #,  #,%#. @.  ,# %+    @,   :# .M.    :# ,#,@: :% 
 ,@    %%  %#+:   :@%   ,#    #,  #, +#.@.  #+:+M,   @,   :# .M     :# ,# .@::% 
 ,@  .%#.  %:      ,@   :@    #,  @,  +#@. :#:::%#   @,   :# .M,    #+ :#  .@#% 
 ,@+#@+    %+,,. .:#:   :@    #,  @,   +M..@,   .@:  @:   :#  +@,..%#. :#   .@+ 
 ,%+,      :%%#. :%,    ,+    +,  %.    : .+     ::  +,   ,+   ,%##:   ,+    .: 
                                                                                                                                        
                               - created by Napo_II
                                    - """ + v + """
    			          - python 3.7
                - https://github.com/NapoII/Final-Destination

""")

print(f0)

####################################################################################################
#Import

import os # für die Ordner Struktur
from os import listdir
from os.path import isfile, join
import shutil
import win32con, win32api,os    # um ico Bild für Folder einzustellen
from datetime import date
import time
from configparser import ConfigParser

####################################################################################################

aktuellesDatum = date.today()

script_path = os.path.dirname(os.path.realpath(__file__))
ico_dir = (script_path.replace('\\','/')) + "/ico/"

FD_input = input("Wie heißt die gewünschte Festplatte der Final Destination: ")
FD_path = str(FD_input)+":\\"

path = r"C:/Users/space/Desktop/Final Destination/"
dir = r"E:/Backup/desktop.ini"
ico = r"E:/Bilder/Icons/icons8-kategorisieren-64.ico,0"




Datei_Doppelt  = []
skip_LIST = ["desktop.ini", "Log_Files"]

Datei_Art_Bilder = r"Bilder"
Filter_liste_Bilder = [".png",".jpeg",".gif",".tif",".jpg"]

Datei_Art_Dokumente = r"Dokumente"
Filter_liste_Dokumente = [".txt",".ui",".pdf",".docx",".xlsx",".ini"]

Datei_Art_Audio = r"Audio"
Filter_liste_Audio = [".wav",".mp3"]

Datei_Art_Projekte = r"Projekte"
Filter_liste_Projekte = [".py"]

Datei_Art_Pr0grame = r"Pr0grame"
Filter_liste_Pr0grame = [".exe"]

Datei_Art_Cheack_to_delt = r"Cheack_to_delt"
Filter_liste_Cheack_to_delt = [".url",".lnk"]

Datei_Art_In_welchen_Ordner = r"In_welchen_Ordner"
Filter_liste_In_welchen_Ordner = [".zip",".tar.xz",".xz"]

####################################################################################################
#Config Datei

path_config = "E:/Pr0grame/My_ Pyhton/work_in_progress/Final Destination/config_Final_Destination.ini"


if os.path.exists(path_config):                       # Prüft datei pfad nach exsistänz Ture/False
  print ( "Final Destination Config wurde geladen.")
else:
  print("Standard Config wird erstellt --> ["+str(path_config)+"] ")

  config = ConfigParser()

  config['Bilder'] = {
      'Filter_liste_Bilder': ".png " ".jpeg " ".gif " ".tif " ".jpg ",
  }

  config['skip_LIST'] = {
      'Filter_liste_Bilder': "desktop.ini " "Log_Files ",
  }

  config['Dokumente'] = {
      'Filter_liste_Dokumente': ".txt " ".ui " ".pdf " ".docx " ".xlsx " ".ini ",
  }

  config['Audio'] = {
      'Filter_liste_Audio': ".wav " ".mp3 ",
  }

  config['Projekte'] = {
      'Filter_liste_Projekte': ".py ",
  }

  config['Pr0grame'] = {
      'Filter_liste_Pr0grame': ".exe ",
  }

  config['Cheack_to_delt'] = {
      'Filter_liste_Cheack_to_delt': ".url " ".lnk ",
  }

  config['skip_LIST'] = {
      'Filter_liste_skip_LIST': "desktop.ini " "Log_Files ",
  }

  config['In_welchen_Ordner'] = {
      'Filter_liste_In_welchen_Ordner': ".zip " ".tar.xz " ".xz ",
  }
  with open(path_config,'w') as f:
        config.write(f)

def get_config_Filter_key (Datei_Art):
  parser = ConfigParser()
  parser.read(path_config)
  Filter_liste_ = "Filter_liste_"+str(Datei_Art)
  Config_sections = parser.get(Datei_Art, Filter_liste_ )
  def stringToList(string):
      listRes = list(string.split(" "))
      return listRes
  return (stringToList(Config_sections))

####################################################################################################
# Ordner Struktur wird erstllet / geprüft

print("\n")
print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
folder = "Final Destination"
dir = "~/Desktop/"+str(folder)           # gibt gewünschten Datei-Pfad an
full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name

if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
    print("Ordner Struktur existiert bereits")
    print("  ->   " + str(full_path))
else:                                               # Erstellt Ordner falls nicht vorhadnen
    os.makedirs(full_path)
    print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
    print("  ->   " + str(full_path))
print("\n")

########## Ordner Eigenschaften werden festgelegt
def ini_datei(full_path, Datei_Art ):
    File_name = "desktop.ini"       #Datei name
    complete_pathName = os.path.join(full_path, File_name)     # Path + text datei name

    if os.path.exists(complete_pathName):                       # Prüft datei pfad nach exsistänz Ture/False
        print("desktop.ini existiert bereits")
        print("  ->   " + str(complete_pathName))
    else:
        print("desktop.ini ["+str(File_name)+"] wird erstellt...")
        file1 = open(complete_pathName, "w")
        full_ico = ico_dir + Datei_Art + ".ico" # Datei erstellen          
        toFile = "[.ShellClassInfo]\n" + "IconResource=" + full_ico + ",0" + "\n" + "[ViewState]\n" + "Mode=\n" + "Vid=\n" + "FolderType=Generic"
        file1.write(toFile)                                                    # Datei wird gefüllt mit input
        file1.close()
        win32api.SetFileAttributes(complete_pathName,win32con.FILE_ATTRIBUTE_HIDDEN) # versteckt datei 
        win32api.SetFileAttributes(complete_pathName,win32con.FILE_ATTRIBUTE_SYSTEM) # datei auf normal
        win32api.SetFileAttributes(complete_pathName,win32con.FILE_ATTRIBUTE_HIDDEN) # datei verstecken . damit ini vom system übernommen wird

ini_datei(full_path, "Final Destination")


#####################################################################################################
#Log File

# Ordner Struktur wird erstllet / geprüft

print("\n")
print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
folder = "Log_Files"
dir = "~/Desktop/Final Destination/"+str(folder)           # gibt gewünschten Datei-Pfad an
full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name

if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
    print("Ordner Struktur existiert bereits")
    print("  ->   " + str(full_path))
else:                                               # Erstellt Ordner falls nicht vorhadnen
    os.makedirs(full_path)
    print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
    print("  ->   " + str(full_path))
print("\n")

## Unter Ornder nach datum name erstellt
folder = (aktuellesDatum.strftime("%m_%Y"))

full_path = str(full_path)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an

if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
    print("Ordner Struktur existiert bereits")
    print("  ->   " + str(full_path))
else:                                               # Erstellt Ordner falls nicht vorhadnen
    os.makedirs(full_path)
    print("Der Ordner ["+ (folder) +"] wurde erstellt im Verzeichnis:" )
    print("  ->   " + str(full_path))
print("\n")

####################################################################################################
# text Datei erstellen nach Datum und Uhrzeit

start_time = time.time()
datei_Date = (time.strftime("%d_%m_%Y - %H.%M"))
   # Generiert date formater
name_of_file = ("Final_Destination - Log - "+(datei_Date))                      # Generiert Datei name

save_path = full_path

completeName = os.path.join(save_path, name_of_file+".txt")     # Path + text datei name
print("Textdatei ["+str(name_of_file)+"] wird erstellt...")
file1 = open(completeName, "a")                                 # Datei erstellen
file1.close()                                                   # Datei wird gespeichert und geschlossen

####################################################################################################

### Data in Text Datei gespeichert
def Fill_log (fill_input):
    toFile = fill_input             # def inhalt das hinzugefügt wird
    file1 = open(completeName, "a")                                 # Datei wird geöffnet # zufüge modus
    print("Datei ["+str(name_of_file) + "] wird beschrieben und gespeichtert...")
    file1.write(str(toFile) +"\n")                                             # Datei wird gefüllt mit input
    file1.close()                                                   # Datei wird geschlossen und gespeichert

#####################################################################################################

def Datei_Filter(Datei_Art) :
    Fill_log("----------------------------------------------------------------------------------------------------")
    Fill_log ("Datei art: "+str(Datei_Art))

    Filter_liste = get_config_Filter_key (Datei_Art)

    Fill_log ("Es wird gefiltert nach: "+str(Filter_liste)+"\n")

    Filter = Filter_liste
    destination = FD_path + Datei_Art

    # Ordner Struktur wird erstllet / geprüft
    print("\n")
    print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
    folder = Datei_Art
    dir = destination           # gibt gewünschten Datei-Pfad an
    full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name

    if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
        print("Ordner Struktur existiert bereits")
        print("  ->   " + str(full_path))
    else:                                               # Erstellt Ordner falls nicht vorhadnen
        os.makedirs(full_path)
        print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
        print("  ->   " + str(full_path))
    print("\n")

    ini_datei(full_path, Datei_Art)

    File_list = [ f for f in listdir(path) if isfile(join(path,f)) ] # liest datein namen aus und fügt sie einer Liste hinzu.
    
    
    # Filtert Skipp Datein herauss
    skip_LIST_1 = skip_LIST
    skip_len = len(skip_LIST_1)+1
    while True :
        skip_len = skip_len - 1
        if skip_len == 0 :
            break

        Skip_datei = str(skip_LIST_1.pop())
        try:
            File_list.remove(Skip_datei)
            skip_LIST_1.append(Skip_datei)
        except:
            skip_LIST_1.append(Skip_datei)

    print ("\n")
    Fill_log ("Es wurden folgende Datein gefunden: ")
    print ("Es wurden folgende Datein gefunden: ")
    Fill_log (File_list)
    Fill_log ("\n")

    print (File_list)
    print ("\n")

    len_a = len(Filter)+1
    while True:
        len_a = len_a - 1
        if len_a == 0:
            break

        datei_end = Filter.pop()
        datei_end_match = list(filter(lambda x: datei_end in x, File_list))
        len_b = len(datei_end_match)+1
        while True:
            len_b = len_b - 1
            if len_b == 0 :
                break
            datei_end_name = datei_end_match.pop()
            try:
                shutil.move(f"{path}/{datei_end_name}", destination)
                print (" Datei [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(destination)  )
                Fill_log(" Datei [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(destination)  )
            except: 
                Datei_Doppelt.append(datei_end_name)
                print("\n")
                print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
                folder = Datei_Art
                folder_2 = "Dublikate"
                dir = destination + "/" + folder_2           # gibt gewünschten Datei-Pfad an
                full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name
                
                if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
                    print("Ordner Struktur existiert bereits")
                    print("  ->   " + str(full_path))
                else:                                               # Erstellt Ordner falls nicht vorhadnen
                    os.makedirs(full_path)
                    print("Der Ordner ["+folder_2+"] wurde erstellt im Verzeichnis:" )
                    print("  ->   " + str(full_path))
                print("\n")
                print (" Die Datei [ " + str(datei_end_name) + " ] ist schon im Ordner --> |"+ str(destination) +" vorhaden"  )

                ini_datei(full_path, folder_2 )
                
                try:
                    shutil.move(f"{path}/{datei_end_name}", dir)
                    print (" Datei [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(dir)  )
                    Fill_log(" Datei [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(dir)  )
                except:
                    print("Die Datei [ " + str(datei_end_name) + " ] ist schon doppelt vorhanden ")
                    Fill_log("Die Datei [ " + str(datei_end_name) + " ] ist schon doppelt vorhanden ")
                    Fill_log ("\n")

def Ordner_Filter(Datei_Art):
    Fill_log("----------------------------------------------------------------------------------------------------")
    Fill_log ("Datei art: Ordner\n")

    files = []
    paths = []

    for file in os.listdir(path):
        if os.path.isdir(file):
            paths.append(file) 
        else:
            files.append(file)
    
    # Filtert Skipp Datein herauss
    skip_LIST_2 = skip_LIST 
    skip_len = len(skip_LIST_2)+1
    while True :
        skip_len = skip_len - 1
        if skip_len == 0 :
            break
        Skip_datei = (skip_LIST_2.pop())

        try:
            files.remove(Skip_datei)
            skip_LIST_2.append(Skip_datei)
        except:
            skip_LIST_2.append(Skip_datei)

    len_d = len(files)+1
    while True:
        len_d = len_d - 1
        if len_d == 0:
            break
        files_x = files.pop()
        
        path_c = path + files_x
        isdir = os.path.isdir(path_c)

        if isdir == True:
            datei_end_name = files_x
            destination = FD_path + Datei_Art

            # Ordner Struktur wird erstllet / geprüft
            print("\n")
            print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
            folder = Datei_Art
            dir = destination           # gibt gewünschten Datei-Pfad an
            full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name

            if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
                print("Ordner Struktur existiert bereits")
                print("  ->   " + str(full_path))
            else:                                               # Erstellt Ordner falls nicht vorhadnen
                os.makedirs(full_path)
                print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
                print("  ->   " + str(full_path))
            print("\n")

            ini_datei(full_path, Datei_Art)

            try:
                shutil.move(f"{path_c}", destination)
                print (" Ordner [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(destination)  )
                Fill_log (" Ordner [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(destination)  )
                Fill_log ("\n")
            except: 
                Datei_Doppelt.append(datei_end_name)
                print("\n")
                print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
                folder = Datei_Art
                folder_2 = "Dublikate"
                dir = destination + "/" + folder_2           # gibt gewünschten Datei-Pfad an
                full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name
                
                if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
                    print("Ordner Struktur existiert bereits")
                    print("  ->   " + str(full_path))
                else:                                               # Erstellt Ordner falls nicht vorhadnen
                    os.makedirs(full_path)
                    print("Der Ordner ["+folder_2+"] wurde erstellt im Verzeichnis:" )
                    print("  ->   " + str(full_path))
                print("\n")
                print (" Der Ordner [ " + str(datei_end_name) + " ] ist schon im Ordner --> |"+ str(destination) +" vorhaden"  )

                ini_datei(full_path, folder_2 )
                try:
                    shutil.move(f"{path}/{datei_end_name}", dir)
                    print (" Datei [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(dir)  )
                    Fill_log (" Datei [ " + str(datei_end_name) + " ] Verschoben nach -> " + str(dir)  )
                    Fill_log ("\n")
                except:
                    print("Der Ordner [" + str(datei_end_name) + "] ist schon doppelt vorhanden ")
                    Fill_log ("Der Ordner [" + str(datei_end_name) + "] ist schon doppelt vorhanden ")
                    Fill_log ("\n")

def Folder_cheack(path):
    files = []
    paths = []

    for file in os.listdir(path):
        if os.path.isdir(file):
            paths.append(file) 
        else:
            files.append(file)
    len_d = len(files)+1
    while True:
        len_d = len_d - 1
        if len_d == 0:
            break
        files_x = files.pop()
        path_c = path + files_x
        isdir = os.path.isdir(path_c)
        if isdir == True:
            return True


def if_to_Datei_Art_cheack(Datei_Art_In_welchen_Ordner):
    File_list = [ f for f in listdir(path) if isfile(join(path,f)) ] # liest datein namen aus und fügt sie einer Liste hinzu.
    Filter = get_config_Filter_key (Datei_Art_In_welchen_Ordner)
    Len_e = len(Filter)+1
    while True:
        Len_e = Len_e - 1
        if Len_e == 0:
            break
        datei_end = Filter.pop()
        datei_end_match = list(filter(lambda x: datei_end in x, File_list))
        print(datei_end_match)
        if len(datei_end_match) == 1 :
            return True
        else :
            return False

Fill_log (f0)
Fill_log ("Der Drop in Ordner befindet sich in -->" + str(path) + "\n" +"Die gefunden Datein/Ordner wurden verschoben nach --> "+ str(FD_path)+ "\n")

Datei_Filter(Datei_Art_Bilder)
Datei_Filter(Datei_Art_Dokumente)
Datei_Filter(Datei_Art_Audio)
Datei_Filter(Datei_Art_Projekte)
Datei_Filter(Datei_Art_Pr0grame)
Datei_Filter(Datei_Art_Cheack_to_delt)

Cheack_da = if_to_Datei_Art_cheack(Datei_Art_In_welchen_Ordner)

Datei_Filter(Datei_Art_In_welchen_Ordner)

Folder_da = (Folder_cheack(path))
if Folder_da == None:
    Folder_da = False

if Folder_da == True or Cheack_da == True:
    Manuel_cheack = True
else:
    Manuel_cheack = False

Ordner_Filter(Datei_Art_In_welchen_Ordner)

print(f0)
os.startfile(FD_path)

print(str(completeName))
os.system("\""+str(completeName)+"\"")

XY = input("Drücke [ ENTER ] um das Programm zu beenden.")

#####################################################################################################
#   To_Do :
#   -> .ini datei verküpfung
#####################################################################################################