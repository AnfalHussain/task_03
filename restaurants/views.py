from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list':[{
    	'restaurant_name':"ChocolateBar",
    	'food_type':"Desserts",},
    	{'restaurant_name':"KFC",
    	'food_type':"Fried Chicken",},
    	{
    	'restaurant_name':"Junkyard",
    	'food_type':"Junk Food",},]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 
    	'my_object':{
    	"restaurant_name" :"KFC",
    	'food_type':"Fried Chicken",
    	}
    }
    return render(request, 'detail.html', context)
