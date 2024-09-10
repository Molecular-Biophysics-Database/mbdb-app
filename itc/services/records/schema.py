import marshmallow as ma
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.utils import get_value
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode
from oarepo_communities.schemas.parent import CommunitiesParentSchema
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.polymorphic import PolymorphicSchema
from oarepo_runtime.services.schema.validation import validate_date
from oarepo_workflows.services.records.schema import WorkflowParentSchema


class GeneratedParentSchema(WorkflowParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)

    communities = ma_fields.Nested(CommunitiesParentSchema)


class ItcSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: ItcMetadataSchema())

    state = ma_fields.String(dump_only=True)
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


class ItcMetadataSchema(Schema):
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

    associated_publication = ma_fields.Nested(lambda: AssociatedPublicationSchema())

    chemical_environments = ma_fields.List(
        ma_fields.Nested(lambda: ChemicalEnvironmentsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    collection_start_time = ma_fields.String(
        required=True, validate=[validate_date("%Y-%m-%d")]
    )

    depositors = ma_fields.Nested(lambda: DepositorsSchema(), required=True)

    entities_of_interest = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesOfInterestItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    funding_references = ma_fields.List(
        ma_fields.Nested(lambda: FundingReferencesItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    instrument = ma_fields.Nested(lambda: InstrumentSchema(), required=True)

    record_information = ma_fields.Nested(
        lambda: RecordInformationSchema(), required=True
    )

    results = ma_fields.List(
        ma_fields.Nested(lambda: ResultsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    schema_version = ma_fields.String(required=True, validate=[OneOf(["0.9.25"])])

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


class ChemicalEnvironmentsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    constituents = ma_fields.List(
        ma_fields.Nested(lambda: ConstituentsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    name = ma_fields.String(required=True)

    ph = ma_fields.Float(required=True)

    solvent = ma_fields.List(
        ma_fields.Nested(lambda: SolventItemSchema()),
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

    Complex_substance_of_industrial_origin = ma_fields.Nested(
        lambda: Complex_substance_of_industrial_originSchema(),
        required=True,
        data_key="Complex substance of industrial origin",
        attribute="Complex substance of industrial origin",
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

    Complex_substance_of_industrial_origin = ma_fields.Nested(
        lambda: EntitiesOfInterestItemComplex_substance_of_industrial_originSchema(),
        required=True,
        data_key="Complex substance of industrial origin",
        attribute="Complex substance of industrial origin",
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


class Complex_substance_of_chemical_originSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Lipid_assembly = ma_fields.Nested(
        lambda: Lipid_assemblySchema(),
        required=True,
        data_key="Lipid assembly",
        attribute="Lipid assembly",
    )

    type_field = "class"


class EntitiesOfInterestItemComplex_substance_of_chemical_originSchema(
    PolymorphicSchema
):
    class Meta:
        unknown = ma.RAISE

    Lipid_assembly = ma_fields.Nested(
        lambda: Complex_substance_of_chemical_originLipid_assemblySchema(),
        required=True,
        data_key="Lipid assembly",
        attribute="Lipid assembly",
    )

    type_field = "class"


class Complex_substance_of_chemical_originLipid_assemblySchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

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
        ma_fields.Nested(lambda: ComponentsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer(validate=[ma.validate.Range(min=-1)])

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    size = ma_fields.Nested(lambda: SizeSchema())

    storage = ma_fields.Nested(lambda: StorageSchema())

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
        ma_fields.Nested(lambda: ComponentsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    external_databases = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.Nested(lambda: QualityControlsSchema())

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


class Lipid_assemblySchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

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
        ma_fields.Nested(lambda: ComponentsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    name = ma_fields.String(required=True)

    number_of_mono_layers = ma_fields.Integer(validate=[ma.validate.Range(min=-1)])

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    size = ma_fields.Nested(lambda: SizeSchema())

    storage = ma_fields.Nested(lambda: StorageSchema())

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
        ma_fields.Nested(lambda: ComponentsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    external_databases = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    molecular_weight = ma_fields.Nested(lambda: MolecularWeightSchema(), required=True)

    name = ma_fields.String(required=True)

    quality_controls = ma_fields.Nested(lambda: QualityControlsSchema())

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


class ComponentsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(lambda: ComponentsItemChemicalSchema(), required=True)

    Polymer = ma_fields.Nested(lambda: ComponentsItemPolymerSchema(), required=True)

    type_field = "type"


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

    quality_controls = ma_fields.Nested(lambda: QualityControlsSchema())

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])

    variant = ma_fields.String()


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

    quality_controls = ma_fields.Nested(lambda: QualityControlsSchema())

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

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

    quality_controls = ma_fields.Nested(lambda: QualityControlsSchema())

    sequence = ma_fields.String()

    source_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

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


class MethodSpecificParametersSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    cell_temperature = ma_fields.Nested(lambda: TemperatureSchema(), required=True)

    cell_volume = ma_fields.Nested(lambda: CellVolumeSchema(), required=True)

    data_analysis = ma_fields.List(
        ma_fields.Nested(lambda: DataAnalysisItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    feedback_mode = ma_fields.String(validate=[OneOf(["None", "Low", "High"])])

    injection_mode = ma_fields.Nested(lambda: InjectionModeSchema())

    measurements = ma_fields.List(
        ma_fields.Nested(lambda: MeasurementsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    reference_power = ma_fields.Nested(lambda: ReferencePowerSchema(), required=True)

    schema_version = ma_fields.String(required=True, validate=[OneOf(["0.1.0"])])

    stirring_speed = ma_fields.Nested(lambda: StirringSpeedSchema(), required=True)


class QualityControlsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    homogeneity = ma_fields.Nested(lambda: HomogeneitySchema())

    identity = ma_fields.Nested(lambda: IdentitySchema())

    purity = ma_fields.Nested(lambda: PuritySchema())


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


class IdentitySchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    No = ma_fields.Nested(lambda: NoSchema(), required=True)

    Yes = ma_fields.Nested(lambda: IdentityYesSchema(), required=True)

    type_field = "assessed"


class InjectionModeSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Single_injection = ma_fields.Nested(
        lambda: Single_injectionSchema(),
        required=True,
        data_key="Single injection",
        attribute="Single injection",
    )

    Titration = ma_fields.Nested(lambda: TitrationSchema(), required=True)

    type_field = "type"


class MeasurementsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    name = ma_fields.String(required=True)

    sample_in_cell = ma_fields.Nested(lambda: SampleInCellSchema(), required=True)

    sample_in_syringe = ma_fields.Nested(lambda: SampleInCellSchema(), required=True)


class ResultsItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Association_rate_kOn = ma_fields.Nested(
        lambda: Association_rate_kOnSchema(),
        required=True,
        data_key="Association rate kOn",
        attribute="Association rate kOn",
    )

    Change_in_Gibbs_free_energy_deltaG = ma_fields.Nested(
        lambda: Change_in_enthalpy_deltaHSchema(),
        required=True,
        data_key="Change in Gibbs free energy deltaG",
        attribute="Change in Gibbs free energy deltaG",
    )

    Change_in_enthalpy_deltaH = ma_fields.Nested(
        lambda: Change_in_enthalpy_deltaHSchema(),
        required=True,
        data_key="Change in enthalpy deltaH",
        attribute="Change in enthalpy deltaH",
    )

    Change_in_entropy_deltaS = ma_fields.Nested(
        lambda: Change_in_entropy_deltaSSchema(),
        required=True,
        data_key="Change in entropy deltaS",
        attribute="Change in entropy deltaS",
    )

    Concentration = ma_fields.Nested(
        lambda: ResultsItemConcentrationSchema(), required=True
    )

    Constant_of_association_KA = ma_fields.Nested(
        lambda: Constant_of_association_KASchema(),
        required=True,
        data_key="Constant of association KA",
        attribute="Constant of association KA",
    )

    Constant_of_dissociation_KD = ma_fields.Nested(
        lambda: Constant_of_dissociation_KDSchema(),
        required=True,
        data_key="Constant of dissociation KD",
        attribute="Constant of dissociation KD",
    )

    Dissociation_rate_kOff = ma_fields.Nested(
        lambda: Dissociation_rate_kOffSchema(),
        required=True,
        data_key="Dissociation rate kOff",
        attribute="Dissociation rate kOff",
    )

    Half_maximal_effective_concentration_EC50 = ma_fields.Nested(
        lambda: ResultsItemConcentrationSchema(),
        required=True,
        data_key="Half maximal effective concentration EC50",
        attribute="Half maximal effective concentration EC50",
    )

    Hill_coefficient = ma_fields.Nested(
        lambda: Hill_coefficientSchema(),
        required=True,
        data_key="Hill coefficient",
        attribute="Hill coefficient",
    )

    Molecular_weight = ma_fields.Nested(
        lambda: Molecular_weightSchema(),
        required=True,
        data_key="Molecular weight",
        attribute="Molecular weight",
    )

    Stoichiometry = ma_fields.Nested(lambda: StoichiometrySchema(), required=True)

    type_field = "type"


class SolventItemSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Chemical = ma_fields.Nested(lambda: SolventItemChemicalSchema(), required=True)

    type_field = "type"


class Association_rate_kOnSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


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
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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


class Change_in_enthalpy_deltaHSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class Change_in_entropy_deltaSSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class ChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    basic_information = ma_fields.Nested(
        lambda: BasicInformationSchema(), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

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
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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


class Complex_substance_of_biological_originVirionSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

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

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf(["Fresh water", "Marine", "Ice core", "Sediment", "Sewage", "Soil"])
        ],
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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


class Complex_substance_of_industrial_originSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey"])]
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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


class ComponentsItemChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    basic_information = ma_fields.Nested(
        lambda: BasicInformationSchema(), required=True
    )

    copy_number = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    name = ma_fields.String(required=True)

    type = ma_fields.String(required=True, validate=[OneOf(["Polymer", "Chemical"])])


class Constant_of_association_KASchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class Constant_of_dissociation_KDSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class DepositorsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(
        ma_fields.Nested(lambda: ContributorsItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    depositor = ma_fields.Nested(lambda: ContributorsItemSchema(), required=True)

    principal_contact = ma_fields.Nested(
        lambda: ContributorsItemSchema(), required=True
    )


class Dissociation_rate_kOffSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class EntitiesOfInterestItemChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    basic_information = ma_fields.Nested(
        lambda: BasicInformationSchema(), required=True
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
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source = ma_fields.String(
        required=True,
        validate=[
            OneOf(["Fresh water", "Marine", "Ice core", "Sediment", "Sewage", "Soil"])
        ],
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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


class EntitiesOfInterestItemComplex_substance_of_industrial_originSchema(
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
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    product = ma_fields.String(
        required=True, validate=[OneOf(["Beer", "Cell medium", "Whey"])]
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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


class Hill_coefficientSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class IdentityYesSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    assessed = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])

    by_fingerprinting = ma_fields.Nested(lambda: ByFingerprintingSchema())

    by_intact_mass = ma_fields.Nested(lambda: ByIntactMassSchema())

    by_sequencing = ma_fields.Nested(lambda: BySequencingSchema())


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


class Molecular_weightSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class RecordInformationSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    embargoed = ma_fields.Nested(lambda: OpenSchema(), required=True)

    open = ma_fields.Nested(lambda: OpenSchema(), required=True)

    restricted = ma_fields.Nested(lambda: RestrictedSchema(), required=True)

    type_field = "access_rights"


class ResultsItemConcentrationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class SampleInCellSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    chemical_environment = ma_fields.Nested(lambda: EntitySchema(), required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    targets = ma_fields.List(
        ma_fields.Nested(lambda: TargetsItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )


class SolventItemChemicalSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    basic_information = ma_fields.Nested(
        lambda: BasicInformationSchema(), required=True
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    name = ma_fields.String(required=True)

    type = ma_fields.String(required=True, validate=[OneOf(["Chemical"])])


class StoichiometrySchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    entities_involved = ma_fields.List(
        ma_fields.Nested(lambda: EntitiesInvolvedItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    value_error = ma_fields.Nested(lambda: ValueErrorSchema())


class TitrationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    injection_parameters = ma_fields.List(
        ma_fields.Nested(lambda: InjectionParametersItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    number_injections = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=1.0)]
    )

    type = ma_fields.String(
        required=True, validate=[OneOf(["Single injection", "Titration"])]
    )


class VirionSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    additional_specifications = ma_fields.List(
        ma_fields.String(), validate=[ma.validate.Length(min=1)]
    )

    capsid_type = ma_fields.String(
        required=True,
        validate=[OneOf(["None", "Native", "Genetically Engineered", "Synthetic"])],
    )

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

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

    host_organism = ma_fields.Nested(lambda: ExpressionOrganismSchema())

    name = ma_fields.String(required=True)

    preparation_protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    source_organism = ma_fields.Nested(
        lambda: ExpressionOrganismSchema(), required=True
    )

    storage = ma_fields.Nested(lambda: StorageSchema())

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


class AssociatedPublicationSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Article = ma_fields.Nested(lambda: ArticleSchema(), required=True)

    Book = ma_fields.Nested(lambda: BookSchema(), required=True)

    Thesis = ma_fields.Nested(lambda: ThesisSchema(), required=True)

    type_field = "type"


class BasicInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    additional_identifiers = ma_fields.List(ma_fields.String())

    chemical_formula = ma_fields.String()

    molecular_weight = ma_fields.Nested(lambda: BasicInformationMolecularWeightSchema())

    title = i18n_strings


class BiologicalPostprocessingItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    position = ma_fields.String()

    protocol = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    type = ma_fields.String(required=True)


class ByIntactMassSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    deviation_from_expected_mass = ma_fields.Nested(
        lambda: MolecularWeightSchema(), required=True
    )

    method = ma_fields.String(
        required=True, validate=[OneOf(["Mass spectrometry", "SDS-PAGE"])]
    )


class ContributorsItemSchema(DictOnlySchema):
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


class DataAnalysisItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    data_fitting = ma_fields.Nested(lambda: DataFittingSchema())

    data_processing = ma_fields.List(
        ma_fields.Nested(lambda: DataProcessingItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    measurements = ma_fields.List(
        ma_fields.Nested(lambda: EntitySchema()), validate=[ma.validate.Length(min=1)]
    )

    results = ma_fields.List(
        ma_fields.Nested(lambda: EntitySchema()), validate=[ma.validate.Length(min=1)]
    )

    type = ma_fields.String(
        required=True, validate=[OneOf(["Simple model", "Complex model"])]
    )


class EntitiesInvolvedItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    copy_number = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])

    entity = ma_fields.Nested(lambda: EntitySchema(), required=True)


class HomogeneitySchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    No = ma_fields.Nested(lambda: NoSchema(), required=True)

    Yes = ma_fields.Nested(lambda: YesSchema(), required=True)

    type_field = "assessed"


class InjectionParametersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    n_injections = ma_fields.Float(required=True)

    volume = ma_fields.Nested(lambda: CellVolumeSchema(), required=True)


class OpenSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    access_rights = ma_fields.String(
        required=True, validate=[OneOf(["open", "embargoed", "restricted"])]
    )

    copyright = ma_fields.String(
        required=True,
        validate=[OneOf(["Anyone is free to distribute the data and metadata"])],
    )

    date_available = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    deposition_date = ma_fields.String(
        required=True, validate=[validate_date("%Y-%m-%d")]
    )

    external_identifier = ma_fields.String()

    license = ma_fields.Nested(lambda: LicenseSchema())

    publisher = ma_fields.String(required=True, validate=[OneOf(["MBDB"])])

    resource_type = ma_fields.String(required=True)

    resource_type_general = ma_fields.String(
        required=True, validate=[OneOf(["Dataset"])]
    )

    subject_category = ma_fields.String(required=True, validate=[OneOf(["Biophysics"])])

    title = ma_fields.String(required=True)


class PuritySchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    No = ma_fields.Nested(lambda: NoSchema(), required=True)

    Yes = ma_fields.Nested(lambda: PurityYesSchema(), required=True)

    type_field = "assessed"


class Single_injectionSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    type = ma_fields.String(
        required=True, validate=[OneOf(["Single injection", "Titration"])]
    )

    volume = ma_fields.Nested(lambda: CellVolumeSchema(), required=True)


class StorageSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    duration = ma_fields.Nested(lambda: DurationSchema())

    storage_preparation = ma_fields.List(
        ma_fields.Nested(lambda: ProtocolItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    temperature = ma_fields.Nested(lambda: TemperatureSchema(), required=True)


class TargetsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    concentration = ma_fields.Nested(lambda: ConcentrationSchema(), required=True)

    entity = ma_fields.Nested(lambda: EntitySchema(), required=True)


class AffiliationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    city = ma_fields.String()

    country = ma_fields.String()

    state = ma_fields.String()

    title = i18n_strings


class ArticleSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    journal = ma_fields.String(required=True)

    pid = ma_fields.String(required=True)

    title = ma_fields.String()

    type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )


class BasicInformationMolecularWeightSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String()

    value = ma_fields.Float()


class BookSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    pid = ma_fields.String(required=True)

    publisher = ma_fields.String(required=True)

    title = ma_fields.String()

    type = ma_fields.String(
        required=True, validate=[OneOf(["Article", "Book", "Thesis"])]
    )


class ByFingerprintingSchema(DictOnlySchema):
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


class BySequencingSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    coverage = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=0.0, max=100.0)]
    )

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


class CellVolumeSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(required=True, validate=[OneOf(["ml", "µl"])])

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])


class ConcentrationSchema(DictOnlySchema):
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

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])


class DataFittingSchema(DictOnlySchema):
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


class DataProcessingItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    link_to_source_code = ma_fields.String()

    name = ma_fields.String(required=True)

    software_name = ma_fields.String()

    software_version = ma_fields.String()


class DurationSchema(DictOnlySchema):
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

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])


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


class FundingReferencesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    funder_name = ma_fields.String()

    grant_id = ma_fields.String()

    title = i18n_strings


class InstrumentSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    manufacturer = ma_fields.String()

    title = i18n_strings


class LicenseSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String(required=True, validate=[OneOf(["CC0 1.0 Universal"])])

    url = ma_fields.String(
        required=True,
        validate=[OneOf(["https://creativecommons.org/publicdomain/zero/1.0/"])],
    )


class LocationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    longitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )


class MolecularWeightSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(
        required=True, validate=[OneOf(["g/mol", "Da", "kDa", "MDa"])]
    )

    value = ma_fields.Float(required=True, validate=[ma.validate.Range(min=-1.0)])


class NoSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    assessed = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])


class ProtocolItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    name = ma_fields.String(required=True)


class PurityYesSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    assessed = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])

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


class ReferencePowerSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(required=True, validate=[OneOf(["µcal/s", "µJ/s"])])

    value = ma_fields.Float(required=True)


class RestrictedSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    access_rights = ma_fields.String(
        required=True, validate=[OneOf(["open", "embargoed", "restricted"])]
    )

    copyright = ma_fields.String(
        required=True,
        validate=[
            OneOf(["The depositors retains copyright to the data files and metadata"])
        ],
    )

    date_available = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    deposition_date = ma_fields.String(
        required=True, validate=[validate_date("%Y-%m-%d")]
    )

    external_identifier = ma_fields.String()

    publisher = ma_fields.String(required=True, validate=[OneOf(["MBDB"])])

    resource_type = ma_fields.String(required=True)

    resource_type_general = ma_fields.String(
        required=True, validate=[OneOf(["Dataset"])]
    )

    subject_category = ma_fields.String(required=True, validate=[OneOf(["Biophysics"])])

    title = ma_fields.String(required=True)


class SizeSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    lower = ma_fields.Float(validate=[ma.validate.Range(min=0.0)])

    mean = ma_fields.Float(required=True, validate=[ma.validate.Range(min=0.0)])

    median = ma_fields.Float(validate=[ma.validate.Range(min=0.0)])

    type = ma_fields.String(
        required=True, validate=[OneOf(["radius", "diameter", "path length"])]
    )

    unit = ma_fields.String(
        required=True, validate=[OneOf(["Å", "nm", "μm", "mm", "cm", "m"])]
    )

    upper = ma_fields.Float(validate=[ma.validate.Range(min=0.0)])


class StirringSpeedSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(required=True, validate=[OneOf(["RPM"])])

    value = ma_fields.Integer(required=True, validate=[ma.validate.Range(min=0)])


class TemperatureSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    unit = ma_fields.String(required=True, validate=[OneOf(["K", "°C", "°F"])])

    value = ma_fields.Float(required=True)


class ThesisSchema(DictOnlySchema):
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


class ValueErrorSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    is_relative = ma_fields.Boolean(required=True)

    lower = ma_fields.Float(required=True)

    upper = ma_fields.Float(required=True)


class YesSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    assessed = ma_fields.String(required=True, validate=[OneOf(["Yes", "No"])])

    expected_number_of_species = ma_fields.Integer(
        required=True, validate=[ma.validate.Range(min=1)]
    )

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

    number_of_species_observed = ma_fields.Integer(
        required=True, validate=[ma.validate.Range(min=1)]
    )


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
