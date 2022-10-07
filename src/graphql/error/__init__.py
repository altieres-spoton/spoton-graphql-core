"""GraphQL Errors

The :mod:`graphql.error` package is responsible for creating and formatting GraphQL
errors.
"""

from .graphql_error import GraphQLError, GraphQLErrorExtensions, GraphQLFormattedError

from .syntax_error import GraphQLSyntaxError

from .located_error import located_error


def format_error(error: GraphQLError) -> GraphQLFormattedError:
    return GraphQLFormattedError(error).formatted


__all__ = [
    "GraphQLError",
    "GraphQLErrorExtensions",
    "GraphQLFormattedError",
    "GraphQLSyntaxError",
    "located_error",
]
