
import SHA256

input_ = 'Hello SHA256'

result = SHA256.doHash(input_)

print('HASH: ', result)
print('TYPE: ', type(result))
print('LENGTH: ', len(result))

