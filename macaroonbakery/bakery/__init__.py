# Copyright 2017 Canonical Ltd.
# Licensed under the LGPLv3, see LICENCE file for details.

from .versions import (
    VERSION_0,
    VERSION_1,
    VERSION_2,
    VERSION_3,
    LATEST_VERSION,
)
from .authorizer import (
    ACLAuthorizer,
    Authorizer,
    AuthorizerFunc,
    ClosedAuthorizer,
    EVERYONE,
)
from .codec import (
    decode_caveat,
    encode_caveat,
    encode_uvarint,
)
from .checker import (
    AuthChecker,
    AuthInfo,
    Checker,
    LOGIN_OP,
    Op,
)
from .error import (
    AuthInitError,
    CaveatNotRecognizedError,
    DischargeRequiredError,
    IdentityError,
    PermissionDenied,
    ThirdPartyCaveatCheckFailed,
    ThirdPartyInfoNotFound,
    VerificationError,
)
from .identity import (
    ACLIdentity,
    Identity,
    IdentityClient,
    NoIdentities,
    SimpleIdentity,
)
from .keys import (
    generate_key,
    PrivateKey,
    PublicKey,
)
from .store import (
    MemoryOpsStore,
    MemoryKeyStore,
)
from .third_party import (
    ThirdPartyCaveatInfo,
    ThirdPartyInfo,
    legacy_namespace,
)
from .macaroon import (
    Macaroon,
    MacaroonJSONDecoder,
    MacaroonJSONEncoder,
    ThirdPartyLocator,
    ThirdPartyStore,
    macaroon_version,
)
from .discharge import (
    ThirdPartyCaveatChecker,
    discharge,
    discharge_all,
    local_third_party_caveat,
)
from .oven import (
    Oven,
    canonical_ops,
)
from .bakery import Bakery
from macaroonbakery._utils import (
    b64decode,
    macaroon_to_dict,
)

__all__ = [
    'ACLAuthorizer',
    'ACLIdentity',
    'AuthChecker',
    'AuthInfo',
    'AuthInitError',
    'Authorizer',
    'AuthorizerFunc',
    'VERSION_0',
    'VERSION_1',
    'VERSION_2',
    'VERSION_3',
    'Bakery',
    'CaveatNotRecognizedError',
    'Checker',
    'ClosedAuthorizer',
    'DischargeRequiredError',
    'EVERYONE',
    'Identity',
    'IdentityClient',
    'IdentityError',
    'LATEST_VERSION',
    'LOGIN_OP',
    'Macaroon',
    'MacaroonJSONDecoder',
    'MacaroonJSONEncoder',
    'MemoryKeyStore',
    'MemoryOpsStore',
    'NoIdentities',
    'Op',
    'Oven',
    'PermissionDenied',
    'PrivateKey',
    'PublicKey',
    'SimpleIdentity',
    'ThirdPartyCaveatCheckFailed',
    'ThirdPartyCaveatChecker',
    'ThirdPartyCaveatInfo',
    'ThirdPartyInfo',
    'ThirdPartyInfoNotFound',
    'ThirdPartyLocator',
    'ThirdPartyStore',
    'VERSION',
    'VerificationError',
    'b64decode',
    'canonical_ops',
    'decode_caveat',
    'discharge',
    'discharge_all',
    'encode_caveat',
    'encode_uvarint',
    'generate_key',
    'legacy_namespace',
    'local_third_party_caveat',
    'macaroon_to_dict',
    'macaroon_version',
]
