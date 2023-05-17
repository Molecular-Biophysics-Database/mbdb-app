import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow import validate as ma_validate
from oarepo_runtime.ui import marshmallow as l10n
from oarepo_runtime.ui.marshmallow import InvenioUISchema


class MbdbMstUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: MbdbMstMetadataUISchema())


class MbdbMstMetadataUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    general_parameters = ma_fields.Nested(lambda: GeneralParametersUISchema())

    method_specific_parameters = ma_fields.Nested(
        lambda: MethodSpecificParametersUISchema()
    )

    title = ma_fields.String()


class GeneralParametersUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    associated_publications = ma_fields.Nested(lambda: AssociatedPublicationsUISchema())

    chemical_information = ma_fields.Nested(lambda: ChemicalInformationUISchema())

    depositors = ma_fields.Nested(lambda: DepositorsUISchema())

    derived_parameters = ma_fields.List(
        ma_fields.Nested(lambda: DerivedParametersItemUISchema())
    )

    funding_reference = ma_fields.List(
        ma_fields.Nested(lambda: FundingReferenceItemUISchema())
    )

    instrument = ma_fields.Nested(lambda: InstrumentUISchema())

    physical_environment_at_sample_handling = ma_fields.Nested(
        lambda: PhysicalEnvironmentAtSampleHandlingUISchema()
    )

    raw_data_information = ma_fields.Nested(lambda: RawDataInformationUISchema())

    record = ma_fields.Nested(lambda: RecordUISchema())

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


class ChemicalInformationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environments = ma_fields.List(
        ma_fields.Nested(lambda: ChemicalEnvironmentsItemUISchema())
    )

    entities_of_interest = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemUISchema())
    )


class InstrumentUISchema(ma.Schema):
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

    performance_test = ma_fields.Nested(lambda: PerformanceTestUISchema())


class ChemicalEnvironmentsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    constituents = ma_fields.List(ma_fields.Nested(lambda: ConstituentsItemUISchema()))

    degassing_method = ma_fields.String(
        validate=[ma_validate.OneOf(["Low pressure", "Heating", "Sonication bath"])]
    )

    dynamic_viscosity = ma_fields.Nested(lambda: DynamicViscosityUISchema())

    ionic_strength = ma_fields.Nested(lambda: IonicStrengthUISchema())

    name = ma_fields.String()

    pH = ma_fields.Nested(lambda: PHUISchema())

    solvent = ma_fields.List(ma_fields.Nested(lambda: SolventItemUISchema()))

    ultrafiltration_method = ma_fields.Nested(lambda: UltrafiltrationMethodUISchema())


class PerformanceTestUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_information = ma_fields.String()

    published_test_protocol = ma_fields.Nested(lambda: AdditionalItemUISchema())

    report = ma_fields.Nested(lambda: ReportUISchema())

    sample_composition = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemUISchema())
    )


class PhysicalEnvironmentAtSampleHandlingUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    atmosphere = ma_fields.Nested(lambda: AtmosphereUISchema())

    humidity = ma_fields.Nested(lambda: HumidityUISchema())

    pressure = ma_fields.Nested(lambda: PressureUISchema())

    temperature = ma_fields.Nested(lambda: TemperatureUISchema())


class AtmosphereUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    composition = ma_fields.List(ma_fields.Nested(lambda: SolventItemUISchema()))


class Complex_substance_of_chemical_originUISchema(ma.Schema):
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

    details = ma_fields.Nested(lambda: DetailsUISchema())

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

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


class ConstituentsItemUISchema(ma.Schema):
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

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    celltype = ma_fields.String()

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    class_ = ma_fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    components = ma_fields.List(ma_fields.Nested(lambda: ComponentsItemUISchema()))

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema())

    copy_number = ma_fields.Float()

    derived_from = ma_fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    description = ma_fields.String()

    details = ma_fields.Nested(lambda: DetailsUISchema())

    envelope_type = ma_fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    expression_organism = ma_fields.Nested(lambda: OrganismUISchema())

    expression_source_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

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

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: OrganismUISchema())

    inchikey = ma_fields.String()

    isotopic_labeling = ma_fields.String()

    location = ma_fields.Nested(lambda: LocationUISchema())

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    name = ma_fields.String()

    organ = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismUISchema())

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

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    product = ma_fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

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

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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

    variant = ma_fields.String()


class DetailsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    components = ma_fields.List(ma_fields.Nested(lambda: ComponentsItemUISchema()))

    number_of_mono_layers = ma_fields.Integer()

    size = ma_fields.Nested(lambda: DetailsSizeUISchema())

    type = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet", "Other"])
        ]
    )


class MethodSpecificParametersUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_analysis = ma_fields.List(ma_fields.Nested(lambda: DataAnalysisItemUISchema()))

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

    measurements = ma_fields.List(ma_fields.Nested(lambda: MeasurementsItemUISchema()))

    signal_type = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Initial intensity", "TRIC/MST", "Spectral shift"])
        ]
    )


class Molecular_assemblyUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    components = ma_fields.List(ma_fields.Nested(lambda: ComponentsItemUISchema()))

    external_databases = ma_fields.List(ma_fields.String())

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class SolventItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    components = ma_fields.List(ma_fields.Nested(lambda: ComponentsItemUISchema()))

    copy_number = ma_fields.Float()

    expression_organism = ma_fields.Nested(lambda: OrganismUISchema())

    expression_source_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    inchikey = ma_fields.String()

    isotopic_labeling = ma_fields.String()

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    name = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismUISchema())

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

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class ChemicalUISchema(ma.Schema):
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
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class ComponentsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    copy_number = ma_fields.Float()

    expression_organism = ma_fields.Nested(lambda: OrganismUISchema())

    expression_source_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    inchikey = ma_fields.String()

    isotopic_labeling = ma_fields.String()

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    name = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismUISchema())

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
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class MeasurementsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    measured_data = ma_fields.Nested(lambda: MeasuredDataUISchema())

    name = ma_fields.String()

    position = ma_fields.String()

    sample = ma_fields.Nested(lambda: SampleUISchema())


class PolymerUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    copy_number = ma_fields.Float()

    expression_organism = ma_fields.Nested(lambda: OrganismUISchema())

    expression_source_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Isolated", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    name = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismUISchema())

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
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class Body_fluidUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema())

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

    organism = ma_fields.Nested(lambda: OrganismUISchema())

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

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


class Cell_fractionUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    celltype = ma_fields.String()

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema())

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

    organism = ma_fields.Nested(lambda: OrganismUISchema())

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

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


class Complex_substance_of_biological_originUISchema(ma.Schema):
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

    celltype = ma_fields.String()

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema())

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

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: OrganismUISchema())

    name = ma_fields.String()

    organ = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismUISchema())

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

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


class Complex_substance_of_environmental_originUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    description = ma_fields.String()

    location = ma_fields.Nested(lambda: LocationUISchema())

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
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

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

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


class Complex_substance_of_industrial_production_originUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    description = ma_fields.String()

    name = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    product = ma_fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

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


class QualityControlsItemUISchema(ma.Schema):
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

    report = ma_fields.Nested(lambda: ReportUISchema())

    storage_from_QC_to_measurement = ma_fields.Nested(
        lambda: StorageFromQCToMeasurementUISchema()
    )

    technique = ma_fields.String()


class SampleUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environment = ma_fields.Nested(lambda: EntityUISchema())

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

    ligands = ma_fields.List(ma_fields.Nested(lambda: LigandsItemUISchema()))

    preparation = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    targets = ma_fields.List(ma_fields.Nested(lambda: LigandsItemUISchema()))


class VirionUISchema(ma.Schema):
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

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema())

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

    host_organism = ma_fields.Nested(lambda: OrganismUISchema())

    name = ma_fields.String()

    organism = ma_fields.Nested(lambda: OrganismUISchema())

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    storage = ma_fields.Nested(lambda: StorageFromQCToMeasurementUISchema())

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


class AssociatedPublicationsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional = ma_fields.List(ma_fields.Nested(lambda: AdditionalItemUISchema()))

    main = ma_fields.Nested(lambda: AdditionalItemUISchema())


class DerivedParametersItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema())
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class LigandsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema())

    entity = ma_fields.Nested(lambda: EntityUISchema())


class ModificationsUISchema(ma.Schema):
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


class RawDataInformationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    collection_start_time = l10n.LocalizedDate()

    file_information = ma_fields.List(ma_fields.Nested(lambda: ReportUISchema()))


class RecordUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    access_rights = ma_fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    date_available = l10n.LocalizedDate()

    deposition_date = l10n.LocalizedDate()

    identifier = ma_fields.String()

    keywords = ma_fields.List(ma_fields.String())

    measurement_group_id = ma_fields.String()

    metadata_access_rights = ma_fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    project = ma_fields.Nested(lambda: ProjectUISchema())

    publisher = ma_fields.String(validate=[ma_validate.OneOf(["MBDB"])])

    resource_type = ma_fields.String()

    resource_type_general = ma_fields.String(validate=[ma_validate.OneOf(["dataset"])])

    subject_category = ma_fields.String()

    title = ma_fields.String()

    version = ma_fields.String()


class StorageFromQCToMeasurementUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    duration = ma_fields.Nested(lambda: DurationUISchema())

    storage_preparation = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )

    temperature = ma_fields.Nested(lambda: TemperatureUISchema())


class AdditionalItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    authors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemUISchema()))

    pid = ma_fields.String()

    publication_year = ma_fields.Integer()

    publisher = ma_fields.String()

    resource_type = ma_fields.String(
        validate=[ma_validate.OneOf(["Article", "Book", "Thesis"])]
    )

    title = ma_fields.String()


class BiologicalPostprocessingItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    modification = ma_fields.String()

    monomer_position = ma_fields.Integer()

    protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
    )


class ConcentrationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    obtained_protocol = ma_fields.List(
        ma_fields.Nested(lambda: StoragePreparationItemUISchema())
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class DataAnalysisItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma_fields.Nested(lambda: DataFittingUISchema())

    data_processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: ProcessingStepsItemUISchema())
    )

    derived_parameter = ma_fields.Nested(lambda: EntityUISchema())

    f_cold_and_hot = ma_fields.Nested(lambda: FColdAndHotUISchema())


class DepositorsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemUISchema()))

    depositor = ma_fields.Nested(lambda: AuthorsItemUISchema())

    principal_contact = ma_fields.Nested(lambda: AuthorsItemUISchema())


class DurationUISchema(ma.Schema):
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class DynamicViscosityUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    unit = ma_fields.String(validate=[ma_validate.OneOf(["Pa s"])])

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class EntitiesInvolvedItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    entity = ma_fields.Nested(lambda: EntityUISchema())

    stoichiometry = ma_fields.Float()


class HumidityUISchema(ma.Schema):
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class MeasuredDataUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    x_data = ma_fields.Nested(lambda: XDataUISchema())

    y_data = ma_fields.Nested(lambda: XDataUISchema())


class OrganismUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_taxonomic_information = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTaxonomicInformationItemUISchema())
    )

    ncbi_taxid = ma_fields.String()


class PHUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    value = ma_fields.Float()

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class PressureUISchema(ma.Schema):
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class ProjectUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    description = ma_fields.String()

    owner = ma_fields.Nested(lambda: AuthorsItemUISchema())

    title = ma_fields.String()


class ReportUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    name = ma_fields.String()

    processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: ProcessingStepsItemUISchema())
    )

    recommended_software = ma_fields.String()

    size = ma_fields.Nested(lambda: SizeUISchema())

    source = ma_fields.String(
        validate=[ma_validate.OneOf(["Instrument software", "User annotated", "MBDB"])]
    )

    type = ma_fields.String(
        validate=[ma_validate.OneOf(["text", "binary", "text and binary"])]
    )


class TemperatureUISchema(ma.Schema):
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class AdditionalTaxonomicInformationItemUISchema(ma.Schema):
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


class AuthorsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(ma_fields.String())

    full_name = ma_fields.String()

    identifiers = ma_fields.List(ma_fields.String())


class DataFittingUISchema(ma.Schema):
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


class DetailsSizeUISchema(ma.Schema):
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


class EntityUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    _version = ma_fields.String(data_key="@v", attribute="@v")

    name = ma_fields.String()


class FColdAndHotUISchema(ma.Schema):
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


class FundingReferenceItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    award_number = ma_fields.String()

    funder_name = ma_fields.String()

    funding_program = ma_fields.String()


class IonicStrengthUISchema(ma.Schema):
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


class LocationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    S_N_latitude_ = ma_fields.Float(data_key="S-N(latitude)", attribute="S-N(latitude)")

    W_E_longitude_ = ma_fields.Float(
        data_key="W-E(longitude)", attribute="W-E(longitude)"
    )


class ProcessingStepsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    link_to_source_code = ma_fields.String()

    name = ma_fields.String()

    software_name = ma_fields.String()

    software_tool = ma_fields.String()

    software_version = ma_fields.String()


class SizeUISchema(ma.Schema):
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


class StoragePreparationItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    name = ma_fields.String()


class SupplierUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    catalog_number = ma_fields.String()

    further_information = ma_fields.List(ma_fields.String())

    name = ma_fields.String()


class UltrafiltrationMethodUISchema(ma.Schema):
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


class ValueErrorUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    error_level = ma_fields.Float()

    errors_are_relative = ma_fields.Boolean()

    lower_error = ma_fields.Float()

    upper_error = ma_fields.Float()


class XDataUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    name = ma_fields.String()

    unit = ma_fields.String()

    values = ma_fields.List(ma_fields.Float())
