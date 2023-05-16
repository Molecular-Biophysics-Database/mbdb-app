import marshmallow as ma
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from marshmallow import fields as ma_fields
from marshmallow import validate as ma_validate
from marshmallow.utils import get_value
from marshmallow_utils.fields import SanitizedUnicode
from oarepo_runtime.polymorphic import PolymorphicSchema
from oarepo_runtime.validation import validate_date


class MbdbMstSchema(InvenioBaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: MbdbMstMetadataSchema())
    files = ma_fields.Nested(
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


class MbdbMstMetadataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    general_parameters = ma_fields.Nested(lambda: GeneralParametersSchema())

    method_specific_parameters = ma_fields.Nested(
        lambda: MethodSpecificParametersSchema()
    )

    title = ma_fields.String()


class GeneralParametersSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    associated_publications = ma_fields.Nested(lambda: AssociatedPublicationsSchema())

    chemical_information = ma_fields.Nested(lambda: ChemicalInformationSchema())

    depositors = ma_fields.Nested(lambda: DepositorsSchema())

    derived_parameters = ma_fields.List(
        ma_fields.Nested(lambda: DerivedParametersItemSchema())
    )

    funding_reference = ma_fields.List(
        ma_fields.Nested(lambda: FundingReferenceItemSchema())
    )

    instrument = ma_fields.Nested(lambda: InstrumentSchema())

    physical_environment_at_sample_handling = ma_fields.Nested(
        lambda: PhysicalEnvironmentAtSampleHandlingSchema()
    )

    raw_data_information = ma_fields.Nested(lambda: RawDataInformationSchema())

    record = ma_fields.Nested(lambda: RecordSchema())

    technique = ma_fields.String(
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
        ]
    )


class ChemicalInformationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environments = ma_fields.List(
        ma_fields.Nested(lambda: ChemicalEnvironmentsItemSchema())
    )

    entities_of_interest = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemSchema())
    )


class InstrumentSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    manufacturer = ma_fields.String(
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
        ]
    )

    model = ma_fields.String()

    name = ma_fields.String()

    performance_test = ma_fields.Nested(lambda: PerformanceTestSchema())


class ChemicalEnvironmentsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    constituents = ma_fields.List(ma_fields.Nested(lambda: ConstituentsItemSchema()))

    degassing_method = ma_fields.String(
        validate=[ma_validate.OneOf(["Low pressure", "Heating", "Sonication bath"])]
    )

    dynamic_viscosity = ma_fields.Nested(lambda: DynamicViscositySchema())

    ionic_strength = ma_fields.Nested(lambda: IonicStrengthSchema())

    name = ma_fields.String()

    pH = ma_fields.Nested(lambda: PHSchema())

    solvent = ma_fields.List(ma_fields.Nested(lambda: SolventItemSchema()))

    ultrafiltration_method = ma_fields.Nested(lambda: UltrafiltrationMethodSchema())


class PerformanceTestSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_information = ma_fields.String()

    published_test_protocol = ma_fields.Nested(lambda: AdditionalItemSchema())

    report = ma_fields.Nested(lambda: ReportSchema())

    sample_composition = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemSchema())
    )


class PhysicalEnvironmentAtSampleHandlingSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    atmosphere = ma_fields.Nested(lambda: AtmosphereSchema())

    humidity = ma_fields.Nested(lambda: HumiditySchema())

    pressure = ma_fields.Nested(lambda: PressureSchema())

    temperature = ma_fields.Nested(lambda: TemperatureSchema())


class AtmosphereSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    composition = ma_fields.List(ma_fields.Nested(lambda: SolventItemSchema()))


class ConstituentsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(lambda: ChemicalSchema())

    Complex_substance_of_biological_origin = ma_fields.Nested(
        lambda: Complex_substance_of_biological_originSchema(),
        data_key="Complex substance of biological origin",
        attribute="Complex substance of biological origin",
    )

    Complex_substance_of_chemical_origin = ma_fields.Nested(
        lambda: Complex_substance_of_chemical_originSchema(),
        data_key="Complex substance of chemical origin",
        attribute="Complex substance of chemical origin",
    )

    Complex_substance_of_environmental_origin = ma_fields.Nested(
        lambda: Complex_substance_of_environmental_originSchema(),
        data_key="Complex substance of environmental origin",
        attribute="Complex substance of environmental origin",
    )

    Complex_substance_of_industrial_production_origin = ma_fields.Nested(
        lambda: Complex_substance_of_industrial_production_originSchema(),
        data_key="Complex substance of industrial production origin",
        attribute="Complex substance of industrial production origin",
    )

    Molecular_assembly = ma_fields.Nested(
        lambda: Molecular_assemblySchema(),
        data_key="Molecular assembly",
        attribute="Molecular assembly",
    )

    Polymer = ma_fields.Nested(lambda: PolymerSchema())

    type_field = "type"


class Complex_substance_of_chemical_originSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    class_ = ma_fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    description = ma_fields.String()

    details = ma_fields.Nested(lambda: DetailsSchema())

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma_fields.String(
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

    Chemical = ma_fields.Nested(lambda: ChemicalSchema())

    Molecular_assembly = ma_fields.Nested(
        lambda: Molecular_assemblySchema(),
        data_key="Molecular assembly",
        attribute="Molecular assembly",
    )

    Polymer = ma_fields.Nested(lambda: PolymerSchema())

    type_field = "type"


class DetailsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    components = ma_fields.List(ma_fields.Nested(lambda: ComponentsItemSchema()))

    number_of_mono_layers = ma_fields.Integer()

    size = ma_fields.Nested(lambda: DetailsSizeSchema())

    type = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet", "Other"])
        ]
    )


class Molecular_assemblySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    components = ma_fields.List(ma_fields.Nested(lambda: ComponentsItemSchema()))

    external_databases = ma_fields.List(ma_fields.String())

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
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


class ComponentsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(lambda: ChemicalSchema())

    Polymer = ma_fields.Nested(lambda: PolymerSchema())

    type_field = "type"


class MethodSpecificParametersSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_analysis = ma_fields.List(ma_fields.Nested(lambda: DataAnalysisItemSchema()))

    excitation_led_color = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                [
                    "RED (ex 605–645nm, em 660–730nm)",
                    "RED (ex 610–645nm, em 680–730nm)",
                    "GREEN (ex 555-585nm, em 605-690nm)",
                    "GREEN (ex 515-550nm, em 565-600nm)",
                    "BLUE (ex 480–500nm, em 515–550nm)",
                    "BLUE (ex 460–500nm, em 515–560nm)",
                    "UV (ex 260-300nm, em 330-380nm)",
                ]
            )
        ]
    )

    excitation_led_power = ma_fields.Integer()

    experiment_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Affinity", "Concentration", "Other"])]
    )

    ir_mst_laser_power = ma_fields.Integer()

    label_free = ma_fields.Boolean()

    measurements = ma_fields.List(ma_fields.Nested(lambda: MeasurementsItemSchema()))

    signal_type = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Initial intensity", "TRIC/MST", "Spectral shift"])
        ]
    )


class ChemicalSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    copy_number = ma_fields.Float()

    inchikey = ma_fields.String()

    isotopic_labeling = ma_fields.String()

    name = ma_fields.String()

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
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

    Body_fluid = ma_fields.Nested(
        lambda: Body_fluidSchema(), data_key="Body fluid", attribute="Body fluid"
    )

    Cell_fraction = ma_fields.Nested(
        lambda: Cell_fractionSchema(),
        data_key="Cell fraction",
        attribute="Cell fraction",
    )

    Virion = ma_fields.Nested(lambda: VirionSchema())

    type_field = "derived_from"


class MeasurementsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    measured_data = ma_fields.Nested(lambda: MeasuredDataSchema())

    name = ma_fields.String()

    position = ma_fields.String()

    sample = ma_fields.Nested(lambda: SampleSchema())


class PolymerSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    copy_number = ma_fields.Float()

    expression_organism = ma_fields.Nested(lambda: OrganismSchema())

    expression_source_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    modifications = ma_fields.Nested(lambda: ModificationsSchema())

    name = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismSchema())

    polymer_type = ma_fields.String(
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

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemSchema())
    )

    sequence = ma_fields.String()

    supplier = ma_fields.Nested(lambda: SupplierSchema())

    type = ma_fields.String(
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

    variant = ma_fields.String()


class Body_fluidSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationSchema())

    derived_from = ma_fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma_fields.String()

    fluid = ma_fields.String(
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

    health_status = ma_fields.String()

    name = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismSchema())

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma_fields.String(
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

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    celltype = ma_fields.String()

    concentration = ma_fields.Nested(lambda: ConcentrationSchema())

    derived_from = ma_fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma_fields.String()

    fraction = ma_fields.String(
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

    health_status = ma_fields.String()

    name = ma_fields.String()

    organ = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismSchema())

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    tissue = ma_fields.String()

    type = ma_fields.String(
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

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    description = ma_fields.String()

    location = ma_fields.Nested(lambda: LocationSchema())

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    source = ma_fields.String(
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

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma_fields.String(
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

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    description = ma_fields.String()

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    product = ma_fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma_fields.String(
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

    parameter = ma_fields.String(
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

    report = ma_fields.Nested(lambda: ReportSchema())

    storage_from_QC_to_measurement = ma_fields.Nested(
        lambda: StorageFromQCToMeasurementSchema()
    )

    technique = ma_fields.String()


class SampleSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environment = ma_fields.Nested(lambda: EntitySchema())

    container = ma_fields.String(
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

    ligands = ma_fields.List(ma_fields.Nested(lambda: LigandsItemSchema()))

    preparation = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    targets = ma_fields.List(ma_fields.Nested(lambda: LigandsItemSchema()))


class VirionSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    Genetic_material = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                ["No genetic material", "Virus genome", "Synthetic", "Other"]
            )
        ]
    )

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema())

    derived_from = ma_fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma_fields.String()

    envelope_type = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: OrganismSchema())

    name = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismSchema())

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementSchema())

    type = ma_fields.String(
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


class AssociatedPublicationsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional = ma_fields.List(ma_fields.Nested(lambda: AdditionalItemSchema()))

    main = ma_fields.Nested(lambda: AdditionalItemSchema())


class DerivedParametersItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema())
    )

    name = ma_fields.String()

    type = ma_fields.String(
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

    unit = ma_fields.String()

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class LigandsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma_fields.Nested(lambda: ConcentrationSchema())

    entity = ma_fields.Nested(lambda: EntitySchema())


class ModificationsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    biological_postprocessing = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    chemical = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )

    synthesis = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemSchema())
    )


class RawDataInformationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    collection_start_time = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    file_information = ma_fields.List(ma_fields.Nested(lambda: ReportSchema()))


class RecordSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    access_rights = ma_fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    date_available = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    deposition_date = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    identifier = ma_fields.String()

    keywords = ma_fields.List(ma_fields.String())

    measurement_group_id = ma_fields.String()

    metadata_access_rights = ma_fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    project = ma_fields.Nested(lambda: ProjectSchema())

    publisher = ma_fields.String(validate=[ma_validate.OneOf(["MBDB"])])

    resource_type = ma_fields.String()

    resource_type_general = ma_fields.String(validate=[ma_validate.OneOf(["dataset"])])

    subject_category = ma_fields.String()

    title = ma_fields.String()

    version = ma_fields.String()


class StorageFromQCToMeasurementSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    duration = ma_fields.Nested(lambda: DurationSchema())

    storage_preparation = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    temperature = ma_fields.Nested(lambda: TemperatureSchema())


class AdditionalItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    authors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemSchema()))

    pid = ma_fields.String()

    publication_year = ma_fields.Integer()

    publisher = ma_fields.String()

    resource_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Article", "Book", "Thesis"])]
    )

    title = ma_fields.String()


class BiologicalPostprocessingItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    modification = ma_fields.String()

    monomer_position = ma_fields.Integer()

    protocol = ma_fields.List(ma_fields.Nested(lambda: StoragePreparationItemSchema()))


class ConcentrationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    obtained_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemSchema())
    )

    unit = ma_fields.String(
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
        ]
    )

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class DataAnalysisItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma_fields.Nested(lambda: DataFittingSchema())

    data_processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: ProcessingStepsItemSchema())
    )

    derived_parameter = ma_fields.Nested(lambda: EntitySchema())

    f_cold_and_hot = ma_fields.Nested(lambda: FColdAndHotSchema())


class DepositorsSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemSchema()))

    depositor = ma_fields.Nested(lambda: AuthorsItemSchema())

    principal_contact = ma_fields.Nested(lambda: AuthorsItemSchema())


class DurationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
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
        ]
    )

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class DynamicViscositySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    unit = ma_fields.String(validate=[ma_validate.OneOf(["Pa s"])])

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class EntitiesInvolvedItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    entity = ma_fields.Nested(lambda: EntitySchema())

    stoichiometry = ma_fields.Float()


class HumiditySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma_fields.Boolean()

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    unit = ma_fields.String(validate=[ma_validate.OneOf(["%", "g/m^3", "oz/y^3"])])

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class MeasuredDataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    x_data = ma_fields.Nested(lambda: XDataSchema())

    y_data = ma_fields.Nested(lambda: XDataSchema())


class OrganismSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_taxonomic_information = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTaxonomicInformationItemSchema())
    )

    ncbi_taxid = ma_fields.String()


class PHSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class PressureSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma_fields.Boolean()

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    unit = ma_fields.String(
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
        ]
    )

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class ProjectSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    description = ma_fields.String()

    owner = ma_fields.Nested(lambda: AuthorsItemSchema())

    title = ma_fields.String()


class ReportSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    name = ma_fields.String()

    processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: ProcessingStepsItemSchema())
    )

    recommended_software = ma_fields.String()

    size = ma_fields.Nested(lambda: SizeSchema())

    source = ma_fields.String(
        validate=[ma_validate.OneOf(["Instrument software", "User annotated", "MBDB"])]
    )

    type = ma_fields.String(
        validate=[ma_validate.OneOf(["text", "binary", "text and binary"])]
    )


class TemperatureSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma_fields.Boolean()

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    operational_value = ma_fields.String(
        validate=[ma_validate.OneOf(["Room temperature", "On Ice", "Other"])]
    )

    unit = ma_fields.String(validate=[ma_validate.OneOf(["K", "°C", "°F"])])

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class AdditionalTaxonomicInformationItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    class_ = ma_fields.String(data_key="class", attribute="class")

    domain = ma_fields.String()

    genus = ma_fields.String()

    kingdom = ma_fields.String()

    order = ma_fields.String()

    phylum = ma_fields.String()

    realm = ma_fields.String()

    species = ma_fields.String()

    strain = ma_fields.String()


class AuthorsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(ma_fields.String())

    full_name = ma_fields.String()

    identifiers = ma_fields.List(ma_fields.String())


class DataFittingSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    model = ma_fields.String()

    quality = ma_fields.Float()

    quality_type = ma_fields.String(
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

    software_name = ma_fields.String()

    software_version = ma_fields.String()


class DetailsSizeSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    distribution_type = ma_fields.String()

    lower = ma_fields.Float()

    mean = ma_fields.Float()

    median = ma_fields.Float()

    type = ma_fields.String(
        validate=[ma_validate.OneOf(["radius", "diameter", "path length", "Other"])]
    )

    unit = ma_fields.String(
        validate=[ma_validate.OneOf(["Å", "nm", "μm", "mm", "cm", "m"])]
    )

    upper = ma_fields.Float()


class EntitySchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    _version = ma_fields.String(data_key="@v", attribute="@v")

    name = ma_fields.String()


class FColdAndHotSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    f_cold_end = ma_fields.Float()

    f_cold_start = ma_fields.Float()

    f_hot_end = ma_fields.Float()

    f_hot_start = ma_fields.Float()

    time_unit = ma_fields.String(
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
        ]
    )


class FundingReferenceItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    award_number = ma_fields.String()

    funder_name = ma_fields.String()

    funding_program = ma_fields.String()


class IonicStrengthSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
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
        ]
    )

    value = ma_fields.Float()


class LocationSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    S_N_latitude_ = ma_fields.Float(data_key="S-N(latitude)", attribute="S-N(latitude)")

    W_E_longitude_ = ma_fields.Float(
        data_key="W-E(longitude)", attribute="W-E(longitude)"
    )


class ProcessingStepsItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    link_to_source_code = ma_fields.String()

    name = ma_fields.String()

    software_name = ma_fields.String()

    software_tool = ma_fields.String()

    software_version = ma_fields.String()


class SizeSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                [
                    "bytes (B)",
                    "kilobytes (kB)",
                    "megabytes (MB)",
                    "gigabytes (GB)",
                    "terabytes (TB)",
                    "kibibytes (KiB)",
                    "mebibytes (MiB)",
                    "gibibytes (GiB)",
                    "tebibytes (TiB)",
                ]
            )
        ]
    )

    value = ma_fields.Float()


class StoragePreparationItemSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    name = ma_fields.String()


class SupplierSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    catalog_number = ma_fields.String()

    further_information = ma_fields.List(ma_fields.String())

    name = ma_fields.String()


class UltrafiltrationMethodSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    filter_material = ma_fields.String(
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

    pore_size = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                ["0.2 µm", "0.22 µm", "0.45 µm", "0.5 µm", "1.2 µm", "Other"]
            )
        ]
    )


class ValueErrorSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    error_level = ma_fields.Float()

    errors_are_relative = ma_fields.Boolean()

    lower_error = ma_fields.Float()

    upper_error = ma_fields.Float()


class XDataSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    name = ma_fields.String()

    unit = ma_fields.String()

    values = ma_fields.List(ma_fields.Float())


class FilesOptionsSchema(ma.Schema):
    """Basic files options schema class."""

    enabled = ma_fields.Bool(missing=True)
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
