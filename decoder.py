def decode_string(encodingTable, tokens):
     decoded_text = ""
     while True:
        count_decoded = 0
        token_buffer = []
        for token in tokens:
            if encodingTable[token][0] == token:
                token_buffer += [token]
            else:
                print(encodingTable[token])
                token_buffer += [encodingTable[token][0][0]]
                token_buffer += [encodingTable[token][0][1]]
            tokens = token_buffer        
        if count_decoded == 0:
            break

     for token in tokens:
        decoded_text += chr(token)
     return decoded_text

