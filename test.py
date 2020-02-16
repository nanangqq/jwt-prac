import requests

# create user
# print(requests.post('http://localhost:3000/api/auth/register', data={
#     'username':'ging2',
#     'password':'test'
# }).text)

# login
print(requests.post('http://localhost:3000/api/auth/login', data={
    'username':'ging',
    'password':'test'
}).json())

# check
# print(requests.get('http://localhost:3000/api/auth/checkjwt?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4OTgxZGZjODMwOTM0M2M5ZjlhNjEiLCJ1c2VybmFtZSI6ImdpbmcyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1ODE4MTgzNzgsImV4cCI6MTU4MjQyMzE3OCwiaXNzIjoiZ2luZyIsInN1YiI6InVzZXJJbmZvIn0.tya84xIzkplc3PgYDdeG1nWlLKLyA_h0MJ0G64WA3cs').text)
# print(requests.get('http://localhost:3000/api/auth/checkjwt?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4OTgxZGZjODMwOTM0M2M5ZjlhNjEiLCJ1c2VybmFtZSI6ImdpbmcyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1ODE4MTgzNzgsImV4cCI6MTU4MjQyMzE3OCwiaXNzIjoiZ2luZyIsInN1YiI6InVzZXJJbmZvIn0.tya84xIzkplc3PgYDdeG1nWlLKLyA_h0MJ0G64WA3c').text)
# print(requests.get('http://localhost:3000/api/auth/checkjwt', headers={'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4OTgxZGZjODMwOTM0M2M5ZjlhNjEiLCJ1c2VybmFtZSI6ImdpbmcyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1ODE4MTgzNzgsImV4cCI6MTU4MjQyMzE3OCwiaXNzIjoiZ2luZyIsInN1YiI6InVzZXJJbmZvIn0.tya84xIzkplc3PgYDdeG1nWlLKLyA_h0MJ0G64WA3cs'}).text)

#list
# print(requests.post(
#     'http://localhost:3000/api/user/assign-admin/ging2',
#     headers={
#         'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4MWYyZTc1NTFlMDViMzQzNmU2MzIiLCJ1c2VybmFtZSI6ImdpbmciLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTgxODIyOTE3LCJleHAiOjE1ODI0Mjc3MTcsImlzcyI6ImdpbmciLCJzdWIiOiJ1c2VySW5mbyJ9.-c5BxAf4_xQUR_QNtcNDx4ywZpzXTktjcTBlUrQ_udQ'
#     }
# ).json())

# print(requests.post(
#     'http://localhost:3000/api/user/assign-admin/ginggg',
#     headers={
#         'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4MWYyZTc1NTFlMDViMzQzNmU2MzIiLCJ1c2VybmFtZSI6ImdpbmciLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTgxODIyOTE3LCJleHAiOjE1ODI0Mjc3MTcsImlzcyI6ImdpbmciLCJzdWIiOiJ1c2VySW5mbyJ9.-c5BxAf4_xQUR_QNtcNDx4ywZpzXTktjcTBlUrQ_udQ'
#     }
# ).json())

# print(requests.get(
#     'http://localhost:3000/api/user/list',
#     headers={
#         'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4MWYyZTc1NTFlMDViMzQzNmU2MzIiLCJ1c2VybmFtZSI6ImdpbmciLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTgxODIyOTE3LCJleHAiOjE1ODI0Mjc3MTcsImlzcyI6ImdpbmciLCJzdWIiOiJ1c2VySW5mbyJ9.-c5BxAf4_xQUR_QNtcNDx4ywZpzXTktjcTBlUrQ_udQ'
#     }
# ).json())

### 비번 암호화 이후
# create user
# print(requests.post('http://localhost:3000/api/auth/register', data={
#     'username':'ginggg',
#     'password':'test'
# }).text)

# login
print(requests.post('http://localhost:3000/api/auth/login', data={
    'username':'ginggg',
    'password':'test'
}).json())

# check
# print(requests.get('http://localhost:3000/api/auth/checkjwt?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4OTgxZGZjODMwOTM0M2M5ZjlhNjEiLCJ1c2VybmFtZSI6ImdpbmcyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1ODE4MTgzNzgsImV4cCI6MTU4MjQyMzE3OCwiaXNzIjoiZ2luZyIsInN1YiI6InVzZXJJbmZvIn0.tya84xIzkplc3PgYDdeG1nWlLKLyA_h0MJ0G64WA3cs').text)
# print(requests.get('http://localhost:3000/api/auth/checkjwt?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4OTgxZGZjODMwOTM0M2M5ZjlhNjEiLCJ1c2VybmFtZSI6ImdpbmcyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1ODE4MTgzNzgsImV4cCI6MTU4MjQyMzE3OCwiaXNzIjoiZ2luZyIsInN1YiI6InVzZXJJbmZvIn0.tya84xIzkplc3PgYDdeG1nWlLKLyA_h0MJ0G64WA3c').text)
# print(requests.get('http://localhost:3000/api/auth/checkjwt', headers={'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4OTgxZGZjODMwOTM0M2M5ZjlhNjEiLCJ1c2VybmFtZSI6ImdpbmcyIiwiYWRtaW4iOmZhbHNlLCJpYXQiOjE1ODE4MTgzNzgsImV4cCI6MTU4MjQyMzE3OCwiaXNzIjoiZ2luZyIsInN1YiI6InVzZXJJbmZvIn0.tya84xIzkplc3PgYDdeG1nWlLKLyA_h0MJ0G64WA3cs'}).text)

# list
# print(requests.post(
#     'http://localhost:3000/api/user/assign-admin/ging2',
#     headers={
#         'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4MWYyZTc1NTFlMDViMzQzNmU2MzIiLCJ1c2VybmFtZSI6ImdpbmciLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTgxODIyOTE3LCJleHAiOjE1ODI0Mjc3MTcsImlzcyI6ImdpbmciLCJzdWIiOiJ1c2VySW5mbyJ9.-c5BxAf4_xQUR_QNtcNDx4ywZpzXTktjcTBlUrQ_udQ'
#     }
# ).json())

# print(requests.post(
#     'http://localhost:3000/api/user/assign-admin/ginggg',
#     headers={
#         'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4MWYyZTc1NTFlMDViMzQzNmU2MzIiLCJ1c2VybmFtZSI6ImdpbmciLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTgxODIyOTE3LCJleHAiOjE1ODI0Mjc3MTcsImlzcyI6ImdpbmciLCJzdWIiOiJ1c2VySW5mbyJ9.-c5BxAf4_xQUR_QNtcNDx4ywZpzXTktjcTBlUrQ_udQ'
#     }
# ).json())

# print(requests.get(
#     'http://localhost:3000/api/user/list',
#     headers={
#         'x-access-token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTQ4MWYyZTc1NTFlMDViMzQzNmU2MzIiLCJ1c2VybmFtZSI6ImdpbmciLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNTgxODIyOTE3LCJleHAiOjE1ODI0Mjc3MTcsImlzcyI6ImdpbmciLCJzdWIiOiJ1c2VySW5mbyJ9.-c5BxAf4_xQUR_QNtcNDx4ywZpzXTktjcTBlUrQ_udQ'
#     }
# ).json())

