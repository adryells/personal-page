import graphene


class BasicOrderEnum(graphene.Enum):
    ALPHABETICAL = "ALPHABETICAL"
    REVERSE_ALPHA = "REVERSE_ALPHA"
    RECENT = "RECENT"
    OLD = "OLD"
