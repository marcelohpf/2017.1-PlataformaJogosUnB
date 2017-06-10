from information.models import Rating, Information
from rest_framework.decorators import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


class VoteView(APIView):

    permission_classes = (permissions.AllowAny, )

    # @login_required
    def post(self, request, pk=None):
        information = get_object_or_404(Information, pk=pk)
        try:
            rating = Rating.objects.get(
                email_voter=request.data['email_voter'])
            rating.delete()
        except:
            rating = None

        rating = Rating(vote=request.data['vote'],
                        email_voter=request.data['email_voter'],
                        information=information)
        try:
            rating.save()
            return Response({'status': 'Vote successfully done.'},
                            status.HTTP_201_CREATED)
        except:
            return Response({'status': 'The vote could not be done.'},
                            status.HTTP_400_BAD_REQUEST)
