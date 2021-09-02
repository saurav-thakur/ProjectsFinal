from django.shortcuts import render
import pickle
import pandas as pd
# Create your views here.


def home(request):
    # model = pickle.load(open('carpredictionmodel.pkl', 'rb'))
    model = pd.read_pickle('carpredictionmodel.pkl')

    answer = []

    a1 = request.POST.get('levy', 751.0)
    a2 = request.POST.get('manufacturer', 'KIA')
    a3 = request.POST.get('model', 'Optima')
    a4 = request.POST.get('productionyear', '2013')
    a5 = request.POST.get('category', 'Sedan')
    a6 = request.POST.get('leatherinterior', 'Yes')
    a7 = request.POST.get('fueltype', 'Petrol')
    a8 = request.POST.get('enginevolume', '2.4')
    a9 = request.POST.get('mileage', 180800.0)
    a10 = request.POST.get('cylinders', '4.0')
    a11 = request.POST.get('gearboxtype', 'Automatic')
    a12 = request.POST.get('drivewheels', 'Front')
    a13 = request.POST.get('doors', '04-May')
    a14 = request.POST.get('wheel', 'Left wheel')
    a15 = request.POST.get('color', 'White')
    a16 = request.POST.get('airbags', '4')
    a17 = request.POST.get('isturbo', 'Non-Turbo')

    # answer.append(request.GET['levy'])
    # answer.append(request.GET['manufacturer'])
    # answer.append(request.GET['model'])
    # answer.append(request.GET['productionyear'])
    # answer.append(request.GET['category'])
    # answer.append(request.GET['leatherinterior'])
    # answer.append(request.GET['fueltype'])
    # answer.append(request.GET['enginevolume'])
    # answer.append(request.GET['mileage'])
    # answer.append(request.GET['cylinders'])
    # answer.append(request.GET['gearboxtype'])
    # answer.append(request.GET['drivewheels'])
    # answer.append(request.GET['doors'])
    # answer.append(request.GET['wheel'])
    # answer.append(request.GET['color'])
    # answer.append(request.GET['airbags'])
    # answer.append(request.GET['isturbo'])

    # answer[[request.GET['levy'], request.GET['manufacturer'], request.GET['model'],
    #         request.GET['productionyear'], request.GET['category'], request.GET[
    #             'leatherinterior'], request.GET['fueltype'], request.GET['fueltype'],
    #         request.GET['enginevolume'], request.GET['mileage'], request.GET[
    #             'cylinders'], request.GET['gearboxtype'], request.GET['drivewheels'],
    #         request.GET['doors'], request.GET['wheel'], request.GET['color'], request.GET['airbags'], request.GET['isturbo']]]

    # pred = model.predict([answer])
    cols = ['Levy', 'Manufacturer', 'Model', 'Prod. year', 'Category',
            'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
            'Cylinders', 'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color',
            'Airbags', 'isTurbo']

    ans = [[a1, a2, a3, a4, a5, a6, a7, a8, a9,
            a10, a11, a12, a13, a14, a15, a16, a17]]
    print(ans)
    df = pd.DataFrame(ans, columns=cols)
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    print(df)
    # print(df)
    # df = df.astype({col: int for col in ['Levy', 'Mileage']})

    pred = round(model.predict(df)[0],2)

    context = {'pred': pred}

    return render(request, 'App/home.html', context)
