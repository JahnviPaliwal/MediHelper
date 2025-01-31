from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from .cost_making import cost_making


def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            data =[user_profile.age, user_profile.bmi, user_profile.children]
            model_url = 'health_cost_model.pkl' #path for Cost prediction model
            result = cost_making(model_url, data)
            age = user_profile.age
            sex = user_profile.sex
            bmi = user_profile.bmi
            children = user_profile.children
            smoker = user_profile.smoker
            region = user_profile.region
            charges = user_profile.charges
            final_data = [f'Age:{age}', f'Gender:{sex}', f'BMI: {bmi}', f'Children: {children}', f'Smoke: {smoker}', f'Region: {region}', f'Charges: {charges}', f'Result: {result}']

            return render(request, 'Cost_calculator/result.html', {'result': final_data})  # Redirect to a success page or display results
    else:
        form = UserProfileForm()

    return render(request, 'Cost_calculator/user_profile.html', {'form': form})
