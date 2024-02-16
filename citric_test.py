from hashlib import sha256

citric_sheep_secret = 'CitricSheep'
if __name__ == "__main__":
        citric_sheep_encode = sha256(
                str(
                        sum(
                                list(
                                        map(
                                                lambda x: ord(x)*int(len(citric_sheep_secret)), [*citric_sheep_secret]
                                        )
                                )
                        )
                ).encode('utf-8')
        ).hexdigest()
        print(citric_sheep_encode)
