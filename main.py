from collections import defaultdict
from decoder import decode_string
from encoder import encode_string


def show_encoded_string(encodingTable, tokens):
     for token in tokens:
          if encodingTable[token][0] == token:
               print(chr(token), end = "")
          else:
               print(f"[{token}]", end = "")
     print("\n")

def main():
    
    #text = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
    text = "ababcde"
    encoding_table, tokens_two = encode_string(text)
    show_encoded_string(encoding_table, tokens_two)

    print(decode_string(encoding_table, tokens_two))


if __name__ == "__main__":
        main()