import random
import time
import string

cipher = bytes.fromhex(
    "f60d1ef6307bc56ed4f3f8fe41ea969b84bb2aae8bdcc4dd45b3083b601303b923ebba81ca"
)

def is_printable_flag(b):
    try:
        s = b.decode()
    except:
        return False

    # must be readable + contain flag structure
    return (
        all(c in string.printable for c in s)
        and "{" in s
        and "}" in s
    )

now = int(time.time())

for seed in range(now - 86400, now + 86400):  # ±24 HOURS
    random.seed(seed)

    keystream = bytearray(
        int(random.random() * 256)
        for _ in range(len(cipher))
    )

    plaintext = bytes(c ^ k for c, k in zip(cipher, keystream))
    print(repr(plaintext.decode()))

    if is_printable_flag(plaintext):
        print("FOUND SEED:", seed)
        print("FLAG:", plaintext.decode())
        break
