from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from core.models import Faq, Block, User, Poll
from . import serializers
from rest_framework.views import APIView
from api.serializers import UserWrite, BlockWrite
from rest_framework import status



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'faq': 'api/faq - просмотр всех тем справки, добавление справки',
        'faq detail': 'api/faq/title - просмотр и редактирование справки',
        'member list': 'api/user - просмотр всех юзеров, добавление и редактирование юзеров'
                       'обязательные поля: username и user_id_tg',
        'member detail': 'api/user/user_id - просмотр и редактирование юзера',
        'block list': 'api/block - просмотр списка заблокированных юзеров',
        'block detail': 'api/block/user_id - блокирование юзеров, обязательное поле: user',
        'poll': 'api/poll - просмотр и сохранение голосовалок, для добавления методом post отправить "keyboard_id:<int>, "user_id: <int>',
        'poll detail': 'api/poll/<keyboard_id> - просмотр конкретной голосовалки'
    }
    return Response(api_urls)


class FaqList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = serializers.FaqSerializer


class FaqDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = serializers.FaqSerializer
    lookup_field = 'title'


class BlockWriteList(APIView):
    def get(self, request):
        queryset = Block.objects.all()
        block_list = BlockWrite(queryset, many=True)
        return Response(block_list.data)

    def post(self, request):
        serializer = BlockWrite(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockWriteDetail(APIView):
    def get(self, request, user):
        queryset = Block.objects.get(user=user)
        block = BlockWrite(queryset)
        return Response(block.data, status=status.HTTP_200_OK)


class UserWriteList(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer_for_queryset = UserWrite(queryset, many=True)
        return Response(serializer_for_queryset.data)

    def post(self, request):
        serializer = UserWrite(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserWriteDetail(APIView):
    def get(self, request, user_id_tg):
        queryset = User.objects.get(user_id_tg=user_id_tg)
        user = UserWrite(queryset)
        return Response(user.data, status=status.HTTP_200_OK)


class PollWriteList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = serializers.PollWrite


class PollDetailList(APIView):
    def get(self, request, keyboard_id):
        queryset = Poll.objects.filter(keyboard_id=keyboard_id)
        serializer_class = serializers.PollWrite(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)