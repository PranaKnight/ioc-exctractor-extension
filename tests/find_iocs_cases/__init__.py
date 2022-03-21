from .asns import ASN_DATA
from .cves import CVE_DATA
from .domains import DOMAIN_DATA
from .email import EMAIL_DATA
from .hashes import HASH_DATA
from .ip_addr import IP_DATA
from .tlp_labels import TLP_DATA
from .attack_data import ATTACK_DATA
from .registry_keys import REGISTRY_DATA
from .file_paths import PATH_DATA
from .ids import ID_DATA
from .coins import COIN_DATA
from .mac_addr import MAC_DATA
from .user_agents import UA_DATA

cases = [
    TLP_DATA,
    DOMAIN_DATA,
    EMAIL_DATA,
    HASH_DATA,
    CVE_DATA,
    IP_DATA,
    ASN_DATA,
    ATTACK_DATA,
    REGISTRY_DATA,
    PATH_DATA,
    ID_DATA,
    COIN_DATA,
    MAC_DATA,
    UA_DATA,
]

ALL_TESTS = [val for sublist in cases for val in sublist]
