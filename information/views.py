from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,"index.html")

def get_value(request):
    return render (request,('get_value.html'),{'product': product})
product = [["P001","Pen",2.50,8],
           ["P002","Ruler",1.50,10]]

def save_data(request):
    if request.method == 'POST':
        p_id = request.POST['prod_id']
        p_qty = request.POST['prod_qty']

        for value in product:
            if value[0]== p_id:
                total = float(p_qty) *value [2]

        dict = {
            'P_CODE' : p_id,
            'quantity': p_qty,
            'total' : total
            }
        return render (request,('save_data.html'),dict)
