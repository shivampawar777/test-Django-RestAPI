from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer, LoginSerializer


@api_view(['GET', 'POST', 'PUT'])
def index(request):
    info = {
        "name" : "ABC",
        "address" : "Pune",
        "age" : "18",
    }
    if request.method == 'GET':
        data = request.GET.get('name')
        return Response(data)
    
    elif request.method == 'POST':
        data = request.data
        print("\n***Info***")
        print(data)
        return Response(info)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializer(obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({"Message" : "Person information deleted.."})
        

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        data = serializer.data # data can be accepted and...
        print(data) # the data has been shown into the console log
        return Response({'Message' : 'Login successfull'})

    return Response(serializer.errors)