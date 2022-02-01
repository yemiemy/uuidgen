from django.shortcuts import render
from django.http import JsonResponse
import uuid
from .models import UUID

def uuid_gen(request):
    new_uuid = uuid.uuid4().hex

    obj, created = UUID.objects.get_or_create(uuid = new_uuid)

    qs = UUID.objects.order_by('-id')

    data = {}

    for q in qs:
        data[str(q.timestamp)] = q.uuid
    
    return JsonResponse(data, status=200)