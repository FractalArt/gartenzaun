#!/usr/bin/env python3
"""
Encrypt and decrypt secret messages using the 'Gartenzaun' method.

The method proceeds by separating the letters into two groups according to
whether their position in the sentence is even or odd. After that, both groups
of letters are concatenated to form the secret encypted version of the message.

Example
-------
Message: "This is a secret message"

In the encryption process we also consider the whitespaces. In this case the message reads
"This_is_a_secret_message"

Splitting the symbols in the message into ones with even and odd positions we find:

even: T i _ s a s c e _ e s g  -> "Ti sasce esg"
odd :  h s i _ _ e r t m s a e -> "hsi  ertmsae"

Finally, the secret message reads

Secret message: "Ti sasce esghsi ertmsae"
"""
import argparse as ap
import math


def setup_cli():
    """Setup command line interface."""
    parser = ap.ArgumentParser(
        description="Encrypt or decrypt a secret message using the 'Gartenzaun' method."
    )
    subparsers = parser.add_subparsers(dest="method")

    # encryption
    encrypt = subparsers.add_parser("encrypt")
    encrypt.add_argument("message", type=str, help="The message to encrypt")

    # decryption
    decrypt = subparsers.add_parser("decrypt")
    decrypt.add_argument("secret", type=str, help="The secret message to decrypt")

    return parser.parse_args()


def encrypt(message: str) -> str:
    """Encrypt the `message` using the 'Gartenzaun' method."""
    even = []
    odd = []
    for idx, symbol in enumerate(message):
        if idx % 2 == 0:
            even.append(symbol)
        else:
            odd.append(symbol)
    return f"{''.join(even)}{''.join(odd)}"


def decrypt(secret: str) -> str:
    """Decrypt a `secret` message encrypted using the 'Gartenzaun' method"""
    middle = int(math.ceil(len(secret) / 2))
    left, right = secret[: middle], secret[middle:]
    decrypted = []
    for i in range(len(left)):
        decrypted.append(left[i])
        if i < len(right):
            decrypted.append(right[i])

    return "".join(decrypted)


if __name__ == "__main__":

    # parse command-line arguments
    args = setup_cli()

    if args.method == "encrypt":
        encrypted = encrypt(args.message)
        print(f"Encrypted message: {encrypted}")
    if args.method == "decrypt":
        decrypted = decrypt(args.secret)
        print(f"Decrypted message: {decrypted}")
