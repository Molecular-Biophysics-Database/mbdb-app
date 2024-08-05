import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.validate import OneOf
from oarepo_requests.services.ui_schema import UIRequestsSerializationMixin
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import InvenioUISchema, LocalizedDate
from oarepo_vocabularies.services.ui_schema import VocabularyI18nStrUIField


class BliUISchema(UIRequestsSerializationMixin, InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    collected_default_search_fields = ma_fields.String()

    metadata = ma_fields.Nested(lambda: BliMetadataUISchema())


class BliMetadataUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    general_parameters = ma_fields.Nested(
        lambda: GeneralParametersUISchema(), required=True
    )

    method_specific_parameters = ma_fields.Nested(
        lambda: MethodSpecificParametersUISchema(), required=True
    )


class GeneralParametersUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    associated_publication = ma_fields.Nested(lambda: AssociatedPublicationUISchema())

    chemical_environments = ma_fields.List(
        ma_fields.Nested(lambda: ChemicalEnvironmentsItemUISchema()), required=True
    )

    collection_start_time = LocalizedDate(required=True)

    depositors = ma_fields.Nested(lambda: DepositorsUISchema(), required=True)

    entities_of_interest = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesOfInterestItemUISchema()), required=True
    )

    funding_references = ma_fields.List(
        ma_fields.Nested(lambda: FundingReferencesItemUISchema())
    )

    instrument = ma_fields.Nested(lambda: InstrumentUISchema(), required=True)

    record_information = ma_fields.Nested(
        lambda: RecordInformationUISchema(), required=True
    )

    results = ma_fields.List(ma_fields.Nested(lambda: ResultsItemUISchema()))

    schema_version = ma_fields.String(required=True, validate=[OneOf(["0.9.24"])])

    technique = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Bio-layer interferometry (BLI)",
                    "Microscale thermophoresis/Temperature related intensity change (MST/TRIC)",
                    "Surface plasmon resonance (SPR)",
                    "Isothermal Titration Calorimetry (ITC)",
                ]
            )
        ],
    )


class ChemicalEnvironmentsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    constituents = ma_fields.List(ma_fields.Nested(lambda: ConstituentsItemUISchema()))

    name = ma_fields.String(required=True)

    ph = ma_fields.Float(required=True)

    solvent = ma_fields.List(
        ma_fields.Nested(lambda: SolventItemUISchema()), required=True
    )


class Complex_substance_of_chemical_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    assembly_type = ma_fields.String(
        required=True, validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet"])]
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    size = ma_fields.Nested(lambda: SizeUISchema())

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Complex_substance_of_chemical_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    assembly_type = ma_fields.String(
        required=True, validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet"])]
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    size = ma_fields.Nested(lambda: SizeUISchema())

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class ConstituentsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    assembly_type = ma_fields.String(
        required=True, validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet"])]
    )

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    capsid_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    cell_type = ma_fields.String()

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                ]
            )
        ],
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Ribosome",
                    "Cell wall",
                    "VesicleCell lysate/Cytoplasm",
                    "Cell Membrane",
                    "Extracellular matrix",
                    "Lysosome",
                    "Golgi Apparatus",
                    "Mitochondrion",
                    "Nucleus",
                    "Rough Endoplasmic Reticulum",
                    "Smooth Endoplasmic Reticulum",
                    "Vacuole",
                    "Chloroplast",
                ]
            )
        ],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    location = ma_fields.Nested(lambda: LocationUISchema(), required=True)

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer()

    organ = ma_fields.String()

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                ]
            )
        ],
    )

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey"])]
    )

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    sequence = ma_fields.String()

    size = ma_fields.Nested(lambda: SizeUISchema())

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf(["Fresh water", "Marine", "Ice core", "Sediment", "Sewage", "Soil"])
        ],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )

    variant = ma_fields.String()


class EntitiesOfInterestItemComplex_substance_of_chemical_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    assembly_type = ma_fields.String(
        required=True, validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet"])]
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    size = ma_fields.Nested(lambda: SizeUISchema())

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_chemical_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    assembly_type = ma_fields.String(
        required=True, validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet"])]
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    size = ma_fields.Nested(lambda: SizeUISchema())

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemMolecular_assemblyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    external_databases = ma_fields.List(ma_fields.String())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    assembly_type = ma_fields.String(
        required=True, validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet"])]
    )

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    capsid_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    cell_type = ma_fields.String()

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                ]
            )
        ],
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Ribosome",
                    "Cell wall",
                    "VesicleCell lysate/Cytoplasm",
                    "Cell Membrane",
                    "Extracellular matrix",
                    "Lysosome",
                    "Golgi Apparatus",
                    "Mitochondrion",
                    "Nucleus",
                    "Rough Endoplasmic Reticulum",
                    "Smooth Endoplasmic Reticulum",
                    "Vacuole",
                    "Chloroplast",
                ]
            )
        ],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    location = ma_fields.Nested(lambda: LocationUISchema(), required=True)

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer()

    organ = ma_fields.String()

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                ]
            )
        ],
    )

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey"])]
    )

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    sequence = ma_fields.String()

    size = ma_fields.Nested(lambda: SizeUISchema())

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf(["Fresh water", "Marine", "Ice core", "Sediment", "Sewage", "Soil"])
        ],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )

    variant = ma_fields.String()


class Molecular_assemblyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema()), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    external_databases = ma_fields.List(ma_fields.String())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class ComponentsItemPolymerUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    copy_number = ma_fields.Float(required=True)

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                ]
            )
        ],
    )

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])

    variant = ma_fields.String()


class ComponentsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    copy_number = ma_fields.Float(required=True)

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                ]
            )
        ],
    )

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])

    variant = ma_fields.String()


class EntitiesOfInterestItemPolymerUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                ]
            )
        ],
    )

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )

    variant = ma_fields.String()


class MethodSpecificParametersUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    data_analysis = ma_fields.List(ma_fields.Nested(lambda: DataAnalysisItemUISchema()))

    experiment_type = ma_fields.String(
        required=True, validate=[OneOf(["Affinity", "Quantification", "Other"])]
    )

    measurement_protocol = ma_fields.List(
        ma_fields.Nested(lambda: MeasurementProtocolItemUISchema()), required=True
    )

    measurements = ma_fields.List(
        ma_fields.Nested(lambda: MeasurementsItemUISchema()), required=True
    )

    plates = ma_fields.List(
        ma_fields.Nested(lambda: PlatesItemUISchema()), required=True
    )

    schema_version = ma_fields.String(required=True, validate=[OneOf(["0.9.7"])])

    sensors = ma_fields.List(
        ma_fields.Nested(lambda: SensorsItemUISchema()), required=True
    )


class PolymerUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                ]
            )
        ],
    )

    quality_controls = ma_fields.Nested(lambda: QualityControlsUISchema())

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )

    variant = ma_fields.String()


class MeasurementsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    measurement_protocol_step = ma_fields.Nested(
        lambda: EntityUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    sample = ma_fields.Nested(lambda: SampleUISchema(), required=True)

    sensor = ma_fields.Nested(lambda: EntityUISchema(), required=True)


class QualityControlsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    homogeneity = ma_fields.Nested(lambda: HomogeneityUISchema())

    identity = ma_fields.Nested(lambda: IdentityUISchema())

    purity = ma_fields.Nested(lambda: PurityUISchema())


class Association_rate_kOnUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "M^-1 s^-1",
                    "M^-2 s^-1",
                    "mM^-1 s^-1",
                    "mM^-2 s^-1",
                    "µM^-1 s^-1",
                    "µM^-2 s^-1",
                    "nM^-1 s^-1",
                    "nM^-2 s^-1",
                ]
            )
        ],
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class Body_fluidUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                ]
            )
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Cell_fractionUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    cell_type = ma_fields.String()

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Ribosome",
                    "Cell wall",
                    "VesicleCell lysate/Cytoplasm",
                    "Cell Membrane",
                    "Extracellular matrix",
                    "Lysosome",
                    "Golgi Apparatus",
                    "Mitochondrion",
                    "Nucleus",
                    "Rough Endoplasmic Reticulum",
                    "Smooth Endoplasmic Reticulum",
                    "Vacuole",
                    "Chloroplast",
                ]
            )
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Change_in_enthalpy_deltaHUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["kcal/mol", "kJ/mol"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class Change_in_entropy_deltaSUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["kcal/molK", "kJ/molK"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class ChemicalUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originBody_fluidUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                ]
            )
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originCell_fractionUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    cell_type = ma_fields.String()

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Ribosome",
                    "Cell wall",
                    "VesicleCell lysate/Cytoplasm",
                    "Cell Membrane",
                    "Extracellular matrix",
                    "Lysosome",
                    "Golgi Apparatus",
                    "Mitochondrion",
                    "Nucleus",
                    "Rough Endoplasmic Reticulum",
                    "Smooth Endoplasmic Reticulum",
                    "Vacuole",
                    "Chloroplast",
                ]
            )
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    cell_type = ma_fields.String()

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                ]
            )
        ],
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Ribosome",
                    "Cell wall",
                    "VesicleCell lysate/Cytoplasm",
                    "Cell Membrane",
                    "Extracellular matrix",
                    "Lysosome",
                    "Golgi Apparatus",
                    "Mitochondrion",
                    "Nucleus",
                    "Rough Endoplasmic Reticulum",
                    "Smooth Endoplasmic Reticulum",
                    "Vacuole",
                    "Chloroplast",
                ]
            )
        ],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originVirionUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic"])],
    )

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Complex_substance_of_environmental_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    location = ma_fields.Nested(lambda: LocationUISchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf(["Fresh water", "Marine", "Ice core", "Sediment", "Sewage", "Soil"])
        ],
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class Complex_substance_of_industrial_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey"])]
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class ComponentsItemChemicalUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    copy_number = ma_fields.Float(required=True)

    name = ma_fields.String(required=True)

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])


class Constant_of_association_KAUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                ["M^-1", "M^-2", "mM^-1", "mM^-2", "µM^-1", "µM^-2", "nM^-1", "nM^-2"]
            )
        ],
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class Constant_of_dissociation_KDUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(
        required=True,
        validate=[OneOf(["M", "M^2", "mM", "mM^2", "µM", "µM^2", "nM", "nM^2"])],
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class DepositorsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemUISchema()))

    depositor = ma_fields.Nested(lambda: ContributorsItemUISchema(), required=True)

    principal_contact = ma_fields.Nested(
        lambda: ContributorsItemUISchema(), required=True
    )


class Dissociation_rate_kOffUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["s^-1"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class EntitiesOfInterestItemChemicalUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_biological_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    cell_type = ma_fields.String()

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                ]
            )
        ],
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Ribosome",
                    "Cell wall",
                    "VesicleCell lysate/Cytoplasm",
                    "Cell Membrane",
                    "Extracellular matrix",
                    "Lysosome",
                    "Golgi Apparatus",
                    "Mitochondrion",
                    "Nucleus",
                    "Rough Endoplasmic Reticulum",
                    "Smooth Endoplasmic Reticulum",
                    "Vacuole",
                    "Chloroplast",
                ]
            )
        ],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_environmental_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    location = ma_fields.Nested(lambda: LocationUISchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf(["Fresh water", "Marine", "Ice core", "Sediment", "Sewage", "Soil"])
        ],
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_industrial_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey"])]
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class IdentityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    by_fingerprinting = ma_fields.Nested(lambda: ByFingerprintingUISchema())

    by_intact_mass = ma_fields.Nested(lambda: ByIntactMassUISchema())

    by_sequencing = ma_fields.Nested(lambda: BySequencingUISchema())

    checked = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])


class IdentityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    by_fingerprinting = ma_fields.Nested(lambda: ByFingerprintingUISchema())

    by_intact_mass = ma_fields.Nested(lambda: ByIntactMassUISchema())

    by_sequencing = ma_fields.Nested(lambda: BySequencingUISchema())

    checked = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])


class ModificationsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    biological_postprocessing = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    chemical = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    synthesis = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )


class Molecular_weightUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(
        required=True, validate=[OneOf(["g/mol", "Da", "kDa", "MDa"])]
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class PlatesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    name = ma_fields.String(required=True)

    sealing = ma_fields.String()

    supplier = ma_fields.Nested(lambda: SupplierUISchema(), required=True)

    surface_modification = ma_fields.Nested(lambda: SurfaceModificationUISchema())

    type = ma_fields.String(required=True)

    wells = ma_fields.String(required=True, validate=[OneOf(["96", "384"])])


class ResultsItemConcentrationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "M",
                    "mM",
                    "µM",
                    "nM",
                    "pM",
                    "fM",
                    "aM",
                    "g/L",
                    "mg/mL",
                    "µg/mL",
                    "ng/mL",
                    "mol/kg",
                    "mmol/kg",
                    "v/v %",
                    "w/w %",
                    "v/w %",
                    "w/v %",
                    "U/ml",
                    "% saturated",
                ]
            )
        ],
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class ResultsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["unitless"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class ResultsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["unitless"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class SampleUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    analytes = ma_fields.List(ma_fields.Nested(lambda: AnalytesItemUISchema()))

    chemical_environment = ma_fields.Nested(lambda: EntityUISchema(), required=True)

    plate = ma_fields.Nested(lambda: EntityUISchema(), required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema())
    )

    temperature = ma_fields.Nested(lambda: TemperatureUISchema())

    well_position = ma_fields.String(required=True)


class SensorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    hydration_time = ma_fields.Nested(lambda: DurationUISchema())

    ligand = ma_fields.Nested(lambda: LigandUISchema())

    name = ma_fields.String(required=True)

    previously_used = ma_fields.Boolean()

    sensor_id = ma_fields.String()

    supplier = ma_fields.Nested(lambda: SupplierUISchema(), required=True)

    surface_properties = ma_fields.String()


class SolventItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma_fields.String(required=True)

    type = ma_fields.String(required=True, validate=[OneOf(["Chemical"])])


class SolventItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    basic_information = ma_fields.Nested(
        lambda: BasicInformationUISchema(), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma_fields.String(required=True)

    type = ma_fields.String(required=True, validate=[OneOf(["Chemical"])])


class StoichiometryUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Concentration",
                    "Stoichiometry",
                    "Constant of association KA",
                    "Constant of dissociation KD",
                    "Half maximal effective concentration EC50",
                    "Hill coefficient",
                    "Association rate kOn",
                    "Dissociation rate kOff",
                    "Change in enthalpy deltaH",
                    "Change in entropy deltaS",
                    "Change in Gibbs free energy deltaG",
                    "Molecular weight",
                ]
            )
        ],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["per complex"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class VirionUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic"])],
    )

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUISchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial origin",
                ]
            )
        ],
    )


class AnalytesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    entity = ma_fields.Nested(lambda: EntityUISchema(), required=True)


class BasicInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    additional_identifiers = ma_fields.List(ma_fields.String())

    chemical_formula = ma_fields.String()

    molecular_weight = ma_fields.Nested(
        lambda: BasicInformationMolecularWeightUISchema()
    )

    title = VocabularyI18nStrUIField()


class BiologicalPostprocessingItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    position = ma_fields.String()

    protocol = ma_fields.List(ma_fields.Nested(lambda: ProtocolItemUISchema()))

    type = ma_fields.String(required=True)


class ByIntactMassUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    deviation_from_expected_mass = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    method = ma_fields.String(
        required=True, validate=[OneOf(["Mass spectrometry", "SDS-PAGE"])]
    )


class ContributorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(ma_fields.Nested(lambda: AffiliationsItemUISchema()))

    family_name = ma_fields.String(required=True)

    given_name = ma_fields.String(required=True)

    identifiers = ma_fields.List(ma_fields.String())


class DataAnalysisItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma_fields.Nested(lambda: DataFittingUISchema())

    data_processing = ma_fields.List(
        ma_fields.Nested(lambda: DataProcessingItemUISchema())
    )

    measurements = ma_fields.List(ma_fields.Nested(lambda: EntityUISchema()))

    results = ma_fields.List(ma_fields.Nested(lambda: EntityUISchema()))


class EntitiesInvolvedItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    copy_number = ma_fields.Float(required=True)

    entity = ma_fields.Nested(lambda: EntityUISchema(), required=True)


class LigandUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    entity = ma_fields.Nested(lambda: EntityUISchema())

    immobilization_chemistry = ma_fields.String()

    immobilization_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema())
    )


class MeasurementProtocolItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    name = ma_fields.String(required=True)

    shaking_speed = ma_fields.Nested(lambda: ShakingSpeedUISchema(), required=True)

    start_time = ma_fields.Nested(lambda: DurationUISchema(), required=True)

    time_length = ma_fields.Nested(lambda: DurationUISchema(), required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Association",
                    "Baseline",
                    "Dissociation",
                    "Regeneration",
                    "Load",
                    "Wash",
                    "Activation",
                ]
            )
        ],
    )


class StorageUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    duration = ma_fields.Nested(lambda: DurationUISchema())

    storage_preparation = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema())
    )

    temperature = ma_fields.Nested(lambda: TemperatureUISchema(), required=True)


class SurfaceModificationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemUISchema()), required=True
    )

    type = ma_fields.String()


class AffiliationsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    city = ma_fields.String()

    country = ma_fields.String()

    state = ma_fields.String()

    title = VocabularyI18nStrUIField()


class ArticleUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    journal = ma_fields.String(required=True)

    pid = ma_fields.String(required=True)

    title = ma_fields.String()

    type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )


class AssociatedPublicationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    degree_type = ma_fields.String(
        required=True, validate=[OneOf(["PhD", "Habilitation", "Master", "Bachelor"])]
    )

    journal = ma_fields.String(required=True)

    pid = ma_fields.String(required=True)

    publisher = ma_fields.String(required=True)

    title = ma_fields.String()

    type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )


class BasicInformationMolecularWeightUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String()

    value = ma_fields.Float()


class BookUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    pid = ma_fields.String(required=True)

    publisher = ma_fields.String(required=True)

    title = ma_fields.String()

    type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )


class ByFingerprintingUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    method = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Protease digest + Mass spectrometry",
                    "Restriction enzyme digest + Gel electrophoresis",
                ]
            )
        ],
    )


class BySequencingUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    coverage = ma_fields.Float(required=True)

    method = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Mass spectrometry-Mass spectrometry",
                    "Edman degradation",
                    "Sanger sequencing",
                    "Next generation sequencing",
                ]
            )
        ],
    )


class ConcentrationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "M",
                    "mM",
                    "µM",
                    "nM",
                    "pM",
                    "fM",
                    "aM",
                    "g/L",
                    "mg/mL",
                    "µg/mL",
                    "ng/mL",
                    "mol/kg",
                    "mmol/kg",
                    "v/v %",
                    "w/w %",
                    "v/w %",
                    "w/v %",
                    "U/ml",
                    "% saturated",
                ]
            )
        ],
    )

    value = ma_fields.Float(required=True)


class DataFittingUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    model = ma_fields.String(required=True)

    quality = ma_fields.Float()

    quality_type = ma_fields.String(
        validate=[
            OneOf(
                [
                    "R^2",
                    "SEM",
                    "red. Chi^2",
                    "1sigma",
                    "2sigma",
                    "3sigma",
                    "5sigma",
                    "Skewness",
                ]
            )
        ]
    )

    software_name = ma_fields.String()

    software_version = ma_fields.String()


class DataProcessingItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    link_to_source_code = ma_fields.String()

    name = ma_fields.String(required=True)

    software_name = ma_fields.String()

    software_version = ma_fields.String()


class DurationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "nanoseconds",
                    "microseconds",
                    "milliseconds",
                    "seconds",
                    "minutes",
                    "hours",
                    "days",
                    "months",
                    "years",
                ]
            )
        ],
    )

    value = ma_fields.Float(required=True)


class EntityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = ma_fields.String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    name = ma_fields.String(required=True)


class ExpressionOrganismUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    rank = ma_fields.String()

    title = VocabularyI18nStrUIField()


class FundingReferencesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    funder_name = ma_fields.String()

    grant_id = ma_fields.String()

    title = VocabularyI18nStrUIField()


class HomogeneityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    checked = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])

    expected_number_of_species = ma_fields.Integer(required=True)

    method = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Dynamic light scattering",
                    "Size exclusion chromatography",
                    "Native Gel Electrophoresis",
                    "Mass photometry",
                ]
            )
        ],
    )

    number_of_species_observed = ma_fields.Integer(required=True)


class HomogeneityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    checked = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])

    expected_number_of_species = ma_fields.Integer(required=True)

    method = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Dynamic light scattering",
                    "Size exclusion chromatography",
                    "Native Gel Electrophoresis",
                    "Mass photometry",
                ]
            )
        ],
    )

    number_of_species_observed = ma_fields.Integer(required=True)


class InstrumentUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    manufacturer = ma_fields.String()

    title = VocabularyI18nStrUIField()


class LocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float(required=True)

    longitude = ma_fields.Float(required=True)


class MolecularWeightUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True, validate=[OneOf(["g/mol", "Da", "kDa", "MDa"])]
    )

    value = ma_fields.Float(required=True)


class NoUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    checked = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])


class ProtocolItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    name = ma_fields.String(required=True)


class PurityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    checked = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])

    method = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                ["SDS-PAGE", "Capillary Electrophoresis", "Agarose Gel electrophoresis"]
            )
        ],
    )

    purity_percentage = ma_fields.String(
        required=True, validate=[OneOf(["<90 %", ">90 %", ">95 %", ">99 %"])]
    )


class PurityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    checked = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])

    method = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                ["SDS-PAGE", "Capillary Electrophoresis", "Agarose Gel electrophoresis"]
            )
        ],
    )

    purity_percentage = ma_fields.String(
        required=True, validate=[OneOf(["<90 %", ">90 %", ">95 %", ">99 %"])]
    )


class RecordInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    access_rights = ma_fields.String(
        required=True,
        validate=[OneOf(["open access", "embargoed access", "restricted access"])],
    )

    date_available = LocalizedDate()

    deposition_date = LocalizedDate(required=True)

    external_identifier = ma_fields.String()

    metadata_access_rights = ma_fields.String(
        required=True,
        validate=[OneOf(["open access", "embargoed access", "restricted access"])],
    )

    publisher = ma_fields.String(required=True, validate=[OneOf(["MBDB"])])

    resource_type = ma_fields.String(required=True)

    resource_type_general = ma_fields.String(
        required=True, validate=[OneOf(["Dataset"])]
    )

    subject_category = ma_fields.String(required=True, validate=[OneOf(["Biophysics"])])

    title = ma_fields.String(required=True)


class ShakingSpeedUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(required=True, validate=[OneOf(["RPM"])])

    value = ma_fields.Integer(required=True)


class SizeUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    lower = ma_fields.Float()

    mean = ma_fields.Float(required=True)

    median = ma_fields.Float()

    type = ma_fields.String(
        required=True, validate=[OneOf(["radius", "diameter", "path length"])]
    )

    unit = ma_fields.String(
        required=True, validate=[OneOf(["Å", "nm", "μm", "mm", "cm", "m"])]
    )

    upper = ma_fields.Float()


class SupplierUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    catalog_number = ma_fields.String()

    further_information = ma_fields.List(ma_fields.String())

    name = ma_fields.String(required=True)


class TemperatureUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(required=True, validate=[OneOf(["K", "°C", "°F"])])

    value = ma_fields.Float(required=True)


class ThesisUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    degree_type = ma_fields.String(
        required=True, validate=[OneOf(["PhD", "Habilitation", "Master", "Bachelor"])]
    )

    pid = ma_fields.String(required=True)

    title = ma_fields.String()

    type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )


class ValueErrorUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    is_relative = ma_fields.Boolean(required=True)

    lower = ma_fields.Float(required=True)

    upper = ma_fields.Float(required=True)
