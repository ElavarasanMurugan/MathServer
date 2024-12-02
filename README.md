# Ex.05 Design a Website for Server Side Processing
## Date: 02-11-2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```

math.html

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>
             Power Calculator
        </title>
        <style>
            *{
                margin: 0;
                padding: 0;
                background-color:none;
            }


            .header{
    background-color: #0f9fcf;
    color:white;
    font-size: 13px;
    text-align: center;
    padding: 10px;
    font-variant: small-caps;
}
.definition{
    padding-top: 10px;
    padding-left: 5px;
    font-size: x-large;
    font-style:oblique;
}
.table{
    background-color: lavender;
    display: block;
    padding-top: 10px;
    padding-bottom: 10px;
    margin-left: 460px;
    margin-right: 460px;
    border-radius: 15px;
}
.i1{
    font-style: italic;
    padding: 15px;
    font-size: x-large;
}
.i2{
    border-radius: 5px;
    width: 180px;
    height: 25px;
    font-variant:unset;
    font-family: cursive;
    font-size: medium;
}
.i3{
    font-style: italic;
    padding: 15px;
    font-size: x-large;
}
.r1{
    font-style: italic;
    padding: 15px;
    font-size: x-large;
    
}
.r2{
    border-radius: 5px;
    width: 180px;
    height: 25px;
    font-variant:unset;
    font-family: cursive;
    font-size: medium;
}
.r3{
    font-style: italic;
    padding: 15px;
    font-size: x-large;
}
.p1{
    font-style: italic;
    padding: 15px;
    font-size: x-large;
    
}
.p2{
    border-radius: 5px;
    width: 180px;
    height: 25px;
    font-variant:unset;
    font-family: cursive;
    font-size: medium;
}
.p3{
    font-style: italic;
    padding: 15px;
    font-size: x-large;
}
.c1{
    background-color:#0f9fcf;
    border-radius: 5px;
    font-size: 16px;
    color: whitesmoke;
    width: 100px;
    height: 35px;
    text-align: center;
    cursor: pointer;
    border: none;
    transition: background-color 0.3s ease;
}
#result{
    padding-top: 10px;
    font-size: larger;
    font-style: oblique;
}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>
                Power calculation of a lamp
                <br>
                Elavarasan M (24900162) 
            </h1>
        </div>
        <div class="definition">
            <p>
                Here is the definition of Power: Power is the rate at which energy is transferred or converted. In the case of a lamp, it can be calculated using the formula:<br> <b>P = I² * R</b> where I is the intensity and R is the resistance.
            </p>
        </div>
        <br>
        <hr>
        <br>
        <div class="table" align="center">
            <h2>
                Calculation of Power
            </h2>
            <form method="POST">
                {% csrf_token %}
                <table>
                    <tr>
                        <td class="i1">
                            Intensity  (I) :
                        </td>
                        <td>
                            <input type="number" id="intensity" name="Intensity" placeholder="Enter the intensity"  class="i2" value="{{I}}">
                        </td>
                        <td class="i3">
                            in Amperes (A)
                        </td>
                    </tr>
                    <tr>
                        <td class="r1">
                            Resistance (R) :
                        </td>
                        <td>
                            <input type="number" id="resistance" name="Resistance" placeholder="Enter the resistance" class="r2" value="{{R}}">
                        </td>
                        <td class="r3">
                            in Ohm (Ω)
                        </td>
                    </tr>
                    <tr>
                        <td class="p1">
                            Power (P) :
                        </td>
                        <td>
                            <input type="text" id="power" name="Power" class="p2" value="{{Power}}" readonly>
                        </td>
                        <td class="p3">
                            in Watts 
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td>
                            <input type="submit" value="Calculate" class="c1">
                        </td>
                    </tr>
                </table>
            </form>
        </div>

    </body>
</html>

view.py

from django.shortcuts import render 
def findpower(request): 
    context={} 
    context['Power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('Intensity','0')
        R = request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        Power = int(I) * int(I) * int(R) 
        context['Power'] = Power 
        context['I'] = I
        context['R'] = R
        print('Power=',Power) 
    return render(request,'mathapp/math.html',context)


urls.py

from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('poweroflamb/',views.findpower,name="poweroflamb"),
    path('',views.findpower,name="poweroflambroot")
]


```

## SERVER SIDE PROCESSING:

![alt text](<Screenshot (83).png>)


## HOMEPAGE:
![alt text](<Screenshot (84).png>)

## RESULT:
The program for performing server side processing is completed successfully.
