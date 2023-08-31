import marshmallow as ma
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import validate as ma_validate
from marshmallow.utils import get_value
from marshmallow_utils.fields import SanitizedUnicode
from oarepo_runtime.marshmallow import BaseRecordSchema
from oarepo_runtime.polymorphic import PolymorphicSchema
from oarepo_runtime.validation import validate_date


class MbdbSprSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: MbdbSprMetadataSchema())
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


class MbdbSprMetadataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    general_parameters = ma.fields.Nested(
        lambda: GeneralParametersSchema(), required=True
    )

    method_specific_parameters = ma.fields.Nested(
        lambda: MethodSpecificParametersSchema()
    )


class GeneralParametersSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    associated_publications = ma.fields.Nested(lambda: AssociatedPublicationsSchema())

    chemical_information = ma.fields.Nested(lambda: ChemicalInformationSchema())

    collection_start_time = ma.fields.String(
        required=True, validate=[validate_date("%Y-%m-%d")]
    )

    depositors = ma.fields.Nested(lambda: DepositorsSchema())

    derived_parameters = ma.fields.List(
        ma.fields.Nested(lambda: DerivedParametersItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    funding_reference = ma.fields.List(
        ma.fields.Nested(lambda: FundingReferenceItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    instrument = ma.fields.Nested(lambda: InstrumentSchema())

    physical_conditions_at_sample_handling = ma.fields.Nested(
        lambda: PhysicalConditionsAtSampleHandlingSchema()
    )

    record_information = ma.fields.Nested(lambda: RecordInformationSchema())

    schema_version = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["0.9.8"])]
    )

    technique = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Bio-layer interferometry (BLI)",
                    (
                        "Microscale thermophoresis/Temperature related intensity change"
                        " (MST/TRIC)"
                    ),
                    "Surface plasmon resonance (SPR)",
                ]
            )
        ],
    )


class ChemicalInformationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environments = ma.fields.List(
        ma.fields.Nested(lambda: ChemicalEnvironmentsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    entities_of_interest = ma.fields.List(
        ma.fields.Nested(lambda: EntitiesOfInterestItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class InstrumentSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    manufacturer = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
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
                ]
            )
        ],
    )

    model = ma.fields.String()

    name = ma.fields.String(required=True)

    performance_test = ma.fields.Nested(lambda: PerformanceTestSchema())


class ChemicalEnvironmentsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(required=True, data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    constituents = ma.fields.List(
        ma.fields.Nested(lambda: ConstituentsItemSchema(), required=True),
        validate=[ma.validate.Length(min=1)],
    )

    degassing_method = ma.fields.String(
        validate=[ma_validate.OneOf(["Low pressure", "Heating", "Sonication bath"])]
    )

    dynamic_viscosity = ma.fields.Nested(lambda: DynamicViscositySchema())

    ionic_strength = ma.fields.Nested(lambda: IonicStrengthSchema())

    name = ma.fields.String(required=True)

    pH = ma.fields.Nested(lambda: PHSchema(), required=True)

    solvent = ma.fields.List(
        ma.fields.Nested(lambda: SolventItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    ultrafiltration_method = ma.fields.Nested(lambda: UltrafiltrationMethodSchema())


class PerformanceTestSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_information = ma.fields.String()

    published_test_protocol = ma.fields.Nested(lambda: AdditionalItemSchema())

    report = ma.fields.String(required=True)

    sample_composition = ma.fields.List(
        ma.fields.Nested(lambda: ConstituentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class ConstituentsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma.fields.Nested(lambda: ChemicalSchema(), required=True)

    Complex_substance_of_biological_origin = ma.fields.Nested(
        lambda: Complex_substance_of_biological_originSchema(),
        required=True,
        data_key="Complex substance of biological origin",
        attribute="Complex substance of biological origin",
    )

    Complex_substance_of_chemical_origin = ma.fields.Nested(
        lambda: Complex_substance_of_chemical_originSchema(),
        required=True,
        data_key="Complex substance of chemical origin",
        attribute="Complex substance of chemical origin",
    )

    Complex_substance_of_environmental_origin = ma.fields.Nested(
        lambda: Complex_substance_of_environmental_originSchema(),
        required=True,
        data_key="Complex substance of environmental origin",
        attribute="Complex substance of environmental origin",
    )

    Complex_substance_of_industrial_production_origin = ma.fields.Nested(
        lambda: Complex_substance_of_industrial_production_originSchema(),
        required=True,
        data_key="Complex substance of industrial production origin",
        attribute="Complex substance of industrial production origin",
    )

    Molecular_assembly = ma.fields.Nested(
        lambda: Molecular_assemblySchema(),
        required=True,
        data_key="Molecular assembly",
        attribute="Molecular assembly",
    )

    Polymer = ma.fields.Nested(lambda: PolymerSchema(), required=True)

    type_field = "type"


class EntitiesOfInterestItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma.fields.Nested(
        lambda: EntitiesOfInterestItemChemicalSchema(), required=True
    )

    Complex_substance_of_biological_origin = ma.fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_biological_originSchema(),
        required=True,
        data_key="Complex substance of biological origin",
        attribute="Complex substance of biological origin",
    )

    Complex_substance_of_chemical_origin = ma.fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_chemical_originSchema(),
        required=True,
        data_key="Complex substance of chemical origin",
        attribute="Complex substance of chemical origin",
    )

    Complex_substance_of_environmental_origin = ma.fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_environmental_originSchema(),
        required=True,
        data_key="Complex substance of environmental origin",
        attribute="Complex substance of environmental origin",
    )

    Complex_substance_of_industrial_production_origin = ma.fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_industrial_production_originSchema(),
        required=True,
        data_key="Complex substance of industrial production origin",
        attribute="Complex substance of industrial production origin",
    )

    Molecular_assembly = ma.fields.Nested(
        lambda: EntitiesOfInterestItemMolecular_assemblySchema(),
        required=True,
        data_key="Molecular assembly",
        attribute="Molecular assembly",
    )

    Polymer = ma.fields.Nested(
        lambda: EntitiesOfInterestItemPolymerSchema(), required=True
    )

    type_field = "type"


class Complex_substance_of_chemical_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    class_ = ma.fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    details = ma.fields.Nested(lambda: DetailsSchema(), required=True)

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_chemical_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    class_ = ma.fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    details = ma.fields.Nested(lambda: DetailsSchema(), required=True)

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class PhysicalConditionsAtSampleHandlingSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    atmosphere = ma.fields.Nested(lambda: AtmosphereSchema())

    humidity = ma.fields.Nested(lambda: HumiditySchema())

    pressure = ma.fields.Nested(lambda: PressureSchema())

    temperature = ma.fields.Nested(lambda: TemperatureSchema())


class AtmosphereSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    composition = ma.fields.List(
        ma.fields.Nested(lambda: SolventItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class DetailsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    components = ma.fields.List(
        ma.fields.Nested(lambda: ComponentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    number_of_mono_layers = ma.fields.Integer(
        required=True, validate=[ma.validate.Range(min=-1)]
    )

    size = ma.fields.Nested(lambda: SizeSchema(), required=True)

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet", "Other"])
        ],
    )


class EntitiesOfInterestItemMolecular_assemblySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    components = ma.fields.List(
        ma.fields.Nested(lambda: ComponentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    external_databases = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Molecular_assemblySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    components = ma.fields.List(
        ma.fields.Nested(lambda: ComponentsItemSchema(), required=True),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    external_databases = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class ComponentsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma.fields.Nested(lambda: ComponentsItemChemicalSchema(), required=True)

    Polymer = ma.fields.Nested(lambda: ComponentsItemPolymerSchema(), required=True)

    type_field = "type"


class MethodSpecificParametersSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_analysis = ma.fields.List(
        ma.fields.Nested(lambda: DataAnalysisItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    experiment_type = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Affinity", "Quantification", "Other"])],
    )

    measurement_positions = ma.fields.List(
        ma.fields.Nested(lambda: MeasurementPositionsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    measurement_protocol = ma.fields.List(
        ma.fields.Nested(lambda: MeasurementProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    measurements = ma.fields.List(
        ma.fields.Nested(lambda: MeasurementsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    schema_version = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["0.9.0"])]
    )

    sensor = ma.fields.Nested(lambda: SensorSchema(), required=True)


class SolventItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma.fields.Nested(lambda: SolventItemChemicalSchema(), required=True)

    type_field = "type"


class ChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    inchikey = ma.fields.String(required=True)

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Body_fluid = ma.fields.Nested(
        lambda: Body_fluidSchema(),
        required=True,
        data_key="Body fluid",
        attribute="Body fluid",
    )

    Cell_fraction = ma.fields.Nested(
        lambda: Cell_fractionSchema(),
        required=True,
        data_key="Cell fraction",
        attribute="Cell fraction",
    )

    Virion = ma.fields.Nested(lambda: VirionSchema(), required=True)

    type_field = "derived_from"


class ComponentsItemChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    copy_number = ma.fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    inchikey = ma.fields.String(required=True)

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["Polymer", "Chemical"])]
    )


class ComponentsItemPolymerSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    copy_number = ma.fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])],
    )

    external_databases = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    modifications = ma.fields.Nested(lambda: ModificationsSchema())

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    polymer_type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                    "Other",
                ]
            )
        ],
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    sequence = ma.fields.String()

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["Polymer", "Chemical"])]
    )

    variant = ma.fields.String()


class EntitiesOfInterestItemChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_identifiers = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    inchikey = ma.fields.String(required=True)

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_biological_originSchema(
    PolymorphicSchema
):
    class Meta:
        unknown = ma.RAISE

    Body_fluid = ma.fields.Nested(
        lambda: Complex_substance_of_biological_originBody_fluidSchema(),
        required=True,
        data_key="Body fluid",
        attribute="Body fluid",
    )

    Cell_fraction = ma.fields.Nested(
        lambda: Complex_substance_of_biological_originCell_fractionSchema(),
        required=True,
        data_key="Cell fraction",
        attribute="Cell fraction",
    )

    Virion = ma.fields.Nested(
        lambda: Complex_substance_of_biological_originVirionSchema(), required=True
    )

    type_field = "derived_from"


class EntitiesOfInterestItemPolymerSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])],
    )

    external_databases = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    modifications = ma.fields.Nested(lambda: ModificationsSchema())

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    polymer_type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                    "Other",
                ]
            )
        ],
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    sequence = ma.fields.String()

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )

    variant = ma.fields.String()


class MeasurementsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    measurement_position = ma.fields.Nested(lambda: EntitySchema(), required=True)

    reference_measurement_position = ma.fields.Nested(lambda: EntitySchema())

    reference_samples = ma.fields.List(
        ma.fields.Nested(lambda: ReferenceSamplesItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    samples = ma.fields.List(
        ma.fields.Nested(lambda: ReferenceSamplesItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class PolymerSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])],
    )

    external_databases = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    modifications = ma.fields.Nested(lambda: ModificationsSchema())

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    polymer_type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "cyclic-pseudo-peptide",
                    "peptide nucleic acid",
                    "polydeoxyribonucleotide",
                    "polydeoxyribonucleotide/polyribonucleotide hybrid",
                    "polypeptide(D)",
                    "polypeptide(L)",
                    "polyribonucleotide",
                    "Other",
                ]
            )
        ],
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    sequence = ma.fields.String()

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )

    variant = ma.fields.String()


class SolventItemChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    inchikey = ma.fields.String(required=True)

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma.fields.String(required=True)

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(required=True, validate=[ma_validate.OneOf(["Chemical"])])


class AssociatedPublicationsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional = ma.fields.List(
        ma.fields.Nested(lambda: AdditionalItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    main = ma.fields.Nested(lambda: AdditionalItemSchema())


class Body_fluidSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])],
    )

    fluid = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                    "Other",
                ]
            )
        ],
    )

    health_status = ma.fields.String(required=True)

    name = ma.fields.String(required=True)

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema(), required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Cell_fractionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    cell_type = ma.fields.String()

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])],
    )

    fraction = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
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
                    "Other",
                ]
            )
        ],
    )

    health_status = ma.fields.String(required=True)

    name = ma.fields.String(required=True)

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema(), required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    tissue = ma.fields.String()

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originBody_fluidSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    derived_from = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])],
    )

    fluid = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Blood",
                    "Fecal matter",
                    "Milk",
                    "Plasma",
                    "Saliva",
                    "Serum",
                    "Urine",
                    "Plant extract",
                    "Other",
                ]
            )
        ],
    )

    health_status = ma.fields.String(required=True)

    name = ma.fields.String(required=True)

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema(), required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originCell_fractionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    cell_type = ma.fields.String()

    derived_from = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])],
    )

    fraction = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
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
                    "Other",
                ]
            )
        ],
    )

    health_status = ma.fields.String(required=True)

    name = ma.fields.String(required=True)

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema(), required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    tissue = ma.fields.String()

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Complex_substance_of_biological_originVirionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    Genetic_material = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["No genetic material", "Virus genome", "Synthetic", "Other"]
            )
        ],
    )

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    capsid_type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ],
    )

    derived_from = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])],
    )

    envelope_type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ],
    )

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma.fields.String(required=True)

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema(), required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Complex_substance_of_environmental_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    location = ma.fields.Nested(lambda: LocationSchema(), required=True)

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Fresh water",
                    "Marine",
                    "Ice core",
                    "Sediment",
                    "Sewage",
                    "Soil",
                    "Other",
                ]
            )
        ],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class Complex_substance_of_industrial_production_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    product = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_environmental_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    location = ma.fields.Nested(lambda: LocationSchema(), required=True)

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Fresh water",
                    "Marine",
                    "Ice core",
                    "Sediment",
                    "Sewage",
                    "Soil",
                    "Other",
                ]
            )
        ],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class EntitiesOfInterestItemComplex_substance_of_industrial_production_originSchema(
    ma.Schema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    name = ma.fields.String(required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    product = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class QualityControlsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    parameter = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "aggregation state",
                    "homogeneity",
                    "identity",
                    "purity",
                    "stability",
                    "Other",
                ]
            )
        ],
    )

    report = ma.fields.String(required=True)

    storage_until_measurement = ma.fields.Nested(
        lambda: StorageUntilMeasurementSchema(), required=True
    )

    technique = ma.fields.String(required=True)


class RecordInformationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    access_rights = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ],
    )

    date_available = ma.fields.String(validate=[validate_date("%Y-%m-%d")])

    deposition_date = ma.fields.String(
        required=True, validate=[validate_date("%Y-%m-%d")]
    )

    identifier = ma.fields.String(required=True)

    internal_id = ma.fields.String(required=True)

    keywords = ma.fields.List(
        ma.fields.String(), required=True, validate=[ma.validate.Length(min=1)]
    )

    measurement_group_id = ma.fields.String()

    metadata_access_rights = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ],
    )

    project = ma.fields.Nested(lambda: ProjectSchema())

    publisher = ma.fields.String(required=True, validate=[ma_validate.OneOf(["MBDB"])])

    resource_type = ma.fields.String(required=True)

    resource_type_general = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["Dataset"])]
    )

    subject_category = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["Biophysics"])]
    )

    title = ma.fields.String(required=True)


class ReferenceSamplesItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    analytes = ma.fields.List(
        ma.fields.Nested(lambda: AnalytesItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    chemical_environment = ma.fields.Nested(lambda: EntitySchema(), required=True)

    measurement_step = ma.fields.Nested(lambda: EntitySchema(), required=True)

    position = ma.fields.String()

    preparation = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    temperature = ma.fields.Nested(lambda: TemperatureSchema())


class VirionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    Genetic_material = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["No genetic material", "Virus genome", "Synthetic", "Other"]
            )
        ],
    )

    additional_specifications = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    capsid_type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ],
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])],
    )

    envelope_type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ],
    )

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma.fields.String(required=True)

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema(), required=True)

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementSchema())

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Polymer",
                    "Chemical",
                    "Molecular assembly",
                    "Complex substance of biological origin",
                    "Complex substance of environmental origin",
                    "Complex substance of chemical origin",
                    "Complex substance of industrial production origin",
                ]
            )
        ],
    )


class AdditionalItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    authors = ma.fields.List(
        ma.fields.Nested(lambda: AuthorsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    pid = ma.fields.String(required=True)

    publication_year = ma.fields.Integer(
        required=True, validate=[ma.validate.Range(min=1800)]
    )

    publisher = ma.fields.String()

    resource_type = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["Article", "Book", "Thesis"])]
    )

    title = ma.fields.String()


class AnalytesItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    entity = ma.fields.Nested(lambda: EntitySchema(), required=True)


class DepositorsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma.fields.List(
        ma.fields.Nested(lambda: AuthorsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    depositor = ma.fields.Nested(lambda: AuthorsItemSchema(), required=True)

    principal_contact = ma.fields.Nested(lambda: AuthorsItemSchema(), required=True)


class DerivedParametersItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(required=True, data_key="id", attribute="id")

    entities_involved = ma.fields.List(
        ma.fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    name = ma.fields.String(required=True)

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
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
                ]
            )
        ],
    )

    unit = ma.fields.String(required=True)

    value = ma.fields.Float(required=True)

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class MeasurementPositionsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(required=True, data_key="id", attribute="id")

    flow_cell = ma.fields.String(required=True)

    ligand_information = ma.fields.Nested(lambda: LigandInformationSchema())

    name = ma.fields.String(required=True)

    position = ma.fields.String()


class MeasurementProtocolItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(required=True, data_key="id", attribute="id")

    flow = ma.fields.Nested(lambda: FlowSchema(), required=True)

    name = ma.fields.String(required=True)

    start_time = ma.fields.Nested(lambda: DurationSchema(), required=True)

    time_length = ma.fields.Nested(lambda: DurationSchema(), required=True)

    type = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Association",
                    "Baseline",
                    "Dissociation",
                    "Regeneration",
                    "Load",
                    "Wash",
                    "Activation",
                    "Enhancement",
                ]
            )
        ],
    )


class ModificationsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    biological_postprocessing = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    chemical = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    synthesis = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )


class ProjectSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    description = ma.fields.String(required=True)

    owner = ma.fields.Nested(lambda: AuthorsItemSchema(), required=True)

    title = ma.fields.String(required=True)


class StorageUntilMeasurementSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    duration = ma.fields.Nested(lambda: DurationSchema())

    storage_preparation = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    temperature = ma.fields.Nested(lambda: TemperatureSchema(), required=True)


class AuthorsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma.fields.List(
        ma.fields.Nested(lambda: AffiliationsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    family_name = ma.fields.String(required=True)

    given_name = ma.fields.String(required=True)

    identifiers = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )


class BiologicalPostprocessingItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    modification = ma.fields.String(required=True)

    position = ma.fields.String()

    protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )


class ConcentrationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma.fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    obtained_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    unit = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
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

    value = ma.fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class DataAnalysisItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma.fields.Nested(lambda: DataFittingSchema(), required=True)

    data_processing_steps = ma.fields.List(
        ma.fields.Nested(lambda: DataProcessingStepsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    derived_parameter = ma.fields.Nested(lambda: EntitySchema(), required=True)


class DurationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    unit = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "nanoseconds",
                    "microseconds",
                    "milliseconds",
                    "seconds",
                    "minutes",
                    "hours",
                    "days",
                ]
            )
        ],
    )

    value = ma.fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class DynamicViscositySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    unit = ma.fields.String(required=True, validate=[ma_validate.OneOf(["Pa s"])])

    value = ma.fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class EntitiesInvolvedItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    copy_number = ma.fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    entity = ma.fields.Nested(lambda: EntitySchema(), required=True)


class FlowSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    direction = ma.fields.String(
        validate=[ma_validate.OneOf(["Vertical", "Horizontal"])]
    )

    path = ma.fields.List(
        ma.fields.List(
            ma.fields.Nested(lambda: EntitySchema()),
            validate=[ma.validate.Length(min=1)],
        ),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    rate = ma.fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["mL/min", "µl/s"])]
    )


class HumiditySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma.fields.Boolean(required=True)

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["%", "g/m^3", "oz/y^3"])]
    )

    value = ma.fields.Float(required=True)

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class LigandInformationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    ligand = ma.fields.Nested(lambda: EntitySchema())

    ligand_immobilization_chemistry = ma.fields.String()

    ligand_immobilization_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )


class MolecularWeightSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["g/mol", "Da", "kDa", "MDa"])]
    )

    value = ma.fields.Float(required=True)

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class PHSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    value = ma.fields.Float(required=True)

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class PressureSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma.fields.Boolean(required=True)

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    unit = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
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
                ]
            )
        ],
    )

    value = ma.fields.Float(required=True)

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class SensorSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    previously_used = ma.fields.Boolean()

    sensor_initialization = ma.fields.String(
        validate=[ma_validate.OneOf(["Air", "Glycerol"])]
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema(), required=True)

    surface_properties = ma.fields.String()


class TemperatureSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma.fields.Boolean(required=True)

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    operational_value = ma.fields.String(
        validate=[ma_validate.OneOf(["Room temperature", "On Ice", "Other"])]
    )

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["K", "°C", "°F"])]
    )

    value = ma.fields.Float(required=True)

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class AffiliationsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    city = ma.fields.String()

    country = ma.fields.String()

    state = ma.fields.String()

    title = i18n_strings


class DataFittingSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    model = ma.fields.String(required=True)

    quality = ma.fields.Float()

    quality_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
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

    software_name = ma.fields.String()

    software_version = ma.fields.String()


class DataProcessingStepsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma.fields.String(required=True)

    link_to_source_code = ma.fields.String()

    name = ma.fields.String(required=True)

    software_name = ma.fields.String()

    software_tool = ma.fields.String()

    software_version = ma.fields.String()


class EntitySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    name = ma.fields.String(required=True)


class ExpressionOrganismSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    rank = ma.fields.String()

    title = i18n_strings


class FundingReferenceItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    funder_name = ma.fields.String()

    title = i18n_strings


class IonicStrengthSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    unit = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
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

    value = ma.fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])


class LocationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    S_N_latitude_ = ma.fields.Float(
        required=True,
        data_key="S-N(latitude)",
        attribute="S-N(latitude)",
        validate=[ma.validate.Range(min=-90.0, max=90.0)],
    )

    W_E_longitude_ = ma.fields.Float(
        required=True,
        data_key="W-E(longitude)",
        attribute="W-E(longitude)",
        validate=[ma.validate.Range(min=-180.0, max=180.0)],
    )


class ObtainedProtocolItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma.fields.String(required=True)

    name = ma.fields.String(required=True)


class SizeSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    distribution_type = ma.fields.String()

    lower = ma.fields.Float()

    mean = ma.fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    median = ma.fields.Float(validate=[ma.validate.Range(min=0.0)])

    type = ma.fields.String(
        required=True,
        validate=[ma_validate.OneOf(["radius", "diameter", "path length", "Other"])],
    )

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["Å", "nm", "μm", "mm", "cm", "m"])]
    )

    upper = ma.fields.Float()


class SupplierSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    catalog_number = ma.fields.String()

    further_information = ma.fields.List(
        ma.fields.String(), validate=[ma.validate.Length(min=1)]
    )

    name = ma.fields.String(required=True)


class UltrafiltrationMethodSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    filter_material = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                [
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
                ]
            )
        ]
    )

    pore_size = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                ["0.2 µm", "0.22 µm", "0.45 µm", "0.5 µm", "1.2 µm", "Other"]
            )
        ],
    )


class ValueErrorSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    error_level = ma.fields.Float(validate=[ma.validate.Range(min=0.0)])

    errors_are_relative = ma.fields.Boolean(required=True)

    lower_error = ma.fields.Float(required=True)

    upper_error = ma.fields.Float(required=True)


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
