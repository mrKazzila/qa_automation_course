from collections import namedtuple

Data = namedtuple(
    'Data',
    'method_,'
    'ip_,'
    'url_,'
    'date_time_,'
    'duration_',
)

methods = {
    'GET': 0,
    'POST': 0,
    'HEAD': 0,
    'PUT': 0,
    'OPTIONS': 0,
    'DELETE': 0,
    'CONNECT': 0,
    'TRACE': 0,
    'PATCH': 0,
}
