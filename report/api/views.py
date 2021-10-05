from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .serializers import ReportSerializer, CategorySerializer
from report.models import Report, Category

class ReportAPIList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        report = Report.objects.all()
        serializer = ReportSerializer(report, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportAPIDetail(APIView):
    """
    Retrieve, update or delete a transformer instance
    """
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Report.objects.get(pk=pk)
        except Report.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        report = self.get_object(pk)
        serializer = ReportSerializer(report,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReportList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportbyUser(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReportSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return Report.objects.filter(user=pk)

class CategoryAPIList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)