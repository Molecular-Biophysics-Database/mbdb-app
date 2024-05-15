import CustomField from "../../buildingBlocks/CustomField";
import FormWrapper from "../../buildingBlocks/FormWrapper";
import OptionField from "../../buildingBlocks/OptionField";
import OptionalField from "../../buildingBlocks/OptionalField";

function Size( { name, colorSchema } ) {

  const typeOptions = [
    { value: 'Radius', label: 'Radius' },
    { value: 'Diameter', label: 'Diameter' },
    { value: 'Path length', label: 'Path length' },
  ];

  const unitOptions = [
    { value: 'nm', label: 'nm' },
    { value: 'μm', label: 'μm' },
    { value: 'mm', label: 'mm' },
    { value: 'cm', label: 'cm' },
    { value: 'm', label: 'm' },
  ];

  return (
    <>
      <FormWrapper
        headline='Size'
        tooltip='The size of the lipid assembly'
        colorSchema={colorSchema}
      >
        <div className="flex mb-3">
          <div className="mr-3">
              <OptionField
                  name={name}
                  options={typeOptions}
                  fieldName='type'
                  label='Type'
                  tooltip='The type of size (e.g. radius)'
              />
          </div>
          <div className="mr-3">
              <CustomField
                name={name}
                fieldName='mean'
                label='Mean'
                tooltip='The mean of the size'
              />
          </div>
          <div>
              <OptionField
                  name={name}
                  options={unitOptions}
                  fieldName='unit'
                  label='Unit'
                  tooltip='The unit of the size'
              />
          </div>
        </div>
        <div className="flex -mt-3">
          <div className="mr-3">
              <OptionalField
                  name={name}
                  label='Median'
                  fieldName='median'
                  tooltip='The median of the size'
                  renderChild={({ optionalFieldName }) => (
                      <CustomField
                          name={optionalFieldName}
                          label='Median'
                          tooltip='The median of the size'
                      />
                  )}
              />
          </div>
          <div className="mr-3">
              <OptionalField
                  name={name}
                  label='Upper'
                  fieldName='upper'
                  tooltip='The upper bound of the size'
                  renderChild={({ optionalFieldName }) => (
                      <CustomField
                        name={optionalFieldName}
                          label='Upper'
                          tooltip='The upper bound of the size'
                      />
                  )}
              />
          </div>
          <div>
              <OptionalField
                  name={name}
                  label='Lower'
                  fieldName='lower'
                  tooltip='The lower bound of the size'
                  renderChild={({ optionalFieldName }) => (
                      <CustomField
                        name={optionalFieldName}
                          label='Lower'
                          tooltip='The lower bound of the size'
                      />
                  )}
              />
          </div>
        </div>
      </FormWrapper>
    </>
  );
}

export default Size;