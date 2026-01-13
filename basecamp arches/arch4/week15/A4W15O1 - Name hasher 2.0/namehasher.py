hashmap_key_value = {}
encoded_values = []
decoded_values = []


def encode_string(data: str, hofunction) -> str:
    raise NotImplementedError


def decode_string(data: str, hofunction) -> str:
    raise NotImplementedError


def encode_list(data: list, hofunction) -> list:
    raise NotImplementedError


def decode_list(data: list, hofunction) -> list:
    raise NotImplementedError


def validate_values(encoded: str, decoded: str, hofunction) -> bool:
    raise NotImplementedError


def main():
    raise NotImplementedError


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()
