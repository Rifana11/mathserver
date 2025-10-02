# Ex.05 Design a Website for Server Side Processing
# Date:02.10.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
math.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Power Calculator (P=I²R)</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
    html, body {
      height: 100%;
      margin: 0;
      display: flex;
      justify-content: center; 
      align-items: center;    
      font-family: Arial, sans-serif;
      background-color: rgb(211, 10, 164);
    }
    .container {
      text-align: center;
      padding: 20px;
      border-radius: 10px;
      background-color: #0f37a5aa;
      box-shadow: 0 5px 10px rgba(0,0,0,0.15);
    }
    input {
      padding: 5px;
      margin: 6px 0;
      width: 110px;
      font-size: medium;
    }
    button {
      padding: 8px 16px;
      margin-top: 10px;
      cursor: pointer;
      font-style: italic;
    }
  </style>

</head>
<body>

<div class="container">
    <h1>Power Calculator (P = I² × R)</h1>

    <div>
      <label>Current (I in A): </label>
      <input type="number" id="current" step="any"><br>

      <label>Resistance (R in Ω): </label>
      <input type="number" id="resistance" step="any"><br>

      <button onclick="calculatePower()">Calculate</button>
    </div>

    <h2 id="result">Power will appear here</h2>
  </div>

  <script>
    function calculatePower() {
      let I = parseFloat(document.getElementById("current").value);
      let R = parseFloat(document.getElementById("resistance").value);

      if (!isNaN(I) && !isNaN(R)) {
        let P = I * I * R;
        document.getElementById("result").innerText = "Power = " + P + " Watts";
      } else {
        document.getElementById("result").innerText = "Please enter both values!";
      }
    }
  </script>


</body>
</html>

views.py

from django.shortcuts import render

   def power_calculator(request):

    context = {
        'power': '0',
        'intensity': '0',
        'resistance': '0'
    }

    if request.method == 'POST':
        
        i_str = request.POST.get('intensity', '0')
        r_str = request.POST.get('resistance', '0')

        try:
            
            i = int(i_str)
            r = int(r_str)

            power = (i * i) * r

            context['power'] = str(power)
            context['intensity'] = str(i)
            context['resistance'] = str(r)

        except ValueError:
            context['power'] = 'Error'
            context['intensity'] = i_str
            context['resistance'] = r_str
    return render(request, 'mathapp/math.html', context)

urls.py

from django.urls import path
from . import views 

    urlpatterns = [
    path('', views.power_calculator, name='power_calculator_root'),
    path('power/', views.power_calculator, name='power_calculator'),
]
```
# SERVER SIDE PROCESSING:
![alt text](<math.html - exp5 - Visual Studio Code 02-10-2025 21_36_29.png>)

# HOMEPAGE:
![alt text](<Screenshot 2025-10-02 213144.png>)

# RESULT:
The program for performing server side processing is completed successfully.
