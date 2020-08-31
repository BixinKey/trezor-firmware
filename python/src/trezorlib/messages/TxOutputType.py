# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MultisigRedeemScriptType import MultisigRedeemScriptType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeOutputScriptType = Literal[0, 1, 2, 3, 4, 5]
    except ImportError:
        pass


class TxOutputType(p.MessageType):

    def __init__(
        self,
        address: str = None,
        address_n: List[int] = None,
        amount: int = None,
        script_type: EnumTypeOutputScriptType = None,
        multisig: MultisigRedeemScriptType = None,
        op_return_data: bytes = None,
    ) -> None:
        self.address = address
        self.address_n = address_n if address_n is not None else []
        self.amount = amount
        self.script_type = script_type
        self.multisig = multisig
        self.op_return_data = op_return_data

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address', p.UnicodeType, 0),
            2: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            3: ('amount', p.UVarintType, 0),  # required
            4: ('script_type', p.EnumType("OutputScriptType", (0, 1, 2, 3, 4, 5)), 0),  # required
            5: ('multisig', MultisigRedeemScriptType, 0),
            6: ('op_return_data', p.BytesType, 0),
        }
