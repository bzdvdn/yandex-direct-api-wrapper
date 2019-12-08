def convert(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def generate_params(fields: list, function_kwargs: dict) -> dict:
    return {convert(field): function_kwargs[field] for field in fields if function_kwargs.get(field)}
