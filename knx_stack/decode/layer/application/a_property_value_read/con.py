from typing import Iterable
from knx_stack.definition.layer.application.a_property_value_read.con import Msg
from knx_stack.decode.layer.application import a_property_value


def decode(state: 'knx_stack.State', msg: 'knx_stack.Msg') -> Iterable[Msg]:
    property_values = a_property_value.decode(state, msg)
    property_values_read = [Msg(asap=property_value.asap,
                                object_index=property_value.object_index,
                                property_id=property_value.property_id,
                                number_of_elements=property_value.number_of_elements,
                                start_index=property_value.start_index,
                                status=state.ldata.status)
                            for property_value in property_values]
    return property_values_read
