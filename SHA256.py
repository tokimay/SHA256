a = h0 = 1779033703
b = h1 = 3144134277
c = h2 = 1013904242
d = h3 = 2773480762
e = h4 = 1359893119
f = h5 = 2600822924
g = h6 = 528734635
h = h7 = 1541459225

k = [
    1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221,
    3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580,
    3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986,
    2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895,
    666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037,
    2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344,
    430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779,
    1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298
]


def rightRotate(number: int, rotations: int) -> int:
    return (2 ** 32 - 1) & (number >> rotations | number << (32 - rotations))


def rightShift(number: int, shift: int) -> int:
    return number >> shift


def XOR(number1: int, number2: int) -> int:
    return number1 ^ number2


def AND(number1: int, number2: int) -> int:
    return number1 & number2


def NOT(number):
    return ~number


def doHash(input_: str) -> str:
    global h0, h1, h2, h3, h4, h5, h6, h7, a, b, c, d, e, f, g, h

    # check if the input is string

    bytearrayInput = bytearray(input_, 'UTF-8')
    lengthBytearrayInput = len(bytearrayInput) * 8
    bytearrayInput.append(0x80)

    while ((len(bytearrayInput) * 8 + 64) % 512) != 0:
        bytearrayInput.append(0x00)

    bytearrayInput += lengthBytearrayInput.to_bytes(8, 'big')

    # check if the padding complete

    chunks = []
    for i in range(0, len(bytearrayInput), 64):
        chunks.append(bytearrayInput[i:i + 64])

    for chunk in chunks:
        bytearrayInput_schedule = []
        for i in range(0, 64 * 4, 4):
            bytearrayInput_schedule.append(chunk[i:i + 4])
        for i in range(0, 48, 1):
            term1 = int(bytearrayInput_schedule[i].hex(), 16)
            term2 = int(bytearrayInput_schedule[i + 1].hex(), 16)
            term3 = int(bytearrayInput_schedule[i + 9].hex(), 16)
            term4 = int(bytearrayInput_schedule[i + 14].hex(), 16)

            term1_RR_7 = rightRotate(term2, 7)
            term1_RR_18 = rightRotate(term2, 18)
            term1_RS_3 = rightShift(term2, 3)
            term1XOR = XOR(XOR(term1_RR_7, term1_RR_18), term1_RS_3)

            term4_RR_17 = rightRotate(term4, 17)
            term4_RR_19 = rightRotate(term4, 19)
            term4_RS_10 = rightShift(term4, 10)
            term4XOR = XOR(XOR(term4_RR_17, term4_RR_19), term4_RS_10)

            result = ((term1 + term1XOR + term3 + term4XOR) % 2 ** 32)
            bytearrayInput_schedule[i + 16] = result.to_bytes(8, 'big')
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7
        for i in range(0, 64, 1):
            w = int(bytearrayInput_schedule[i].hex(), 16)
            sigma0 = XOR(XOR(rightRotate(a, 2), rightRotate(a, 13)), rightRotate(a, 22))
            sigma1 = XOR(XOR(rightRotate(e, 6), rightRotate(e, 11)), rightRotate(e, 25))
            choice = XOR((AND(e, f)), (AND((NOT(e)), g)))
            majority = XOR(XOR((AND(a, b)), (AND(a, c))), (AND(b, c)))
            temp2 = ((sigma0 + majority) % 2 ** 32)
            temp1 = (h + sigma1 + choice + k[i] + w) % 2 ** 32
            h = g
            g = f
            f = e
            e = (d + temp1) % 2 ** 32
            d = c
            c = b
            b = a
            a = (temp1 + temp2) % 2 ** 32
        h0 = (h0 + a) % 2 ** 32
        h1 = (h1 + b) % 2 ** 32
        h2 = (h2 + c) % 2 ** 32
        h3 = (h3 + d) % 2 ** 32
        h4 = (h4 + e) % 2 ** 32
        h5 = (h5 + f) % 2 ** 32
        h6 = (h6 + g) % 2 ** 32
        h7 = (h7 + h) % 2 ** 32

    h0 = hex(h0)[2:].zfill(8)
    h1 = hex(h1)[2:].zfill(8)
    h2 = hex(h2)[2:].zfill(8)
    h3 = hex(h3)[2:].zfill(8)
    h4 = hex(h4)[2:].zfill(8)
    h5 = hex(h5)[2:].zfill(8)
    h6 = hex(h6)[2:].zfill(8)
    h7 = hex(h7)[2:].zfill(8)

    return h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7
