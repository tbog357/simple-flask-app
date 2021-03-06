from dataclasses import dataclass, fields


@dataclass
class ModelBase:
    @classmethod
    def __init_from_dict__(cls, input_data_dict: dict):
        result_dict = {}
        model_fields = {field_cls.name: field_cls.type for field_cls in fields(cls)}
        for key, value in input_data_dict.items():
            if key in model_fields:
                result_dict[key] = value
        return cls(**result_dict)

    def to_dict(self, skip_none_value=True):
        return {key: value for key, value in self.__dict__.items() if (not (value is None and skip_none_value))}
