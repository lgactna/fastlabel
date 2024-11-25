class A:
    # have constant with dumped out python stuff (replace posixpath and windowspath with generics)
    #
    # for artifact groups, i think that's the one case where we'd have to deal
    # with the whole import/dependency thing, but that should be fairly easy since
    # we're assuming a flat library layout at a known position
    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                ]
            },
        }
    ]

    # then just validate as a list according to
    # https://stackoverflow.com/questions/58068001/python-pydantic-using-a-list-with-json-objects
    sources = ...
