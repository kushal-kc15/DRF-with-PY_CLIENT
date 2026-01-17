from django.http import JsonResponse
import json

def api_home(request,*args,**kwargs):
  print(request.GET)
  print(request.POST)
  body=request.body #byte string of json data 
  data={}
  try:
    data=json.loads(body)#string of json data --> python dict
  except:
    pass
  print(data)
  print(request.headers)
  data['params']=dict(request.GET)
  # data['headers']=dict(request.headers)
  data['content_type']=request.content_type
  return JsonResponse(data)
