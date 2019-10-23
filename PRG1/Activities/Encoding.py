string_plaintext = input("Enter string to encode: ").replace(" ","").upper()

encode_arrangement = None
while encode_arrangement is None:
    try:
        encode_arrangement = list(map(lambda x: int(x) - 1, input("Enter encode arrangement indexes: ")))
        print(encode_arrangement)

        if max(encode_arrangement) + 1 != len(string_plaintext):
            print("Error: Max encode index ({}) does not match length of plaintext string ({})".format(max(encode_arrangement) + 1, len( string_plaintext)))
            encode_arrangement = None
            continue
        
        for i in range(len(encode_arrangement)):
            if encode_arrangement.index(i) < 0:
                print("Error: Missing encode arrangement index.")
                encode_arrangement = None
                continue

            if encode_arrangement[i] > len(string_plaintext):
                print("Error: Encode index ({}) exceeds length of plaintext string ({})".format(encode_arrangement[i], len(string_plaintext)))
                encode_arrangement = None
                continue

    except ValueError:
        print("Error: Non-int encode arrangement index.")


string_encoded = ""

for encode_arrangement_index in encode_arrangement:
    string_encoded += string_plaintext[encode_arrangement_index]

print(string_encoded)