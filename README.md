# Auto_type_cheat
This program let's you allow to cheat on monkey type typing wesbite with over speed of 106wpm and 97-99% accuracy!

Some things to make sure the program works:-

1.Import all the requirements at first

2.For the address in the 5th line of code make sure you install tesseract-ocr from 
  https://sourceforge.net/projects/tesseract-ocr.mirror/
  and give that folder's path and append it with "\tesseract.exe".
  This is important so that image to text functionality works properly!
  
3.As per your monitor resolution you might have to change the values given in line 12
  image.crop((15,260,1250,400))
  for the best possible results. In order to have a good idea of what are you cropping you may uncomment the image.show() command and it will display you the cropped       image.
  So you may have to play with those values as per your requirements.
  
 4.Here are some results with the above program:
 
 ![image](https://user-images.githubusercontent.com/97832138/222518876-d17e83ea-c441-4c1c-9e78-fd1ebca5a2c2.png)
 ![image](https://user-images.githubusercontent.com/97832138/222519097-4733e7fe-87a0-459f-b541-f07ff5dbe4ed.png)
 ![image](https://user-images.githubusercontent.com/97832138/222519379-ed6f5deb-6348-46de-98ae-d15fd405e794.png)
 ![image](https://user-images.githubusercontent.com/97832138/222520016-e57bf9be-c486-4bf9-b858-068cea938a20.png)

