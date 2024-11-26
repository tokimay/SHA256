# Secure Hash Algorithm 256 bit
## SHA 256

SHA256 is widely used to hash data. It is the main hash algorithm in the bitcoin blockchain.

#### Usage:

```python
import SHA256

_input = 'Hello SHA256'
print('='*8, type(_input))
result = SHA256.do_hash(_input)
print(F"MESSAGE: {_input}\nHASH   : {result}\nLENGTH : {len(result)}\n")
```

#### Result:

```text
======== <class 'str'>
MESSAGE: Hello SHA256
HASH   : 70725d0f78cb0967c0e5171f733619712d239e28f2d279e4b3c3ed97f7456fa3
LENGTH : 64
```