from google_images_download import google_images_download   #importing the library
import pyautogui, time
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

response = google_images_download.googleimagesdownload()   #class instantiation

#creating list of arguments
arguments = {"keywords":"purple cars,","limit":100,"print_urls":True}   
#passing the arguments to the function
paths = response.download(arguments)   
#printing absolute paths of the downloaded images
print(paths)   

#distance = 500

#pyautogui.doubleClick(1635, 104,)

#pyautogui.middleClick(1269, 490,)

#pyautogui.dragRel(-distance, 0, duration=0.7)  # move left
distance = distance - 15

#Commented out but this is if you wanna break discord TOS.
#pyautogui.click()

#pyautogui.click(1164, 614,)




