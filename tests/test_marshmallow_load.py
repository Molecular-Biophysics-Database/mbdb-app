from invenio_app.factory import create_api
import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from mst.services.records.schema import EntitiesOfInterestItemSchema
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema


class GPS(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    entities_of_interest = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesOfInterestItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


def run_marshmallow_test():
    schema = GPS()
    data = schema.load({
        "entities_of_interest": entities,
    })
    assert isinstance(data['entities_of_interest'], list)
    assert len(data['entities_of_interest']) == 2
    assert isinstance(data['entities_of_interest'][0], dict)
    assert isinstance(data['entities_of_interest'][1], dict)


entities = [
{
            "id": "eoi-human-serum",
            "name": "Human serum",
            "type": "Complex substance of biological origin",
            "derived_from": "Body fluid",
            "fluid": "Serum",
            "health_status": "Healthy",
            "source_organism": {
              "id": "taxid:12374"
            },
            "additional_specifications": [
              "Blood was drawn after 12 hours of fasting"
            ],
            "preparation_protocol": [
              {
                "name": "Centrifugation",
                "description": "Tubes were centrifuged for 10 min at 1,300g at 4°C within 2 hours of collection"
              },
              {
                "name": "Aliquotation",
                "description": "The supernatant was distributed among 0.5mL cryostorage tubes that were maintained at 4°C"
              }
            ],
            "storage": {
              "temperature": {
                "value": -80,
                "unit": "°C",
              },
              "storage_preparation": [
                {
                  "name": "Flash freezing in liquid nitrogen",
                  "description": "Aliquotes were placed in liquid nitrogen for 5 min"
                }
              ]
            }
          },
          {
            "id": "eoi-human-hemoglobin",
            "name": "human Hemoglobin",
            "type": "Molecular assembly",
            "external_databases": [
              "pdb:2HCO"
            ],
            "quality_controls": {
              "purity": {
                "checked": "Yes",
                "method": "SDS-PAGE",
                "purity_percentage": ">99 %"
              },
              "homogeneity": {
                "checked": "No"
              }
            },
            "molecular_weight": {
              "value": 64.5,
              "unit": "kDa"
            },
            "components": [
              {
                "name": "Hemoglobin subunit alpha",
                "type": "Polymer",
                "molecular_weight": {
                  "value": 16,
                  "unit": "kDa"
                },
                "copy_number": 2,
                "polymer_type": "polypeptide(L)",
                "source_organism": {
                  "id": "taxid:12374"
                },
                "variant": "WT",
                "expression_source_type": "Natively",
                "external_databases": [
                  "Uniprot:P69905"
                ]
              },
              {
                "name": "Hemoglobin subunit beta",
                "type": "Polymer",
                "molecular_weight": {
                  "value": 16,
                  "unit": "kDa"
                },
                "copy_number": 2,
                "polymer_type": "polypeptide(L)",
                "source_organism": {
                  "id": "taxid:12374"
                },
                "variant": "V2A",
                "modifications": {
                  "biological_postprocessing": [
                    {
                      "position": "S10",
                      "type": "Phosphorylation"
                    }
                  ],
                  "chemical": [
                    {
                      "type": "FITC labelling",
                      "protocol": [
                        {
                          "name": "Make the solution more alkaline",
                          "description": "Addition of 10 ul 1 M bicarbonate to 90 ul protein solution"
                        },
                        {
                          "name": "Solubilise NHS-FITC",
                          "description": "100 % DMSO was added to make a 2 mM concentrated stock of NHS-FITC"
                        },
                        {
                          "name": "Labelling reaction",
                          "description": "Added NHS-FITC stock to protein in a 5:1 molar ratio and incubated sample for 15 min."
                        },
                        {
                          "name": "Removal of unconjugated dye",
                          "description": "Using a 2 ml PD10 column, the unconjugated dye was removed"
                        }
                      ]
                    }
                  ]
                },
                "sequence": "MAHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH",
                "expression_source_type": "Recombinantly",
                "external_databases": [
                  "Uniprot:P68871"
                ]
              }
            ]
          }
]

if __name__ == '__main__':
    api = create_api()
    with api.app_context():
        run_marshmallow_test()