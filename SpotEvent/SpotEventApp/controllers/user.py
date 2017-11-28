from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SpotEventApp.serializers.user import User as userSerializer
from SpotEventApp.serializers.user import Create_user as Create_userSerializer
from SpotEventApp.models.user import User as userModel
from SpotEventApp.serializers.address import Address as addressSerializer
#identifier serializer doesn't have to imported, inheritance form that class
#address is a foreign key of identifier, thus also for user

#this wil get all users and retrun it or add a user to 
#the existing list of users 
# when posting an addres needs to be created too

@api_view(['GET', 'POST'])
def user_request(request):
	if (request.method == 'GET' ):
		users = userModel.objects.all() # returns all users
		serializer = userSerializer(users, many=True, context={'request':request}) #many = True, -> list of multiple user 
		return Response(serializer.data)
	elif (request.method == 'POST'):
		serializer	= Create_userSerializer(data=request.data) # hier creeeren 
		if (serializer.is_valid()):
			user = serializer.save()
			print('created')
			serializer = userSerializer(user, context={'request':request} )	# de gecreeerde user terug geven
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def single_user_request(request, pk): #get one user with the specific
	try: 
		user = userModel.objects.get(id=pk)
	except userModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'GET'):
		serializer = userSerializer(user, context={'request':request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif(request.method == 'PUT'):
		serializer = userSerializer(user, data=request.data, context={'request':request})
		if(serializer.is_valid()):
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	


