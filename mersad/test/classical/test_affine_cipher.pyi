# Stubs for mersad.test.classical.test_affine_cipher (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

# Python Standard Library
import unittest
from typing import Any

class TestShiftCipher(unittest.TestCase):
    base_path: Any = ...
    agent: Any = ...
    plain_text: Any = ...
    k125_sh0_s0: Any = ...
    k173_sh1_s0: Any = ...
    custom_alphabet: Any = ...
    def setUp(self) -> None: ...
    def test_encrypt_without_shuffle(self) -> None: ...
    def test_encrypt_with_shuffle_without_seed(self) -> None: ...
    def test_encrypt_with_custom_alphabet(self) -> None: ...
    def test_decryption_without_shuffle(self) -> None: ...
    def test_decrypt_with_shuffle_without_seed(self) -> None: ...
    def test_decrypt_with_custom_alphabet(self) -> None: ...
    def test_return_key(self) -> None: ...
    def test_temporary_key(self) -> None: ...
    def test_temporary_key_to_permanent(self) -> None: ...
    def test_key_is_lower_than_alphabet_length(self) -> None: ...
    def test_key_and_letter_sequence_length_not_relatively_prime(self) -> None: ...
    def test_none_key(self) -> None: ...
    def test_terminal_application(self) -> None: ...
