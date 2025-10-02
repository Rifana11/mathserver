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