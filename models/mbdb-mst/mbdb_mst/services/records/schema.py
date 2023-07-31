import marshmallow as ma
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import validate as ma_validate
from oarepo_runtime.marshmallow import BaseRecordSchema
from oarepo_runtime.polymorphic import PolymorphicSchema
from oarepo_runtime.validation import validate_date


class MbdbMstSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: MbdbMstMetadataSchema())


class MbdbMstMetadataSchema(ma.Schema):
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

    collection_start_time = ma.fields.String(validate=[validate_date("%Y-%m-%d")])

    depositors = ma.fields.Nested(lambda: DepositorsSchema())

    derived_parameters = ma.fields.List(
        ma.fields.Nested(lambda: DerivedParametersItemSchema())
    )

    funding_reference = ma.fields.List(
        ma.fields.Nested(lambda: FundingReferenceItemSchema())
    )

    instrument = ma.fields.Nested(lambda: InstrumentSchema())

    physical_environment_at_sample_handling = ma.fields.Nested(
        lambda: PhysicalEnvironmentAtSampleHandlingSchema()
    )

    record = ma.fields.Nested(lambda: RecordSchema())

    schema_version = ma.fields.String(validate=[ma_validate.OneOf(["0.9.0"])])

    technique = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(
                [
                    "Bio-layer interferometry (BLI)",
                    "Surface plasmon resonance (SPR)",
                    "Mass Photometry (MP)",
                    "Isothermal titration calorimetry (ITC)",
                    (
                        "Microscale thermophoresis/Temperature related intensity change"
                        " (MST/TRIC)"
                    ),
                ]
            )
        ],
    )


class ChemicalInformationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environments = ma.fields.List(
        ma.fields.Nested(lambda: ChemicalEnvironmentsItemSchema())
    )

    entities_of_interest = ma.fields.List(
        ma.fields.Nested(lambda: EntitiesOfInterestItemSchema())
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

    name = ma.fields.String()

    performance_test = ma.fields.Nested(lambda: PerformanceTestSchema())


class ChemicalEnvironmentsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    constituents = ma.fields.List(ma.fields.Nested(lambda: ConstituentsItemSchema()))

    degassing_method = ma.fields.String(
        validate=[ma_validate.OneOf(["Low pressure", "Heating", "Sonication bath"])]
    )

    dynamic_viscosity = ma.fields.Nested(lambda: DynamicViscositySchema())

    ionic_strength = ma.fields.Nested(lambda: IonicStrengthSchema())

    name = ma.fields.String()

    pH = ma.fields.Nested(lambda: PHSchema(), required=True)

    solvent = ma.fields.List(ma.fields.Nested(lambda: SolventItemSchema()))

    ultrafiltration_method = ma.fields.Nested(lambda: UltrafiltrationMethodSchema())


class PerformanceTestSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_information = ma.fields.String()

    published_test_protocol = ma.fields.Nested(lambda: AdditionalItemSchema())

    report = ma.fields.String()

    sample_composition = ma.fields.List(
        ma.fields.Nested(lambda: ConstituentsItemSchema())
    )


class PhysicalEnvironmentAtSampleHandlingSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    atmosphere = ma.fields.Nested(lambda: AtmosphereSchema())

    humidity = ma.fields.Nested(lambda: HumiditySchema())

    pressure = ma.fields.Nested(lambda: PressureSchema())

    temperature = ma.fields.Nested(lambda: TemperatureSchema())


class AtmosphereSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    composition = ma.fields.List(ma.fields.Nested(lambda: SolventItemSchema()))


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

    additional_specifications = ma.fields.List(ma.fields.String())

    class_ = ma.fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    description = ma.fields.String()

    details = ma.fields.Nested(lambda: DetailsSchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class EntitiesOfInterestItemComplex_substance_of_chemical_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    class_ = ma.fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    description = ma.fields.String()

    details = ma.fields.Nested(lambda: DetailsSchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class SolventItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma.fields.Nested(lambda: SolventItemChemicalSchema(), required=True)

    Molecular_assembly = ma.fields.Nested(
        lambda: SolventItemMolecular_assemblySchema(),
        required=True,
        data_key="Molecular assembly",
        attribute="Molecular assembly",
    )

    Polymer = ma.fields.Nested(lambda: SolventItemPolymerSchema(), required=True)

    type_field = "type"


class DetailsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemSchema()))

    number_of_mono_layers = ma.fields.Integer()

    size = ma.fields.Nested(lambda: SizeSchema(), required=True)

    type = ma.fields.String(
        validate=[
            ma_validate.OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet", "Other"])
        ]
    )


class EntitiesOfInterestItemMolecular_assemblySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemSchema()))

    external_databases = ma.fields.List(ma.fields.String())

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
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
        ]
    )


class Molecular_assemblySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemSchema()))

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    external_databases = ma.fields.List(ma.fields.String())

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
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
        ]
    )


class SolventItemMolecular_assemblySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemSchema()))

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    external_databases = ma.fields.List(ma.fields.String())

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        validate=[ma_validate.OneOf(["Polymer", "Chemical", "Molecular assembly"])]
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

    data_analysis = ma.fields.List(ma.fields.Nested(lambda: DataAnalysisItemSchema()))

    excitation_led_color = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                [
                    "RED (ex 605–645nm, em 660–720nm)",
                    "RED (ex 610–645nm, em 680–720nm)",
                    "GREEN (ex 555-585nm, em 605-690nm)",
                    "GREEN (ex 515-550nm, em 565-600nm)",
                    "BLUE (ex 480–500nm, em 515–550nm)",
                    "BLUE (ex 460–500nm, em 515–560nm)",
                    "UV (ex 260-300nm, em 330-380nm)",
                    "Spectral shift",
                ]
            )
        ]
    )

    excitation_led_power = ma.fields.Float()

    experiment_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Affinity", "Concentration", "Other"])]
    )

    ir_mst_laser_power = ma.fields.Float()

    measurements = ma.fields.List(ma.fields.Nested(lambda: MeasurementsItemSchema()))

    schema_version = ma.fields.String(validate=[ma_validate.OneOf(["0.9.1"])])

    signal_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(["Initial intensity", "TRIC/MST", "Spectral shift"])
        ]
    )


class ChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
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
        ]
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

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    copy_number = ma.fields.Float()

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(validate=[ma_validate.OneOf(["Polymer", "Chemical"])])


class ComponentsItemPolymerSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    copy_number = ma.fields.Float()

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    modifications = ma.fields.Nested(lambda: ModificationsSchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    polymer_type = ma.fields.String(
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
        ]
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    sequence = ma.fields.String()

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(validate=[ma_validate.OneOf(["Polymer", "Chemical"])])

    variant = ma.fields.String()


class EntitiesOfInterestItemChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
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
        ]
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

    additional_specifications = ma.fields.List(ma.fields.String())

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    modifications = ma.fields.Nested(lambda: ModificationsSchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    polymer_type = ma.fields.String(
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
        ]
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    sequence = ma.fields.String()

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
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
        ]
    )

    variant = ma.fields.String()


class MeasurementsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    measured_data = ma.fields.Nested(lambda: MeasuredDataSchema())

    name = ma.fields.String()

    position = ma.fields.String()

    sample = ma.fields.Nested(lambda: SampleSchema(), required=True)


class PolymerSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    modifications = ma.fields.Nested(lambda: ModificationsSchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    polymer_type = ma.fields.String(
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
        ]
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    sequence = ma.fields.String()

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
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
        ]
    )

    variant = ma.fields.String()


class SolventItemChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        validate=[ma_validate.OneOf(["Polymer", "Chemical", "Molecular assembly"])]
    )


class SolventItemPolymerSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    modifications = ma.fields.Nested(lambda: ModificationsSchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    polymer_type = ma.fields.String(
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
        ]
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemSchema())
    )

    sequence = ma.fields.String()

    supplier = ma.fields.Nested(lambda: SupplierSchema())

    type = ma.fields.String(
        validate=[ma_validate.OneOf(["Polymer", "Chemical", "Molecular assembly"])]
    )

    variant = ma.fields.String()


class AssociatedPublicationsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional = ma.fields.List(ma.fields.Nested(lambda: AdditionalItemSchema()))

    main = ma.fields.Nested(lambda: AdditionalItemSchema())


class Body_fluidSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma.fields.String()

    fluid = ma.fields.String(
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
        ]
    )

    health_status = ma.fields.String()

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class Cell_fractionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    celltype = ma.fields.String()

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma.fields.String()

    fraction = ma.fields.String(
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
        ]
    )

    health_status = ma.fields.String()

    name = ma.fields.String()

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    tissue = ma.fields.String()

    type = ma.fields.String(
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
        ]
    )


class Complex_substance_of_biological_originBody_fluidSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma.fields.String()

    fluid = ma.fields.String(
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
        ]
    )

    health_status = ma.fields.String()

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class Complex_substance_of_biological_originCell_fractionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    celltype = ma.fields.String()

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma.fields.String()

    fraction = ma.fields.String(
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
        ]
    )

    health_status = ma.fields.String()

    name = ma.fields.String()

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    tissue = ma.fields.String()

    type = ma.fields.String(
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
        ]
    )


class Complex_substance_of_biological_originVirionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    Genetic_material = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["No genetic material", "Virus genome", "Synthetic", "Other"]
            )
        ]
    )

    additional_specifications = ma.fields.List(ma.fields.String())

    capsid_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma.fields.String()

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class Complex_substance_of_environmental_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    description = ma.fields.String()

    location = ma.fields.Nested(lambda: LocationSchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    source = ma.fields.String(
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
        ]
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class Complex_substance_of_industrial_production_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    description = ma.fields.String()

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    product = ma.fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class EntitiesOfInterestItemComplex_substance_of_environmental_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    description = ma.fields.String()

    location = ma.fields.Nested(lambda: LocationSchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    source = ma.fields.String(
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
        ]
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class EntitiesOfInterestItemComplex_substance_of_industrial_production_originSchema(
    ma.Schema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    description = ma.fields.String()

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    product = ma.fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class QualityControlsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    parameter = ma.fields.String(
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
        ]
    )

    report = ma.fields.String()

    storage_from_QC_to_measurement = ma.fields.Nested(
        lambda: StorageFromQCToMeasurementSchema(), required=True
    )

    technique = ma.fields.String()


class RecordSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    access_rights = ma.fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    date_available = ma.fields.String(validate=[validate_date("%Y-%m-%d")])

    deposition_date = ma.fields.String(validate=[validate_date("%Y-%m-%d")])

    identifier = ma.fields.String()

    keywords = ma.fields.List(ma.fields.String())

    measurement_group_id = ma.fields.String()

    metadata_access_rights = ma.fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    project = ma.fields.Nested(lambda: ProjectSchema())

    publisher = ma.fields.String(validate=[ma_validate.OneOf(["MBDB"])])

    resource_type = ma.fields.String()

    resource_type_general = ma.fields.String(validate=[ma_validate.OneOf(["dataset"])])

    subject_category = ma.fields.String()

    title = ma.fields.String()

    version = ma.fields.String()


class SampleSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environment = ma.fields.Nested(lambda: EntitySchema())

    container = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                [
                    "Monolith Standard Capillary",
                    "Monolith Premium Capillary",
                    "Monolith LabelFree Capillary",
                    "Monolith LabelFree Premium Capillary",
                    "Monolith NT.Automated Capillary Chip",
                    "Monolith NT.Automated Premium Capillary Chip",
                    "Monolith NT.Automated LabelFree Capillary Chip",
                    "Monolith NT.Automated LabelFree Premium Capillary Chip",
                    "384-well plate",
                    "other",
                ]
            )
        ]
    )

    ligands = ma.fields.List(ma.fields.Nested(lambda: LigandsItemSchema()))

    preparation = ma.fields.List(ma.fields.Nested(lambda: ObtainedProtocolItemSchema()))

    targets = ma.fields.List(ma.fields.Nested(lambda: LigandsItemSchema()))


class VirionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    Genetic_material = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["No genetic material", "Virus genome", "Synthetic", "Other"]
            )
        ]
    )

    additional_specifications = ma.fields.List(ma.fields.String())

    capsid_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma.fields.String()

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismSchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    storage = ma.fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma.fields.String(
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
        ]
    )


class AdditionalItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    authors = ma.fields.List(ma.fields.Nested(lambda: AuthorsItemSchema()))

    pid = ma.fields.String()

    publication_year = ma.fields.Integer()

    publisher = ma.fields.String()

    resource_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Article", "Book", "Thesis"])]
    )

    title = ma.fields.String()


class DepositorsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma.fields.List(ma.fields.Nested(lambda: AuthorsItemSchema()))

    depositor = ma.fields.Nested(lambda: AuthorsItemSchema(), required=True)

    principal_contact = ma.fields.Nested(lambda: AuthorsItemSchema(), required=True)


class DerivedParametersItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    entities_involved = ma.fields.List(
        ma.fields.Nested(lambda: EntitiesInvolvedItemSchema())
    )

    name = ma.fields.String()

    type = ma.fields.String(
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
        ]
    )

    unit = ma.fields.String()

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class LigandsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma.fields.Nested(lambda: ConcentrationSchema(), required=True)

    entity = ma.fields.Nested(lambda: EntitySchema())


class ModificationsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    biological_postprocessing = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    chemical = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    synthesis = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )


class ProjectSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    description = ma.fields.String()

    owner = ma.fields.Nested(lambda: AuthorsItemSchema(), required=True)

    title = ma.fields.String()


class StorageFromQCToMeasurementSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    duration = ma.fields.Nested(lambda: DurationSchema())

    storage_preparation = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
    )

    temperature = ma.fields.Nested(lambda: TemperatureSchema(), required=True)


class AuthorsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma.fields.List(ma.fields.Nested(lambda: AffiliationsItemSchema()))

    full_name = ma.fields.String()

    identifiers = ma.fields.List(ma.fields.String())


class BiologicalPostprocessingItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    modification = ma.fields.String()

    monomer_position = ma.fields.Integer()

    protocol = ma.fields.List(ma.fields.Nested(lambda: ObtainedProtocolItemSchema()))


class ConcentrationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma.fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    obtained_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemSchema())
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

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class DataAnalysisItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma.fields.Nested(lambda: DataFittingSchema(), required=True)

    data_processing_steps = ma.fields.List(
        ma.fields.Nested(lambda: DataProcessingStepsItemSchema())
    )

    derived_parameter = ma.fields.Nested(lambda: EntitySchema())

    f_cold_and_hot = ma.fields.Nested(lambda: FColdAndHotSchema())


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

    value = ma.fields.Float()

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

    unit = ma.fields.String(validate=[ma_validate.OneOf(["Pa s"])])

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class EntitiesInvolvedItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    entity = ma.fields.Nested(lambda: EntitySchema())

    stoichiometry = ma.fields.Float()


class HumiditySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma.fields.Boolean()

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["%", "g/m^3", "oz/y^3"])]
    )

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class MeasuredDataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    x_data = ma.fields.Nested(lambda: XDataSchema(), required=True)

    y_data = ma.fields.Nested(lambda: XDataSchema(), required=True)


class PHSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class PressureSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma.fields.Boolean()

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

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorSchema())


class TemperatureSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma.fields.Boolean()

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

    value = ma.fields.Float()

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

    model = ma.fields.String()

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

    description = ma.fields.String()

    link_to_source_code = ma.fields.String()

    name = ma.fields.String()

    software_name = ma.fields.String()

    software_tool = ma.fields.String()

    software_version = ma.fields.String()


class EntitySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    name = ma.fields.String()


class ExpressionOrganismSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    rank = ma.fields.String()

    title = i18n_strings


class FColdAndHotSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    f_cold_end = ma.fields.Float()

    f_cold_start = ma.fields.Float()

    f_hot_end = ma.fields.Float()

    f_hot_start = ma.fields.Float()

    time_unit = ma.fields.String(
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

    value = ma.fields.Float()


class LocationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    S_N_latitude_ = ma.fields.Float(data_key="S-N(latitude)", attribute="S-N(latitude)")

    W_E_longitude_ = ma.fields.Float(
        data_key="W-E(longitude)", attribute="W-E(longitude)"
    )


class ObtainedProtocolItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma.fields.String()

    name = ma.fields.String()


class SizeSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    distribution_type = ma.fields.String()

    lower = ma.fields.Float()

    mean = ma.fields.Float()

    median = ma.fields.Float()

    type = ma.fields.String(
        validate=[ma_validate.OneOf(["radius", "diameter", "path length", "Other"])]
    )

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["Å", "nm", "μm", "mm", "cm", "m"])]
    )

    upper = ma.fields.Float()


class SupplierSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    catalog_number = ma.fields.String()

    further_information = ma.fields.List(ma.fields.String())

    name = ma.fields.String()


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
        validate=[
            ma_validate.OneOf(
                ["0.2 µm", "0.22 µm", "0.45 µm", "0.5 µm", "1.2 µm", "Other"]
            )
        ]
    )


class ValueErrorSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    error_level = ma.fields.Float()

    errors_are_relative = ma.fields.Boolean()

    lower_error = ma.fields.Float()

    upper_error = ma.fields.Float()


class XDataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    name = ma.fields.String()

    unit = ma.fields.String()

    values = ma.fields.List(ma.fields.Float())
