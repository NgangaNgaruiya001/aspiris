from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Sum
from .models import SalesData

from django.db.models import Sum, F
from django.shortcuts import render
from .models import SalesData

from django.db.models import F, Sum
from django.shortcuts import render
from .models import SalesData

from django.db.models.functions import Cast
from django.db.models import IntegerField


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or any page of your choice



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Replace 'home' with the name of your default landing page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'reports/login.html')



def regional_sales_summary(request, region):
    # Dynamically build the field names for the selected region
    region_qty_field = f'QTY_{region}'  # This will be something like 'QTY_Nairobi_A'
    region_sales_field = f'SALE_VALUE_{region}'  # This will be something like 'SALE_VALUE_Nairobi_A'
    
    # Check if the fields exist in the model
    if not hasattr(SalesData, region_qty_field) or not hasattr(SalesData, region_sales_field):
        return render(request, 'reports/regional_sales_summary.html', {
            'error': f"Invalid region field: {region}",
            'region': region
        })

    # Aggregate data by CardName, Branch, and Dscription, summing the quantities and sales values
    sales_data = SalesData.objects.values('CardName', 'BRANCH', 'Dscription') \
        .annotate(
            total_qty=Cast(Sum(F(region_qty_field)), IntegerField()),  # Format to 0 decimals
            total_sales=Cast(Sum(F(region_sales_field)), IntegerField())  # Format to 0 decimals
        ).filter(total_qty__gt=1, total_sales__gt=1)  # Filter out zero values

    # Return the data to the template
    return render(request, 'reports/regional_sales_summary.html', {
        'sales_data': sales_data,
        'region': region
    })


from django.shortcuts import render
from django.db.models import Sum, F
from .models import SalesData


def dashboard(request):
    # List of all regions
    regions = ['Nairobi_A', 'Nairobi_B', 'Nakuru', 'Nyeri', 'Kisumu', 'Eldoret', 'Mombasa']

    # Pass data to the template
    context = {
        'regions': regions,
    }
    return render(request, 'reports/dashboard.html', context)


# def dynamic_sales_data(request):
#     # Get the current month and year or use a query parameter from the request
#     month = request.GET.get('month', 12)  # Default to December if no month is specified
#     year = request.GET.get('year', 2023)  # Default to 2023 if no year is specified

#     # Filter data based on the month and year
#     sales_data = SalesData.objects.filter(DocMonth=month, DocYear=year).values('ItemCode', 'Dscription', 'TotalFrgn', 'DocMonth') \
#         .annotate(
#             qty=Sum('Quantity'),
#             sales_value=Sum('LineTotal')
#         )

#     # Calculating YTD and MTD
#     ytd_data = SalesData.objects.filter(DocYear=year).values('ItemCode').annotate(
#         ytd_sales_value=Sum('LineTotal'),
#         ytd_qty=Sum('Quantity')
#     )

#     mtd_data = SalesData.objects.filter(DocMonth=month, DocYear=year).values('ItemCode').annotate(
#         mtd_sales_value=Sum('LineTotal'),
#         mtd_qty=Sum('Quantity')
#     )

#     return render(request, 'reports/dynamic_sales_data.html', {
#         'sales_data': sales_data,
#         'ytd_data': ytd_data,
#         'mtd_data': mtd_data,
#         'month': month,
#         'year': year
#     })



# reports/views.py
from django.db.models import Sum
from django.shortcuts import render

def dynamic_sales_data(request):
    # Get the current month and year or use a query parameter from the request
    month = request.GET.get('month', 12)  # Default to December if no month is specified
    year = request.GET.get('year', 2024)  # Default to 2024 if no year is specified

    # Filter data based on the month and year
    sales_data = SalesData.objects.filter(DocMonth=month, DocYear=year).values('ItemCode', 'Dscription', 'TotalFrgn', 'DocMonth') \
        .annotate(
            qty=Sum('Quantity'),
            sales_value=Sum('LineTotal')
        )

    # Calculating YTD and MTD
    ytd_data = SalesData.objects.filter(DocYear=year).values('ItemCode').annotate(
        ytd_sales_value=Sum('LineTotal'),
        ytd_qty=Sum('Quantity')
    )

    mtd_data = SalesData.objects.filter(DocMonth=month, DocYear=year).values('ItemCode').annotate(
        mtd_sales_value=Sum('LineTotal'),
        mtd_qty=Sum('Quantity')
    )

    # Format the sales data, YTD, and MTD values with no decimals and comma separation
    for entry in sales_data:
        entry['qty'] = f"{entry['qty']:,}"  # Format qty with comma separator
        entry['sales_value'] = f"{int(entry['sales_value']):,}"  # Format sales value with comma separator and no decimals

    for entry in ytd_data:
        entry['ytd_sales_value'] = f"{int(entry['ytd_sales_value']):,}"  # Format YTD sales with no decimals
        entry['ytd_qty'] = f"{entry['ytd_qty']:,}"  # Format YTD qty with comma separator

    for entry in mtd_data:
        entry['mtd_sales_value'] = f"{int(entry['mtd_sales_value']):,}"  # Format MTD sales with no decimals
        entry['mtd_qty'] = f"{entry['mtd_qty']:,}"  # Format MTD qty with comma separator

    return render(request, 'reports/dynamic_sales_data.html', {
        'sales_data': sales_data,
        'ytd_data': ytd_data,
        'mtd_data': mtd_data,
        'month': month,
        'year': year
    })



from django.shortcuts import render
from .models import SalesTarget, SalesData
from django.db.models import Sum
from datetime import datetime

from django.shortcuts import render
from .models import SalesTarget, SalesData
from django.db.models import Sum

from django.shortcuts import render
from .models import SalesTarget, SalesData

from django.shortcuts import render



from django.shortcuts import render
from .models import SalesTarget, SalesData

def regional_sales_comparison(request):
    selected_months = request.GET.getlist('months')

    # Step 1: Get Sales Targets based on selected months
    if selected_months:
        targets = SalesTarget.objects.filter(Month__in=selected_months)  # Target filtered by selected months
    else:
        targets = SalesTarget.objects.all()  # All targets if no month is selected

    # Step 2: Get Sales Data (Actual Sales) based on selected months
    if selected_months:
        regional_sales = SalesData.objects.filter(DocMonth__in=selected_months)  # Actual sales filtered by selected months
    else:
        regional_sales = SalesData.objects.all() 
    region_totals = {
        'Nairobi A': {'Cardio': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                       'Gyn': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                       'Pain': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                       'total_target': 0, 'total_actual': 0, 'total_percent_achieved': 0},
        'Nairobi B': {'Cardio': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                       'Gyn': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                       'Pain': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                       'total_target': 0, 'total_actual': 0, 'total_percent_achieved': 0},
        'Nakuru': {'Cardio': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                   'Gyn': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                   'Pain': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                   'total_target': 0, 'total_actual': 0, 'total_percent_achieved': 0},
        'Nyeri': {'Cardio': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                  'Gyn': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                  'Pain': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                  'total_target': 0, 'total_actual': 0, 'total_percent_achieved': 0},
        'Kisumu': {'Cardio': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                   'Gyn': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                   'Pain': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                   'total_target': 0, 'total_actual': 0, 'total_percent_achieved': 0},
        'Eldoret': {'Cardio': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                    'Gyn': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                    'Pain': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                    'total_target': 0, 'total_actual': 0, 'total_percent_achieved': 0},
        'Mombasa': {'Cardio': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                    'Gyn': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                    'Pain': {'target': 0, 'actual': 0, 'percent_achieved': 0},
                    'total_target': 0, 'total_actual': 0, 'total_percent_achieved': 0},
    }

    # Step 5: Process Sales Targets Data
    for target in targets:
        region = target.Region
        sub_division = target.Sub_division
        target_value = target.Sales

        if region in region_totals:
            if sub_division == "Cardio":
                region_totals[region]['Cardio']['target'] += target_value
            elif sub_division == "Gyn":
                region_totals[region]['Gyn']['target'] += target_value
            elif sub_division == "Pain":
                region_totals[region]['Pain']['target'] += target_value
    # Step 6: Process Regional Sales Data (Actual Sales)
    for sales in regional_sales:
        if sales.TotalFrgn == 'Cardio':
            if sales.QTY_Nairobi_A is not None:
                region_totals['Nairobi A']['Cardio']['actual'] += sales.SALE_VALUE_Nairobi_A
            if sales.QTY_Nairobi_B is not None:
                region_totals['Nairobi B']['Cardio']['actual'] += sales.SALE_VALUE_Nairobi_B
            if sales.QTY_Nakuru is not None:
                region_totals['Nakuru']['Cardio']['actual'] += sales.SALE_VALUE_Nakuru
            if sales.QTY_Nyeri is not None:
                region_totals['Nyeri']['Cardio']['actual'] += sales.SALE_VALUE_Nyeri
            if sales.QTY_Kisumu is not None:
                region_totals['Kisumu']['Cardio']['actual'] += sales.SALE_VALUE_Kisumu
            if sales.QTY_Eldoret is not None:
                region_totals['Eldoret']['Cardio']['actual'] += sales.SALE_VALUE_Eldoret
            if sales.QTY_Mombasa is not None:
                region_totals['Mombasa']['Cardio']['actual'] += sales.SALE_VALUE_Mombasa

        elif sales.TotalFrgn == 'Gyn':
            if sales.QTY_Nairobi_A is not None:
                region_totals['Nairobi A']['Gyn']['actual'] += sales.SALE_VALUE_Nairobi_A
            if sales.QTY_Nairobi_B is not None:
                region_totals['Nairobi B']['Gyn']['actual'] += sales.SALE_VALUE_Nairobi_B
            if sales.QTY_Nakuru is not None:
                region_totals['Nakuru']['Gyn']['actual'] += sales.SALE_VALUE_Nakuru
            if sales.QTY_Nyeri is not None:
                region_totals['Nyeri']['Gyn']['actual'] += sales.SALE_VALUE_Nyeri
            if sales.QTY_Kisumu is not None:
                region_totals['Kisumu']['Gyn']['actual'] += sales.SALE_VALUE_Kisumu
            if sales.QTY_Eldoret is not None:
                region_totals['Eldoret']['Gyn']['actual'] += sales.SALE_VALUE_Eldoret
            if sales.QTY_Mombasa is not None:
                region_totals['Mombasa']['Gyn']['actual'] += sales.SALE_VALUE_Mombasa

        elif sales.TotalFrgn == 'Pain':
            if sales.QTY_Nairobi_A is not None:
                region_totals['Nairobi A']['Pain']['actual'] += sales.SALE_VALUE_Nairobi_A
            if sales.QTY_Nairobi_B is not None:
                region_totals['Nairobi B']['Pain']['actual'] += sales.SALE_VALUE_Nairobi_B
            if sales.QTY_Nakuru is not None:
                region_totals['Nakuru']['Pain']['actual'] += sales.SALE_VALUE_Nakuru
            if sales.QTY_Nyeri is not None:
                region_totals['Nyeri']['Pain']['actual'] += sales.SALE_VALUE_Nyeri
            if sales.QTY_Kisumu is not None:
                region_totals['Kisumu']['Pain']['actual'] += sales.SALE_VALUE_Kisumu
            if sales.QTY_Eldoret is not None:
                region_totals['Eldoret']['Pain']['actual'] += sales.SALE_VALUE_Eldoret
            if sales.QTY_Mombasa is not None:
                region_totals['Mombasa']['Pain']['actual'] += sales.SALE_VALUE_Mombasa

    # Step 7: Calculate Totals and Percentages for Each Region
    for region, data in region_totals.items():
        total_target = 0
        total_actual = 0
        for sub_division in ['Cardio', 'Gyn', 'Pain']:
            target = float(data[sub_division]['target'])  # Cast target to float
            actual = float(data[sub_division]['actual'])  # Cast actual to float
            data[sub_division]['percent_achieved'] = round((actual / target) * 100, 2) if target > 0 else 0

            data[sub_division]['target'] = '{:,.0f}'.format(target)
            data[sub_division]['actual'] = '{:,.0f}'.format(actual)

            total_target += target
            total_actual += actual

        data['total_target'] = '{:,.0f}'.format(total_target)
        data['total_actual'] = '{:,.0f}'.format(total_actual)
        data['total_percent_achieved'] = round((total_actual / total_target) * 100, 2) if total_target > 0 else 0

    # Step 8: Calculate Rankings based on the total percentage achieved
    cardio_sorted = sorted(region_totals.items(), key=lambda item: item[1]['Cardio']['percent_achieved'], reverse=True)
    cardio_rank = {region: rank + 1 for rank, (region, data) in enumerate(cardio_sorted)}

    gyn_sorted = sorted(region_totals.items(), key=lambda item: item[1]['Gyn']['percent_achieved'], reverse=True)
    gyn_rank = {region: rank + 1 for rank, (region, data) in enumerate(gyn_sorted)}

    pain_sorted = sorted(region_totals.items(), key=lambda item: item[1]['Pain']['percent_achieved'], reverse=True)
    pain_rank = {region: rank + 1 for rank, (region, data) in enumerate(pain_sorted)}

    total_sorted = sorted(region_totals.items(), key=lambda item: item[1]['total_percent_achieved'], reverse=True)
    total_rank = {region: rank + 1 for rank, (region, data) in enumerate(total_sorted)}

    for region, data in region_totals.items():
        data['total_rank'] = total_rank.get(region, None)
        data['cardio_rank'] = cardio_rank.get(region, None)
        data['gyn_rank'] = gyn_rank.get(region, None)
        data['pain_rank'] = pain_rank.get(region, None)

    # Step 9: Prepare Data for Rendering
    context = {
        'region_totals': region_totals,
        'selected_months': selected_months,
    }

    # Step 10: Render the Template
    return render(request, 'reports/regional_sales_comparison.html', context)
