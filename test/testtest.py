from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.sagan import Result, DnsResult
from measurements import kwargs_a, kwargs_i


def create(kwargs):
    is_success, results = AtlasResultsRequest(**kwargs).create()
    if is_success:
        for result in results:
            my_result = DnsResult.get(result)
            if not my_result.is_error:
                timestamp = result['timestamp']
                serial = result['result']['answers'][0]['SERIAL']
                print(timestamp, serial)


create(kwargs_i)
