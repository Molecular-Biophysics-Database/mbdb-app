import marshmallow as ma
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as InvenioParentSchema,
)
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.utils import get_value
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.polymorphic import PolymorphicSchema
from oarepo_runtime.services.schema.validation import validate_date


class GeneratedParentSchema(InvenioParentSchema):
    """"""


class MbdbSprSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: MbdbSprMetadataSchema())
    parent = ma.fields.Nested(GeneratedParentSchema)
    files = ma.fields.Nested(
        lambda: FilesOptionsSchema(), load_default={"enabled": True}
    )

    # todo this needs to be generated for [default preview] to work
    def get_attribute(self, obj, attr, default):
        """Override how attributes are retrieved when dumping.

        NOTE: We have to access by attribute because although we are loading
              from an external pure dict, but we are dumping from a data-layer
              object whose fields should be accessed by attributes and not
              keys. Access by key runs into FilesManager key access protection
              and raises.
        """
        if attr == "files":
            return getattr(obj, attr, default)
        else:
            return get_value(obj, attr, default)


class MbdbSprMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    general_parameters = ma_fields.Nested(
        lambda: GeneralParametersSchema(), required=True
    )

    method_specific_parameters = ma_fields.Nested(
        lambda: MethodSpecificParametersSchema(), required=True
    )


class GeneralParametersSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    associated_publications = ma_fields.Nested(lambda: AssociatedPublicationsSchema())

    chemical_information = ma_fields.Nested(
        lambda: ChemicalInformationSchema(), required=True
    )

    collection_start_time = ma_fields.String(
        required=True, validate=[validate_date("%Y-%m-%d")]
    )

    depositors = ma_fields.Nested(lambda: DepositorsSchema(), required=True)

    derived_parameters = ma_fields.List(
        ma_fields.Nested(lambda: DerivedParametersItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    funding_reference = ma_fields.List(
        ma_fields.Nested(lambda: FundingReferenceItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    instrument = ma_fields.Nested(lambda: InstrumentSchema(), required=True)

    physical_conditions_at_sample_handling = ma_fields.Nested(
        lambda: PhysicalConditionsAtSampleHandlingSchema()
    )

    raw_measurements = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    record_information = ma_fields.Nested(
        lambda: RecordInformationSchema(), required=True
    )

    schema_version = ma_fields.String(required=True, validate=[OneOf(["0.9.15"])])

    technique = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Bio-layer interferometry (BLI)",
                (
                    "Microscale thermophoresis/Temperature related intensity change"
                    " (MST/TRIC)"
                ),
                "Surface plasmon resonance (SPR)",
            ])
        ],
    )


class ChemicalInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    chemical_environments = ma_fields.List(
        ma_fields.Nested(lambda: ChemicalEnvironmentsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    entities_of_interest = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesOfInterestItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class InstrumentSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    manufacturer = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Bio-Rad",
                "Bruker",
                "Cytiva",
                "Gatorbio",
                "GE Healthcare",
                "Nanotemper",
                "Nicoya Life",
                "Sartorius",
                "Malvern Panalytical",
                "Refeyn",
                "TA Instruments",
            ])
        ],
    )

    model = ma_fields.String()

    name = ma_fields.String(required=True)

    performance_test = ma_fields.Nested(lambda: PerformanceTestSchema())


class ChemicalEnvironmentsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    constituents = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemSchema(), required=True),
        validate=[ma.validate.Length(min=1)],
    )

    degassing_method = ma_fields.String(
        validate=[OneOf(["Low pressure", "Heating", "Sonication bath"])]
    )

    dynamic_viscosity = ma_fields.Nested(lambda: DynamicViscositySchema())

    ionic_strength = ma_fields.Nested(lambda: IonicStrengthSchema())

    name = ma_fields.String(required=True)

    ph = ma_fields.Nested(lambda: PhSchema(), required=True)

    solvent = ma_fields.List(
        ma_fields.Nested(lambda: SolventItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    ultrafiltration_method = ma_fields.Nested(lambda: UltrafiltrationMethodSchema())


class PerformanceTestSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_information = ma_fields.String()

    published_test_protocol = ma_fields.Nested(lambda: AdditionalItemSchema())

    report = ma_fields.String(required=True)

    sample_composition = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class ConstituentsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(lambda: ChemicalSchema(), required=True)

    Complex_substance_of_biological_origin = ma_fields.Nested(
        lambda: Complex_substance_of_biological_originSchema(),
        required=True,
        data_key="Complex substance of biological origin",
        attribute="Complex substance of biological origin",
    )

    Complex_substance_of_chemical_origin = ma_fields.Nested(
        lambda: Complex_substance_of_chemical_originSchema(),
        required=True,
        data_key="Complex substance of chemical origin",
        attribute="Complex substance of chemical origin",
    )

    Complex_substance_of_environmental_origin = ma_fields.Nested(
        lambda: Complex_substance_of_environmental_originSchema(),
        required=True,
        data_key="Complex substance of environmental origin",
        attribute="Complex substance of environmental origin",
    )

    Complex_substance_of_industrial_production_origin = ma_fields.Nested(
        lambda: Complex_substance_of_industrial_production_originSchema(),
        required=True,
        data_key="Complex substance of industrial production origin",
        attribute="Complex substance of industrial production origin",
    )

    Molecular_assembly = ma_fields.Nested(
        lambda: Molecular_assemblySchema(),
        required=True,
        data_key="Molecular assembly",
        attribute="Molecular assembly",
    )

    Polymer = ma_fields.Nested(lambda: PolymerSchema(), required=True)

    type_field = "type"


class EntitiesOfInterestItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(
        lambda: EntitiesOfInterestItemChemicalSchema(), required=True
    )

    Complex_substance_of_biological_origin = ma_fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_biological_originSchema(),
        required=True,
        data_key="Complex substance of biological origin",
        attribute="Complex substance of biological origin",
    )

    Complex_substance_of_chemical_origin = ma_fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_chemical_originSchema(),
        required=True,
        data_key="Complex substance of chemical origin",
        attribute="Complex substance of chemical origin",
    )

    Complex_substance_of_environmental_origin = ma_fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_environmental_originSchema(),
        required=True,
        data_key="Complex substance of environmental origin",
        attribute="Complex substance of environmental origin",
    )

    Complex_substance_of_industrial_production_origin = ma_fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_industrial_production_originSchema(),
        required=True,
        data_key="Complex substance of industrial production origin",
        attribute="Complex substance of industrial production origin",
    )

    Molecular_assembly = ma_fields.Nested(
        lambda: EntitiesOfInterestItemMolecular_assemblySchema(),
        required=True,
        data_key="Molecular assembly",
        attribute="Molecular assembly",
    )

    Polymer = ma_fields.Nested(
        lambda: EntitiesOfInterestItemPolymerSchema(), required=True
    )

    type_field = "type"


class Complex_substance_of_chemical_originSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid_assembly"])],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    details = ma_fields.Nested(lambda: DetailsSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_chemical_originSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid_assembly"])],
    )

    details = ma_fields.Nested(lambda: DetailsSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class PhysicalConditionsAtSampleHandlingSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    atmosphere = ma_fields.Nested(lambda: AtmosphereSchema())

    humidity = ma_fields.Nested(lambda: HumiditySchema())

    pressure = ma_fields.Nested(lambda: PressureSchema())

    temperature = ma_fields.Nested(lambda: TemperatureSchema())


class AtmosphereSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    composition = ma_fields.List(
        ma_fields.Nested(lambda: SolventItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class DetailsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    number_of_mono_layers = ma_fields.Integer(
        required=True, validate=[ma.validate.Range(min=-1)]
    )

    size = ma_fields.Nested(lambda: SizeSchema(), required=True)

    type = ma_fields.String(
        required=True,
        validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet", "Other"])],
    )


class EntitiesOfInterestItemMolecular_assemblySchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    external_databases = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Molecular_assemblySchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    external_databases = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class ComponentsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(lambda: ComponentsItemChemicalSchema(), required=True)

    Polymer = ma_fields.Nested(lambda: ComponentsItemPolymerSchema(), required=True)

    type_field = "type"


class MethodSpecificParametersSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    data_analysis = ma_fields.List(
        ma_fields.Nested(lambda: DataAnalysisItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    experiment_type = ma_fields.String(
        required=True, validate=[OneOf(["Affinity", "Quantification", "Other"])]
    )

    measurement_positions = ma_fields.List(
        ma_fields.Nested(lambda: MeasurementPositionsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    measurement_protocol = ma_fields.List(
        ma_fields.Nested(lambda: MeasurementProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    measurements = ma_fields.List(
        ma_fields.Nested(lambda: MeasurementsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    schema_version = ma_fields.String(required=True, validate=[OneOf(["0.9.2"])])

    sensor = ma_fields.Nested(lambda: SensorSchema(), required=True)


class SolventItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(lambda: SolventItemChemicalSchema(), required=True)

    type_field = "type"


class ChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Complex_substance_of_biological_originSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Body_fluid = ma_fields.Nested(
        lambda: Body_fluidSchema(),
        required=True,
        data_key="Body fluid",
        attribute="Body fluid",
    )

    Cell_fraction = ma_fields.Nested(
        lambda: Cell_fractionSchema(),
        required=True,
        data_key="Cell fraction",
        attribute="Cell fraction",
    )

    Virion = ma_fields.Nested(lambda: VirionSchema(), required=True)

    type_field = "derived_from"


class ComponentsItemChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    copy_number = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])


class ComponentsItemPolymerSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    copy_number = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    modifications = ma_fields.Nested(lambda: ModificationsSchema())

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "cyclic-pseudo-peptide",
                "peptide nucleic acid",
                "polydeoxyribonucleotide",
                "polydeoxyribonucleotide/polyribonucleotide hybrid",
                "polypeptide(D)",
                "polypeptide(L)",
                "polyribonucleotide",
                "Other",
            ])
        ],
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])

    variant = ma_fields.String()


class EntitiesOfInterestItemChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_identifiers = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_biological_originSchema(
    PolymorphicSchema
):
    class Meta:
        unknown = ma.RAISE

    Body_fluid = ma_fields.Nested(
        lambda: Complex_substance_of_biological_originBody_fluidSchema(),
        required=True,
        data_key="Body fluid",
        attribute="Body fluid",
    )

    Cell_fraction = ma_fields.Nested(
        lambda: Complex_substance_of_biological_originCell_fractionSchema(),
        required=True,
        data_key="Cell fraction",
        attribute="Cell fraction",
    )

    Virion = ma_fields.Nested(
        lambda: Complex_substance_of_biological_originVirionSchema(), required=True
    )

    type_field = "derived_from"


class EntitiesOfInterestItemPolymerSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    modifications = ma_fields.Nested(lambda: ModificationsSchema())

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "cyclic-pseudo-peptide",
                "peptide nucleic acid",
                "polydeoxyribonucleotide",
                "polydeoxyribonucleotide/polyribonucleotide hybrid",
                "polypeptide(D)",
                "polypeptide(L)",
                "polyribonucleotide",
                "Other",
            ])
        ],
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )

    variant = ma_fields.String()


class MeasurementsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    measurement_position = ma_fields.Nested(lambda: EntitySchema(), required=True)

    name = ma_fields.String(required=True)

    reference_measurement_position = ma_fields.Nested(lambda: EntitySchema())

    reference_samples = ma_fields.List(
        ma_fields.Nested(lambda: ReferenceSamplesItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    samples = ma_fields.List(
        ma_fields.Nested(lambda: ReferenceSamplesItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class PolymerSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    modifications = ma_fields.Nested(lambda: ModificationsSchema())

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    polymer_type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "cyclic-pseudo-peptide",
                "peptide nucleic acid",
                "polydeoxyribonucleotide",
                "polydeoxyribonucleotide/polyribonucleotide hybrid",
                "polypeptide(D)",
                "polypeptide(L)",
                "polyribonucleotide",
                "Other",
            ])
        ],
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )

    variant = ma_fields.String()


class SolventItemChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Chemical"])])


class AssociatedPublicationsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    main = ma_fields.Nested(lambda: AdditionalItemSchema())


class Body_fluidSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Blood",
                "Fecal matter",
                "Milk",
                "Plasma",
                "Saliva",
                "Serum",
                "Urine",
                "Plant extract",
                "Other",
            ])
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Cell_fractionSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    cell_type = ma_fields.String()

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf([
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
                "Other",
            ])
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Complex_substance_of_biological_originBody_fluidSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fluid = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Blood",
                "Fecal matter",
                "Milk",
                "Plasma",
                "Saliva",
                "Serum",
                "Urine",
                "Plant extract",
                "Other",
            ])
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Complex_substance_of_biological_originCell_fractionSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    cell_type = ma_fields.String()

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    fraction = ma_fields.String(
        required=True,
        validate=[
            OneOf([
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
                "Other",
            ])
        ],
    )

    health_status = ma_fields.String(required=True)

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Complex_substance_of_biological_originVirionSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    capsid_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic", "Other"])],
    )

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Complex_substance_of_environmental_originSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    location = ma_fields.Nested(lambda: LocationSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Fresh water",
                "Marine",
                "Ice core",
                "Sediment",
                "Sewage",
                "Soil",
                "Other",
            ])
        ],
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class Complex_substance_of_industrial_production_originSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_environmental_originSchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    location = ma_fields.Nested(lambda: LocationSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Fresh water",
                "Marine",
                "Ice core",
                "Sediment",
                "Sewage",
                "Soil",
                "Other",
            ])
        ],
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_industrial_production_originSchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class QualityControlsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    parameter = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "aggregation state",
                "homogeneity",
                "identity",
                "purity",
                "stability",
                "Other",
            ])
        ],
    )

    report = ma_fields.String(required=True)

    storage_until_measurement = ma_fields.Nested(
        lambda: StorageUntilMeasurementSchema(), required=True
    )

    technique = ma_fields.String(required=True)


class RecordInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    access_rights = ma_fields.String(
        required=True,
        validate=[OneOf(["open access", "embargoed access", "restricted access"])],
    )

    date_available = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    deposition_date = ma_fields.String(
        required=True, validate=[validate_date("%Y-%m-%d")]
    )

    identifier = ma_fields.String(required=True)

    internal_id = ma_fields.String(required=True)

    keywords = ma_fields.List(
        ma_fields.String(), required=True, validate=[ma.validate.Length(min=1)]
    )

    measurement_group_id = ma_fields.String()

    metadata_access_rights = ma_fields.String(
        required=True,
        validate=[OneOf(["open access", "embargoed access", "restricted access"])],
    )

    project = ma_fields.Nested(lambda: ProjectSchema())

    publisher = ma_fields.String(required=True, validate=[OneOf(["MBDB"])])

    resource_type = ma_fields.String(required=True)

    resource_type_general = ma_fields.String(
        required=True, validate=[OneOf(["Dataset"])]
    )

    subject_category = ma_fields.String(required=True, validate=[OneOf(["Biophysics"])])

    title = ma_fields.String(required=True)


class ReferenceSamplesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    analytes = ma_fields.List(
        ma_fields.Nested(lambda: AnalytesItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    chemical_environment = ma_fields.Nested(lambda: EntitySchema(), required=True)

    measurement_step = ma_fields.Nested(lambda: EntitySchema(), required=True)

    position = ma_fields.String()

    preparation = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    temperature = ma_fields.Nested(lambda: TemperatureSchema())


class VirionSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    capsid_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic", "Other"])],
    )

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Polymer",
                "Chemical",
                "Molecular assembly",
                "Complex substance of biological origin",
                "Complex substance of environmental origin",
                "Complex substance of chemical origin",
                "Complex substance of industrial production origin",
            ])
        ],
    )


class AdditionalItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authors = ma_fields.List(
        ma_fields.Nested(lambda: AuthorsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    pid = ma_fields.String(required=True)

    publication_year = ma_fields.Integer(
        required=True, validate=[ma.validate.Range(min=1900)]
    )

    publisher = ma_fields.String()

    resource_type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )

    title = ma_fields.String()


class AnalytesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    entity = ma_fields.Nested(lambda: EntitySchema(), required=True)


class DepositorsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(
        ma_fields.Nested(lambda: AuthorsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    depositor = ma_fields.Nested(lambda: AuthorsItemSchema(), required=True)

    principal_contact = ma_fields.Nested(lambda: AuthorsItemSchema(), required=True)


class DerivedParametersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    name = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Concentration",
                "Stoichiometry",
                "Constant of association (K_A)",
                "Constant of dissociation (K_D)",
                "Association rate (k_on)",
                "Dissociation rate (k_off)",
                "Change in enthalpy (delta H)",
                "Change in entropy (delta S)",
                "Change in Gibbs free energy (delta G)",
                "Molecular weight (MW)",
            ])
        ],
    )

    unit = ma_fields.String(required=True)

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class MeasurementPositionsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    flow_cell = ma_fields.String(required=True)

    ligand_information = ma_fields.Nested(lambda: LigandInformationSchema())

    name = ma_fields.String(required=True)

    position = ma_fields.String()


class MeasurementProtocolItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    flow = ma_fields.Nested(lambda: FlowSchema(), required=True)

    name = ma_fields.String(required=True)

    start_time = ma_fields.Nested(lambda: DurationSchema(), required=True)

    time_length = ma_fields.Nested(lambda: DurationSchema(), required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Association",
                "Baseline",
                "Dissociation",
                "Regeneration",
                "Load",
                "Wash",
                "Activation",
                "Enhancement",
            ])
        ],
    )


class ModificationsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    biological_postprocessing = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    chemical = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    synthesis = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )


class ProjectSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    description = ma_fields.String(required=True)

    owner = ma_fields.Nested(lambda: AuthorsItemSchema(), required=True)

    title = ma_fields.String(required=True)


class StorageUntilMeasurementSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    duration = ma_fields.Nested(lambda: DurationSchema())

    storage_preparation = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    temperature = ma_fields.Nested(lambda: TemperatureSchema(), required=True)


class AuthorsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: AffiliationsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    family_name = ma_fields.String(required=True)

    given_name = ma_fields.String(required=True)

    identifiers = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )


class BiologicalPostprocessingItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    modification = ma_fields.String(required=True)

    position = ma_fields.String()

    protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )


class ConcentrationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])]
    )

    obtained_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf([
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
            ])
        ],
    )

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class DataAnalysisItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma_fields.Nested(lambda: DataFittingSchema())

    data_processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: DataProcessingStepsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    derived_parameter = ma_fields.Nested(lambda: EntitySchema())

    measurements = ma_fields.List(
        ma_fields.Nested(lambda: EntitySchema()), validate=[ma.validate.Length(min=1)]
    )


class DurationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "nanoseconds",
                "microseconds",
                "milliseconds",
                "seconds",
                "minutes",
                "hours",
                "days",
                "months",
                "years",
            ])
        ],
    )

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class DynamicViscositySchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["Pa s"])])

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class EntitiesInvolvedItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    copy_number = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    entity = ma_fields.Nested(lambda: EntitySchema(), required=True)


class FlowSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    direction = ma_fields.String(validate=[OneOf(["Vertical", "Horizontal"])])

    path = ma_fields.List(
        ma_fields.List(
            ma_fields.Nested(lambda: EntitySchema()),
            validate=[ma.validate.Length(min=1)],
        ),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    rate = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    unit = ma_fields.String(required=True, validate=[OneOf(["mL/min", "µl/s"])])


class HumiditySchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma_fields.Boolean(required=True)

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["%", "g/m^3", "oz/y^3"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class LigandInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    ligand = ma_fields.Nested(lambda: EntitySchema())

    ligand_immobilization_chemistry = ma_fields.String()

    ligand_immobilization_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )


class MolecularWeightSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True, validate=[OneOf(["g/mol", "Da", "kDa", "MDa"])]
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class PhSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class PressureSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma_fields.Boolean(required=True)

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "Pa",
                "kPa",
                "MPa",
                "Bar",
                "mBar",
                "atm",
                "Torr",
                "PSI",
                "mmHg",
                "inchHg",
            ])
        ],
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class SensorSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    previously_used = ma_fields.Boolean()

    sensor_initialization = ma_fields.String(validate=[OneOf(["Air", "Glycerol"])])

    supplier = ma_fields.Nested(lambda: SupplierSchema(), required=True)

    surface_properties = ma_fields.String()


class TemperatureSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma_fields.Boolean(required=True)

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    operational_value = ma_fields.String(
        validate=[OneOf(["Room temperature", "On Ice", "Other"])]
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["K", "°C", "°F"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class AffiliationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    city = ma_fields.String()

    country = ma_fields.String()

    state = ma_fields.String()

    title = i18n_strings


class DataFittingSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    model = ma_fields.String(required=True)

    quality = ma_fields.Float()

    quality_type = ma_fields.String(
        validate=[
            OneOf([
                "R^2",
                "SEM",
                "red. Chi^2",
                "1sigma",
                "2sigma",
                "3sigma",
                "5sigma",
                "Skewness",
            ])
        ]
    )

    software_name = ma_fields.String()

    software_version = ma_fields.String()


class DataProcessingStepsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    link_to_source_code = ma_fields.String()

    name = ma_fields.String(required=True)

    software_name = ma_fields.String()

    software_tool = ma_fields.String()

    software_version = ma_fields.String()


class EntitySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = ma_fields.String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    name = ma_fields.String(required=True)


class ExpressionOrganismSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    rank = ma_fields.String()

    title = i18n_strings


class FundingReferenceItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    funder_name = ma_fields.String()

    title = i18n_strings


class IonicStrengthSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True,
        validate=[
            OneOf([
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
            ])
        ],
    )

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])


class LocationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    longitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )


class ObtainedProtocolItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    name = ma_fields.String(required=True)


class SizeSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    distribution_type = ma_fields.String()

    lower = ma_fields.Float()

    mean = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    median = ma_fields.Float(validate=[ma.validate.Range(min=0.0)])

    type = ma_fields.String(
        required=True, validate=[OneOf(["radius", "diameter", "path length", "Other"])]
    )

    unit = ma_fields.String(
        required=True, validate=[OneOf(["Å", "nm", "μm", "mm", "cm", "m"])]
    )

    upper = ma_fields.Float()


class SupplierSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    catalog_number = ma_fields.String()

    further_information = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    name = ma_fields.String(required=True)


class UltrafiltrationMethodSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    filter_material = ma_fields.String(
        validate=[
            OneOf([
                "Polyethersulfone (PES)",
                "Polyvinylidene flouride (PVDF)",
                "Cellulose acetate (CA)",
                "Composite regenerated cellulose (CRC)",
                "Microporous Glass Fiber (MGF)",
                "Nylon",
                "Polytetrafluoroethylene (PTFE)",
                "Hydrophilic Polytetrafluoroethylene (PTFE)",
                "Mixed cellulose ester (MCE)",
                "Polypropylene (PP)",
            ])
        ]
    )

    pore_size = ma_fields.String(
        required=True,
        validate=[OneOf(["0.2 µm", "0.22 µm", "0.45 µm", "0.5 µm", "1.2 µm", "Other"])],
    )


class ValueErrorSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    error_level = ma_fields.Float(validate=[ma.validate.Range(min=0.0)])

    errors_are_relative = ma_fields.Boolean(required=True)

    lower_error = ma_fields.Float(required=True)

    upper_error = ma_fields.Float(required=True)


class FilesOptionsSchema(ma.Schema):
    """Basic files options schema class."""

    enabled = ma.fields.Bool(missing=True)
    # allow unsetting
    default_preview = SanitizedUnicode(allow_none=True)

    def get_attribute(self, obj, attr, default):
        """Override how attributes are retrieved when dumping.

        NOTE: We have to access by attribute because although we are loading
              from an external pure dict, but we are dumping from a data-layer
              object whose fields should be accessed by attributes and not
              keys. Access by key runs into FilesManager key access protection
              and raises.
        """
        value = getattr(obj, attr, default)

        if attr == "default_preview" and not value:
            return default

        return value
