import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.validate import OneOf
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import InvenioUISchema, LocalizedDate
from oarepo_vocabularies.services.ui_schema import VocabularyI18nStrUIField


class MbdbMstUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    collected_default_search_fields = ma_fields.String()

    metadata = ma_fields.Nested(lambda: MbdbMstMetadataUISchema())


class MbdbMstMetadataUISchema(Schema):
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

    associated_publications = ma_fields.Nested(lambda: AssociatedPublicationsUISchema())

    chemical_information = ma_fields.Nested(
        lambda: ChemicalInformationUISchema(), required=True
    )

    collection_start_time = LocalizedDate(required=True)

    depositors = ma_fields.Nested(lambda: DepositorsUISchema(), required=True)

    derived_parameters = ma_fields.List(
        ma_fields.Nested(lambda: DerivedParametersItemUISchema())
    )

    funding_reference = ma_fields.List(
        ma_fields.Nested(lambda: FundingReferenceItemUISchema())
    )

    instrument = ma_fields.Nested(lambda: InstrumentUISchema(), required=True)

    physical_conditions_at_sample_handling = ma_fields.Nested(
        lambda: PhysicalConditionsAtSampleHandlingUISchema()
    )

    raw_measurements = ma_fields.List(ma_fields.String())

    record_information = ma_fields.Nested(
        lambda: RecordInformationUISchema(), required=True
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


class ChemicalInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    chemical_environments = ma_fields.List(
        ma_fields.Nested(lambda: ChemicalEnvironmentsItemUISchema()), required=True
    )

    entities_of_interest = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesOfInterestItemUISchema(), required=True),
        required=True,
    )


class InstrumentUISchema(DictOnlySchema):
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

    performance_test = ma_fields.Nested(lambda: PerformanceTestUISchema())


class ChemicalEnvironmentsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    constituents = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemUISchema(), required=True)
    )

    degassing_method = ma_fields.String(
        validate=[OneOf(["Low pressure", "Heating", "Sonication bath"])]
    )

    dynamic_viscosity = ma_fields.Nested(lambda: DynamicViscosityUISchema())

    ionic_strength = ma_fields.Nested(lambda: IonicStrengthUISchema())

    name = ma_fields.String(required=True)

    ph = ma_fields.Nested(lambda: PhUISchema(), required=True)

    solvent = ma_fields.List(
        ma_fields.Nested(lambda: SolventItemUISchema(), required=True), required=True
    )

    ultrafiltration_method = ma_fields.Nested(lambda: UltrafiltrationMethodUISchema())


class PerformanceTestUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_information = ma_fields.String()

    published_test_protocol = ma_fields.Nested(lambda: AdditionalItemUISchema())

    report = ma_fields.String(required=True)

    sample_composition = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemUISchema(), required=True),
        required=True,
    )


class Complex_substance_of_chemical_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid_assembly"])],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    details = ma_fields.Nested(lambda: DetailsUISchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class ConstituentsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    cell_type = ma_fields.String()

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid_assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema(), required=True), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    details = ma_fields.Nested(lambda: DetailsUISchema(), required=True)

    envelope_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

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

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic", "Other"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    location = ma_fields.Nested(lambda: LocationUISchema(), required=True)

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

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

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

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

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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

    variant = ma_fields.String()


class EntitiesOfInterestItemComplex_substance_of_chemical_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid_assembly"])],
    )

    details = ma_fields.Nested(lambda: DetailsUISchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class EntitiesOfInterestItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    cell_type = ma_fields.String()

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    class_ = ma_fields.String(
        required=True,
        data_key="class",
        attribute="class",
        validate=[OneOf(["Lipid_assembly"])],
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema(), required=True), required=True
    )

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    details = ma_fields.Nested(lambda: DetailsUISchema(), required=True)

    envelope_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

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

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic", "Other"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    location = ma_fields.Nested(lambda: LocationUISchema(), required=True)

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

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

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

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

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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

    variant = ma_fields.String()


class PhysicalConditionsAtSampleHandlingUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    atmosphere = ma_fields.Nested(lambda: AtmosphereUISchema())

    humidity = ma_fields.Nested(lambda: HumidityUISchema())

    pressure = ma_fields.Nested(lambda: PressureUISchema())

    temperature = ma_fields.Nested(lambda: TemperatureUISchema())


class AtmosphereUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    composition = ma_fields.List(
        ma_fields.Nested(lambda: SolventItemUISchema(), required=True), required=True
    )


class DetailsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema(), required=True), required=True
    )

    number_of_mono_layers = ma_fields.Integer(required=True)

    size = ma_fields.Nested(lambda: SizeUISchema(), required=True)

    type = ma_fields.String(
        required=True,
        validate=[OneOf(["Micelle", "Liposome", "Nanodisc", "Sheet", "Other"])],
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
        ma_fields.Nested(lambda: ComponentsItemUISchema(), required=True), required=True
    )

    external_databases = ma_fields.List(ma_fields.String())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class MethodSpecificParametersUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    data_analysis = ma_fields.List(ma_fields.Nested(lambda: DataAnalysisItemUISchema()))

    excitation_led_color = ma_fields.String(
        required=True,
        validate=[
            OneOf([
                "RED (ex 605-645nm, em 660-720nm)",
                "RED (ex 610-645nm, em 680-720nm)",
                "GREEN (ex 555-585nm, em 605-690nm)",
                "GREEN (ex 515-550nm, em 565-600nm)",
                "BLUE (ex 480-500nm, em 515-550nm)",
                "BLUE (ex 460-500nm, em 515-560nm)",
                "UV (ex 260-300nm, em 330-380nm)",
                "Spectral shift",
            ])
        ],
    )

    excitation_led_power = ma_fields.Float(required=True)

    experiment_type = ma_fields.String(
        required=True, validate=[OneOf(["Affinity", "Concentration", "Other"])]
    )

    ir_mst_laser_power = ma_fields.Float(required=True)

    measurements = ma_fields.List(
        ma_fields.Nested(lambda: MeasurementsItemUISchema()), required=True
    )

    schema_version = ma_fields.String(required=True, validate=[OneOf(["0.9.6"])])

    signal_type = ma_fields.String(
        required=True,
        validate=[OneOf(["Initial intensity", "TRIC/MST", "Spectral shift"])],
    )


class Molecular_assemblyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    chemical_modifications = ma_fields.List(
        ma_fields.Nested(lambda: BiologicalPostprocessingItemUISchema())
    )

    components = ma_fields.List(
        ma_fields.Nested(lambda: ComponentsItemUISchema(), required=True), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    external_databases = ma_fields.List(ma_fields.String())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class ChemicalUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class ComponentsItemChemicalUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    copy_number = ma_fields.Float(required=True)

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])


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
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])

    variant = ma_fields.String()


class ComponentsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    copy_number = ma_fields.Float(required=True)

    expression_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    expression_source_type = ma_fields.String(
        required=True, validate=[OneOf(["Natively", "Recombinantly", "Synthetically"])]
    )

    external_databases = ma_fields.List(ma_fields.String())

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    modifications = ma_fields.Nested(lambda: ModificationsUISchema())

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

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
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])

    variant = ma_fields.String()


class EntitiesOfInterestItemChemicalUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class MeasurementsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    measured_data = ma_fields.Nested(lambda: MeasuredDataUISchema())

    name = ma_fields.String(required=True)

    position = ma_fields.String(required=True)

    sample = ma_fields.Nested(lambda: SampleUISchema(), required=True)


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
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

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


class SolventItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Chemical"])])


class SolventItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_identifiers = ma_fields.List(ma_fields.String())

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    inchikey = ma_fields.String(required=True)

    isotopic_labeling = ma_fields.String()

    molecular_weight = ma_fields.Nested(
        lambda: MolecularWeightUISchema(), required=True
    )

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.List(
        ma_fields.Nested(lambda: QualityControlsItemUISchema())
    )

    supplier = ma_fields.Nested(lambda: SupplierUISchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Chemical"])])


class AssociatedPublicationsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional = ma_fields.List(ma_fields.Nested(lambda: AdditionalItemUISchema()))

    main = ma_fields.Nested(lambda: AdditionalItemUISchema())


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
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_biological_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    cell_type = ma_fields.String()

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
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

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic", "Other"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_biological_originVirionUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

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

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_environmental_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    location = ma_fields.Nested(lambda: LocationUISchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
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

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class Complex_substance_of_industrial_production_originUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class EntitiesOfInterestItemComplex_substance_of_biological_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    cell_type = ma_fields.String()

    derived_from = ma_fields.String(
        required=True, validate=[OneOf(["Body fluid", "Cell fraction", "Virion"])]
    )

    envelope_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
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

    genetic_material = ma_fields.String(
        required=True,
        validate=[OneOf(["No genetic material", "Virus genome", "Synthetic", "Other"])],
    )

    health_status = ma_fields.String(required=True)

    host_cell_type = ma_fields.String()

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    organ = ma_fields.String()

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
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

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class EntitiesOfInterestItemComplex_substance_of_industrial_production_originUISchema(
    DictOnlySchema
):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(ma_fields.String())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey", "Other"])]
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class QualityControlsItemUISchema(DictOnlySchema):
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
        lambda: StorageUntilMeasurementUISchema(), required=True
    )

    technique = ma_fields.String(required=True)


class RecordInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    access_rights = ma_fields.String(
        required=True,
        validate=[OneOf(["open access", "embargoed access", "restricted access"])],
    )

    date_available = LocalizedDate()

    deposition_date = LocalizedDate(required=True)

    identifier = ma_fields.String(required=True)

    internal_id = ma_fields.String(required=True)

    keywords = ma_fields.List(ma_fields.String(), required=True)

    measurement_group_id = ma_fields.String()

    metadata_access_rights = ma_fields.String(
        required=True,
        validate=[OneOf(["open access", "embargoed access", "restricted access"])],
    )

    project = ma_fields.Nested(lambda: ProjectUISchema())

    publisher = ma_fields.String(required=True, validate=[OneOf(["MBDB"])])

    resource_type = ma_fields.String(required=True)

    resource_type_general = ma_fields.String(
        required=True, validate=[OneOf(["Dataset"])]
    )

    subject_category = ma_fields.String(required=True, validate=[OneOf(["Biophysics"])])

    title = ma_fields.String(required=True)


class SampleUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    chemical_environment = ma_fields.Nested(lambda: EntityUISchema(), required=True)

    container = ma_fields.String(
        required=True,
        validate=[
            OneOf([
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
            ])
        ],
    )

    ligands = ma_fields.List(
        ma_fields.Nested(lambda: LigandsItemUISchema()), required=True
    )

    preparation = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    targets = ma_fields.List(
        ma_fields.Nested(lambda: LigandsItemUISchema()), required=True
    )


class VirionUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(ma_fields.String())

    capsid_type = ma_fields.String(
        required=True,
        validate=[
            OneOf(["None", "Native", "Genetically Engineered", "Synthetic", "Other"])
        ],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

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

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismUISchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()), required=True
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismUISchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageUntilMeasurementUISchema())

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


class AdditionalItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemUISchema()))

    pid = ma_fields.String(required=True)

    publication_year = ma_fields.Integer(required=True)

    publisher = ma_fields.String()

    resource_type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )

    title = ma_fields.String()


class DepositorsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemUISchema()))

    depositor = ma_fields.Nested(lambda: AuthorsItemUISchema(), required=True)

    principal_contact = ma_fields.Nested(lambda: AuthorsItemUISchema(), required=True)


class DerivedParametersItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemUISchema()), required=True
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class LigandsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma_fields.Nested(lambda: ConcentrationUISchema(), required=True)

    entity = ma_fields.Nested(lambda: EntityUISchema(), required=True)


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


class ProjectUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    description = ma_fields.String(required=True)

    owner = ma_fields.Nested(lambda: AuthorsItemUISchema(), required=True)

    title = ma_fields.String(required=True)


class StorageUntilMeasurementUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    duration = ma_fields.Nested(lambda: DurationUISchema())

    storage_preparation = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema())
    )

    temperature = ma_fields.Nested(lambda: TemperatureUISchema(), required=True)


class AuthorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(ma_fields.Nested(lambda: AffiliationsItemUISchema()))

    family_name = ma_fields.String(required=True)

    given_name = ma_fields.String(required=True)

    identifiers = ma_fields.List(ma_fields.String())


class BiologicalPostprocessingItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    modification = ma_fields.String(required=True)

    position = ma_fields.String()

    protocol = ma_fields.List(ma_fields.Nested(lambda: ObtainedProtocolItemUISchema()))


class ConcentrationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])]
    )

    obtained_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ObtainedProtocolItemUISchema())
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

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class DataAnalysisItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma_fields.Nested(lambda: DataFittingUISchema())

    data_processing_steps = ma_fields.List(
        ma_fields.Nested(lambda: DataProcessingStepsItemUISchema())
    )

    derived_parameter = ma_fields.Nested(lambda: EntityUISchema())

    f_cold_and_hot = ma_fields.Nested(lambda: FColdAndHotUISchema())

    measurements = ma_fields.List(ma_fields.Nested(lambda: EntityUISchema()))


class DurationUISchema(DictOnlySchema):
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

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class DynamicViscosityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["Pa s"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class EntitiesInvolvedItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    copy_number = ma_fields.Float(required=True)

    entity = ma_fields.Nested(lambda: EntityUISchema(), required=True)


class HumidityUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    controlled = ma_fields.Boolean(required=True)

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    unit = ma_fields.String(required=True, validate=[OneOf(["%", "g/m^3", "oz/y^3"])])

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class MeasuredDataUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    x_data = ma_fields.Nested(lambda: XDataUISchema(), required=True)

    y_data = ma_fields.Nested(lambda: XDataUISchema(), required=True)


class MolecularWeightUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True, validate=[OneOf(["g/mol", "Da", "kDa", "MDa"])]
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class PhUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    obtained_by = ma_fields.String(
        required=True,
        validate=[OneOf(["Measurement", "Calculation", "Assumption", "Other"])],
    )

    value = ma_fields.Float(required=True)

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class PressureUISchema(DictOnlySchema):
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class TemperatureUISchema(DictOnlySchema):
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

    value_error = ma_fields.Nested(lambda: ValueErrorUISchema())


class AffiliationsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    city = ma_fields.String()

    country = ma_fields.String()

    state = ma_fields.String()

    title = VocabularyI18nStrUIField()


class DataFittingUISchema(DictOnlySchema):
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


class DataProcessingStepsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    link_to_source_code = ma_fields.String()

    name = ma_fields.String(required=True)

    software_name = ma_fields.String()

    software_tool = ma_fields.String()

    software_version = ma_fields.String()


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


class FColdAndHotUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    f_cold_end = ma_fields.Float(required=True)

    f_cold_start = ma_fields.Float(required=True)

    f_hot_end = ma_fields.Float(required=True)

    f_hot_start = ma_fields.Float(required=True)

    time_unit = ma_fields.String(
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


class FundingReferenceItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    funder_name = ma_fields.String()

    title = VocabularyI18nStrUIField()


class IonicStrengthUISchema(DictOnlySchema):
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

    value = ma_fields.Float(required=True)


class LocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float(required=True)

    longitude = ma_fields.Float(required=True)


class ObtainedProtocolItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    name = ma_fields.String(required=True)


class SizeUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    distribution_type = ma_fields.String()

    lower = ma_fields.Float()

    mean = ma_fields.Float(required=True)

    median = ma_fields.Float()

    type = ma_fields.String(
        required=True, validate=[OneOf(["radius", "diameter", "path length", "Other"])]
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


class UltrafiltrationMethodUISchema(DictOnlySchema):
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


class ValueErrorUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    error_level = ma_fields.Float()

    errors_are_relative = ma_fields.Boolean(required=True)

    lower_error = ma_fields.Float(required=True)

    upper_error = ma_fields.Float(required=True)


class XDataUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    name = ma_fields.String()

    unit = ma_fields.String(required=True)

    values = ma_fields.List(ma_fields.Float(), required=True)
