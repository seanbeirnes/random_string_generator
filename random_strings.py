# A class for creating random strings and passwords.
class random_strings:
    
    def __get_random_char(self, alpha_lower=True, alpha_upper=True, numeric=True, special=True):
        import secrets
        import string

        chars = ""
        chars += string.ascii_lowercase if alpha_lower else ""
        chars += string.ascii_uppercase if alpha_upper else ""
        chars += string.digits if numeric else ""
        chars += string.punctuation if special else ""

        return secrets.choice(chars)


    def get_random_string(self, length=10):
        return ''.join([self.__get_random_char() for _ in range(length)])


    def get_random_password(self, length=10):
        import secrets

        num_alpha_lower_chars = max(length // 2, 2)  # Ensure at least 2 lowercase alpha characters
        num_alpha_upper_chars = max(length // 4, 2)  # Ensure at least 2 uppercase alpha characters
        num_numeric_chars = max(length // 6, 2)  # Ensure at least 2 numeric characters
        num_special_chars = length - num_alpha_lower_chars - num_alpha_upper_chars - num_numeric_chars

        lower_alpha_chars = [ self.__get_random_char( alpha_upper=False, numeric=False, special=False ) for _ in range(num_alpha_lower_chars) ]
        upper_alpha_chars = [ self.__get_random_char( alpha_lower=False, numeric=False, special=False) for _ in range(num_alpha_upper_chars) ]
        numeric_chars = [ self.__get_random_char(alpha_lower=False, alpha_upper=False, special=False) for _ in range(num_numeric_chars) ]
        special_chars = [ self.__get_random_char(alpha_lower=False, alpha_upper=False, numeric=False) for _ in range(num_special_chars) ]

        password_list = lower_alpha_chars + upper_alpha_chars + numeric_chars + special_chars

        for _ in range(length // 2):
            secrets.SystemRandom().shuffle(password_list)

        return ''.join(password_list)
    

    def get_token(self, bytes, url_safe=False):
        # Returns a hex token of nbytes. If "url_safe" is True, the token will be safe for use in a URL.
        import secrets

        if url_safe:
            return secrets.token_urlsafe(bytes)
        else: 
            return secrets.token_hex(bytes)
