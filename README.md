# Gartenzaun Transposition

This is a small implementation of the simple `Gartenzaun` transposition 'encryption' method
used for an introductory Python workshop.

******

## How the `Gartenzaun` transposition works

The method can be used to exchange 'secret' messages and it works as follows. Given a secret message,
such as "*This is my secret message*", start by splitting the symbols (letters, digits, whitespaces, 
punctuation marks, etc) of the sentence into two groups depending on whether their position in the
sentence is even or odd. Afterwards the two groups are concatenated. This gives:
| | |
| :--- | :--- |  
| Message: | This_is_my_secret_message  |  
| Even:    | T i _ s m _ e r t m s a e  |  
| Odd:     |  h s i _ y s c e _ e s g   |  
| Secret:  | Ti sm ertmsaehsi ysce esg  |  
| | |  

******

## Usage

Using the script [`gartenzaun.py`](gartenzaun.py), a message can be encrypted as follows

```sh
> python3 gartenzaun.py encrypt "This is my secret message"
Encrypted message: Ti sm ertmsaehsi ysce esg
```

Decryption works in the same way:

```sh
> python3 gartenzaun.py decrypt "Ti sm ertmsaehsi ysce esg"
Decrypted message: This is my secret message
```
