from django.shortcuts import render

def get_list_or_none(model_name):
    object_name = None
    try:
        object_name =  model_name.objects.all()
    except model_name.DoesNotExist:
        pass
    else:
        return object_name

def filter_list_or_none(model_name, **kwargs):
    object_list = None
    try:
       object_list = model_name.objects.filter(**kwargs)
    except:
        pass
    else:
        return object_list
