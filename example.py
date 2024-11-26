import SHA256

_input = 'Hello SHA256'
print('='*8, type(_input))
result = SHA256.do_hash(_input)
print(F"MESSAGE: {_input}\nHASH   : {result}\nLENGTH : {len(result)}\n")

_input = b'Hello SHA256'
print('='*8, type(_input))
result = SHA256.do_hash(_input)
print(F"MESSAGE: {_input}\nHASH   : {result}\nLENGTH : {len(result)}\n")

s = 'Hello SHA256'
_input = bytearray()
_input.extend(map(ord, s))
print('='*8, type(_input))
result = SHA256.do_hash(_input)
print(F"MESSAGE: {_input}\nHASH   : {result}\nLENGTH : {len(result)}\n")

s = 'Hello SHA256'
_input = bytearray()
_input.extend(map(ord, s))
_input = int.from_bytes(_input, "big")
print('='*8, type(_input))
result = SHA256.do_hash(_input)
print(F"MESSAGE: {_input}\nHASH   : {result}\nLENGTH : {len(result)}\n")

s = 'Hello SHA256'
_input = bytearray()
_input.extend(map(ord, s))
_input = int.from_bytes(_input, "big")
_input = hex(_input)[2:]
print('='*8, 'hex')
result = SHA256.do_hash(_input)
print(F"MESSAGE: 0x{_input}\nHASH   : {result}\nLENGTH : {len(result)}\n")