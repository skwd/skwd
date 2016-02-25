#
# Print openssl supported TLS version
#

import ssl
for _,name in ssl._PROTOCOL_NAMES.items():
    print(name)

