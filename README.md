# Digital-Clock-with-Python
In this post, I will show you how to build and design your digital clock window using python. This is a simple project to get started with Tkinter, which is a built-in package that comes with Python. Tkinter is basically a graphical user interface package. It has great features that can be used to create simple applications. And today we will use it to create our digital clock.

The great part of building your own digital clock is you can customize it as you wish. From text font to background color, all the features are available to be customized. If you are ready, let get started!

# Table of Contents 
 Python
 
 Import Libraries
 
 Application Window
 
 Digital Clock Function
 
 Run the Application
 
 Python
 
# Python 
Python is a general-purpose programming language that is becoming ever more popular for analyzing data. Python also lets you work quickly and integrate systems more effectively. Companies from all around the world are utilizing Python to gather bits of knowledge from their data. The official Python page if you want to learn more.

# Import Libraries
We will use two libraries in this project. And both of them come with Python, which means we don’t have to install them. These kind of libraries is called Python built-in packages.

The main package we will use is Tkinter. You can learn more about Tkinter from here, the official documentation page.

So for this step, all we need to do is to import them to our program:

```
from tkinter import Label, Tk
import time
```
# Application Window
In this step, we will first define the window panel using Tkinter package. And after that, we will define the text design that we want to use for the digital clock.

Define the Window
As mentioned earlier, we will use Tkinter package. Tkinter is can be defined as Tk. And after defining it, we will customize it.

```
root= Tk()

root.title("My Digital Time")

root.geometry("350x150")

root.resizable(0,0)
```

Defining the Tkinter function

Giving a title to our application window
Defining the size of our video, for example in my case, it’s 350pixels width to 150pixels height
The window is not resizable, because the text values are not responsive design. And we don’t want our design to look weird when the window size is changed.
Perfect, our basic application window is ready! Now, let’s work on the design.

The Label Design
The cool step of the program is this one. Because you can put your own preferences into the design. This step will make your work different from others. If you love designing things, it’s time to show off your skills. 🙂

There are four elements that we will customize:

The font of the digital numbers
The background color of our digital clock
The color of the digital numbers, make sure it is not the same color as your background 😉
The border width of the text
Here are the values that I used for my design:
```
text_font= ("ds-digital", 50,)

background = "#f2e750"

foreground= "#363529"

border_width = 25
```
For colors, feel free to use RGB values or hex values. In my case, I used the hex values of the colors. I use google’s color picker that is available on the browser. Just search “Color picker” on google search. And you will see it.

Now, let’s combine the elements and define our label. Label function is the text that will show our time.

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)

label.grid(row=0, column=1)

If you want to learn more about the attributes of the Label function, here is a nice page I found.

# Digital Clock Function
If we are working on an application project, functions are the best way to make things work. Functions are also great because they make the program more structured and easier to understand. Alright, let’s define our digital clock function then:
```
def time_clock():

   string = strftime("%H:%M:%S")
   
   label.config(text=string)
   
   label.after(200, time_clock)
 ```  
In the first line, we are getting real-time using the time package. And we are also defining the format that we want it to be. Since we are designing a digital clock, “hour, minutes, seconds” will be a nice format to go with.
In the second line, we are just assigning the real-time to the label method. This way the digital time will be updated.
And lastly, we are calling the function again so that the digital clock is showing the live time. This way every 200 milliseconds the time is getting updated. In programming, this is called a recursion loop. Calling the same function, inside the function. Feels like inceptions, isn’t that cool?


#Run the Application

Great! You made it until this step, which is the final step of our application project. As you know functions will not run unless you call them. To trigger the application, we will call the function. Let’s run the application:
```
time_clock()

root.mainloop()
```
Thank You.

# AUTHOR INFO.
Khalid Mohamed Abdi

Somali

Email: Khalidhajilacag@gmail.com
