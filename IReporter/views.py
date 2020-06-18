from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import InterventionRecord
from .serializers import InterventionSerializer
from rest_framework.decorators import api_view,APIView,permission_classes


# Create your views here.
class intervention_list(APIView):
    def get(self,request):
    #GET LIST OF INTERVENTION RECORDS,POST A NEW INTERVENTION,DELETE ALL INTERVENTIONS...
        intervention =InterventionRecord.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            intervention = InterventionRecord.filter(title__icontains=title)
        
        intervention_serializers = InterventionSerializer(intervention, many=True)
        return JsonResponse(intervention_serializers.data, safe=False)

    # #CREATE AND SAVE A NEW INTERVENTION RECORD
    def post(self,request):        
        intervention_data = JSONParser().parse(request)
        intervention_serializer = InterventionSerializer(data=intervention_data)
        if intervention_serializer.is_valid():
            intervention_serializer.save()
            return JsonResponse(intervention_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(intervention_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class intervention_detail(APIView):
    def get(self,request,pk):
    #FIND TUTORIAL BY pk(id)

        try:
            intervention=InterventionRecord.objects.get(id=pk)
        
            intervention_serializer=InterventionSerializer(intervention)
            return JsonResponse(intervention_serializer.data)
        except InterventionRecord.DoesNotExist:
            return JsonResponse({'message': 'The Intervention Record does not exist!'}, status=status.HTTP_404_NOT_FOUND) 
        
    def put(self,request,pk):
        try:
            intervention=InterventionRecord.objects.get(id=pk)
            intervention_data=JSONParser().parse(request)
            intervention_serializer=InterventionSerializer(intervention,data=intervention_data)
            if intervention_serializer.is_valid():
                intervention_serializer.save()
                return JsonResponse(intervention_serializer.data)
            return JsonResponse(intervention_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except InterventionRecord.DoesNotExist:
            return JsonResponse({'message': 'The Intervention Record does not exist!'}, status=status.HTTP_404_NOT_FOUND) 
    def delete(self,request,pk):
        # DELETE A CERTAIN INTERVENTION RECORD
        
        try:
            intervention=InterventionRecord.objects.get(id=pk)
            intervention.delete()
            return JsonResponse({'message': 'Intervention Record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except InterventionRecord.DoesNotExist:
            return JsonResponse({'message': 'The Intervention Record does not exist!'}, status=status.HTTP_404_NOT_FOUND) 



class intervention_list_status(APIView):
    def get(self,request):
        #Get all  resolved INtervention
        try:
            intervention=InterventionRecord.objects.filter(status='resolved')
            intervention_serializer=InterventionSerializer(intervention,many=True)
            return  JsonResponse(intervention_serializer.data,safe=False)
        except InterventionRecord.DoesNotExist:
            return JsonResponse({'message': 'The Status does not exist!'}, status=status.HTTP_404_NOT_FOUND) 




