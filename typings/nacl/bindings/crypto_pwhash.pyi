"""
This type stub file was generated by pyright.
"""

has_crypto_pwhash_scryptsalsa208sha256 = ...
crypto_pwhash_scryptsalsa208sha256_STRPREFIX = ...
crypto_pwhash_scryptsalsa208sha256_SALTBYTES = ...
crypto_pwhash_scryptsalsa208sha256_STRBYTES = ...
crypto_pwhash_scryptsalsa208sha256_PASSWD_MIN = ...
crypto_pwhash_scryptsalsa208sha256_PASSWD_MAX = ...
crypto_pwhash_scryptsalsa208sha256_BYTES_MIN = ...
crypto_pwhash_scryptsalsa208sha256_BYTES_MAX = ...
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MIN = ...
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MAX = ...
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MIN = ...
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MAX = ...
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_INTERACTIVE = ...
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_INTERACTIVE = ...
crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_SENSITIVE = ...
crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_SENSITIVE = ...
if has_crypto_pwhash_scryptsalsa208sha256:
    crypto_pwhash_scryptsalsa208sha256_STRPREFIX = ...
    crypto_pwhash_scryptsalsa208sha256_SALTBYTES = ...
    crypto_pwhash_scryptsalsa208sha256_STRBYTES = ...
    crypto_pwhash_scryptsalsa208sha256_PASSWD_MIN = ...
    crypto_pwhash_scryptsalsa208sha256_PASSWD_MAX = ...
    crypto_pwhash_scryptsalsa208sha256_BYTES_MIN = ...
    crypto_pwhash_scryptsalsa208sha256_BYTES_MAX = ...
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MIN = ...
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_MAX = ...
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MIN = ...
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_MAX = ...
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_INTERACTIVE = ...
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_INTERACTIVE = ...
    crypto_pwhash_scryptsalsa208sha256_OPSLIMIT_SENSITIVE = ...
    crypto_pwhash_scryptsalsa208sha256_MEMLIMIT_SENSITIVE = ...
crypto_pwhash_ALG_ARGON2I13 = ...
crypto_pwhash_ALG_ARGON2ID13 = ...
crypto_pwhash_ALG_DEFAULT = ...
crypto_pwhash_SALTBYTES = ...
crypto_pwhash_STRBYTES = ...
crypto_pwhash_PASSWD_MIN = ...
crypto_pwhash_PASSWD_MAX = ...
crypto_pwhash_BYTES_MIN = ...
crypto_pwhash_BYTES_MAX = ...
crypto_pwhash_argon2i_STRPREFIX = ...
crypto_pwhash_argon2i_MEMLIMIT_MIN = ...
crypto_pwhash_argon2i_MEMLIMIT_MAX = ...
crypto_pwhash_argon2i_OPSLIMIT_MIN = ...
crypto_pwhash_argon2i_OPSLIMIT_MAX = ...
crypto_pwhash_argon2i_OPSLIMIT_INTERACTIVE = ...
crypto_pwhash_argon2i_MEMLIMIT_INTERACTIVE = ...
crypto_pwhash_argon2i_OPSLIMIT_MODERATE = ...
crypto_pwhash_argon2i_MEMLIMIT_MODERATE = ...
crypto_pwhash_argon2i_OPSLIMIT_SENSITIVE = ...
crypto_pwhash_argon2i_MEMLIMIT_SENSITIVE = ...
crypto_pwhash_argon2id_STRPREFIX = ...
crypto_pwhash_argon2id_MEMLIMIT_MIN = ...
crypto_pwhash_argon2id_MEMLIMIT_MAX = ...
crypto_pwhash_argon2id_OPSLIMIT_MIN = ...
crypto_pwhash_argon2id_OPSLIMIT_MAX = ...
crypto_pwhash_argon2id_OPSLIMIT_INTERACTIVE = ...
crypto_pwhash_argon2id_MEMLIMIT_INTERACTIVE = ...
crypto_pwhash_argon2id_OPSLIMIT_MODERATE = ...
crypto_pwhash_argon2id_MEMLIMIT_MODERATE = ...
crypto_pwhash_argon2id_OPSLIMIT_SENSITIVE = ...
crypto_pwhash_argon2id_MEMLIMIT_SENSITIVE = ...
SCRYPT_OPSLIMIT_INTERACTIVE = ...
SCRYPT_MEMLIMIT_INTERACTIVE = ...
SCRYPT_OPSLIMIT_SENSITIVE = ...
SCRYPT_MEMLIMIT_SENSITIVE = ...
SCRYPT_SALTBYTES = ...
SCRYPT_STRBYTES = ...
SCRYPT_PR_MAX = ...
LOG2_UINT64_MAX = ...
UINT64_MAX = ...
SCRYPT_MAX_MEM = ...

def nacl_bindings_pick_scrypt_params(opslimit, memlimit):
    """Python implementation of libsodium's pickparams"""
    ...

def crypto_pwhash_scryptsalsa208sha256_ll(passwd, salt, n, r, p, dklen=..., maxmem=...):
    """
    Derive a cryptographic key using the ``passwd`` and ``salt``
    given as input.

    The work factor can be tuned by by picking different
    values for the parameters

    :param bytes passwd:
    :param bytes salt:
    :param bytes salt: *must* be *exactly* :py:const:`.SALTBYTES` long
    :param int dklen:
    :param int opslimit:
    :param int n:
    :param int r: block size,
    :param int p: the parallelism factor
    :param int maxmem: the maximum available memory available for scrypt's
                       operations
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
    ...

def crypto_pwhash_scryptsalsa208sha256_str(passwd, opslimit=..., memlimit=...):
    """
    Derive a cryptographic key using the ``passwd`` and ``salt``
    given as input, returning a string representation which includes
    the salt and the tuning parameters.

    The returned string can be directly stored as a password hash.

    See :py:func:`.crypto_pwhash_scryptsalsa208sha256` for a short
    discussion about ``opslimit`` and ``memlimit`` values.

    :param bytes passwd:
    :param int opslimit:
    :param int memlimit:
    :return: serialized key hash, including salt and tuning parameters
    :rtype: bytes
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
    ...

def crypto_pwhash_scryptsalsa208sha256_str_verify(passwd_hash, passwd):
    """
    Verifies the ``passwd`` against the ``passwd_hash`` that was generated.
    Returns True or False depending on the success

    :param passwd_hash: bytes
    :param passwd: bytes
    :rtype: boolean
    :raises nacl.exceptions.UnavailableError: If called when using a
        minimal build of libsodium.
    """
    ...

def crypto_pwhash_alg(outlen, passwd, salt, opslimit, memlimit, alg):
    """
    Derive a raw cryptographic key using the ``passwd`` and the ``salt``
    given as input to the ``alg`` algorithm.

    :param outlen: the length of the derived key
    :type outlen: int
    :param passwd: The input password
    :type passwd: bytes
    :param opslimit: computational cost
    :type opslimit: int
    :param memlimit: memory cost
    :type memlimit: int
    :param alg: algorithm identifier
    :type alg: int
    :return: derived key
    :rtype: bytes
    """
    ...

def crypto_pwhash_str_alg(passwd, opslimit, memlimit, alg):
    """
    Derive a cryptographic key using the ``passwd`` given as input
    and a random ``salt``, returning a string representation which
    includes the salt, the tuning parameters and the used algorithm.

    :param passwd: The input password
    :type passwd: bytes
    :param opslimit: computational cost
    :type opslimit: int
    :param memlimit: memory cost
    :type memlimit: int
    :param alg: The algorithm to use
    :type alg: int
    :return: serialized derived key and parameters
    :rtype: bytes
    """
    ...

def crypto_pwhash_str_verify(passwd_hash, passwd):
    """
    Verifies the ``passwd`` against a given password hash.

    Returns True on success, raises InvalidkeyError on failure
    :param passwd_hash: saved password hash
    :type passwd_hash: bytes
    :param passwd: password to be checked
    :type passwd: bytes
    :return: success
    :rtype: boolean
    """
    ...

crypto_pwhash_argon2i_str_verify = ...