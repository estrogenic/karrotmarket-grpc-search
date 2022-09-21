import search_pb2 as search
import response_pb2 as response
import requests


search = search.Search()
search.request_id = 8

query = search.query_data.add()
query.keyword = "Apple"  # searching keyword
query.region_ids = 1339  # searching region
query.post_per_page = 30  # post cnt per request
query.unknown = 1  # not required but impacted

headers = {'content-type': 'application/protobuf'}
r = requests.post('https://search-server.kr.karrotmarket.com/api/v1', stream=True, data=search.SerializeToString(), headers=headers)

decoded_content = response.Response()
decoded_content.ParseFromString(r.content)

for a in decoded_content.doc_list.doc_data:
    print(f"{a.location_str, a.title, a.content}")


with open('./response.bin', 'wb') as f:
    f.write(r.content)

