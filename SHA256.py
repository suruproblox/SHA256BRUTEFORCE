import hashlib
import itertools
import string

def brute_force_sha256(target_hash, max_length=5, charset=string.ascii_letters + string.digits):
    """
    Attempts to brute-force a SHA-256 hash by generating combinations of characters.

    :param target_hash: The SHA-256 hash to match.
    :param max_length: The maximum length of combinations to try.
    :param charset: The set of characters to use for combinations.
    :return: The original input if found, or None if not.
    """
    for length in range(1, max_length + 1):
        print(f"Trying combinations of length {length}...")
        for combination in itertools.product(charset, repeat=length):
            candidate = ''.join(combination)
            candidate_hash = hashlib.sha256(candidate.encode()).hexdigest()
            if candidate_hash == target_hash:
                return candidate
    return None


# Example usage
if __name__ == "__main__":
    target_hash = input("Enter the SHA-256 hash to brute-force: ").strip()
    max_length = int(input("Enter the maximum length of strings to try: ").strip())

    print("Brute-forcing... This may take a while!")
    result = brute_force_sha256(target_hash, max_length=max_length)

    if result:
        print(f"Success! The original input is: {result}")
    else:
        print("Failed to find a match within the given parameters.")
