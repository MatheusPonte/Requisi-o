### **Robot requisition 1.0**
Robo in installer for meireles user, they need a password.

> Companie requested have a password

This application is used to automatically register users in **Procon** at the request stage.
Remember to get an excel with coluns : **Data, Partes, Ato, Valor and Nº**

Make sure the login and password from current website stay the same that the previous one.

In case any changes occurs in login, make sure to update your new attributes in archive **.env**  : **Login and Senha**.

 **Build again running**
`pyinstaller --onedir --hidden-import "flet_desktop" --hidden-import "pyautogui" --add-data "img;img" --add-data "function;function" --add-data "src;src" --add-data "Task;Task" --add-data ".env;." --icon=conversando_Y1Z_icon.ico --name RoboRequisição  main.py
`

If you want a new installer, install "InnoSetup", this is a program for creating new installers : 
[How to make a installer](https://www.youtube.com/watch?v=5U-nBAfbSek)
