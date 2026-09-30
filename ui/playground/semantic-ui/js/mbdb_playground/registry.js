// Every component of the PoC plan (conversion_docs/poc/plan/index.md), in plan order.
// An entry with `load` is built: its story is lazily loaded when its tab opens.
// An entry without `load` is planned only. Adding `load` together with the story
// file is part of every block's definition of done.
//
// `design` is relative to conversion_docs/poc/.

export const STEPS = [
  { step: "0b", title: "Playground", inProgress: false },
  { step: 1, title: "Building blocks" },
  { step: 2, title: "Leaf shared blocks" },
  { step: 3, title: "Composite shared blocks" },
  { step: 4, title: "Entity forms" },
  { step: 5, title: "Section" },
];

export const REGISTRY = [
  {
    step: "0b",
    key: "SampleTextField",
    title: "Sample: plain TextField",
    design: "design/Playground.md",
    load: () => import("./stories/SampleTextField.story"),
  },

  {
    step: 1,
    key: "FieldHelp",
    title: "AliasPackages and FieldHelp",
    design: "design/building-blocks/AliasPackages.md",
  },
  {
    step: 1,
    key: "FieldGroup",
    design: "design/building-blocks/FieldGroup.md",
  },
  {
    step: 1,
    key: "TextField",
    title: "TextField / NumberField / TextAreaField",
    design: "design/building-blocks/TextField.md",
  },
  {
    step: 1,
    key: "SelectField",
    design: "design/building-blocks/SelectField.md",
  },
  {
    step: 1,
    key: "ButtonGroupField",
    design: "design/building-blocks/ButtonGroupField.md",
  },
  {
    step: 1,
    key: "ValueUnitField",
    design: "design/building-blocks/ValueUnitField.md",
  },
  {
    step: 1,
    key: "DiscriminatorField",
    design: "design/building-blocks/DiscriminatorField.md",
  },
  {
    step: 1,
    key: "StringListField",
    design: "design/building-blocks/StringListField.md",
  },
  {
    step: 1,
    key: "TableArrayField",
    design: "design/building-blocks/TableArrayField.md",
  },
  {
    step: 1,
    key: "SummaryItem",
    design: "design/building-blocks/SummaryItem.md",
  },
  {
    step: 1,
    key: "DetailView",
    design: "design/building-blocks/DetailView.md",
  },
  {
    step: 1,
    key: "ModalArrayField",
    design: "design/building-blocks/ModalArrayField.md",
  },
  {
    step: 1,
    key: "ModalObjectField",
    design: "design/building-blocks/ModalObjectField.md",
  },
  {
    step: 1,
    key: "ToggleFieldGroup",
    design: "design/building-blocks/ToggleFieldGroup.md",
  },
  {
    step: 1,
    key: "DefaultsAndIds",
    title: "Defaults and ids",
    design: "design/building-blocks/DefaultsAndIds.md",
  },

  { step: 2, key: "Protocol", design: "design/shared/Protocol.md" },
  {
    step: 2,
    key: "MolecularWeight",
    design: "design/shared/MolecularWeight.md",
  },
  { step: 2, key: "Location", design: "design/shared/Location.md" },
  { step: 2, key: "Size", design: "design/shared/Size.md" },
  { step: 2, key: "Sequence", design: "design/shared/Sequence.md" },
  {
    step: 2,
    key: "ExternalDatabases",
    design: "design/shared/ExternalDatabases.md",
  },
  {
    step: 2,
    key: "VocabularyFields",
    design: "design/shared/VocabularyFields.md",
  },
  {
    step: 2,
    key: "BasicInformation",
    design: "design/shared/BasicInformation.md",
  },

  { step: 3, key: "Modifications", design: "design/shared/Modifications.md" },
  { step: 3, key: "Purity", design: "design/shared/Purity.md" },
  { step: 3, key: "Identity", design: "design/shared/Identity.md" },
  { step: 3, key: "Homogeneity", design: "design/shared/Homogeneity.md" },
  {
    step: 3,
    key: "QualityControls",
    design: "design/shared/QualityControls.md",
  },
  { step: 3, key: "Storage", design: "design/shared/Storage.md" },
  {
    step: 3,
    key: "ComponentChemical",
    design: "design/shared/ComponentChemical.md",
  },
  {
    step: 3,
    key: "ComponentPolymer",
    design: "design/shared/ComponentPolymer.md",
  },
  { step: 3, key: "Components", design: "design/shared/Components.md" },
  {
    step: 3,
    key: "LipidAssemblyDetails",
    design: "design/shared/LipidAssemblyDetails.md",
  },

  { step: 4, key: "Chemical", design: "design/entities/Chemical.md" },
  { step: 4, key: "Polymer", design: "design/entities/Polymer.md" },
  {
    step: 4,
    key: "MolecularAssembly",
    design: "design/entities/MolecularAssembly.md",
  },
  {
    step: 4,
    key: "ComplexSubstanceCommon",
    design: "design/entities/ComplexSubstanceCommon.md",
  },
  {
    step: 4,
    key: "ComplexSubstanceOfIndustrialOrigin",
    design: "design/entities/ComplexSubstanceOfIndustrialOrigin.md",
  },
  {
    step: 4,
    key: "ComplexSubstanceOfEnvironmentalOrigin",
    design: "design/entities/ComplexSubstanceOfEnvironmentalOrigin.md",
  },
  {
    step: 4,
    key: "ComplexSubstanceOfBiologicalOrigin",
    design: "design/entities/ComplexSubstanceOfBiologicalOrigin.md",
  },
  { step: 4, key: "BodyFluid", design: "design/entities/BodyFluid.md" },
  { step: 4, key: "CellFraction", design: "design/entities/CellFraction.md" },
  { step: 4, key: "Virion", design: "design/entities/Virion.md" },
  {
    step: 4,
    key: "SolidTissueSample",
    design: "design/entities/SolidTissueSample.md",
  },
  {
    step: 4,
    key: "ComplexSubstanceOfChemicalOrigin",
    design: "design/entities/ComplexSubstanceOfChemicalOrigin.md",
  },

  {
    step: 5,
    key: "EntitiesOfInterest",
    design: "design/EntitiesOfInterest.md",
  },
];
