from django.http import HttpResponse, JsonResponse
from space_messages.models import SpaceMessage


def index(request):
    msgs = SpaceMessage.objects.all().order_by('id')

    result_string = ''
    for message in msgs:
        result_string += message.text + ' read=' + str(message.is_read) + '<br>'

    return HttpResponse(result_string)


def mark_read(request):
    if not request.GET.get('id'):
        return HttpResponse(status=400)

    SpaceMessage.objects.filter(id=id).update(is_read=True)
    return HttpResponse('OK')


def get_messages(request):
    if not request.GET.get('last_id'):
        return HttpResponse(status=400)

    last_id = int(request.GET['last_id'])
    last_msgs = SpaceMessage.objects.filter(id__gt=last_id, is_read=False)
    messages_list = list(last_msgs.values('id', 'msg_date', 'text', 'is_read'))

    return JsonResponse(messages_list, safe=False)
