from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# class Student_info(viewsets.ViewSet):
#     def get(self,request):
#         stud = Student.objects.all()
#         serializer = StudentSerializer(stud,many=True)
#         return Response(serializer.data)
#     def create(self,request):
#         data = request.data 
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'mgs':'Data Created...!'})
#     def retrieve(self,request,pk):
#         stud = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stud)
#         return Response(serializer.data)
#     def destroy(self,request,pk):
#         stud = Student.objects.get(pk=pk)
#         stud.delete()
#         return Response({'mgs':'Data Deleted...!'})
#     def update(self,request,pk):    
#         stud = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stud,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'mgs':'Full Update data....!'})
#     def partial_update(self,request,pk):
#         stud = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(stud,data=request.data,partial=True)

class Student_info(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer