from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_409_CONFLICT


class ConflictException(APIException):
    status_code = HTTP_409_CONFLICT
    default_code = 'conflict_exception'
    default_detail = 'a database conflict occurred'
