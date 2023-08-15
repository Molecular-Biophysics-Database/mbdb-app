import marshmallow as ma
from marshmallow import validate as ma_validate
from oarepo_runtime.ui import marshmallow as l10n
from oarepo_runtime.ui.marshmallow import InvenioUISchema
from oarepo_vocabularies.services.ui_schema import VocabularyI18nStrUIField


class MbdbMstUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma.fields.Nested(lambda: MbdbMstMetadataUISchema())


class MbdbMstMetadataUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    general_parameters = ma.fields.Nested(
        lambda: GeneralParametersUISchema(), required=True
    )

    method_specific_parameters = ma.fields.Nested(
        lambda: MethodSpecificParametersUISchema()
    )


class GeneralParametersUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    associated_publications = ma.fields.Nested(lambda: AssociatedPublicationsUISchema())

    chemical_information = ma.fields.Nested(lambda: ChemicalInformationUISchema())

    collection_start_time = l10n.LocalizedDate()

    depositors = ma.fields.Nested(lambda: DepositorsUISchema())

    derived_parameters = ma.fields.List(
        ma.fields.Nested(lambda: DerivedParametersItemUISchema())
    )

    funding_reference = ma.fields.List(
        ma.fields.Nested(lambda: FundingReferenceItemUISchema())
    )

    instrument = ma.fields.Nested(lambda: InstrumentUISchema())

    physical_conditions_at_sample_handling = ma.fields.Nested(
        lambda: PhysicalConditionsAtSampleHandlingUISchema()
    )

    record_information = ma.fields.Nested(lambda: RecordInformationUISchema())

    schema_version = ma.fields.String(validate=[ma_validate.OneOf(["0.9.4"])])

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


class ChemicalInformationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environments = ma.fields.List(
        ma.fields.Nested(lambda: ChemicalEnvironmentsItemUISchema())
    )

    entities_of_interest = ma.fields.List(
        ma.fields.Nested(lambda: EntitiesOfInterestItemUISchema())
    )


class InstrumentUISchema(ma.Schema):
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

    performance_test = ma.fields.Nested(lambda: PerformanceTestUISchema())


class ChemicalEnvironmentsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    constituents = ma.fields.List(ma.fields.Nested(lambda: ConstituentsItemUISchema()))

    degassing_method = ma.fields.String(
        validate=[ma_validate.OneOf(["Low pressure", "Heating", "Sonication bath"])]
    )

    dynamic_viscosity = ma.fields.Nested(lambda: DynamicViscosityUISchema())

    ionic_strength = ma.fields.Nested(lambda: IonicStrengthUISchema())

    name = ma.fields.String()

    pH = ma.fields.Nested(lambda: PHUISchema(), required=True)

    solvent = ma.fields.List(ma.fields.Nested(lambda: SolventItemUISchema()))

    ultrafiltration_method = ma.fields.Nested(lambda: UltrafiltrationMethodUISchema())


class PerformanceTestUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_information = ma.fields.String()

    published_test_protocol = ma.fields.Nested(lambda: AdditionalItemUISchema())

    report = ma.fields.String()

    sample_composition = ma.fields.List(
        ma.fields.Nested(lambda: ConstituentsItemUISchema())
    )


class Complex_substance_of_chemical_originUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    class_ = ma.fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    details = ma.fields.Nested(lambda: DetailsUISchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class ConstituentsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    Genetic_material = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["No genetic material", "Virus genome", "Synthetic", "Other"]
            )
        ]
    )

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    capsid_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    cell_type = ma.fields.String()

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    class_ = ma.fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemUISchema()))

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    details = ma.fields.Nested(lambda: DetailsUISchema(), required=True)

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

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

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    location = ma.fields.Nested(lambda: LocationUISchema(), required=True)

    modifications = ma.fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

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

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    product = ma.fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma.fields.String()

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

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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

    variant = ma.fields.String()


class EntitiesOfInterestItemComplex_substance_of_chemical_originUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    class_ = ma.fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    details = ma.fields.Nested(lambda: DetailsUISchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class EntitiesOfInterestItemUISchema(ma.Schema):
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

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    capsid_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    cell_type = ma.fields.String()

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    class_ = ma.fields.String(
        data_key="class",
        attribute="class",
        validate=[ma_validate.OneOf(["Lipid_assembly"])],
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemUISchema()))

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    details = ma.fields.Nested(lambda: DetailsUISchema(), required=True)

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

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

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    location = ma.fields.Nested(lambda: LocationUISchema(), required=True)

    modifications = ma.fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

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

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    product = ma.fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma.fields.String()

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

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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

    variant = ma.fields.String()


class PhysicalConditionsAtSampleHandlingUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    atmosphere = ma.fields.Nested(lambda: AtmosphereUISchema())

    humidity = ma.fields.Nested(lambda: HumidityUISchema())

    pressure = ma.fields.Nested(lambda: PressureUISchema())

    temperature = ma.fields.Nested(lambda: TemperatureUISchema())


class AtmosphereUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    composition = ma.fields.List(ma.fields.Nested(lambda: SolventItemUISchema()))


class DetailsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemUISchema()))

    number_of_mono_layers = ma.fields.Integer()

    size = ma.fields.Nested(lambda: SizeUISchema(), required=True)

    type = ma.fields.String(
        validate=[
            ma_validate.OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet", "Other"])
        ]
    )


class EntitiesOfInterestItemMolecular_assemblyUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemUISchema()))

    external_databases = ma.fields.List(ma.fields.String())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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


class MethodSpecificParametersUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_analysis = ma.fields.List(ma.fields.Nested(lambda: DataAnalysisItemUISchema()))

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

    measurements = ma.fields.List(ma.fields.Nested(lambda: MeasurementsItemUISchema()))

    schema_version = ma.fields.String(validate=[ma_validate.OneOf(["0.9.1"])])

    signal_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(["Initial intensity", "TRIC/MST", "Spectral shift"])
        ]
    )


class Molecular_assemblyUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    chemical_modifications = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    components = ma.fields.List(ma.fields.Nested(lambda: ComponentsItemUISchema()))

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    external_databases = ma.fields.List(ma.fields.String())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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


class ChemicalUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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


class ComponentsItemChemicalUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    copy_number = ma.fields.Float()

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

    type = ma.fields.String(validate=[ma_validate.OneOf(["Polymer", "Chemical"])])


class ComponentsItemPolymerUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    copy_number = ma.fields.Float()

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    modifications = ma.fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

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
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma.fields.String()

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

    type = ma.fields.String(validate=[ma_validate.OneOf(["Polymer", "Chemical"])])

    variant = ma.fields.String()


class ComponentsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    copy_number = ma.fields.Float()

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    modifications = ma.fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

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
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma.fields.String()

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

    type = ma.fields.String(validate=[ma_validate.OneOf(["Polymer", "Chemical"])])

    variant = ma.fields.String()


class EntitiesOfInterestItemChemicalUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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


class EntitiesOfInterestItemPolymerUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    modifications = ma.fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

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
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma.fields.String()

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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


class MeasurementsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    measured_data = ma.fields.Nested(lambda: MeasuredDataUISchema())

    name = ma.fields.String()

    position = ma.fields.String()

    sample = ma.fields.Nested(lambda: SampleUISchema(), required=True)


class PolymerUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    expression_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma.fields.List(ma.fields.String())

    modifications = ma.fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

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
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma.fields.String()

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

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


class SolventItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

    type = ma.fields.String(validate=[ma_validate.OneOf(["Chemical"])])


class SolventItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma.fields.List(ma.fields.String())

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    inchikey = ma.fields.String()

    isotopic_labeling = ma.fields.String()

    molecular_weight = ma.fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma.fields.String()

    quality_controls = ma.fields.List(
        ma.fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma.fields.Nested(lambda: SupplierUISchema())

    type = ma.fields.String(validate=[ma_validate.OneOf(["Chemical"])])


class AssociatedPublicationsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional = ma.fields.List(ma.fields.Nested(lambda: AdditionalItemUISchema()))

    main = ma.fields.Nested(lambda: AdditionalItemUISchema())


class Body_fluidUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

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

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Cell_fractionUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    cell_type = ma.fields.String()

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

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

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_biological_originBody_fluidUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

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

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_biological_originCell_fractionUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    cell_type = ma.fields.String()

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

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

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_biological_originUISchema(ma.Schema):
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

    cell_type = ma.fields.String()

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

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

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma.fields.String()

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_biological_originVirionUISchema(ma.Schema):
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

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_environmental_originUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    location = ma.fields.Nested(lambda: LocationUISchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
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

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_industrial_production_originUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma.fields.List(ma.fields.String())

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    product = ma.fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class EntitiesOfInterestItemComplex_substance_of_biological_originUISchema(ma.Schema):
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

    cell_type = ma.fields.String()

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

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

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma.fields.String()

    organ = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class EntitiesOfInterestItemComplex_substance_of_environmental_originUISchema(
    ma.Schema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    location = ma.fields.Nested(lambda: LocationUISchema(), required=True)

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
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

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class EntitiesOfInterestItemComplex_substance_of_industrial_production_originUISchema(
    ma.Schema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    additional_specifications = ma.fields.List(ma.fields.String())

    name = ma.fields.String()

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    product = ma.fields.String(
        validate=[ma_validate.OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class QualityControlsItemUISchema(ma.Schema):
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

    storage_until_measurement = ma.fields.Nested(
        lambda: StorageUntilMeasurementUISchema(), required=True
    )

    technique = ma.fields.String()


class RecordInformationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    access_rights = ma.fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    date_available = l10n.LocalizedDate()

    deposition_date = l10n.LocalizedDate()

    identifier = ma.fields.String()

    internal_id = ma.fields.String()

    keywords = ma.fields.List(ma.fields.String())

    measurement_group_id = ma.fields.String()

    metadata_access_rights = ma.fields.String(
        validate=[
            ma_validate.OneOf(["open access", "embargoed access", "restricted access"])
        ]
    )

    project = ma.fields.Nested(lambda: ProjectUISchema())

    publisher = ma.fields.String(validate=[ma_validate.OneOf(["MBDB"])])

    resource_type = ma.fields.String()

    resource_type_general = ma.fields.String(validate=[ma_validate.OneOf(["Dataset"])])

    subject_category = ma.fields.String(validate=[ma_validate.OneOf(["Biophysics"])])

    title = ma.fields.String()


class SampleUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    chemical_environment = ma.fields.Nested(lambda: EntityUISchema())

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

    ligands = ma.fields.List(ma.fields.Nested(lambda: LigandsItemUISchema()))

    preparation = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    targets = ma.fields.List(ma.fields.Nested(lambda: LigandsItemUISchema()))


class VirionUISchema(ma.Schema):
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

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma.fields.String(
        validate=[ma_validate.OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma.fields.String(
        validate=[
            ma_validate.OneOf(
                ["None", "Native", "Genetically Engineered", "Synthetic", "Other"]
            )
        ]
    )

    host_cell_type = ma.fields.String()

    host_organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma.fields.String()

    organism = ma.fields.Nested(lambda: ExpressionOrganismUISchema())

    preparation_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    storage = ma.fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class AdditionalItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    authors = ma.fields.List(ma.fields.Nested(lambda: AuthorsItemUISchema()))

    pid = ma.fields.String()

    publication_year = ma.fields.Integer()

    publisher = ma.fields.String()

    resource_type = ma.fields.String(
        validate=[ma_validate.OneOf(["Article", "Book", "Thesis"])]
    )

    title = ma.fields.String()


class DepositorsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma.fields.List(ma.fields.Nested(lambda: AuthorsItemUISchema()))

    depositor = ma.fields.Nested(lambda: AuthorsItemUISchema(), required=True)

    principal_contact = ma.fields.Nested(lambda: AuthorsItemUISchema(), required=True)


class DerivedParametersItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    entities_involved = ma.fields.List(
        ma.fields.Nested(lambda: EntitiesInvolvedItemUISchema())
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

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class LigandsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma.fields.Nested(lambda: ConcentrationUISchema(), required=True)

    entity = ma.fields.Nested(lambda: EntityUISchema())


class ModificationsUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    biological_postprocessing = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    chemical = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    synthesis = ma.fields.List(
        ma.fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )


class ProjectUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    description = ma.fields.String()

    owner = ma.fields.Nested(lambda: AuthorsItemUISchema(), required=True)

    title = ma.fields.String()


class StorageUntilMeasurementUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    duration = ma.fields.Nested(lambda: DurationUISchema())

    storage_preparation = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    temperature = ma.fields.Nested(lambda: TemperatureUISchema(), required=True)


class AuthorsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma.fields.List(ma.fields.Nested(lambda: AffiliationsItemUISchema()))

    family_name = ma.fields.String()

    given_name = ma.fields.String()

    identifiers = ma.fields.List(ma.fields.String())


class BiologicalPostprocessingItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    modification = ma.fields.String()

    position = ma.fields.String()

    protocol = ma.fields.List(ma.fields.Nested(lambda: ObtainedProtocolItemUISchema()))


class ConcentrationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma.fields.String(
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ]
    )

    obtained_protocol = ma.fields.List(
        ma.fields.Nested(lambda: ObtainedProtocolItemUISchema())
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

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class DataAnalysisItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma.fields.Nested(lambda: DataFittingUISchema(), required=True)

    data_processing_steps = ma.fields.List(
        ma.fields.Nested(lambda: DataProcessingStepsItemUISchema())
    )

    derived_parameter = ma.fields.Nested(lambda: EntityUISchema())

    f_cold_and_hot = ma.fields.Nested(lambda: FColdAndHotUISchema())


class DurationUISchema(ma.Schema):
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

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class DynamicViscosityUISchema(ma.Schema):
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

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class EntitiesInvolvedItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    copy_number = ma.fields.Float()

    entity = ma.fields.Nested(lambda: EntityUISchema())


class HumidityUISchema(ma.Schema):
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

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class MeasuredDataUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    x_data = ma.fields.Nested(lambda: XDataUISchema(), required=True)

    y_data = ma.fields.Nested(lambda: XDataUISchema(), required=True)


class MolecularWeightUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    unit = ma.fields.String(
        required=True, validate=[ma_validate.OneOf(["g/mol", "Da", "kDa", "MDa"])]
    )

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class PHUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma.fields.String(
        required=True,
        validate=[
            ma_validate.OneOf(["Measurement", "Calculation", "Assumption", "Other"])
        ],
    )

    value = ma.fields.Float()

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class PressureUISchema(ma.Schema):
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

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class TemperatureUISchema(ma.Schema):
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

    value_error = ma.fields.Nested(lambda: ValueErrorUISchema())


class AffiliationsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    city = ma.fields.String()

    country = ma.fields.String()

    state = ma.fields.String()

    title = VocabularyI18nStrUIField()


class DataFittingUISchema(ma.Schema):
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


class DataProcessingStepsItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma.fields.String()

    link_to_source_code = ma.fields.String()

    name = ma.fields.String()

    software_name = ma.fields.String()

    software_tool = ma.fields.String()

    software_version = ma.fields.String()


class EntityUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    name = ma.fields.String()


class ExpressionOrganismUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    rank = ma.fields.String()

    title = VocabularyI18nStrUIField()


class FColdAndHotUISchema(ma.Schema):
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


class FundingReferenceItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    _version = ma.fields.String(data_key="@v", attribute="@v")

    funder_name = ma.fields.String()

    title = VocabularyI18nStrUIField()


class IonicStrengthUISchema(ma.Schema):
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


class LocationUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    S_N_latitude_ = ma.fields.Float(data_key="S-N(latitude)", attribute="S-N(latitude)")

    W_E_longitude_ = ma.fields.Float(
        data_key="W-E(longitude)", attribute="W-E(longitude)"
    )


class ObtainedProtocolItemUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    description = ma.fields.String()

    name = ma.fields.String()


class SizeUISchema(ma.Schema):
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


class SupplierUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    catalog_number = ma.fields.String()

    further_information = ma.fields.List(ma.fields.String())

    name = ma.fields.String()


class UltrafiltrationMethodUISchema(ma.Schema):
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


class ValueErrorUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    error_level = ma.fields.Float()

    errors_are_relative = ma.fields.Boolean()

    lower_error = ma.fields.Float()

    upper_error = ma.fields.Float()


class XDataUISchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    _id = ma.fields.String(data_key="id", attribute="id")

    name = ma.fields.String()

    unit = ma.fields.String()

    values = ma.fields.List(ma.fields.Float())
