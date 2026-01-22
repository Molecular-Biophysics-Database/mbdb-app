# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""CSL based Schema for Invenio RDM Records."""

from edtf import parse_edtf
from edtf.parser.edtf_exceptions import EDTFParseException
from edtf.parser.parser_classes import Date, Interval
from marshmallow import Schema, fields, missing
from marshmallow_utils.fields import SanitizedUnicode


class CSLCreatorSchema(Schema):
    """Creator/contributor common schema."""
    given = fields.Str(attribute="given_name", missing=None)
    family = fields.Str(attribute="family_name", missing=None)
    literal = fields.Method("get_literal")

    def get_literal(self, obj):
        family = obj.get("family_name")
        given = obj.get("given_name")
        if family and given:
            return f"{family}, {given}"
        return family or given or missing


def add_if_not_none(year, month, day):
    """Adds year, month a day to a list if each are not None."""
    _list = []
    _list.append(year) if year else None
    _list.append(month) if month else None
    _list.append(day) if day else None
    return _list


def map_resource_type_to_csl(resource_type):
    mapping = {
        "Annual report": "report",
        "Article": "article",
        "Article - accepted version": "article",
        "Article - corrected version": "article",
        "Article - draft": "article",
        "Article - published version": "article",
        "Article - submitted version": "article",
        "Article - updated version": "article",
        "Book": "book",
        "Book chapter": "chapter",
        "Business trip report": "report",
        "Cartographic material": "map",
        "Certified methodology": "article",
        "Conference paper": "paper-conference",
        "Conference poster": "graphic",
        "Conference presentation": "paper-conference",
        "Conference proceeding": "chapter",
        "Conference programme": "pamphlet",
        "Conservation report": "report",
        "Dataset": "dataset",
        "Educational material": "pamphlet",
        "Exhibition catalogue or guide": "pamphlet",
        "Field report": "report",
        "Heritage procedure": "legislation",
        "Methodology without certification": "manuscript",
        "Other": "webpage",
        "Press release": "article-newspaper",
        "Project report": "report",
        "Research report": "report",
        "Review": "review",
        "Specialized map": "map",
        "Statistical or status report": "report",
        "Studies and analyses": "manuscript",
        "Trade literature": "pamphlet",
        "Treatment procedure": "legislation",
    }

    return mapping.get(resource_type, "article")


class CSLJSONSchema(Schema):
    """CSL Marshmallow Schema."""

    id_ = SanitizedUnicode(data_key="id", attribute="id")
    type = fields.Method("get_resource_type")
    title = fields.Method("get_title")
    abstract = fields.Method("get_abstract")
    author = fields.List(
        fields.Nested(CSLCreatorSchema()), attribute="metadata.creators"
    )
    issued = fields.Method("get_issued")
    language = fields.Method("get_language")
    version = SanitizedUnicode(attribute="metadata.version")
    publisher = fields.Method("get_publisher")
    URL = fields.Method("get_url")

    def get_title(self, obj):
        """Get title."""
        metadata = obj["metadata"]
        title = (metadata.
                 get("general_parameters", {})
                 .get("record_information", {})
                 .get("title", ""))
        sanitized = SanitizedUnicode()._deserialize(
            title, None, None
        )
        return sanitized

    def get_publisher(self, obj):
        """Get publisher."""
        metadata = obj["metadata"]
        publisher = (metadata
                     .get("general_parameters", {})
                     .get("record_information", {})
                     .get("publisher", ""))
        sanitized = SanitizedUnicode()._deserialize(
            publisher, None, None
        )
        return sanitized if sanitized else missing

    def get_abstract(self, obj):
        """Get abstract."""
        abstract = obj["metadata"].get("abstract", [])
        return (
            {
                entry["lang"]: {"value": entry["value"]}
                for entry in abstract
                if "lang" in entry and "value" in entry
            }
            if abstract
            else missing
        )

    def get_resource_type(self, obj):
        """Map our resource type to CSL"""
        metadata = obj["metadata"]
        resource_type = (metadata.get("general_parameters", {})
                         .get("record_information", {})
                         .get("resource_type_general", ""))

        return map_resource_type_to_csl(resource_type)

    def get_issued(self, obj):
        """Get issued dates."""
        try:
            metadata = obj["metadata"]
            date_issued = (metadata.get("general_parameters", {})
                         .get("record_information", {})
                         .get("deposition_date", ""))
            parsed = parse_edtf(date_issued)
        except EDTFParseException:
            return missing
        except StopIteration:
            return missing

        if isinstance(parsed, Date):
            parts = add_if_not_none(parsed.year, parsed.month, parsed.day)
            return {"date-parts": [parts]}
        elif isinstance(parsed, Interval):
            d1 = parsed.lower
            d2 = parsed.upper
            return {
                "date-parts": [
                    add_if_not_none(d1.year, d1.month, d1.day),
                    add_if_not_none(d2.year, d2.month, d2.day),
                ]
            }
        else:
            return missing

    def get_language(self, obj):
        """Get language."""
        metadata = obj["metadata"]
        languages = metadata.get("languages", "")

        if languages:
            language_id = languages[0].get("id")
            return language_id

        return missing

    def get_url(self, obj):
        """Get URL."""
        metadata = obj["metadata"]
        object_ids = metadata.get("pids", {})
        doi = next(
            (o["identifier"] for o in object_ids if o["scheme"].lower() == "doi"), None
        )
        url = None
        if doi:
            url = f"https://doi.org/{doi}"
        else:
            url = next(
                (
                    o["url"]
                    for o in object_ids
                    if o["scheme"].lower() != "doi" and o.get("url")
                ),
                None,
            )
        return url if url else missing