import CustomField from "../../buildingBlocks/CustomField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import ArrayField from "../../buildingBlocks/ArrayField";
import Size from "./Size";
import Components from "./components/Components";
import OptionField from "../../buildingBlocks/OptionField";

function Details({ name, colorSchema }) {

  const detailsTypeOptions = [
    { value: 'Micelle', label: 'Micelle' },
    { value: 'Liposome', label: 'Liposome' },
    { value: 'Nanodisc', label: 'Nanodisc' },
    { value: 'Sheet', label: 'Sheet' },
  ];

  return (
    <>
      <FormWrapper colorSchema={colorSchema} headline='Details' tooltip='The chemical origin where the complex substance was derived from'>
        <div className="flex mb-3">
          <div className="mr-3">
              <OptionField
                  name={name}
                  options={detailsTypeOptions}
                  fieldName='type'
                  label='Type'
                  tooltip='The type of lipid assembly'
              />
          </div>
          <div>
              <CustomField 
                  name={name}
                  fieldName='number_of_mono_layers'
                  label='Number of mono layers'
                  tooltip='The number of lipid mono layers in the lipid assembly, -1 if unknown'
              />
          </div>
        </div>
        <div className="mb-3">
            <ArrayField
                name={name}
                label='Additional specification'
                fieldName='additional_specifications'
                tooltip='Additional information about the lipid assembly, if applicable'
                renderChild={({ arrayName, index }) => (
                    <CustomField
                        name={`${arrayName}.${index}`}
                        label={`Additional specification ${index + 1}`}
                        width='w-[15rem]'
                        tooltip='Additional information about the lipid assembly, if applicable'
                    />
                )}
            />
        </div>
        <div className="mb-3">
          <Size
            name={`${name}.size`}
            colorSchema={colorSchema === 'light' ? '' : 'light'}
          />
        </div>
        <div>
          <Components
            tooltip='Description of the individual components (e.g. polypeptide, heme, lipids, metal ions etc.) the molecular assembly is composed of (e.g. Hemoglobin alpha) and how many copies of each component were present'
            name={`${name}.components`}
            colorSchema={colorSchema === 'light' ? '' : 'light'}
          />
        </div>
      </FormWrapper>
    </>
  );
}

export default Details;