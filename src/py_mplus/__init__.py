from py_mplus.objects import MPData
from py_mplus.objects.response import Response
import uuid

HEADER = str(uuid.uuid4())


def parse(buffer: bytes):
    data = MPData(list(buffer))
    return Response(data, len(data))
