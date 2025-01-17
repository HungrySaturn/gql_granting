import strawberry
import typing
import datetime
import uuid
import logging

from utils.Dataloaders import getLoadersFromInfo, getUserFromInfo
from .BaseGQLModel import BaseGQLModel


from GraphTypeDefinitions._GraphResolvers import (
    resolve_id,
    resolve_name,
    resolve_name_en,
    resolve_changedby,
    resolve_created,
    resolve_lastchange,
    resolve_createdby,
    resolve_rbacobject,
    createRootResolver_by_id,
)
from ._GraphPermissions import RoleBasedPermission, OnlyForAuthentized

@strawberry.federation.type(
    keys=["id"],
    description="Study program language")
class AcProgramLanguageTypeGQLModel(BaseGQLModel):
    @classmethod
    def getLoader(cls, info):
        loader = getLoadersFromInfo(info).programlanguages
        return loader

    id = resolve_id
    name = resolve_name
    name_en = resolve_name_en
    lastchange = resolve_lastchange
    
#################################################
# Query
#################################################

@strawberry.field(
    description="""Finds a program language its id""",
    permission_classes=[OnlyForAuthentized()])
async def program_language_by_id(
        self, info: strawberry.types.Info, id:uuid.UUID
    ) -> typing.Optional[AcProgramLanguageTypeGQLModel]:
        result = await AcProgramLanguageTypeGQLModel.resolve_reference(info, id)
        return result

