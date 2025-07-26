from django.shortcuts import render
from .forms import InputForm

def calculate(request):
    result = error = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            try:
                if a < 1:
                    error = "Value A is too small."
                elif b == 0:
                    error = "Value B will not change the result."
                elif c < 0:
                    error = "Value C must be non-negative."
                else:
                    cube_c = c ** 3
                    if cube_c > 1000:
                        calc = (cube_c ** 0.5) * 10
                    else:
                        calc = (cube_c ** 0.5) / a
                    result = calc + b
            except Exception as e:
                error = f"Error during calculation: {e}"
        else:
            error = "Invalid input. Please enter numeric values."
    else:
        form = InputForm()
    
    return render(request, 'calculator/result.html', {'form': form, 'result': result, 'error': error})
