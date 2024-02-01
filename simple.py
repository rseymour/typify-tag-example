import json
from enum import Enum

from typing import Annotated, Union, Literal, List

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class FooBar(BaseModel):
    my_type: Literal['FooBar'] = 'FooBar'
    count: int
    size: float | None = None


class Baz(BaseModel):
    my_type: Literal['Baz'] = 'Baz'
    count: int
    size: float | None = None


DemItems = Annotated[Union[FooBar,Baz],Field(..., discriminator='my_type')]

class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    fbz: List[DemItems]


main_model_schema = MainModel.model_json_schema()  # (1)!
print(json.dumps(main_model_schema, indent=2))  # (2)!

